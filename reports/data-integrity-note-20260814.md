# 数据完整性说明 — 2026-08-14

## 价格基准决策
**采用 portfolio-latest.md 用户确认价（8/13成交价）为权威基准。**

### 原因
- portfolio-latest.md 标注"用户确认实际成交价"，且盈亏率内部一致：
  - MSFT: $495.885/$333.194 = +48.8% ✓ (与表中+48.8%一致)
  - AVGO: 8/13新建@$416.00 = 接近市场价 (若市场为$528则限价单不可能成交)
- Subagent A (9d2f920f) 返回价格 (META $754/MSFT $570/AVGO $528/TSM $547) 与用户确认价差15-28%
- 单日15-28%涨幅不可能：S&P 500 8/13仅因软通胀数据创普通新高，无META单日+28%新闻
- Subagent称其数据来自stockanalysis.com(Yahoo 403)，可能为缓存/错误数据

### 处理
- **价格/市值/分布**: 全部采用 portfolio-latest.md 用户确认价
- **Subagent定性发现** (FCF趋势/财报beat/催化剂): 价格无关，可采信
  - META: Q2 FCF骤降至$784M，CapEx上调至$130-145B，Zuckerberg"超智宣言"8/11
  - MSFT: Azure FY27Q1指引+45% CC，EPS beat
  - ADBE: YTD -37.5%，$25B回购，FCF yield 9.6% (最便宜)
  - AVGO: AI半导体$10.8B (+143%)，record Q2
  - TSM: 7月营收NT$467.58B纪录(+44.7% YoY)，上调Q3指引

### 行动
- 最终报告所有数字基于 portfolio-latest.md 价 + financial_rigor.py 脚本计算
- Subagent定性发现作为辅助论据，不作为价格数据源
