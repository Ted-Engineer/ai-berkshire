---
name: daily-brief
description: "每日投研简报:行情+新闻+组合监控+操作信号,无参数时自动读取 portfolio-latest.md。当用户想做每日投研工作流、早间简报时调用。"
---

## DSH adapter note

This skill is generated from `skills/daily-brief.md` so Claude Code, Codex, TRAE, and DSH users share one canonical workflow. DSH discovers it as a project-level skill at `.dsh/skills/daily-brief/SKILL.md` (rank 100, highest local priority).

- Treat `$ARGUMENTS` as the user's request in the current DSH session.
- Map Claude-only surfaces to the DSH tools available in this session:
  - `Task`(单个后台子代理)→ DSH `subagent`(默认后台运行,可在同一条消息里并行启动多个)。
  - `TaskCreate`(创建多个并行子任务)→ 并行启动多个 `subagent`;当需要大规模 fan-out 编排(几十个 agent、多阶段、结构化结果)时用 `workflow`。
  - `WebSearch` / `WebFetch` → DSH `web_search`(始终可用,无需 `.claude/settings.local.json` 白名单;`WebFetch` 抓全文的能力用 `web_search` 返回的来源 URL + snippet 替代)。
  - `Bash` → DSH `bash`。
  - `Read` / `Write` / `Edit` / `Glob` / `Grep` → DSH 同名工具。
  - `Skill` → DSH `skill`(用于调用其他 ai-berkshire skill)。
  - `TodoWrite` → DSH `todo_write`。
- 配套 Python 工具原地可用:在仓库根目录运行 `python3 tools/financial_rigor.py ...` / `python3 tools/report_audit.py ...` 等(零外部依赖,见 CLAUDE.md 工具表)。DSH skill 为项目级部署,工具路径相对项目根直接生效。
- 引用其他 skill(如 `skills/financial-data.md`)时,优先用 `skill` 工具按名字加载(如 `financial-data`),而非读相对路径文件。
- 研究质量规则保留:开始研究前先 `date` 确认今天日期作为「最新数据」基准并在报告头部标注截止日期;关键财务数据至少 2 个独立来源交叉验证;估值/算术用 `tools/financial_rigor.py`精确计算;诚实标注低置信结论与数据缺口。
- 报告输出沿用既有命名规范:`reports/{公司名}/` 目录 或 `reports/{公司名}-{type}-{YYYYMMDD}.md`。

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
