#!/usr/bin/env python3
"""Have a local Ollama model read a session and propose updates to the vault.

Nothing in the vault changes. The script writes a proposals page for you to review:

    Ingestion/Session 39 proposals.md

Tick the items you agree with (edit their wording if you like), then run apply_ingestion.py.

    python3 scripts/ingest_session.py --model qwen3:8b               # latest session
    python3 scripts/ingest_session.py --model qwen3:8b "Session 39"

What the model is asked for: a short recap, new notes for people/places/things that have none,
one fact line per affected note, status changes for quests and mysteries, and open questions.

What the script checks before showing you anything (failures go under "Rejected"):
  - every item must quote the session as evidence, and the quote must really be in the session;
  - new notes must be named in the session and must not already exist;
  - facts must be about a note that exists or is being proposed;
  - folders, labels and statuses must be from the allowed lists.

Options: --model NAME (or OLLAMA_MODEL)  --host URL  --ctx N  --think
Run update_all.py first, so the session is set up and linked.
"""
import argparse
import difflib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vault_names  # noqa: E402
from link_session import session_path  # noqa: E402

VAULT = vault_names.VAULT
OUT_DIR = VAULT / "Ingestion"
FOLDERS = vault_names.FOLDERS
LABELS = ["", "reported", "suspicion"]
STATUSES = ["active", "unresolved", "upcoming", "partially resolved", "resolved", "completed"]
REPLY_ROOM = 8192
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]")

SCHEMA = {
    "type": "object",
    "properties": {
        "recap": {"type": "string"},
        "new_notes": {"type": "array", "items": {"type": "object", "properties": {
            "name": {"type": "string"}, "folder": {"type": "string", "enum": FOLDERS},
            "aliases": {"type": "array", "items": {"type": "string"}},
            "summary": {"type": "string"}, "evidence": {"type": "string"}},
            "required": ["name", "folder", "summary", "evidence"]}},
        "facts": {"type": "array", "items": {"type": "object", "properties": {
            "note": {"type": "string"}, "fact": {"type": "string"},
            "label": {"type": "string", "enum": LABELS}, "evidence": {"type": "string"}},
            "required": ["note", "fact", "label", "evidence"]}},
        "status_changes": {"type": "array", "items": {"type": "object", "properties": {
            "note": {"type": "string"}, "status": {"type": "string", "enum": STATUSES},
            "reason": {"type": "string"}, "evidence": {"type": "string"}},
            "required": ["note", "status", "reason", "evidence"]}},
        "open_questions": {"type": "array", "items": {"type": "object", "properties": {
            "note": {"type": "string"}, "question": {"type": "string"}},
            "required": ["note", "question"]}},
    },
    "required": ["recap", "new_notes", "facts", "status_changes", "open_questions"],
}

SYSTEM = """You update a Dungeons & Dragons campaign wiki from one session's notes.
Work only from the SESSION text. Never add anything the session doesn't say.

Produce:
1. recap: 2-3 sentences, under 80 words, past or present tense, naming the key people and events.
2. new_notes: people, places, factions, items or quests that are NAMED in the session and have no
   entry in EXISTING NOTES (check names and "also called"). Give the folder, any other names used
   for it in the session, a 1-2 sentence summary, and evidence.
3. facts: for each existing or new note the session changes or adds to, one short line per
   development, written so it makes sense on that note's page. Use the note's exact name.
   label: "reported" if a character only claims or says it; "suspicion" if it is a guess, theory
   or uncertain; "" if the session states it happened.
4. status_changes: only for notes in Quests or Clues & Mysteries whose status the session changes.
5. open_questions: questions the session raises but leaves unanswered, attached to a note.

Every evidence value must be an exact quote copied from the SESSION, 5 to 25 words long.
Skip anything you can't support with a quote. Fewer correct items beat many guesses."""


def plain(text):
    return LINK.sub(lambda m: m.group(2) or m.group(1), text)


def norm(text):
    text = plain(text).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"[*_~`]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def session_body(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"%% session-history:start %%.*?%% session-history:end %%", "", text, flags=re.S)
    return text.strip()


def note_body(text, limit=1500):
    text = session_body(text)
    text = re.sub(r"^# .*\n", "", text, count=1)
    text = plain(text).strip()
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + " …"


def catalogue():
    rows, index = [], {}
    for folder in FOLDERS:
        for p in sorted((VAULT / folder).glob("*.md")):
            t = p.read_text(encoding="utf-8")
            aliases = vault_names.aliases_of(vault_names.frontmatter(t))
            first = re.split(r"(?<=[.!?])\s", note_body(t, 400).replace("\n", " "), maxsplit=1)[0][:160]
            rows.append(f"- {p.stem} [{folder}]" + (f" (also called: {', '.join(aliases)})" if aliases else "") + f": {first}")
            for n in [p.stem] + aliases:
                index.setdefault(norm(n), p.stem)
    return rows, index


def words(text):
    return re.findall(r"[a-z0-9']+", norm(text))


def evidence_ok(quote, session_norm):
    """True if the quote really is in the session: exactly, or with at least 80% of its words
    appearing in one unbroken run (allows small punctuation or wording slips)."""
    q = words(quote)
    if len(q) < 3:
        return False
    if " ".join(q) in " ".join(words(session_norm)):
        return True
    s = words(session_norm)
    sm = difflib.SequenceMatcher(None, s, q, autojunk=False)
    best = sm.find_longest_match(0, len(s), 0, len(q))
    if best.size < 3:
        return False
    # Look only at the part of the session around the best match, so matches can't be
    # gathered from all over the session.
    lo, hi = max(0, best.a - best.b - 3), min(len(s), best.a + (len(q) - best.b) + 3)
    local = difflib.SequenceMatcher(None, s[lo:hi], q, autojunk=False)
    matched = sum(b.size for b in local.get_matching_blocks())
    return matched >= 0.85 * len(q)


STOP = {"the", "of", "and", "lady", "lord", "sir", "a", "an"}


def name_in_session(name, session_norm):
    """Every meaningful word of the name appears in the session ("Owens Warehouse" passes when the
    session says "warehouse of Lord Richard Owens"; spaces are ignored, so "spellbook" matches
    "spell book")."""
    squashed = session_norm.replace(" ", "")
    ws = [w for w in words(name) if w not in STOP]
    return bool(ws) and all(w in session_norm or w in squashed for w in ws)


def tokens(text):
    return round(len(text) / 3.7)


def call(host, path, payload=None, timeout=1800):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(host.rstrip("/") + path, data=data, method="POST" if data else "GET",
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def context_limit(host, model):
    info = call(host, "/api/show", {"model": model}, timeout=30)
    for k, v in (info.get("model_info") or {}).items():
        if k.endswith(".context_length"):
            return int(v)
    return None


def parse_reply(content):
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.S).strip()
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", content, re.S)
        if m:
            return json.loads(m.group(0))
        raise


def validate(data, session_text, index):
    s_norm = norm(session_text)
    accepted = {"recap": [], "new_notes": [], "facts": [], "status_changes": [], "open_questions": []}
    rejected = []

    def resolve(name, new_names):
        n = norm(name)
        return index.get(n) or new_names.get(n)

    recap = (data.get("recap") or "").strip()
    if recap:
        accepted["recap"].append({"text": recap})

    new_names = {}
    for item in data.get("new_notes") or []:
        name = (item.get("name") or "").strip()
        why = None
        if not name:
            why = "no name"
        elif norm(name) in index:
            why = f"already exists as [[{index[norm(name)]}]]"
        elif not name_in_session(name, s_norm):
            why = "name doesn't appear in the session"
        elif item.get("folder") not in FOLDERS:
            why = f"unknown folder {item.get('folder')!r}"
        elif not evidence_ok(item.get("evidence", ""), s_norm):
            why = "evidence quote isn't in the session"
        if why:
            rejected.append(("New note", name or "?", why))
            continue
        aliases = [a for a in item.get("aliases") or [] if a and norm(a) != norm(name) and norm(a) not in index]
        accepted["new_notes"].append({"name": name, "folder": item["folder"], "aliases": aliases,
                                      "summary": item.get("summary", "").strip(), "evidence": item["evidence"]})
        new_names[norm(name)] = name
        for a in aliases:
            new_names.setdefault(norm(a), name)

    seen = set()
    for item in data.get("facts") or []:
        target = resolve(item.get("note", ""), new_names)
        fact = (item.get("fact") or "").strip()
        label = item.get("label", "")
        why = None
        if not target:
            why = f"no note called {item.get('note')!r}"
        elif not fact:
            why = "empty fact"
        elif label not in LABELS:
            why = f"unknown label {label!r}"
        elif not evidence_ok(item.get("evidence", ""), s_norm):
            why = "evidence quote isn't in the session"
        elif (target, norm(fact)) in seen:
            why = "duplicate"
        if why:
            rejected.append(("Fact", f"{item.get('note')}: {fact}", why))
            continue
        seen.add((target, norm(fact)))
        accepted["facts"].append({"note": target, "fact": fact, "label": label, "evidence": item["evidence"]})

    for item in data.get("status_changes") or []:
        target = resolve(item.get("note", ""), new_names)
        folder = next((f for f in FOLDERS if (VAULT / f / f"{target}.md").exists()), None) if target else None
        why = None
        if not target:
            why = f"no note called {item.get('note')!r}"
        elif folder not in ("Quests", "Clues & Mysteries"):
            why = "only quests and mysteries have a status"
        elif item.get("status") not in STATUSES:
            why = f"unknown status {item.get('status')!r}"
        elif not evidence_ok(item.get("evidence", ""), s_norm):
            why = "evidence quote isn't in the session"
        if why:
            rejected.append(("Status", f"{item.get('note')} → {item.get('status')}", why))
            continue
        accepted["status_changes"].append({"note": target, "status": item["status"],
                                           "reason": item.get("reason", "").strip(), "evidence": item["evidence"]})

    for item in data.get("open_questions") or []:
        target = resolve(item.get("note", ""), new_names)
        q = (item.get("question") or "").strip()
        if not target or not q:
            rejected.append(("Question", f"{item.get('note')}: {q}", "no such note" if q else "empty"))
            continue
        accepted["open_questions"].append({"note": target, "question": q if q.endswith("?") else q + "?"})
    return accepted, rejected


def write_proposals(session, model, accepted, rejected):
    OUT_DIR.mkdir(exist_ok=True)
    items, lines = {}, []
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines += ["---", f'title: "{session} proposals"', f'session: "[[{session}]]"', f"model: {model}",
              f"generated: {stamp}", "tags:", "  - ingestion", "---", f"# {session} proposals", "",
              f"Suggested by **{model}** from [[{session}]]. Nothing in the vault has changed yet.", "",
              "1. Tick the items you agree with. You can edit an item's wording on its line; keep the `%%id%%` marker.",
              f"2. Run `python3 scripts/apply_ingestion.py \"{session}\"`.",
              "", "Unticked items are ignored. Items under **Rejected** failed the automatic checks and can't be applied.", ""]

    def add(section, prefix, entries, render):
        if not entries:
            return
        lines.append(f"## {section}")
        last_heading = None
        for i, e in enumerate(entries, 1):
            iid = f"{prefix}{i}"
            items[iid] = e
            heading, text, details = render(e)
            if heading and heading != last_heading:
                lines.append(f"### [[{heading}]]")
                last_heading = heading
            lines.append(f"- [ ] %%{iid}%% {text}")
            lines.extend(f"    - {d}" for d in details)
        lines.append("")

    add("Recap", "r", accepted["recap"], lambda e: (None, e["text"], []))
    add("New notes", "n", accepted["new_notes"], lambda e: (
        None, f"**{e['name']}** ({e['folder']}) — {e['summary']}",
        ([f"also called: {', '.join(e['aliases'])}"] if e["aliases"] else []) + [f'evidence: "{e["evidence"]}"']))
    facts = sorted(accepted["facts"], key=lambda e: e["note"].lower())
    add("Facts", "f", facts, lambda e: (
        e["note"], (f"[{e['label']}] " if e["label"] else "") + e["fact"], [f'evidence: "{e["evidence"]}"']))
    add("Status changes", "s", accepted["status_changes"], lambda e: (
        e["note"], f"→ **{e['status']}**: {e['reason']}", [f'evidence: "{e["evidence"]}"']))
    add("Open questions", "q", sorted(accepted["open_questions"], key=lambda e: e["note"].lower()),
        lambda e: (e["note"], e["question"], []))
    if rejected:
        lines.append("## Rejected")
        lines.append("These failed the automatic checks. If one is actually right, add it to the vault by hand.")
        lines += [f"- **{kind}:** {what} — *{why}*" for kind, what, why in rejected]
        lines.append("")

    md = OUT_DIR / f"{session} proposals.md"
    md.write_text("\n".join(lines), encoding="utf-8")
    (OUT_DIR / f"{session} proposals.json").write_text(
        json.dumps({"session": session, "model": model, "generated": stamp, "items": items, "applied": []},
                   indent=1, ensure_ascii=False), encoding="utf-8")
    return md


def main():
    ap = argparse.ArgumentParser(description="Ask a local Ollama model to propose vault updates for a session.")
    ap.add_argument("session", nargs="*")
    ap.add_argument("--model", default=os.environ.get("OLLAMA_MODEL"))
    ap.add_argument("--host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    ap.add_argument("--ctx", type=int)
    ap.add_argument("--think", action="store_true", help="let a thinking model reason first (slower)")
    a = ap.parse_args()
    if not a.host.startswith("http"):
        a.host = "http://" + a.host
    if not a.model:
        sys.exit("Say which model to use, e.g. --model qwen3:8b (run 'ollama list' to see yours).")

    sp = session_path(" ".join(a.session) if a.session else None)
    raw = sp.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        sys.exit(f"{sp.name} hasn't been set up yet. Run update_all.py first, then try again.")
    session_text = session_body(raw)
    rows, index = catalogue()
    linked = list(dict.fromkeys(LINK.findall(raw)))
    linked_names = [t for t, _ in linked if (t in index.values())]
    details = []
    for name in linked_names:
        p = next((VAULT / f / f"{name}.md" for f in FOLDERS if (VAULT / f / f"{name}.md").exists()), None)
        if p:
            details.append(f"### {name}\n{note_body(p.read_text(encoding='utf-8'))}")

    user = ("EXISTING NOTES (name [folder] (also called) : first line)\n" + "\n".join(rows)
            + "\n\nCURRENT TEXT OF NOTES THIS SESSION MENTIONS\n" + "\n\n".join(details)
            + f"\n\nSESSION ({sp.stem})\n" + plain(session_text))
    need = tokens(SYSTEM) + tokens(user) + REPLY_ROOM
    num_ctx = a.ctx or ((need + 2047) // 2048) * 2048

    try:
        call(a.host, "/api/version", timeout=5)
    except (urllib.error.URLError, OSError):
        sys.exit(f"Can't reach Ollama at {a.host}. Is it running? Start the Ollama app, or run 'ollama serve'.")
    try:
        limit = context_limit(a.host, a.model)
    except urllib.error.HTTPError as e:
        sys.exit(f"Ollama doesn't have a model called '{a.model}' ({e.code}). Try: ollama pull {a.model}")
    print(f"Reading {sp.stem} with {a.model}: about {need:,} tokens including room to answer; "
          f"asking for a {num_ctx:,}-token context.")
    if limit and limit < need:
        sys.exit(f"{a.model} holds up to {limit:,} tokens, which isn't enough. Nothing was sent. "
                 "Use a model with a larger context (e.g. qwen3:8b or gpt-oss:20b).")
    print("This can take a few minutes on a laptop…")

    payload = {"model": a.model, "stream": False, "format": SCHEMA, "keep_alive": "10m",
               "options": {"num_ctx": num_ctx, "temperature": 0.2},
               "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]}
    if a.think:
        payload["think"] = True
    try:
        reply = call(a.host, "/api/chat", payload)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        if "format" in body.lower():  # older Ollama without schema support
            payload["format"] = "json"
            reply = call(a.host, "/api/chat", payload)
        else:
            sys.exit(f"Ollama returned an error: {body[:300]}")
    content = (reply.get("message") or {}).get("content", "")
    OUT_DIR.mkdir(exist_ok=True)
    try:
        data = parse_reply(content)
    except (json.JSONDecodeError, ValueError):
        bad = OUT_DIR / f"{sp.stem} model reply.txt"
        bad.write_text(content, encoding="utf-8")
        sys.exit(f"The model's answer wasn't valid JSON. It's saved in {bad.relative_to(VAULT)}. Try again, or try another model.")

    accepted, rejected = validate(data, session_text, index)
    md = write_proposals(sp.stem, a.model, accepted, rejected)
    n = sum(len(v) for v in accepted.values())
    print(f"\n{n} suggestions ready for review, {len(rejected)} rejected by the checks.")
    print(f"Open in Obsidian: {md.relative_to(VAULT)}")
    print(f"Then run: python3 scripts/apply_ingestion.py \"{sp.stem}\"")


if __name__ == "__main__":
    main()
