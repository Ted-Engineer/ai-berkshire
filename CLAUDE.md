# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# AI Berkshire — 项目指令

## 项目概述

基于 Claude Code 的价值投资研究 Skill 合集。四大师框架：巴菲特、芒格、段永平、李录。
GitHub: Ted-Engineer/ai-berkshire

## 相关文件指引（避免重复）

| 文件 | 内容 | 何时查阅 |
|------|------|---------|
| **`CLAUDE.md`**（本文件） | 项目核心指令 + 代码架构 + 投资方法论 | 每次必读 |
| **`AGENTS.md`** | Codex + TRAE 兼容 + 跨工具同步脚本 | 修改 skills/tools 后 |
| **`ai_CLAUDE.md`** | AI 记忆文件：用户偏好 + 历史决策 | 不熟悉项目演进时 |
| **`CONTEXT.md`** | 术语表（研报套餐、密钥、Worker 引擎等 SaaS 概念） | 涉及 SaaS 产品文案时 |
| **`skills/financial-data.md`** | 财务数据获取规范（双源交叉验证） | 涉及财务数据时 |
| **`CONTRIBUTING.md`** | 贡献规范 | 提交 PR 时 |

---

## 代码架构与结构

### 顶层目录

```
skills/        — 投研 Skill 定义（Markdown），通过 Skill 工具调用
codex-skills/  — 同步生成的 Codex Skill（自动从 skills/ 生成，不手动编辑）
codex-prompts/ — Codex slash prompt 兼容层（自动生成）
.trae/skills/  — 同步生成的 TRAE Skill（自动从 skills/ 生成，不手动编辑）
tools/         — Python 数据/验证工具（financial_rigor.py / report_audit.py 等）
scripts/       — 同步脚本（sync-codex-skills.py / sync-trae-skills.py 等）
reports/       — 投资研究报告输出（按公司建文件夹）
assets/        — 图片等静态资源
docs/          — 项目文档
data/          — 临时数据缓存
```

### `tools/` 核心 Python 工具

| 工具 | 用途 | 关键子命令 |
|------|------|-----------|
| `financial_rigor.py` | 精确十进制算术 + 估值验证 | `verify-market-cap` / `verify-valuation` / `three-scenario` / `cross-validate` |
| `report_audit.py` | 报告数据抽检工具 | `extract`（15% 抽样） / `verdict`（准出/打回判决） |
| `realtime_fetch.py` | 实时行情（基于 yfinance） | 批量获取 PE/市值/财务指标 |
| `fetch_quotes.py` | 行情拉取（Yahoo Finance v8 + SSL verify=False） | 用于绕过 yfinance SSL 问题 |
| `twstock_data.py` | 台股专用（FinMind 数据源） | `quote` / `valuation` / `financials` / `revenue` |
| `ashare_data.py` | A 股数据获取 | — |
| `xueqiu_scraper.py` | 雪球数据爬虫 | — |
| `morningstar_fair_value.py` | Morningstar 公允价值 | — |
| `momentum_backtest.py` / `_v2.py` | 动量回测 | — |
| `stock_screener.py` | 股票筛选器 | — |
| `star_history_chart.py` | 历史 K 线图 | — |

**注意**：`tools/` 工具**零外部依赖**（仅 Python stdlib），除 `realtime_fetch.py` 需要 `yfinance`。

### `skills/` 核心 Skill

- `industry-funnel.md` — 行业漏斗筛选
- `bottleneck-hunter.md` — 供应链瓶颈扫描
- `investment-team.md` — 四角色并行分析
- `investment-checklist.md` — 巴菲特六关清单
- `investment-research.md` — 投资研究综合框架
- `industry-research.md` — 行业研究
- `earnings-review.md` / `earnings-team.md` — 财报精读
- `thesis-tracker.md` / `thesis-drift.md` — 买入后追踪
- `portfolio-review.md` — 组合管理
- `management-deep-dive.md` — 管理层纵深
- `news-pulse.md` — 公司新闻脉搏
- `quality-screen.md` — 去劣筛选
- `deep-company-series.md` — 深度公司系列
- `wechat-article.md` — 公众号文章
- `private-company-research.md` — 未上市公司
- `income-investment.md` — 收入型投资
- `financial-data.md` — 财务数据规范
- `dyp-ask.md` — 段永平问答

### `scripts/` 同步脚本（修改 skills/ 后必跑）

```bash
python scripts/sync-codex-skills.py        # 同步 codex-skills/
python scripts/sync-trae-skills.py         # 同步 .trae/skills/（TRAE 项目级 skill）
python scripts/sync-codex-prompts.py       # 同步 codex-prompts/（可选）
python scripts/sync-codex-skills.py --check  # 仅检查不写入
python scripts/sync-trae-skills.py --check   # 仅检查 TRAE skill 不写入
```

---

## 报告目录结构

所有报告按**公司名**建文件夹，公司相关的所有报告放在对应文件夹内：

```
reports/
├── AI产业研究/              — AI产业链全景研究（置顶）
├── 腾讯/                    — 腾讯所有研究报告
├── 拼多多/                  — 拼多多所有研究报告
├── 泡泡玛特/                — 泡泡玛特所有研究报告
├── 核电-industry-20260409.md — 行业报告放根目录
├── AI算力-funnel-20260509.md  — 漏斗筛选报告放根目录
├── AI-轮动判断-20260509.md    — 主题级综合判断报告放根目录
├── portfolio-latest.md       — 组合报告放根目录（持续更新）
└── 多公司对比-checklist-20260408.md — 多公司报告放根目录
```

## 报告命名规范

| Skill | 文件命名格式 | 示例 |
|------|---------|------|
| /investment-team | `{公司名}/` 目录内含4个视角+最终报告 | `reports/拼多多/最终报告.md` |
| /investment-research | `{公司名}-research-{YYYYMMDD}.md` | `reports/腾讯/腾讯-research-20260408.md` |
| /investment-checklist | `{公司名}-checklist-{YYYYMMDD}.md` | `reports/腾讯/腾讯-checklist-20260408.md` |
| /industry-research | `{行业名}-industry-{YYYYMMDD}.md`（根目录） | `reports/核电-industry-20260409.md` |
| /industry-funnel | `{行业名}-funnel-{YYYYMMDD}.md`（根目录） | `reports/AI算力-funnel-20260509.md` |
| /private-company-research | `{公司名}-private-{YYYYMMDD}.md` | `reports/字节跳动/字节跳动-private-20260408.md` |
| /earnings-review | `{公司名}-earnings-{期间}.md` | `reports/腾讯/腾讯-earnings-2025Q4.md` |
| /earnings-team | `{公司名}/` 目录内含4个大师视角+研究底稿+公众号文章+读者评审 | `reports/腾讯/腾讯-earnings-2025Q4.md`（公众号定稿） |
| /thesis-tracker | `{公司名}-thesis.md`（长期维护） | `reports/腾讯/腾讯-thesis.md` |
| /portfolio-review | `portfolio-latest.md`（根目录，持续更新） | `reports/portfolio-latest.md` |
| /management-deep-dive | `{公司名}-management-{YYYYMMDD}.md` | `reports/腾讯/腾讯-management-20260409.md` |

## /investment-team 文件结构

```
reports/{公司名}/
├── README.md                         — 研究框架概览+核心结论
├── 01-商业模式分析-段永平视角.md
├── 02-财务估值分析-巴菲特视角.md
├── 03-行业竞争分析-芒格视角.md
├── 04-风险管理层评估-李录视角.md
└── 最终报告.md                       — Team Lead 综合报告
```

---

## 常用开发命令

### Skill 同步（修改 skills/ 后必跑）

```bash
python scripts/sync-codex-skills.py         # 同步到 codex-skills/
python scripts/sync-trae-skills.py          # 同步到 .trae/skills/（TRAE 项目级 skill）
python scripts/sync-codex-skills.py --check # 仅检查
python scripts/sync-trae-skills.py --check  # 仅检查 TRAE skill
```

### 工具验证

```bash
# 市值手算校验
python tools/financial_rigor.py verify-market-cap \
  --price 510 --shares 9.11e9 --reported 4.65e12 --currency HKD

# 估值验算
python tools/financial_rigor.py verify-valuation \
  --price 510 --eps 23.5 --bvps 120 --fcf-per-share 18

# 三情景估值
python tools/financial_rigor.py three-scenario \
  --price 510 --eps 23.5 --shares 9.11 \
  --growth 0.15 0.10 0.05 \
  --pe 22 18 14 --currency HKD

# 报告审计
python tools/report_audit.py extract --report reports/xxx.md
python tools/report_audit.py verdict \
  --results '[{"id":1,"label":"...","reported_value":...}]' \
  --report xxx
```

### 实时取数（注意 SSL）

`tools/realtime_fetch.py`（yfinance）在 Windows 中文路径下会因 SSL 证书路径报错。**绕开方案**：
- 使用 `tools/fetch_quotes.py`（Yahoo Finance v8 + `verify=False`）
- 或复制 `cacert.pem` 到无中文路径

### Git 操作

```bash
cd ~/ai-berkshire
git pull --rebase origin main   # 推送前必跑（远程经常有新提交）
git add reports/xxx.md
git commit -m "中文描述改了什么"
git push origin main
```

---

## 投研分析核心原则（最高优先级）

- **客观、客观、客观**——所有投研分析必须基于事实和数据，严禁主观臆断
- 严格区分"事实"与"观点"：事实用数据支撑，观点必须明确标注为"观点"或"推测"
- **不预设立场**：不预设看多或看空，先摆数据、再推逻辑、最后得结论。结论必须从数据中自然推出
- 禁止使用"我认为"、"我觉得"、"显然"等主观表述，改用"数据显示"、"证据表明"、"根据XX来源"
- **呈现正反两面**：每个核心判断都必须附带反面论据（"但另一方面..."），让读者自己权衡
- 对不确定的事情诚实说"不确定"或"数据不足"，不要用推测填充确定性
- 所有skill（investment-team、investment-research、earnings-review等）在执行时都必须遵守以上原则
- **价值股 vs 成长股区分评估**：FCF为负≠必然排除。对于收入增速>100%且有大量合同积压（backlog）的基建期成长股（如AI Cloud运营商），应使用"收入增速+合同积压+客户质量"框架评估，而非套用FCF红线。在报告中明确标注"价值股评估"或"成长股评估"

## 研究质量规则（必读）

- **每次研究开始前**，必须执行 `date` 命令确认今天日期，作为"最新数据"的基准，并在报告头部标注数据截止日期
- **记忆系统使用规范（必读·NBIS教训）**：
  - MEMORY.md索引在每次会话自动注入上下文，但**索引≠内容**
  - 执行涉及"候选筛选""新标的搜索""持仓调整"的任务时，**必须Read与任务相关的memory文件**，提取用户曾研究的具体ticker
  - 特别关注：反复出现在多条记忆中的标的（如"next XXX搜索"系列中的XXX本身）
  - 报告中必须列出"读取了哪些memory文件→提取了哪些候选ticker"作为执行证据
  - ❌ 只说"已检索memory"但不展示读取了哪些文件=未执行
- 关键财务数据**至少 2 个独立来源交叉验证**（美股：macrotrends+stockanalysis；港股：aastocks+macrotrends；A股：东方财富+巨潮资讯；台股：FinMind + Goodinfo）
- **高成长股数据补充来源**：对于收入增速>100%的标的，macrotrends/stockanalysis数据可能滞后，须补充公司IR页面最新季度财报、管理层指引（guidance）、合同积压（backlog/RPO）数据
- 所有估计值必须注明"估计"
- 市值必须手算校验：股价 × 总股本 vs 报告市值（用 `financial_rigor.py verify-market-cap`）
- 货币单位要明确（港币/人民币/美元/新台币），防止混淆
- 报告写完后主动询问是否推送到 GitHub

## 报告语言与风格

- 所有报告使用**中文**
- 风格：直接、犀利、不说废话
- 数据必须标注来源，关键数据至少 2 个来源交叉验证
- 评分使用 ★ 符号（★1-5），不含半星
- 穿插巴菲特/芒格/段永平/李录的语录点评

## 编辑规则（修改文件时遵守）

- 保留现有报告文件，除非任务明确要求修改
- 修改范围限制在请求的 skill/tool/script/文档
- 修改 `skills/` 任何文件后，运行 `python scripts/sync-codex-skills.py` 和 `python scripts/sync-trae-skills.py`
- 完成 skill/tool 改动前，运行相关语法或生成检查

---

## 注意事项

- **`.learnings/` 知识库**（每次会话自动注入）：SessionStart hook 会把 `.learnings/LEARNINGS.md` / `ERRORS.md` / `FEATURE_REQUESTS.md` 的摘要注入每个新会话上下文（`scripts/learnings-digest.sh`，配置在 `.claude/settings.json`）。涉及其中条目时按需展开对应文件；全量复盘在 `.learnings/session-summary-2026-08-09.md`。`.learnings/` 已在 .gitignore（本地私有）
- **WebSearch 权限预检**（关键）：用 Skill 工具启动后台 Agent 前，先确认 `.claude/settings.local.json` 含 `"WebSearch"` 白名单，否则后台 Agent 会静默退化为仅凭训练知识作答
- **搜索词多样性**（防止价值偏见）：投研搜索不可全部使用"undervalued"关键词。高成长/高催化标的（如AI Cloud运营商、财报异动股）需要用"growth""momentum""earnings beat""contract backlog"等搜索词。至少30%的搜索使用非"undervalued"关键词
- **异动快速反应**：执行任何投研任务时，首先WebSearch "biggest stock movers today"检查当日异动。如发现用户曾关注标的（memory中有记录）异动>10%，立即纳入评估
- **数据时效**：所有价格/财务数据必须标注数据截止日期
- **诚实原则**：宁可在报告中留白标注"数据不足"，也不要推测填充
- **本项目仅供学习研究，不构成投资建议**
