#!/usr/bin/env python3
"""Link the names of people, places, factions, quests, items and lore in a session note.

Keeps your wording exactly: "Peter" becomes [[Peter Owens|Peter]], which still reads "Peter".
Headings, the metadata block and existing links are left alone. Names that are ordinary
words (Tiny, Queen, Wolf...) are skipped; see AMBIGUOUS in vault_names.py.

    python3 scripts/link_session.py                    # preview links for the latest session
    python3 scripts/link_session.py "Session 39"       # preview a specific session
    python3 scripts/link_session.py "Session 39" --apply

update_all.py applies this automatically to a session the first time it sets it up.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vault_names  # noqa: E402

VAULT = vault_names.VAULT


def session_path(name=None):
    sessions = sorted((VAULT / "Sessions").glob("*.md"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    if not name:
        return sessions[-1]
    want = int(re.search(r"\d+", name).group())
    for p in sessions:
        if int(re.search(r"\d+", p.stem).group()) == want:
            return p
    sys.exit(f"No session note for {name!r} in Sessions/.")


def link_text(text, m):
    """Return (new_text, [(matched, target, line_no)])."""
    fm = re.match(r"^---\n.*?\n---\n", text, re.S)
    head, body = (text[:fm.end()], text[fm.end():]) if fm else ("", text)
    out, changes, in_code = [], [], False
    base_line = head.count("\n")
    for i, line in enumerate(body.split("\n")):
        if line.strip().startswith("```"):
            in_code = not in_code
        if in_code or line.lstrip().startswith("#") or line.startswith("%%"):
            out.append(line)
            continue
        new, last = [], 0
        for s, e, found, target in vault_names.Matcher.find(m, line):
            new.append(line[last:s])
            new.append(f"[[{target}]]" if found == target else f"[[{target}|{found}]]")
            changes.append((found, target, base_line + i + 1))
            last = e
        new.append(line[last:])
        out.append("".join(new))
    return head + "\n".join(out), changes


def link_session(path, apply=False, quiet=False):
    text = path.read_text(encoding="utf-8")
    new, changes = link_text(text, vault_names.matcher())
    if not quiet:
        if changes:
            counts = {}
            for found, target, _ in changes:
                key = found if found == target else f"{found} → {target}"
                counts[key] = counts.get(key, 0) + 1
            verb = "Linked" if apply else "Would link"
            print(f"  {verb} {len(changes)} names in {path.stem}:")
            for k, n in sorted(counts.items(), key=lambda x: x[0].lower()):
                print(f"    {k}" + (f"  (×{n})" if n > 1 else ""))
        else:
            print(f"  No new names to link in {path.stem}.")
    if apply and changes:
        path.write_text(new, encoding="utf-8")
    return changes


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply = "--apply" in sys.argv
    p = session_path(" ".join(args) if args else None)
    if not p.read_text(encoding="utf-8").startswith("---\n"):
        print(f"  {p.name} hasn't been set up yet; run update_all.py first (it links new sessions itself).")
        return
    link_session(p, apply=apply)
    if not apply:
        print("  Nothing changed. Add --apply to write these links.")


if __name__ == "__main__":
    main()
