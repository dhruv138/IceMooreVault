#!/usr/bin/env python3
"""Write the ticked items from a proposals page into the vault.

    python3 scripts/apply_ingestion.py "Session 39"

Reads Ingestion/Session 39 proposals.md (made by ingest_session.py). For every ticked item:
  - Recap        -> a TL;DR box under the session's title (replaces an existing one)
  - New note     -> a new note in the chosen folder, with its summary and other names
  - Fact         -> a line under "Recent developments" on that note, e.g.
                    "- [[Session 39]]: [suspicion] Peter may be the recruiter."
  - Status       -> the quest's or mystery's "**Status:**" line
  - Open question-> a line under "Open questions" on that note
Your edits to an item's wording on the proposals page are used. Items already applied are
skipped, so running it twice is safe. Afterwards it links the new names in the session and runs
the usual update (metadata, session history, dashboard).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import link_session  # noqa: E402
import vault_names  # noqa: E402

VAULT = vault_names.VAULT
OUT_DIR = VAULT / "Ingestion"
HIST = "%% session-history:start %%"
FOLDER_TAG = {"People": "person", "Places": "place", "Factions": "faction", "Quests": "quest",
              "Items": "item", "Lore": "lore", "Clues & Mysteries": "mystery"}
ITEM = re.compile(r"^- \[(?P<tick>[ xX])\] %%(?P<id>[rnfsq]\d+)%% (?P<text>.*)$")


def note_path(name):
    for f in vault_names.FOLDERS:
        p = VAULT / f / f"{name}.md"
        if p.exists():
            return p
    return None


def add_to_section(path, heading, line):
    t = path.read_text(encoding="utf-8")
    if line in t:
        return
    h = t.find(HIST)
    head, tail = (t[:h], t[h:]) if h >= 0 else (t, "")
    if f"\n{heading}\n" in head:
        start = head.index(f"\n{heading}\n") + len(heading) + 2
        nxt = head.find("\n## ", start)
        end = nxt if nxt >= 0 else len(head)
        head = head[:end].rstrip("\n") + "\n" + line + "\n" + ("\n" + head[end:].lstrip("\n") if nxt >= 0 else "")
    else:
        head = head.rstrip("\n") + f"\n\n{heading}\n{line}\n"
    path.write_text(head + ("\n" + tail if tail else ""), encoding="utf-8")


def set_recap(session_file, text):
    t = session_file.read_text(encoding="utf-8")
    t = re.sub(r"\n> \[!summary\] TL;DR\n(?:> .*\n)+", "\n", t)
    t = re.sub(r"(^# Session .*\n)", lambda m: m.group(1) + f"\n> [!summary] TL;DR\n> {text}\n", t, count=1, flags=re.M)
    session_file.write_text(t, encoding="utf-8")


def set_status(path, status):
    t = path.read_text(encoding="utf-8")
    if re.search(r"^\*\*Status:\*\* .*$", t, re.M):
        t = re.sub(r"^\*\*Status:\*\* .*$", f"**Status:** {status}", t, count=1, flags=re.M)
    else:
        t = re.sub(r"(^# .*\n)", lambda m: m.group(1) + f"\n**Status:** {status}\n", t, count=1, flags=re.M)
    path.write_text(t, encoding="utf-8")


def create_note(name, folder, aliases, summary):
    p = VAULT / folder / f"{name}.md"
    if p.exists() or note_path(name):
        return None
    fm = f'---\ntitle: "{name}"\ntags:\n  - {FOLDER_TAG[folder]}\n  - dnd\n'
    if aliases:
        fm += "aliases:\n" + "".join(f'  - "{a}"\n' for a in aliases)
    p.write_text(fm + f"---\n# {name}\n\n{summary.strip()}\n", encoding="utf-8")
    return p


def main():
    if len(sys.argv) < 2:
        sys.exit('Say which session, e.g.: python3 scripts/apply_ingestion.py "Session 39"')
    session = link_session.session_path(" ".join(sys.argv[1:])).stem
    md, js = OUT_DIR / f"{session} proposals.md", OUT_DIR / f"{session} proposals.json"
    if not md.exists() or not js.exists():
        sys.exit(f"No proposals for {session}. Run ingest_session.py first.")
    data = json.loads(js.read_text(encoding="utf-8"))
    items, applied = data["items"], set(data.get("applied", []))

    ticked = {}
    for line in md.read_text(encoding="utf-8").splitlines():
        m = ITEM.match(line)
        if m and m["tick"] in "xX" and m["id"] not in applied:
            ticked[m["id"]] = re.sub(r"\s*✓ applied$", "", m["text"]).strip()
    if not ticked:
        print("Nothing to apply: no new ticked items on the proposals page.")
        return

    sfile = VAULT / "Sessions" / f"{session}.md"
    done, skipped = [], []
    # New notes first, so facts about them have somewhere to go.
    for iid in sorted(ticked, key=lambda i: "rnfsq".index(i[0])):
        e, text = items[iid], ticked[iid]
        kind = iid[0]
        if kind == "r":
            set_recap(sfile, text)
            done.append("recap")
        elif kind == "n":
            m = re.match(r"\*\*(.+?)\*\* \((.+?)\) — (.*)", text)
            name, folder, summary = (m.group(1), m.group(2), m.group(3)) if m else (e["name"], e["folder"], e["summary"])
            if folder not in FOLDER_TAG:
                skipped.append(f"{name}: unknown folder {folder!r}")
                continue
            p = create_note(name, folder, e.get("aliases", []), summary)
            if p:
                done.append(f"new note {folder}/{name}")
            else:
                skipped.append(f"{name}: a note with that name already exists")
                continue
        elif kind in "fq":
            p = note_path(e["note"])
            if not p:
                skipped.append(f"{e['note']}: no such note (was its new note left unticked?)")
                continue
            if kind == "f":
                add_to_section(p, "## Recent developments", f"- [[{session}]]: {text}")
                done.append(f"fact on {e['note']}")
            else:
                add_to_section(p, "## Open questions", f"- [[{session}]]: {text}")
                done.append(f"question on {e['note']}")
        elif kind == "s":
            p = note_path(e["note"])
            m = re.search(r"\*\*(.+?)\*\*", text)
            status = m.group(1) if m else e["status"]
            if p:
                set_status(p, status)
                add_to_section(p, "## Recent developments",
                               f"- [[{session}]]: Status changed to {status}. {e.get('reason', '')}".rstrip())
                done.append(f"status of {e['note']} → {status}")
        applied.add(iid)

    # Mark applied items on the page and in the record.
    lines = []
    for line in md.read_text(encoding="utf-8").splitlines():
        m = ITEM.match(line)
        if m and m["id"] in applied and not line.endswith("✓ applied"):
            line += " ✓ applied"
        lines.append(line)
    md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    data["applied"] = sorted(applied)
    js.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"Applied {len(done)} items to the vault:")
    for d in done:
        print("  •", d)
    for s in skipped:
        print("  ! skipped:", s)

    print("\nLinking new names in the session…")
    link_session.link_session(sfile, apply=True)
    print("\nRunning the usual update…")
    import update_all
    update_all.main()


if __name__ == "__main__":
    main()
