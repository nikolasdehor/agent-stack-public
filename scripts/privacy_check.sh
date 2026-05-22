#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Checking for private paths, obvious secrets, logs, databases, backup caches, and local state..."

bad_files="$(
  find "$ROOT_DIR" -type f \
    \( -name '.env' \
    -o -iname '*secret*' \
    -o -iname '*token*' \
    -o -iname 'auth.json' \
    -o -iname 'credentials*' \
    -o -iname '*.sqlite' \
    -o -iname '*.db' \
    -o -iname '*.log' \
    -o -iname '*.tar.gz' \
    -o -iname '*.zip' \) \
    ! -path "$ROOT_DIR/.git/*"
)"

if [ -n "$bad_files" ]; then
  echo "Potentially unsafe file names found:"
  printf '%s\n' "$bad_files"
  exit 1
fi

local_user="$(id -un 2>/dev/null || true)"

if [ -n "$local_user" ]; then
  if rg -n -i \
    "$local_user" \
    "$ROOT_DIR" \
    --glob '!.git/**' \
    --glob '!scripts/privacy_check.sh' \
    --glob '!scripts/generate_inventory.py'
  then
    echo "Potential local user marker found."
    exit 1
  fi
fi

if rg -n \
  '(/Users/|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|\b([0-9]{1,3}\.){3}[0-9]{1,3}\b|sk-(proj|live|test)-[A-Za-z0-9_-]{20,}|gh[po]_[A-Za-z0-9_]+|BEGIN [A-Z ]*PRIVATE KEY|plugin-backup|plugin-install|temp_git|temp_subdir)' \
  "$ROOT_DIR" \
  --glob '!.git/**' \
  --glob '!scripts/privacy_check.sh' \
  --glob '!scripts/generate_inventory.py'
then
  echo "Potential private content found."
  exit 1
fi

echo "Privacy check passed."
