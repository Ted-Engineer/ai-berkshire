#!/usr/bin/env python3
"""Generate TRAE project-level skills (.trae/skills/) from AI Berkshire canonical skill sources.

Canonical source: skills/*.md
Output:          .trae/skills/<name>/SKILL.md

Usage:
  python scripts/sync-trae-skills.py          # generate/update
  python scripts/sync-trae-skills.py --check  # verify only, no writes
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_SKILLS = ROOT / "skills"
TRAE_SKILLS = ROOT / ".trae" / "skills"

# ---------------------------------------------------------------------------
# Per-skill Chinese descriptions for TRAE (include what + when-to-invoke)
# ---------------------------------------------------------------------------
TRAE_DESCRIPTIONS: dict[str, str] = {
    "bottleneck-hunter": (
        "供应链瓶颈猎手：对超级趋势执行供应链瓶颈扫描、瓶颈定位与投资机会挖掘。"
        "当用户想找「卡脖子」环节的投资标的、分析产业链瓶颈时调用。"
    ),
    "deep-company-series": (
        "看懂XX公司深度系列：撰写3-8篇长文拆解一家公司，发布在公众号/视频号等公开渠道。"
        "当用户想系统性地深度写作一家公司时调用。"
    ),
    "dyp-ask": (
        "段永平问答：扮演段永平（大道至简）本人，用他的思想体系回答投资问题。"
        "当用户想以段永平视角讨论投资决策、生意模式时调用。"
    ),
    "earnings-review": (
        "财报精读：从一手资料（10-K/10-Q/年报PDF）深度解读财报。"
        "当用户想精读一家公司最新季报/年报时调用。"
    ),
    "earnings-team": (
        "财报精读团队：四大师并行解读财报，编辑润色，读者评审，产出可直接发布的公众号文章。"
        "当用户想对财报进行团队化深度分析并输出公开文章时调用。"
    ),
    "financial-data": (
        "财务数据获取与交叉验证规范：定义财务数据来源优先级、双源验证规则、误差处理标准。"
        "此技能由其他投研技能自动引用，当涉及财务数据收集与验证时按本规范执行。"
    ),
    "income-investment": (
        "收入型投资分析：评估公司分红/股息收入的可持续性与吸引力。"
        "当用户想评估股息投资机会、收入型标的时调用。"
    ),
    "industry-funnel": (
        "行业漏斗筛选：从全市场到3家终选标的的价值投资精选流程。"
        "当用户想对某个行业/方向执行漏斗式筛选、从海量标的缩小到核心候选时调用。"
    ),
    "industry-research": (
        "行业投资研究：产业链全景扫描，结合四大师视角进行个股分析。"
        "当用户想系统化研究一个行业的上中下游全貌时调用。"
    ),
    "investment-checklist": (
        "巴菲特价值投资买入前Checklist：六关筛选框架（生意模式/护城河/管理层/财务/估值/安全边际）。"
        "当用户想按巴菲特标准验证一家公司是否值得买入时调用。"
    ),
    "investment-research": (
        "投资研究：巴菲特-芒格-段永平-李录四大师综合分析框架。"
        "当用户想对一家公司进行全套投资研究时调用。"
    ),
    "investment-team": (
        "投研团队：四角色（段永平/巴菲特/芒格/李录）并行分析框架，产出综合研究报告。"
        "当用户想用多Agent并行协作方式深度分析一家公司时调用。"
    ),
    "management-deep-dive": (
        "管理层纵深研究：评估管理层能力、诚信、资本配置记录与激励机制。"
        "当用户想评估一家公司「人」的层面——管理层质量时调用。"
    ),
    "news-pulse": (
        "公司新闻脉搏：股价异动时快速归因，用4个并行Agent侦察事件/政策/对手/情绪。"
        "当持仓股出现异常涨跌（单日±5%或一周±10%），需要快速搞清楚发生了什么时调用。"
    ),
    "portfolio-rebalance": (
        "组合调仓全流程:持仓重研+行业分布体检+全市场候选扫描(300只)+双重准入验证,产出操作信号。"
        "当用户想做周期性调仓决策、生成买卖方案时调用(全量/lite/子集三种模式)。"
    ),
    "portfolio-review": (
        "组合管理：从「研究公司」到「管理组合」——审视持仓结构、集中度风险、再平衡方案。"
        "当用户想评估当前投资组合的健康状况、是否需要调仓时调用。"
    ),
    "private-company-research": (
        "未上市公司研究：多Agent并行深度研究框架，专为未上市/Pre-IPO公司设计。"
        "当用户想研究蚂蚁集团、小红书、SpaceX等未上市公司的投资价值时调用。"
    ),
    "quality-screen": (
        "去劣筛选：7条指标快速排除非一流公司。"
        "当用户想快速筛选股票池、排除烂公司或平庸公司时调用。"
    ),
    "thesis-drift": (
        "投资论文漂移检测：区分事实变化与措辞变化，判定论文是否仍有效。"
        "当用户想检查对某公司的投资论文是否仍然成立时调用。"
    ),
    "thesis-tracker": (
        "投资论文追踪：买入后的纪律维护系统，持续跟踪核心论据是否被破坏。"
        "当用户想持续监控已持有公司的核心投资逻辑时调用。"
    ),
    "wechat-article": (
        "微信公众号文章：作者-编辑-读者三Agent协作，产出可直接发布的公众号深度文章。"
        "当用户想将投资研究内容转化为公众号文章时调用。"
    ),
}


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Split frontmatter (--- ... ---) from body. Returns (frontmatter_text or None, body)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :].lstrip("\n")


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def yaml_quote(value: str) -> str:
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def trae_frontmatter(name: str) -> str:
    desc = TRAE_DESCRIPTIONS.get(name, f"AI Berkshire 投研技能：{name}")
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {yaml_quote(desc)}\n"
        "---\n\n"
    )


def trae_adapter_note(name: str, source_name: str) -> str:
    """Generate TRAE adapter note explaining tool mapping."""
    return (
        "## TRAE adapter note\n\n"
        f"This skill is generated from `skills/{source_name}` so Claude Code, "
        "Codex, and TRAE users share one canonical workflow.\n\n"
        "- Treat `$ARGUMENTS` as the user's request in the current TRAE session.\n"
        "- When the source mentions Claude-only surfaces, use the following TRAE equivalents:\n"
        "  - `Bash` / shell commands → TRAE `RunCommand` (PowerShell).\n"
        "  - `TeamCreate` / `TaskCreate` / `TaskUpdate` → TRAE `Task` tool (subagent types: "
        "general_purpose_task, Explore, Plan).\n"
        "  - `WebSearch` permission pre-check (`.claude/settings.local.json`) → "
        "**Not needed in TRAE**: WebSearch is always available, no permission white-list required.\n"
        "  - `python tools/xxx.py` → TRAE can use `python tools/xxx.py` or `python tools/xxx.py` "
        "from the repository root. Run commands from the repo root (f:\\ai-berkshire) with "
        "`RunCommand`.\n"
        "  - `Read` / `Write` / `SearchReplace` / `Glob` / `Grep` → Same tools available in TRAE.\n"
        "  - `WebFetch` / `WebSearch` → Same tools available in TRAE.\n"
        "  - `Skill` tool → Same in TRAE (for invoking other AI Berkshire skills).\n"
        "- Use shared project tools from `tools/` in this repository. Prefer running commands from "
        "the repository root with paths like `python tools/financial_rigor.py ...`.\n"
        "- Before starting research, run the `date` command to confirm today's date; treat it as "
        "the baseline for \"latest\" data and state the data cutoff date in the report header. "
        "Never assume the current date from training data.\n"
        "- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use "
        "exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.\n"
        "- Report output follows the same naming convention: `reports/{company}/` or "
        "`reports/{company}-{type}-{YYYYMMDD}.md`.\n\n"
    )


def main() -> None:
    check = "--check" in sys.argv[1:]
    unknown_args = [arg for arg in sys.argv[1:] if arg != "--check"]
    if unknown_args:
        raise SystemExit(f"Unknown argument(s): {', '.join(unknown_args)}")

    if not check:
        TRAE_SKILLS.mkdir(parents=True, exist_ok=True)

    count = 0
    stale: list[str] = []
    for source in sorted(CLAUDE_SKILLS.glob("*.md")):
        name = source.stem
        source_text = source.read_text(encoding="utf-8")

        # Strip existing frontmatter (if any, e.g. news-pulse.md)
        _, body = split_frontmatter(source_text)

        target_dir = TRAE_SKILLS / name
        target = target_dir / "SKILL.md"
        content = (
            trae_frontmatter(name)
            + trae_adapter_note(name, source.name)
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
            print("TRAE skills are out of date:")
            for path in stale:
                print(f"  {path}")
            raise SystemExit(1)
        print(f"Checked {count} TRAE skills in {TRAE_SKILLS.relative_to(ROOT)}")
        return

    print(f"Generated {count} TRAE skills in {TRAE_SKILLS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()