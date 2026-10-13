#!/usr/bin/env python3
"""Build dashboard/Icemoor Dashboard.html from the vault.

Reads note metadata (type, status, first_seen), session metadata (number, date, TL;DR,
locations) and which sessions link to which notes, then writes one self-contained HTML
page. Run from the vault root after updating sessions:

    python3 scripts/build_dashboard.py
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from update_session_history import FOLDERS, LINK, body_of, sentences, snippet, session_num  # noqa: E402

VAULT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "dashboard_template.html"
OUT = VAULT / "dashboard" / "Icemoor Dashboard.html"


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip().strip('"')
            out[key] = val if val else []
        elif key and line.strip().startswith("- "):
            if not isinstance(out[key], list):
                out[key] = []
            out[key].append(line.strip()[2:].strip().strip('"'))
    return out


def link_name(s):
    m = re.match(r"\[\[([^\]|#]+)", s or "")
    return m.group(1) if m else None


def first_paragraph(text):
    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    body = re.sub(r"^# .*\n", "", body, flags=re.M)
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if b and not b.startswith(("#", "%%", ">", "-", "|", "**Status")):
            return b
    return ""


def plain(s):
    s = LINK.sub(lambda m: m.group(2) or m.group(1), s)
    return re.sub(r"\*\*|__|`", "", s).strip()


def marked(s):
    """Keep links as {{Target|shown}} tokens for the page to turn into buttons."""
    s = LINK.sub(lambda m: "{{" + m.group(1).strip() + "|" + (m.group(2) or m.group(1)).strip() + "}}", s)
    return re.sub(r"\*\*|__|`", "", s).strip()


def main():
    entities = {}
    for folder in FOLDERS:
        for p in sorted((VAULT / folder).glob("*.md")):
            t = p.read_text(encoding="utf-8")
            fm = frontmatter(t)
            entities[p.stem] = {
                "name": p.stem,
                "folder": folder,
                "type": fm.get("type") or "",
                "status": fm.get("status") or "",
                "party": fm.get("party_member") == "true",
                "kind": fm.get("location_type") or fm.get("item_type") or "",
                "summary": marked(first_paragraph(t))[:400],
                "appearances": [],
            }

    sessions = []
    for sp in sorted((VAULT / "Sessions").glob("*.md"), key=session_num):
        t = sp.read_text(encoding="utf-8")
        fm = frontmatter(t)
        tl = re.search(r"> \[!summary\] TL;DR\n> (.*)", t)
        num = session_num(sp)
        seen = set()
        for sentence in sentences(body_of(t)):
            for m in LINK.finditer(sentence):
                name = m.group(1).strip()
                if name in entities and name not in seen:
                    seen.add(name)
                    entities[name]["appearances"].append([num, snippet(sentence)])
        sessions.append({
            "num": num,
            "name": sp.stem,
            "date": fm.get("date") or "",
            "dateNote": fm.get("date_note") or "",
            "tldr": marked(tl.group(1)) if tl else marked(" ".join(sentences(body_of(t))[:2]))[:360],
            "where": [link_name(x) for x in fm.get("locations", []) if link_name(x)],
        })

    # Older sessions rarely link quests or mysteries by name, so a thread also counts the
    # sessions its own note cites (e.g. "[[Session 37]]: ..." lines), outside the generated history.
    for name, e in entities.items():
        if e["type"] not in ("quest", "mystery"):
            continue
        t = (VAULT / e["folder"] / f"{name}.md").read_text(encoding="utf-8")
        t = re.sub(r"%% session-history:start %%.*?%% session-history:end %%", "", t, flags=re.S)
        t = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
        have = {a[0] for a in e["appearances"]}
        for line in t.splitlines():
            for m in re.finditer(r"\[\[Session (\d+)\]\]", line):
                n = int(m.group(1))
                if n not in have:
                    have.add(n)
                    e["appearances"].append([n, snippet(re.sub(r"^\s*-\s*\[\[Session \d+\]\]:?\s*", "", line))])
        e["appearances"].sort(key=lambda a: a[0])

    data = {"sessions": sessions, "entities": list(entities.values())}
    html = TEMPLATE.read_text(encoding="utf-8").replace(
        "/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(VAULT)}: {len(sessions)} sessions, {len(entities)} notes, "
          f"{len(html)//1024} KB")


if __name__ == "__main__":
    main()
