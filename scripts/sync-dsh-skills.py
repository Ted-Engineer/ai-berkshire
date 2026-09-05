#!/usr/bin/env python3
"""Generate DSH (DeepSeek Harness) project-level skills from AI Berkshire canonical sources.

Canonical source: skills/*.md
Output:          .dsh/skills/<name>/SKILL.md

DSH discovers project-level skills at <projectRoot>/.dsh/skills (rank 100, the
highest local-discovery priority). This mirrors scripts/sync-codex-skills.py and
scripts/sync-trae-skills.py so Claude Code, Codex, TRAE, and DSH users share one
canonical workflow defined in skills/*.md.

Usage:
  python3 scripts/sync-dsh-skills.py          # generate/update
  python3 scripts/sync-dsh-skills.py --check  # verify only, no writes
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_SKILLS = ROOT / "skills"
DSH_SKILLS = ROOT / ".dsh" / "skills"

# ---------------------------------------------------------------------------
# Per-skill Chinese descriptions (what + when-to-invoke).
# Platform-neutral; shared shape with the Codex/TRAE generators.
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _skill_descriptions import SKILL_DESCRIPTIONS as DSH_DESCRIPTIONS


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


def dsh_frontmatter(name: str) -> str:
    desc = DSH_DESCRIPTIONS.get(name, f"AI Berkshire 投研技能:{name}")
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {yaml_quote(desc)}\n"
        "---\n\n"
    )


def dsh_adapter_note(name: str, source_name: str) -> str:
    """Generate the DSH adapter note mapping Claude-only surfaces to DSH tools."""
    return (
        "## DSH adapter note\n\n"
        f"This skill is generated from `skills/{source_name}` so Claude Code, Codex, TRAE, "
        "and DSH users share one canonical workflow. DSH discovers it as a project-level skill "
        f"at `.dsh/skills/{name}/SKILL.md` (rank 100, highest local priority).\n\n"
        "- Treat `$ARGUMENTS` as the user's request in the current DSH session.\n"
        "- Map Claude-only surfaces to the DSH tools available in this session:\n"
        "  - `Task`(单个后台子代理)→ DSH `subagent`(默认后台运行,可在同一条消息里并行启动多个)。\n"
        "  - `TaskCreate`(创建多个并行子任务)→ 并行启动多个 `subagent`;当需要大规模 fan-out "
        "编排(几十个 agent、多阶段、结构化结果)时用 `workflow`。\n"
        "  - `WebSearch` / `WebFetch` → DSH `web_search`(始终可用,无需 "
        "`.claude/settings.local.json` 白名单;`WebFetch` 抓全文的能力用 `web_search` 返回的"
        "来源 URL + snippet 替代)。\n"
        "  - `Bash` → DSH `bash`。\n"
        "  - `Read` / `Write` / `Edit` / `Glob` / `Grep` → DSH 同名工具。\n"
        "  - `Skill` → DSH `skill`(用于调用其他 ai-berkshire skill)。\n"
        "  - `TodoWrite` → DSH `todo_write`。\n"
        "- 配套 Python 工具原地可用:在仓库根目录运行 `python3 tools/financial_rigor.py ...` / "
        "`python3 tools/report_audit.py ...` 等(零外部依赖,见 CLAUDE.md 工具表)。DSH skill 为"
        "项目级部署,工具路径相对项目根直接生效。\n"
        "- 引用其他 skill(如 `skills/financial-data.md`)时,优先用 `skill` 工具按名字加载"
        "(如 `financial-data`),而非读相对路径文件。\n"
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
        DSH_SKILLS.mkdir(parents=True, exist_ok=True)

    count = 0
    stale: list[str] = []
    for source in sorted(CLAUDE_SKILLS.glob("*.md")):
        name = source.stem
        source_text = source.read_text(encoding="utf-8")

        # Strip existing frontmatter (if any, e.g. news-pulse.md)
        _, body = split_frontmatter(source_text)

        target_dir = DSH_SKILLS / name
        target = target_dir / "SKILL.md"
        content = (
            dsh_frontmatter(name)
            + dsh_adapter_note(name, source.name)
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
            print("DSH skills are out of date:")
            for path in stale:
                print(f"  {path}")
            raise SystemExit(1)
        print(f"Checked {count} DSH skills in {DSH_SKILLS.relative_to(ROOT)}")
        return

    print(f"Generated {count} DSH skills in {DSH_SKILLS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
