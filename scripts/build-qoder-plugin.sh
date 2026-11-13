#!/usr/bin/env bash
# Assemble, validate and package the ai-berkshire Qoder plugin.
# Source of truth: skills/*.md -> codex-skills/ (via sync) -> qoder-plugin/
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/qoder-plugin"
PLUGIN_TOOLS="financial_rigor.py report_audit.py terminal_value.py portfolio_sigma.py indep_audit.py fetch_quotes.py twstock_data.py xueqiu_scraper.py"

if command -v python3 >/dev/null 2>&1; then PY=python3; else PY=python; fi

"$PY" "$ROOT/scripts/sync-codex-skills.py"

rm -rf "$SRC/skills" "$SRC/tools" "$SRC/scripts"
mkdir -p "$SRC/skills" "$SRC/tools" "$SRC/scripts"
cp -R "$ROOT"/codex-skills/. "$SRC/skills/"
for t in $PLUGIN_TOOLS; do
  cp "$ROOT/tools/$t" "$SRC/tools/"
done
cp "$ROOT/scripts/workflow-gate-hook.sh" "$SRC/scripts/"

"$PY" - "$SRC" <<'PYEOF'
import json
import pathlib
import sys
import zipfile

src = pathlib.Path(sys.argv[1])
manifest = json.loads((src / ".qoder-plugin" / "plugin.json").read_text(encoding="utf-8"))
assert manifest["name"] == "ai-berkshire", manifest["name"]

skills = sorted(p.parent.name for p in (src / "skills").glob("*/SKILL.md"))
assert len(skills) >= 23, f"expected >=23 skills, got {len(skills)}"
for path in (src / "skills").glob("*/SKILL.md"):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"missing frontmatter: {path}"
    assert "name: " in text.split("---", 2)[1], f"missing name: {path}"

tools = sorted(p.name for p in (src / "tools").glob("*.py"))
gate = (src / "scripts" / "workflow-gate-hook.sh").exists()
assert gate, "missing workflow-gate-hook.sh"

version = manifest["version"]
dist = src.parent / "dist"
dist.mkdir(exist_ok=True)
archive = dist / f"ai-berkshire-plugin-{version}.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(src.rglob("*")):
        if path.is_file():
            zf.write(path, path.relative_to(src).as_posix())

with zipfile.ZipFile(archive) as zf:
    names = zf.namelist()
assert ".qoder-plugin/plugin.json" in names, "zip root must contain manifest directly"

print(f"validated {len(skills)} skills, {len(tools)} tools, gate={gate}")
print(f"archive: {archive}")
PYEOF
