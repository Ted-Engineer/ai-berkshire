# Task Plan: 2026-08-14 持仓调整研究（prompt.md v3）

## Goal
基于本次实时数据，对当前10只持仓给出单一动词操作信号，扫描≥200只候选，经 checklist + investment-team 双重验证后输出 Top 2 与可执行调仓方案（持仓≤10只）。

## Current Phase
Phase 1

## Phases

### Phase 1: 持仓核实 + 异动 + 来源F/G + 规划
- [x] date 确认：2026-08-14 00:21 UTC+8
- [x] Read portfolio-latest.md（8-13 23:20 用户确认）
- [x] WebSearch 白名单预检通过
- [ ] 实时行情拉取 + 市值验算
- [ ] 当日异动扫描（movers / earnings beat）
- [ ] 来源F：Read相关memory → 提取ticker清单
- [ ] 来源A：提取待执行/观察/计划项
- [ ] 来源G：对每只持仓搜供应商/客户
- **Status:** in_progress

### Phase 2: 持仓股从零研究（10只 × investment-team）
- [ ] META / BABA / MSFT / ADBE / AVGO
- [ ] BRK.B / INTU / TSM / PYPL / CI
- [ ] 每只一句话判断 + 单一动词
- **Status:** pending

### Phase 3: 行业分布评估（第二步半）
- [ ] 脚本计算五类占比 + 校验行=100%
- [ ] 偏差状态 + 修正方向
- **Status:** pending

### Phase 4: 新候选筛选（来源A-G，≥200只，搜索≥80次）
- [ ] GICS 25组 × 2视角 ≥50
- [ ] AI 15赛道 × 2视角 ≥30
- [ ] 非AI ≥8主题
- [ ] D1-D7 七维
- [ ] /industry-funnel + /bottleneck-hunter
- [ ] candidates.csv ≥200，AI占比≤65%
- **Status:** pending

### Phase 5: Top候选双重验证 + 冒泡终选
- [ ] Top 10-15 过 checklist + investment-team
- [ ] 冒泡排序 Top 2
- [ ] recommended-buys.txt + 验证矩阵
- **Status:** pending

### Phase 6: 最终方案（不覆盖 portfolio-latest.md）
- [ ] reports/portfolio-action-20260814.md
- [ ] 向用户展示执行清单，等待确认
- **Status:** pending

## Key Questions
1. TSM 两张GTC（15@$424 / 15@$390）是否已成交？
2. 8-13后隔夜/盘中持仓或现金是否变化？
3. 现金29.2%超目标（10-20%）→ 本轮必须找部署标的还是等财报？

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| 持仓基线用 8-13 23:20 用户确认版 | 用户未提供新清单；写文件前仍须再确认 |
| 并行Agent按批≤8 | [[agent-concurrency-control]] 用户停过29个 |
| 搜索优先 WebSearch，配额尽切 MCP | prompt 核心约束#6；必须至少用一次 mcp__web-search__search |
| 禁止复用旧评分 | 零复用铁律 |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |

## Notes
- 数据截止基准：2026-08-14
- 本项目仅供学习研究，不构成投资建议
- 用户只看美股（含ADR）
