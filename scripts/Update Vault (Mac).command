#!/bin/bash
# Double-click this file in Finder to update the vault.
cd "$(dirname "$0")/.." || exit 1
if command -v python3 >/dev/null 2>&1; then
  python3 scripts/update_all.py
else
  echo "Python 3 isn't installed yet. See scripts/README.md, step 1."
fi
echo
read -n 1 -s -r -p "Press any key to close this window."
