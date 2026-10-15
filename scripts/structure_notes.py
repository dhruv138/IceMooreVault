#!/usr/bin/env python3
"""Give every note the same, model-friendly layout. Safe to run repeatedly.

For People / Places / Factions / Quests / Items / Lore / Clues & Mysteries notes:
  1. A header card under the title: type, status, other names, first appearance.
  2. Opening prose goes under "## Summary".
  3. "## Recent developments" becomes "## Facts by session".
  4. Evidence labels on bullet points: [reported] when the line is hearsay (someone said,
     told, claimed...), [suspicion] when it contains a guess or theory (suspects, might,
     possibly, a question mark...). An unlabelled bullet is something the session notes
     record as having happened. Write [fact] at the start of a bullet to stop it being
     labelled.
  5. A "## Connections" section listing every labelled link drawn on the canvas boards
     and the Relationships diagrams, as "A —relationship→ B" lines.

For session notes: a header card with the session number and the real-world date it was
played, plus links to the previous and next session. The session text itself is never
changed.

Generated parts sit between %% card %% / %% connections %% markers and are rewritten on
each run. Everything else you write is kept.

Run from anywhere:  python3 scripts/structure_notes.py
"""
import json
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
FOLDERS = ["People", "Places", "Factions", "Quests", "Items", "Lore", "Clues & Mysteries"]
HIST = "%% session-history:start %%"
CARD_S, CARD_E = "%% card:start %%", "%% card:end %%"
CONN_S, CONN_E = "%% connections:start %%", "%% connections:end %%"

TYPE_LABEL = {"pc": "Player character", "npc": "Non-player character", "location": "Place",
              "faction": "Faction", "quest": "Quest", "mystery": "Mystery", "item": "Item",
              "lore": "Lore", "session": "Session"}

SUSPICION = re.compile(
    r"\?|\b(suspect\w*|suspicion\w*|wonder\w*|possibl\w*|perhaps|maybe|might|may be|may have|"
    r"may indicate|likely|probably|unconfirmed|not established|inference|theory|appears to|"
    r"seems|seem to|believes|rumou?r\w*)\b", re.I)
REPORTED = re.compile(
    r"\b(says|said|told|tells|claim\w*|report\w*|according to|heard|hears|insists|admits|"
    r"explain\w*|warn\w*|describe[sd]?)\b", re.I)
MANUAL = re.compile(r"^\[(fact|inference)\]", re.I)      # labels you set; never changed
AUTO = re.compile(r"^\[(reported|suspicion)\]\s*", re.I)  # labels this script sets; recomputed


# --------------------------------------------------------------------- parsing helpers
def split_note(text):
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", text, re.S)
    fm, rest = (m.group(1), m.group(2)) if m else ("", text)
    h = rest.find(HIST)
    body, hist = (rest[:h], rest[h:]) if h >= 0 else (rest, "")
    return fm, body, hist


def fm_value(fm, key):
    m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def fm_list(fm, key):
    m = re.search(rf"^{key}:\n((?:\s+- .*\n?)+)", fm, re.M)
    return [x.strip()[2:].strip().strip('"') for x in m.group(1).splitlines()] if m else []


def strip_block(body, start, end):
    return re.sub(rf"\n*{re.escape(start)}.*?{re.escape(end)}\n*", "\n\n", body, flags=re.S)


# --------------------------------------------------------------------- connections
def load_connections():
    """Labelled edges from canvas boards and Relationships.md mermaid diagrams."""
    edges = []
    for canvas in (VAULT / "00 Campaign" / "Boards").glob("*.canvas"):
        d = json.loads(canvas.read_text(encoding="utf-8"))
        files = {n["id"]: Path(n["file"]).stem for n in d["nodes"] if n.get("type") == "file"}
        for e in d["edges"]:
            a, b, label = files.get(e["fromNode"]), files.get(e["toNode"]), e.get("label", "").strip()
            if a and b and label:
                edges.append((a, label, b, f"{canvas.stem} board"))
    rel = VAULT / "00 Campaign" / "Relationships.md"
    if rel.exists():
        for block in re.findall(r"```mermaid\n(flowchart.*?)```", rel.read_text(encoding="utf-8"), re.S):
            names = dict(re.findall(r'(\w+)\["([^"]+)"\]', block))
            for a, arrow, label, b in re.findall(
                    r'(\w+)(?:\["[^"]*"\])?\s*(-\.->|-->|---)\s*(?:\|"([^"]*)"\|)?\s*(\w+)', block):
                if a in names and b in names:
                    lab = label or "connected to"
                    if arrow == "-.->" and "?" not in lab:
                        lab += "?"  # dotted line on the diagram = suspected link
                    edges.append((names[a], lab, names[b], "Relationships diagram"))
    seen, out = set(), []
    for a, lab, b, src in edges:
        if (a, lab, b) not in seen:
            seen.add((a, lab, b))
            out.append((a, lab, b, src))
    return out


# --------------------------------------------------------------------- evidence labels
def label_bullets(body):
    out = []
    for line in body.split("\n"):
        m = re.match(r"^(\s*-\s+)((?:\[\[Session \d+\]\]:\s*)?)(.*)$", line)
        if not m or line.strip().startswith("- [ ]") or not m.group(3).strip() or MANUAL.match(m.group(3)):
            out.append(line)
            continue
        content = AUTO.sub("", m.group(3))
        text = re.sub(r"\[\[[^\]]*\]\]", " ", content)  # ignore words inside link targets
        if text.rstrip(" *_").endswith("?"):
            tag = ""  # an open question, not a claim
        else:
            tag = "[suspicion] " if SUSPICION.search(text) else "[reported] " if REPORTED.search(text) else ""
        out.append(f"{m.group(1)}{m.group(2)}{tag}{content}")
    return "\n".join(out)


# --------------------------------------------------------------------- entity notes
def card_for(name, fm):
    typ = fm_value(fm, "type")
    bits = [f"**Type:** {TYPE_LABEL.get(typ, typ or 'Note')}"
            + (f" ({(fm_value(fm, 'location_type') or fm_value(fm, 'item_type')).replace('_', ' ')})"
               if fm_value(fm, "location_type") or fm_value(fm, "item_type") else "")]
    if fm_value(fm, "party_member") == "true":
        bits.append("**Party member**")
    if fm_value(fm, "status"):
        bits.append(f"**Status:** {fm_value(fm, 'status')}")
    aliases = [a for a in fm_list(fm, "aliases") if a.lower() != name.lower()]
    if aliases:
        bits.append("**Also called:** " + ", ".join(dict.fromkeys(aliases)))
    if fm_value(fm, "first_seen"):
        bits.append(f"**First seen:** {fm_value(fm, 'first_seen')}")
    return f"{CARD_S}\n" + " · ".join(bits) + f"\n{CARD_E}"


def restructure_entity(path, connections):
    name = path.stem
    text = path.read_text(encoding="utf-8")
    fm, body, hist = split_note(text)
    body = strip_block(body, CARD_S, CARD_E)
    body = strip_block(body, CONN_S, CONN_E)

    m = re.match(r"^\s*(# [^\n]*)\n(.*)$", body, re.S)
    title, rest = (m.group(1), m.group(2)) if m else (f"# {name}", body)

    # status line now lives in the card
    rest = re.sub(r"^\*\*Status:\*\*[^\n]*\n?", "", rest, flags=re.M)
    rest = rest.replace("## Recent developments", "## Facts by session")
    # "See also:" lines become plain links in Summary (kept as text)
    if not re.search(r"^## Summary", rest, re.M):
        first = re.search(r"^## ", rest, re.M)
        intro, tail = (rest[:first.start()], rest[first.start():]) if first else (rest, "")
        if intro.strip():
            rest = "## Summary\n\n" + intro.strip() + "\n\n" + tail.lstrip()
    rest = label_bullets(rest)

    mine = [(a, lab, b, src) for a, lab, b, src in connections if name in (a, b)]
    conn = ""
    if mine:
        lines = []
        for a, lab, b, src in mine:
            tag = "[suspicion] " if "?" in lab else ""
            lines.append(f"- {tag}[[{a}]] —{lab}→ [[{b}]]")
        conn = f"{CONN_S}\n## Connections\n\n" + "\n".join(lines) + f"\n{CONN_E}"

    parts = [title, card_for(name, fm), rest.strip()]
    if conn:
        parts.append(conn)
    new_body = "\n\n".join(p for p in parts if p) + "\n"
    if hist:
        new_body += "\n" + hist.lstrip("\n")
    new = fm + new_body
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


# --------------------------------------------------------------------- sessions
def session_card(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False  # raw, not yet set up: leave it untouched
    fm, body, hist = split_note(text)
    body = strip_block(body, CARD_S, CARD_E)
    m = re.match(r"^\s*(# [^\n]*)\n(.*)$", body, re.S)
    if not m:
        return False
    num = fm_value(fm, "session")
    when = fm_value(fm, "date")
    if when:
        y, mo, d = when.split("-")
        months = ["January", "February", "March", "April", "May", "June", "July", "August",
                  "September", "October", "November", "December"]
        when = f"played {int(d)} {months[int(mo) - 1]} {y} (real-world date of the game night, not an in-world date)"
    else:
        when = fm_value(fm, "date_note") or "date not recorded"
    bits = [f"**Session:** {num}", when[0].upper() + when[1:]]
    if fm_value(fm, "previous_session"):
        bits.append(f"**Previous:** {fm_value(fm, 'previous_session')}")
    if fm_value(fm, "next_session"):
        bits.append(f"**Next:** {fm_value(fm, 'next_session')}")
    new = fm + f"{m.group(1)}\n\n{CARD_S}\n" + " · ".join(bits) + f"\n{CARD_E}\n\n" + m.group(2).lstrip("\n")
    if hist:
        new = new.rstrip("\n") + "\n\n" + hist.lstrip("\n")
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    connections = load_connections()
    changed = 0
    for folder in FOLDERS:
        for p in sorted((VAULT / folder).glob("*.md")):
            changed += restructure_entity(p, connections)
    s_changed = sum(session_card(p) for p in sorted((VAULT / "Sessions").glob("*.md")))
    print(f"structured {changed} notes and {s_changed} sessions; {len(connections)} connections from boards and diagrams")


if __name__ == "__main__":
    main()
