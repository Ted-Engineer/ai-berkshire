---
name: daily-brief
description: "AI Berkshire skill: 每日投研简报：行情+新闻+组合监控+操作信号. Source: skills/daily-brief.md."
---

## Codex adapter note

This skill is generated from `skills/daily-brief.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# 每日投研简报：行情+新闻+组合监控+操作信号

对 $ARGUMENTS 执行每日投研工作流。无参数时自动读取 portfolio-latest.md 获取持仓列表。

## 执行流程

### Step 1: 行情 + 持仓核对（主线程，30秒）

```bash
date
python tools/fetch_quotes.py {所有持仓ticker} 2>/dev/null
```
Read `reports/portfolio-latest.md` 确认持仓。计算每只股票盈亏%、仓位%、总资产。

### Step 2: 新闻脉搏（WebSearch并行）

对持仓股搜索最近48小时新闻：
- `"{持仓股} stock news today"`
- `"{近期财报股} earnings results"`
- `"US stock market today S&P NASDAQ"`
- `"earnings calendar this week"`

### Step 3: 异动检测 + 信号生成

| 检测项 | 阈值 | 动作 |
|--------|------|------|
| 单日涨跌 | >±5% | ⚠️ 归因 |
| 仓位超限 | >20% | 🔻 建议减仓 |
| 仓位过小 | <3% | ⚠️ 标注 |
| 财报当天 | — | 📊 财报速读 |
| 重大新闻 | 并购/监管/诉讼 | 🚨 评估 |
| 触及止损 | -12% | 🛑 预警 |

### Step 3.5: 触发价扫描（watchlist + catalysts）

Read `config/watchlist.md`（价格触发）与 `config/catalysts.md`（日期触发）：

- 现价进入触发价区间（或距触发价 ±3% 以内）→ 🔔 在简报顶部显著标注"XX 触发/接近触发"，提示按零复用铁律重跑 `/investment-checklist {标的}` 后再决策
- catalysts 中 7 天内到期的事件 → 🔔 同样置顶标注（事件名+判据+预设动作）
- 条目超 30 天未重验 → 标注 `⚠️需重验`
- 本步骤只提醒不构成买入指令（8-13 NBIS 踏空的结构性补丁）

### Step 4: 输出简报

写入 `reports/daily/daily-{YYYYMMDD}.md`：

---

## 📋 {日期} 投研简报

**总资产**：$XXX | **现金**：$XXX (XX%) | **持仓**：X只

### 组合快照
| 股票 | 股数 | 现价 | 日涨跌 | 盈亏% | 仓位 | 信号 |
|------|:----:|------|:------:|:-----:|:----:|:----:|

### 新闻脉搏
| 股票 | 重大事件？ | 影响 | 深度研究？ |

### 组合健康
- 最大仓位 / 现金水平 / 止损预警 / FCF红线

### 催化剂日历（7天内）

### 触发价扫描（watchlist）
> "今日无触发" 或 🔔 触发标的+对应动作

### 操作建议
> "今日无需操作" 或 明确动词+理由

---

## 触发深度研究的条件

| 信号 | 建议Skill |
|------|----------|
| 财报发布 | `/earnings-review {股票名}` |
| 单日跌>8% | `/news-pulse {股票名}` |
| 仓位>20%持续 | `/portfolio-review` |
| 止损-12% | 立即讨论执行 |
| 现金>40%+市场跌>5% | `/industry-funnel` |

## 规则

1. 不启动后台Agent——全部主线程完成
2. 只搜48小时内新闻
3. 只给明确信号——禁止"建议关注"
4. 财报日追加财报速读
5. 数据标注来源
6. 周末不拉行情，仅输出周总结+下周日历

*本项目仅供学习研究，不构成投资建议。*
