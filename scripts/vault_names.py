#!/usr/bin/env python3
"""Shared name matching: finds people, places, factions, quests, items and lore in text.

Used by link_session.py (to add links), update_metadata.py (to work out "first seen") and
ingest_session.py (to tell the local model which notes already exist).

Matching rules, chosen to avoid false links:
  - Names come from note file names and their aliases.
  - Names that are ordinary words or could mean two notes (AMBIGUOUS) are never matched.
  - Single-word names must match exactly, capitals included ("Peter", not "peter").
  - Longer names match regardless of capitals ("immovable rod" -> Immovable Rod), except names
    starting with "The" and a few common phrases, which must match exactly.
  - A name followed by an apostrophe and a letter other than "s" isn't matched, so "Theo" in
    "Theo'din" is left alone, but "Peter's" still matches "Peter".
"""
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
FOLDERS = ["People", "Places", "Factions", "Quests", "Items", "Lore", "Clues & Mysteries"]

# Never matched automatically: everyday words, or names that could mean more than one note.
AMBIGUOUS = {"Tiny", "Glasses", "Queen", "Bad", "Wolf", "Ugly", "Ea", "Court", "Onyxcrest",
             "Jane", "Gunther", "Poet", "Bastard"}
# Multi-word names that are also ordinary phrases: matched only with exact capitals.
EXACT_CASE = {"Ring of Gold", "Great Chamber", "Mine District", "Merchant District", "Golden Sea"}


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else ""


def aliases_of(fm):
    if "aliases:" not in fm:
        return []
    block = fm.split("aliases:", 1)[1]
    out = []
    for line in block.splitlines()[1:]:
        m = re.match(r'^\s+-\s+"?(.*?)"?\s*$', line)
        if not m:
            break
        out.append(m.group(1))
    return out


def load_names(vault=VAULT, titles_only=False):
    """Return [(text, target_note)] for every usable name, longest first."""
    names = {}
    for folder in FOLDERS:
        for p in (vault / folder).glob("*.md"):
            names.setdefault(p.stem, p.stem)
            if not titles_only:
                for a in aliases_of(frontmatter(p.read_text(encoding="utf-8"))):
                    if len(a) >= 3:
                        names.setdefault(a, p.stem)
    usable = {t: n for t, n in names.items() if t not in AMBIGUOUS and n not in AMBIGUOUS}
    return sorted(usable.items(), key=lambda x: -len(x[0]))


def case_insensitive(text):
    return " " in text and not text.startswith("The ") and text not in EXACT_CASE


def norm(text):
    return text.replace("’", "'").replace("‘", "'")


class Matcher:
    def __init__(self, names):
        self.lookup = {}
        alternatives = []
        for text, target in names:  # already longest-first, so longer names win
            ci = case_insensitive(text)
            key = norm(text)
            self.lookup[key.lower() if ci else key] = (target, ci)
            pattern = re.escape(key).replace("'", "['’]")  # straight and curly apostrophes match
            alternatives.append(("(?i:" if ci else "(?-i:") + pattern + ")")
        self.rx = None
        if alternatives:
            self.rx = re.compile(r"(?<![\w\[|])(" + "|".join(alternatives) + r")(?!\w)(?!['’][A-Za-rt-z])")

    def target(self, found):
        found = norm(found)
        hit = self.lookup.get(found)
        if hit and not hit[1]:
            return hit[0]
        hit = self.lookup.get(found.lower())
        return hit[0] if hit and hit[1] else None

    def find(self, text):
        """Yield (start, end, matched_text, target) outside existing [[links]]."""
        if not self.rx:
            return
        pos = 0
        for seg in re.split(r"(\[\[.*?\]\])", text):
            if not seg.startswith("[["):
                for m in self.rx.finditer(seg):
                    t = self.target(m.group(1))
                    if t:
                        yield pos + m.start(1), pos + m.end(1), m.group(1), t
            pos += len(seg)


def matcher(vault=VAULT, titles_only=False):
    return Matcher(load_names(vault, titles_only))
