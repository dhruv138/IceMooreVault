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
    """Turn [[Target|shown]] into 'shown' and strip markdown emphasis."""
    text = LINK.sub(lambda m: m.group(2) or m.group(1), text)
    return re.sub(r"[*_`]", "", text)


def body_of(text):
    """Session text without frontmatter, heading or TL;DR callout."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"^# .*\n", "", text, flags=re.M)
    text = re.sub(r"^> .*\n", "", text, flags=re.M)
    return text


def sentences(text):
    text = re.sub(r"\s*\n\s*", " ", text)
    return re.split(r"(?<=[.!?…”\"])\s+(?=[A-Z\[“\"(•-])", text)


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
