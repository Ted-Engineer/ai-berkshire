#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${QODER_SKILLS_DIR:-$HOME/.qoder/skills}"

if command -v python3 >/dev/null 2>&1; then
  PY=python3
else
  PY=python
fi

"$PY" "$ROOT/scripts/sync-codex-skills.py"
mkdir -p "$DEST"

for skill_dir in "$ROOT"/codex-skills/*; do
  [ -d "$skill_dir" ] || continue
  name="$(basename "$skill_dir")"
  rm -rf "$DEST/$name"
  cp -R "$skill_dir" "$DEST/$name"
done

echo "Installed Qoder skills to $DEST"
echo "Open a new Qoder chat session (or restart Qoder) to pick up the skills."
