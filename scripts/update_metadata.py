#!/usr/bin/env python3
"""Prepare new session notes and refresh the metadata block at the top of every note.

What it does, in order:
1. Renames session files to the standard pattern, e.g. "Session_39.md" -> "Session 39.md".
2. Gives a freshly pasted session note its header: a metadata block, a title line, and the
   date, read from the first lines (e.g. "Session 39" / "8 October 2026", or "# Session 39" /
   "**Date:** 8 October 2026"). Those original header lines are removed so the title isn't doubled.
   It then links the names in that new session (link_session.py), keeping the wording.
3. Gives any other note that has no metadata block a basic one.
4. Rewrites the generated fields on every note (type, status, first_seen, and on sessions the
   lists of people, places, factions, quests and items they link to). Anything else in the
   metadata block, and everything below it, is left alone.
5. Works out "first seen" from the first session that links OR mentions a note's name.
6. Adds any new session to 00 Campaign/Timeline.md.
7. Prints reminders: sessions without a TL;DR recap, and names that appear in a session
   without being linked.

Run from anywhere:  python3 scripts/update_metadata.py
"""
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import link_session  # noqa: E402
import vault_names  # noqa: E402

VAULT = Path(__file__).resolve().parent.parent
FOLDER_TYPE = {"Places": "location", "Factions": "faction", "Quests": "quest",
               "Items": "item", "Lore": "lore", "Clues & Mysteries": "mystery", "Sessions": "session"}
FOLDER_TAG = {"People": "person", "Places": "place", "Factions": "faction", "Quests": "quest",
              "Items": "item", "Lore": "lore", "Clues & Mysteries": "mystery", "Sessions": "session"}

# The party. Add a name here when someone joins; PCS are the player characters.
PARTY = {"WISC", "Furgus", "Deanira", "Riffle", "Philip", "Theo'din Corvis"}
PCS = {"WISC", "Furgus", "Deanira", "Riffle", "Philip"}

GENERIC_TAGS = {"dnd", "person", "npc", "character", "place", "faction", "organization", "quest",
                "mystery", "item", "lore", "session", "actual-play", "5e"}
STATUSES = {"active", "unresolved", "resolved", "completed", "upcoming", "partially resolved"}

# Names that are also everyday words. The unlinked-name check skips them to avoid false alarms.
AMBIGUOUS = {"Tiny", "Glasses", "Queen", "Bad", "Wolf", "Ugly", "Val", "Ea", "Oma", "Fizz",
             "Gala", "Gauntlet", "Court", "Sending Stones", "Music Box"}

DATE_RE = re.compile(r"(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+)\.?,?\s+(\d{4})")
SESSION_FILE_RE = re.compile(r"^session[\s_\-]*0*(\d+)$", re.I)


# ---------------------------------------------------------------- helpers
def q(s):
    return '"' + s.replace('"', '\\"') + '"'


def link(name):
    return q(f"[[{name}]]")


def yaml_list(key, names):
    if not names:
        return f"{key}: []"
    return f"{key}:\n" + "\n".join(f"  - {link(n)}" for n in names)


def session_num(p):
    return int(re.search(r"\d+", p.stem).group())


def parse_date(text):
    m = DATE_RE.search(text)
    if not m:
        return None, None
    day, month, year = m.groups()
    for fmt in ("%d %B %Y", "%d %b %Y"):
        try:
            d = datetime.strptime(f"{day} {month} {year}", fmt)
            return d, f"{int(day)} {d.strftime('%B')} {year}"
        except ValueError:
            pass
    return None, f"{day} {month} {year}"


def split(p):
    """Return (frontmatter, body). A note without a metadata block gets a basic one."""
    t = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", t, re.S)
    if m:
        return m.group(1), m.group(2)
    folder = p.relative_to(VAULT).parts[0]
    fm = f"title: {q(p.stem)}\ntags:\n  - {FOLDER_TAG.get(folder, 'note')}\n  - dnd"
    print(f"  added a metadata block to {p.relative_to(VAULT)}")
    return fm, t


def tags_of(fm):
    m = re.search(r"^tags:\n((?:\s+- .*\n?)+)", fm, re.M)
    return [x.strip()[2:].strip() for x in m.group(1).splitlines()] if m else []


def write_fm(p, fields, lists=None, also_owned=()):
    """also_owned: generated keys to drop when they no longer apply (e.g. next_session)."""
    fm, body = split(p)
    owned = set(fields) | set(lists or {}) | set(also_owned)
    out, skip = [], False
    for line in fm.splitlines():
        key = re.match(r"^([a-z_]+):", line)
        if key:
            skip = key.group(1) in owned
        if not skip:
            out.append(line)
    at = next((i + 1 for i, l in enumerate(out) if l.startswith("title:")), 0)
    add = [f"{k}: {v}" for k, v in fields.items()]
    add += [yaml_list(k, v) for k, v in (lists or {}).items()]
    out[at:at] = add
    new = "---\n" + "\n".join(out) + "\n---\n" + body
    if new != p.read_text(encoding="utf-8"):
        p.write_text(new, encoding="utf-8")


# ---------------------------------------------------------------- step 1-2: new sessions
def prepare_sessions():
    """Returns the names of sessions it set up, so reminders can focus on them."""
    sdir, fresh = VAULT / "Sessions", set()
    for p in sorted(sdir.glob("*.md")):
        m = SESSION_FILE_RE.match(p.stem)
        if not m:
            print(f"  ! {p.name}: can't tell the session number from the file name; "
                  f"rename it like 'Session 39.md'")
            continue
        num = int(m.group(1))
        want = sdir / f"Session {num:02d}.md"
        if p != want:
            if want.exists():
                print(f"  ! {p.name} and {want.name} are both session {num}; merge them by hand")
                continue
            p.rename(want)
            print(f"  renamed {p.name} -> {want.name}")
            p = want
        text = p.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            continue
        # Freshly pasted session: pull the date out of the first few lines, drop header lines.
        lines = text.splitlines()
        d, shown = parse_date("\n".join(lines[:3]))

        def is_header(s):
            # Handles "Session 39", "Session 39:", "# Session 39", "8 October 2026",
            # "**Date:** 8 October 2026" and "Session 39 8 October 2026".
            s = s.strip().lstrip("#").strip().replace("**", "").replace("__", "")
            s = re.sub(r"^date\s*:\s*", "", s, flags=re.I)
            rest = re.sub(r"^session\s*0*\d+\s*:?", "", s, flags=re.I).strip(" :—–-")
            rest = re.sub(r"^date\s*:\s*", "", rest, flags=re.I)
            return rest == "" or bool(DATE_RE.fullmatch(rest))

        dropped = 0
        while lines and dropped < 4 and is_header(lines[0]):
            lines.pop(0)
            dropped += 1
        body_lines = lines
        title = f"Session {num} — {shown}" if shown else f"Session {num}"
        fm = (f"---\ntitle: {q(title)}\ntags:\n  - session\n  - actual-play\n  - dnd\n  - 5e\n"
              f"aliases:\n  - {q(f'Session {num}')}\n---\n")
        p.write_text(fm + f"# {title}\n\n" + "\n".join(body_lines).strip("\n") + "\n", encoding="utf-8")
        print(f"  set up {p.name} as {title!r}" + ("" if shown else " (no date found in the first lines)"))
        fresh.add(p.stem)
    return fresh


# ---------------------------------------------------------------- step 3-4: metadata
def refresh(check=frozenset()):
    notes = {p.stem: p for p in VAULT.rglob("*.md")
             if ".git" not in p.parts and p.relative_to(VAULT).parts[0] in set(FOLDER_TYPE) | {"People"}}
    # Raw session files that haven't been set up yet (no metadata block) are left alone.
    for n in [n for n, p in notes.items() if p.relative_to(VAULT).parts[0] == "Sessions"
              and not p.read_text(encoding="utf-8").startswith("---\n")]:
        print(f"  skipped {n}: not set up yet (raw session text)")
        del notes[n]
    sessions = sorted((p for p in notes.values() if p.relative_to(VAULT).parts[0] == "Sessions"),
                      key=session_num)
    first_seen, warnings = {}, []
    # "First seen" counts plain mentions of a note's own name too, not only links.
    title_matcher = vault_names.matcher(VAULT, titles_only=True)

    aliases = {}
    for name, p in notes.items():
        fm, _ = split(p)
        for a in re.findall(r'^\s+- "(.*)"$', fm.split("aliases:")[1], re.M) if "aliases:" in fm else []:
            aliases.setdefault(a, name)

    for i, p in enumerate(sessions):
        fm, body = split(p)
        num = session_num(p)
        tm = re.search(r'^title: "(.*)"', fm, re.M)
        title = tm.group(1) if tm else p.stem
        fields = {"type": "session", "session": str(num)}
        d, shown = parse_date(title)
        if d:
            fields["date"] = d.strftime("%Y-%m-%d")
        elif shown:
            fields["date_note"] = q(f"Source notes say {shown}, which isn't a valid date")
        elif "Missed" in title:
            fields["date_note"] = q("Missed session")
        if i:
            fields["previous_session"] = link(sessions[i - 1].stem)
        if i + 1 < len(sessions):
            fields["next_session"] = link(sessions[i + 1].stem)
        targets = list(dict.fromkeys(re.findall(r"\[\[([^\]|#]+)", body)))
        for _, _, _, mentioned in title_matcher.find(body):
            first_seen.setdefault(mentioned, p.stem)
        groups = {"party": [], "npcs": [], "locations": [], "factions": [], "quests": [], "items": []}
        for name in targets:
            n = notes.get(name)
            if not n or n == p:
                continue
            first_seen.setdefault(name, p.stem)
            folder = n.relative_to(VAULT).parts[0]
            key = {"Places": "locations", "Factions": "factions", "Quests": "quests",
                   "Clues & Mysteries": "quests", "Items": "items"}.get(folder)
            if folder == "People":
                key = "party" if name in PARTY else "npcs"
            if key:
                groups[key].append(name)
        write_fm(p, fields, groups, also_owned=("date", "previous_session", "next_session"))

        # reminders, for new sessions and the latest one only
        if p.stem not in check and i != len(sessions) - 1:
            continue
        if "[!summary]" not in body:
            warnings.append(f"{p.stem} has no TL;DR recap (the dashboard will show its opening lines instead)")
        could = sorted({t for _, t, _ in link_session.link_text(p.read_text(encoding="utf-8"), vault_names.matcher(VAULT))[1]})
        if could:
            warnings.append(f"{p.stem} mentions but doesn't link: {', '.join(could)}. "
                            f"To link them all: python3 scripts/link_session.py \"{p.stem}\" --apply")

    for name, p in notes.items():
        folder = p.relative_to(VAULT).parts[0]
        if folder == "Sessions":
            continue
        fm, body = split(p)
        tags = tags_of(fm)
        f = {}
        if folder == "People":
            f["type"] = "pc" if name in PCS else "npc"
            if name in PARTY:
                f["party_member"] = "true"
        else:
            f["type"] = FOLDER_TYPE[folder]
        if folder in ("Quests", "Clues & Mysteries"):
            m = re.search(r"\*\*Status:\*\* ([^\n.]+)", body)
            st = m.group(1).strip() if m else next((t for t in tags if t in STATUSES), None)
            if st:
                f["status"] = q(st) if " " in st else st
        extra = [t for t in tags if t not in GENERIC_TAGS and t not in STATUSES]
        if extra and folder == "Places":
            f["location_type"] = extra[0]
        if extra and folder == "Items":
            f["item_type"] = extra[0]
        if name in first_seen:
            f["first_seen"] = link(first_seen[name])
        write_fm(p, f)
    return len(sessions), len(notes) - len(sessions), warnings


def update_timeline():
    """Add any session missing from 00 Campaign/Timeline.md, in order."""
    tl = VAULT / "00 Campaign" / "Timeline.md"
    if not tl.exists():
        return
    text = tl.read_text(encoding="utf-8")
    listed = {int(n) for n in re.findall(r"^- \[\[Session (\d+)", text, re.M)}
    added = []
    for p in sorted((VAULT / "Sessions").glob("*.md"), key=session_num):
        raw = p.read_text(encoding="utf-8")
        num = session_num(p)
        if num in listed or not raw.startswith("---\n"):
            continue
        tm = re.search(r'^title: "(.*)"', raw, re.M)
        entry = f"- [[{p.stem}|{tm.group(1) if tm else p.stem}]]"
        lines = text.rstrip("\n").split("\n")
        after = max((i for i, l in enumerate(lines)
                     if (m := re.match(r"^- \[\[Session (\d+)", l)) and int(m.group(1)) < num), default=len(lines) - 1)
        lines.insert(after + 1, entry)
        text = "\n".join(lines) + "\n"
        listed.add(num)
        added.append(p.stem)
    if added:
        tl.write_text(text, encoding="utf-8")
        print(f"  added to Timeline: {', '.join(added)}")


def main():
    print("Checking session files…")
    fresh = prepare_sessions()
    for name in sorted(fresh):
        link_session.link_session(VAULT / "Sessions" / f"{name}.md", apply=True)
    print("Refreshing metadata…")
    n_sessions, n_notes, warnings = refresh(fresh)
    update_timeline()
    print(f"  {n_sessions} sessions and {n_notes} other notes up to date")
    return warnings


if __name__ == "__main__":
    for w in main():
        print("  •", w)
