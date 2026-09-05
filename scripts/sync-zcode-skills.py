#!/usr/bin/env python3
"""Generate ZCode workspace-level skills from AI Berkshire canonical sources.

Canonical source: skills/*.md
Output:          .zcode/skills/<name>/SKILL.md

ZCode discovers workspace skills at <projectRoot>/.zcode/skills (scanned
before .agents/skills within the workspace level). This mirrors
scripts/sync-codex-skills.py, scripts/sync-trae-skills.py, and
scripts/sync-dsh-skills.py so Claude Code, Codex, TRAE, DSH, and ZCode users
share one canonical workflow defined in skills/*.md.

Workflow-enforcement hooks for ZCode live in .zcode/config.json and reuse the
same scripts/*.sh hook programs as Claude Code (see AGENTS.md).

Usage:
  python scripts/sync-zcode-skills.py          # generate/update
  python scripts/sync-zcode-skills.py --check  # verify only, no writes
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_SKILLS = ROOT / "skills"
ZCODE_SKILLS = ROOT / ".zcode" / "skills"

# ---------------------------------------------------------------------------
# Per-skill Chinese descriptions (what + when-to-invoke).
# Shared shape with the Codex/TRAE/DSH generators; keep the wording in sync
# with scripts/sync-dsh-skills.py.
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _skill_descriptions import SKILL_DESCRIPTIONS as ZCODE_DESCRIPTIONS


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


def zcode_frontmatter(name: str) -> str:
    desc = ZCODE_DESCRIPTIONS.get(name, f"AI Berkshire 投研技能:{name}")
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {yaml_quote(desc)}\n"
        "---\n\n"
    )


def zcode_adapter_note(name: str, source_name: str) -> str:
    """Generate the ZCode adapter note mapping Claude-only surfaces to ZCode tools."""
    return (
        "## ZCode adapter note\n\n"
        f"This skill is generated from `skills/{source_name}` so Claude Code, Codex, TRAE, "
        "DSH, and ZCode users share one canonical workflow. ZCode discovers it as a workspace "
        f"skill at `.zcode/skills/{name}/SKILL.md` (project-level, scanned before `.agents/skills`).\n\n"
        "- `$ARGUMENTS` 指本次 Skill 工具调用传入的 `args` 参数。\n"
        "- Map Claude-only surfaces to the ZCode tools available in this session:\n"
        "  - `Task`(后台子代理)→ ZCode `Agent` 工具(同一条消息里发多个 Agent 调用即可并行;"
        "`run_in_background: true` 异步运行,subagent_type 选 `general-purpose` 或 `Explore`)。\n"
        "  - `WebSearch` / `WebFetch` → ZCode 同名工具;受限时切换 MCP 回退链:"
        "`mcp__web-search__search` → `mcp__kepler__web_search` → "
        "`mcp__web-search-prime__web_search_prime`(与 prompt.md 的回退链一致)。\n"
        "  - `Bash` / `Read` / `Write` / `Edit` / `TodoWrite` / `Skill` → ZCode 同名工具"
        "(`Skill` 用于按名字调用其他 ai-berkshire skill)。\n"
        "- 配套 Python 工具在仓库根目录运行:`python tools/financial_rigor.py ...` / "
        "`python tools/report_audit.py ...` 等(零外部依赖,见 CLAUDE.md 工具表;Windows 下无 "
        "`python3` 命令,统一用 `python`)。\n"
        "- 引用其他 skill(如 `skills/financial-data.md`)时,优先用 `Skill` 工具按名字加载"
        "(如 `financial-data`),而非读相对路径文件。\n"
        "- 工作流强制 hook 已在 `.zcode/config.json` 配置,与 Claude Code 共用同一套 "
        "`scripts/*.sh` 与 `.claude/.workflow/` 状态目录:skill 调用与搜索会被自动记录,"
        "Stop 时执行关卡检查(候选数、搜索总量、必跑 skill 等)。\n"
        "- 研究质量规则保留:开始研究前先 `date` 确认今天日期作为「最新数据」基准并在报告头部"
        "标注截止日期;关键财务数据至少 2 个独立来源交叉验证;估值/算术用 `tools/financial_rigor.py`"
        "精确计算;诚实标注低置信结论与数据缺口。\n"
        "- 报告输出沿用既有命名规范:`reports/{公司名}/` 目录 或 "
        "`reports/{公司名}-{type}-{YYYYMMDD}.md`。\n\n"
    )


def main() -> None:
    check = "--check" in sys.argv[1:]
    unknown_args = [arg for arg in sys.argv[1:] if arg != "--check"]
    if unknown_args:
        raise SystemExit(f"Unknown argument(s): {', '.join(unknown_args)}")

    if not check:
        ZCODE_SKILLS.mkdir(parents=True, exist_ok=True)

    count = 0
    stale: list[str] = []
    for source in sorted(CLAUDE_SKILLS.glob("*.md")):
        name = source.stem
        source_text = source.read_text(encoding="utf-8")

        # Strip existing frontmatter (if any, e.g. news-pulse.md)
        _, body = split_frontmatter(source_text)

        target_dir = ZCODE_SKILLS / name
        target = target_dir / "SKILL.md"
        content = (
            zcode_frontmatter(name)
            + zcode_adapter_note(name, source.name)
            + body.rstrip()
            + "\n"
        )

        if check:
            if not target.exists() or target.read_text(encoding="utf-8") != content:
                stale.append(str(target.relative_to(ROOT)))
        else:
            target_dir.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")

        count += 1

    if check:
        if stale:
            print("ZCode skills are out of date:")
            for path in stale:
                print(f"  {path}")
            raise SystemExit(1)
        print(f"Checked {count} ZCode skills in {ZCODE_SKILLS.relative_to(ROOT)}")
        return

    print(f"Generated {count} ZCode skills in {ZCODE_SKILLS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
