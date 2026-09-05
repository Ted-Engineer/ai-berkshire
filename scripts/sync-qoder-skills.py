#!/usr/bin/env python3
"""Generate Qoder skills from AI Berkshire canonical sources.

Canonical source: skills/*.md
Outputs:
  .qoder/skills/<name>/SKILL.md                                   (discovery path)
  .qoder/plugins/ai-berkshire-investment/skills/<name>/SKILL.md   (plugin mirror)

.qoder/skills/ 是 Qoder 实际发现项目级技能的路径（实测无需注册即出现在技能列表）。
插件镜像保留给 plugin 打包/hook 场景；两处内容一致，均从 skills/*.md 生成，勿手改。
This mirrors the codex/trae/dsh/zcode generators so all runtimes share one
canonical workflow defined in skills/*.md.

Note: .qoder/skills/ may also contain hand-written Qoder-only skills (e.g.
repo-health-audit); this script only writes its own 22 and never touches them.

Usage:
  python3 scripts/sync-qoder-skills.py          # generate/update
  python3 scripts/sync-qoder-skills.py --check  # verify only, no writes
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_SKILLS = ROOT / "skills"
QODER_STANDALONE_SKILLS = ROOT / ".qoder" / "skills"
QODER_PLUGIN_SKILLS = ROOT / ".qoder" / "plugins" / "ai-berkshire-investment" / "skills"
OUTPUT_ROOTS = [QODER_STANDALONE_SKILLS, QODER_PLUGIN_SKILLS]

# ---------------------------------------------------------------------------
# Per-skill Chinese descriptions (what + when-to-invoke).
# Shared shape with the Codex/TRAE/DSH/ZCode generators; keep the wording in
# sync with scripts/sync-dsh-skills.py.
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _skill_descriptions import SKILL_DESCRIPTIONS as QODER_DESCRIPTIONS


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Split frontmatter (--- ... ---) from body. Returns (frontmatter_text or None, body)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :].lstrip("\n")


def yaml_quote(value: str) -> str:
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def qoder_frontmatter(name: str) -> str:
    desc = QODER_DESCRIPTIONS.get(name, f"AI Berkshire 投研技能:{name}")
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {yaml_quote(desc)}\n"
        "---\n\n"
    )


def main() -> None:
    check = "--check" in sys.argv[1:]
    unknown_args = [arg for arg in sys.argv[1:] if arg != "--check"]
    if unknown_args:
        raise SystemExit(f"Unknown argument(s): {', '.join(unknown_args)}")

    if not check:
        for out_root in OUTPUT_ROOTS:
            out_root.mkdir(parents=True, exist_ok=True)

    count = 0
    stale: list[str] = []
    for source in sorted(CLAUDE_SKILLS.glob("*.md")):
        name = source.stem
        source_text = source.read_text(encoding="utf-8")

        # Strip existing frontmatter (if any, e.g. news-pulse.md)
        _, body = split_frontmatter(source_text)

        content = (
            qoder_frontmatter(name)
            + body.rstrip()
            + "\n"
        )

        for out_root in OUTPUT_ROOTS:
            target_dir = out_root / name
            target = target_dir / "SKILL.md"
            if check:
                if not target.exists() or target.read_text(encoding="utf-8") != content:
                    stale.append(str(target.relative_to(ROOT)))
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")

        count += 1

    if check:
        if stale:
            print("Qoder skills are out of date:")
            for path in stale:
                print(f"  {path}")
            raise SystemExit(1)
        print(f"Checked {count} Qoder skills in .qoder/skills + plugin mirror")
        return

    print(f"Generated {count} Qoder skills in .qoder/skills + plugin mirror")


if __name__ == "__main__":
    main()
