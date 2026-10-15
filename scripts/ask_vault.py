#!/usr/bin/env python3
"""Ask a local Ollama model questions with the WHOLE vault in its context.

Every question is answered with the complete compiled vault (LLM/Icemoor Full Context.md)
loaded, so nothing is missed because a search didn't pick the right note.

    python3 scripts/ask_vault.py --model gpt-oss:20b                 # chat (type questions)
    python3 scripts/ask_vault.py --model gpt-oss:20b "Who is Klaus?"  # one question

Options:
    --model NAME      Ollama model to use (or set OLLAMA_MODEL). Required.
    --core            Use the reduced context (session recaps only). Misses session details.
    --ctx N           Context window to request, in tokens. Default: sized to fit the vault.
    --show-thinking   Print the model's reasoning as well as its answer.
    --force           Run even if the model's context limit looks too small.
    --host URL        Ollama address (default http://localhost:11434, or OLLAMA_HOST).

Rebuild the context first if you've changed notes:  python3 scripts/update_all.py
Uses only the Python standard library.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
FULL = VAULT / "LLM" / "Icemoor Full Context.md"
CORE = VAULT / "LLM" / "Icemoor Core Context.md"
REPLY_ROOM = 12_288  # tokens kept free for the model's reasoning and answer

SYSTEM = (
    "You are a careful assistant for a Dungeons & Dragons campaign. The user's entire campaign vault is "
    "included below. Treat it as the only source of campaign facts. Follow its 'AI Reading Guide': session "
    "notes outrank summaries; respect the evidence labels ([reported], [suspicion], [inference]); check "
    "'Contradictions and Uncertainties' before stating disputed points as settled. Cite the session numbers "
    "your answer relies on. Keep apart what happened, what someone claimed, what the party suspects, and "
    "your own inference. When asked to speculate or make assumptions, do so, label it as inference, and give "
    "the evidence for and against. If the vault doesn't say, say so.\n\n"
    "=== BEGIN CAMPAIGN VAULT ===\n{vault}\n=== END CAMPAIGN VAULT ==="
)


def estimate_tokens(text):
    return round(len(text) / 3.7)


def call(host, path, payload=None, stream=False, timeout=600):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(host.rstrip("/") + path, data=data,
                                 headers={"Content-Type": "application/json"},
                                 method="POST" if data else "GET")
    resp = urllib.request.urlopen(req, timeout=timeout)
    if stream:
        return resp
    return json.loads(resp.read().decode())


def model_context_limit(host, model):
    info = call(host, "/api/show", {"model": model})
    for key, value in (info.get("model_info") or {}).items():
        if key.endswith(".context_length"):
            return int(value)
    return None


def chat(host, model, messages, num_ctx, show_thinking):
    payload = {"model": model, "messages": messages, "stream": True,
               "options": {"num_ctx": num_ctx}, "keep_alive": "30m"}
    resp = call(host, "/api/chat", payload, stream=True, timeout=3600)
    answer, in_think = [], False
    for line in resp:
        if not line.strip():
            continue
        part = json.loads(line)
        if part.get("error"):
            raise RuntimeError(part["error"])
        msg = part.get("message", {})
        thinking = msg.get("thinking") or ""
        if thinking and show_thinking:
            print(thinking, end="", flush=True)
        chunk = msg.get("content") or ""
        # Some models put their reasoning inside <think> tags in the answer itself.
        out = []
        for piece in re.split(r"(<think>|</think>)", chunk):
            if piece == "<think>":
                in_think = True
            elif piece == "</think>":
                in_think = False
                if show_thinking:
                    print("\n--- answer ---", flush=True)
            elif piece:
                if in_think:
                    if show_thinking:
                        print(piece, end="", flush=True)
                else:
                    out.append(piece)
        text = "".join(out)
        if text:
            print(text, end="", flush=True)
            answer.append(text)
        if part.get("done"):
            break
    print()
    return "".join(answer)


def main():
    ap = argparse.ArgumentParser(description="Ask a local Ollama model about the whole vault.")
    ap.add_argument("question", nargs="*")
    ap.add_argument("--model", default=os.environ.get("OLLAMA_MODEL"))
    ap.add_argument("--core", action="store_true")
    ap.add_argument("--ctx", type=int)
    ap.add_argument("--show-thinking", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    a = ap.parse_args()
    if not a.host.startswith("http"):
        a.host = "http://" + a.host

    if not a.model:
        sys.exit("Say which model to use, e.g. --model gpt-oss:20b (run 'ollama list' to see yours).")
    src = CORE if a.core else FULL
    if not src.exists():
        sys.exit(f"{src.relative_to(VAULT)} doesn't exist yet. Run: python3 scripts/update_all.py")
    vault = src.read_text(encoding="utf-8")
    need = estimate_tokens(SYSTEM) + estimate_tokens(vault) + REPLY_ROOM
    num_ctx = a.ctx or ((need + 4095) // 4096) * 4096

    try:
        call(a.host, "/api/version", timeout=5)
    except (urllib.error.URLError, OSError):
        sys.exit(f"Can't reach Ollama at {a.host}. Is it running? Start the Ollama app, or run 'ollama serve'.")
    try:
        limit = model_context_limit(a.host, a.model)
    except urllib.error.HTTPError as e:
        sys.exit(f"Ollama doesn't have a model called '{a.model}' ({e.code}). Try: ollama pull {a.model}")

    which = "reduced vault (session recaps only)" if a.core else "whole vault"
    print(f"Loading the {which}: about {estimate_tokens(vault):,} tokens. Asking for a {num_ctx:,}-token context window.")
    if limit:
        print(f"{a.model} supports up to {limit:,} tokens.")
        if limit < need and not a.force:
            sys.exit(
                f"\nThat isn't enough: the {which} needs about {need:,} tokens including room to answer.\n"
                "Nothing has been sent, so no part of the vault was silently cut off. Options:\n"
                "  - use a model with a larger context window (see decisions.md)\n"
                "  - add --core to use the reduced vault (it misses session-level detail)\n"
                "  - add --force to try anyway (Ollama would cut part of the vault off)")
    if num_ctx > 65_536:
        print("A window this large takes several GB of extra memory and the first answer can take a while.")

    messages = [{"role": "system", "content": SYSTEM.format(vault=vault)}]
    questions = [" ".join(a.question)] if a.question else None
    try:
        while True:
            if questions is not None:
                if not questions:
                    break
                q = questions.pop(0)
                print(f"\n> {q}\n")
            else:
                try:
                    q = input("\nAsk about the campaign (blank line to quit): ").strip()
                except EOFError:
                    break
                if not q:
                    break
                print()
            messages.append({"role": "user", "content": q})
            reply = chat(a.host, a.model, messages, num_ctx, a.show_thinking)
            messages.append({"role": "assistant", "content": reply})
    except KeyboardInterrupt:
        print("\nStopped.")
    except (RuntimeError, urllib.error.URLError) as e:
        sys.exit(f"\nOllama returned an error: {e}")


if __name__ == "__main__":
    main()
