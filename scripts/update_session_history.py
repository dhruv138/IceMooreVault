#!/usr/bin/env python3
"""Rebuild the "Session history" section on every People/Places/Factions/Quests/Items/Lore/
Clues & Mysteries note.

For each session that links to a note, it adds one line: the session link plus the sentence
where the note is mentioned. Run it from the vault root after adding or editing a session:

    python3 scripts/update_session_history.py

Only the block between the two %% session-history %% markers is touched, so anything you
write elsewhere in a note is left alone.
"""
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
FOLDERS = ["People", "Places", "Factions", "Quests", "Items", "Lore", "Clues & Mysteries"]
START, END = "%% session-history:start %%", "%% session-history:end %%"
MAX_CHARS = 220

LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]")


def plain(text):
    """Turn [[Target|shown]] into 'shown' and strip markdown emphasis and strike-through."""
    text = LINK.sub(lambda m: m.group(2) or m.group(1), text)
    text = text.replace("~~", "")
    return re.sub(r"[*_`]", "", text)


def body_of(text):
    """Session text without frontmatter, headings, TL;DR callout, date lines or rules."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"^#{1,6} .*\n?", "", text, flags=re.M)           # every heading
    text = re.sub(r"^> .*\n?", "", text, flags=re.M)                # callouts
    text = re.sub(r"^%%.*%%\s*\n?", "", text, flags=re.M)           # Obsidian comments
    text = re.sub(r"^\s*\**date\**\s*:\s*\**[^\n]*\d{4}[^\n]*\n?", "", text, flags=re.M | re.I)  # "**Date:** 14 October 2026"
    text = re.sub(r"^\s*(-{3,}|\*{3,})\s*$", "", text, flags=re.M)    # horizontal rules
    return text


LIST_ITEM = re.compile(r"^\s*(?:[-*+•]|\d+[.)])\s+")


def sentences(text):
    """Split into sentences. Each list item counts as its own sentence, so a to-do list
    doesn't get glued onto the paragraph before it."""
    units, para = [], []

    def flush():
        if para:
            joined = " ".join(para)
            units.extend(re.split(r"(?<=[.!?…”\"])\s+(?=[A-Z\[“\"(•-])", joined))
            para.clear()

    for line in text.split("\n"):
        if not line.strip():
            flush()
        elif LIST_ITEM.match(line):
            flush()
            units.append(LIST_ITEM.sub("", line).strip())
        else:
            para.append(line.strip())
    flush()
    return [u for u in units if u.strip()]


def snippet(sentence):
    s = plain(sentence).strip(" •-")
    if len(s) > MAX_CHARS:
        s = s[: MAX_CHARS].rsplit(" ", 1)[0] + "…"
    return s


def session_num(path):
    return int(re.search(r"\d+", path.stem).group())


def main():
    notes = {p.stem: p for f in FOLDERS for p in (VAULT / f).glob("*.md")}
    history = {name: [] for name in notes}
    for sp in sorted((VAULT / "Sessions").glob("*.md"), key=session_num):
        seen_here = set()
        for sentence in sentences(body_of(sp.read_text(encoding="utf-8"))):
            for m in LINK.finditer(sentence):
                target = m.group(1).strip()
                if target in history and target not in seen_here:
                    seen_here.add(target)
                    history[target].append((sp.stem, snippet(sentence)))

    changed = 0
    for name, path in notes.items():
        text = path.read_text(encoding="utf-8")
        text = re.sub(rf"\n*{re.escape(START)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S).rstrip("\n") + "\n"
        rows = history[name]
        if rows:
            lines = [f"> - [[{s}]]: {snip}" for s, snip in rows]
            n = len(rows)
            span = f" · first [[{rows[0][0]}]] · last [[{rows[-1][0]}]]" if n > 1 else f" · [[{rows[0][0]}]]"
            block = (f"\n{START}\n## Session history\n\n"
                     f"> [!info]- {n} session{'s' if n != 1 else ''}{span}\n"
                     + "\n".join(lines) + f"\n{END}\n")
            text = text.rstrip("\n") + "\n" + block
        if text != path.read_text(encoding="utf-8"):
            path.write_text(text, encoding="utf-8")
            changed += 1
    print(f"updated {changed} notes; {sum(1 for r in history.values() if r)} have session history")


if __name__ == "__main__":
    main()
