#!/usr/bin/env python3
"""Run every update step, in order, after adding or editing session notes.

    python3 scripts/update_all.py

1. update_metadata.py         sets up new session files and refreshes each note's metadata
2. update_session_history.py  refreshes the "Session history" box on every note
3. build_dashboard.py         rebuilds dashboard/Icemoor Dashboard.html
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_dashboard  # noqa: E402
import update_metadata  # noqa: E402
import update_session_history  # noqa: E402


def main():
    if sys.version_info < (3, 8):
        sys.exit("These scripts need Python 3.8 or newer. See scripts/README.md, step 1.")
    print("Step 1 of 3: metadata")
    reminders = update_metadata.main()
    print("Step 2 of 3: session history")
    update_session_history.main()
    print("Step 3 of 3: dashboard")
    build_dashboard.main()
    print()
    if reminders:
        print("Things to check in Obsidian:")
        for r in reminders:
            print("  •", r)
        print()
    print("All done. Open the dashboard: dashboard/Icemoor Dashboard.html")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # keep the window readable for non-technical users
        print()
        print("Something went wrong and the update stopped partway:")
        print(f"  {type(e).__name__}: {e}")
        print("Nothing was deleted. Copy the message above when asking for help.")
        sys.exit(1)
