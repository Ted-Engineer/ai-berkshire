# Findings — 2026-08-14 持仓调整

## Requirements
- 持仓≤10只；每标的单一动词+触发条件
- 期限1-6个月；零复用旧研究
- 行业分布符合顶层设计，偏离>10%必须修正
- 候选≥200；搜索≥80；AI候选≤65%
- 新建/换仓必须 checklist + investment-team
- 来源A/F/G必选并展示证据
- 写 portfolio-latest.md 前必须用户确认成交

## Research Findings

### 持仓基线（8-13 23:20 用户确认，尚未用本次行情重算）
| 股票 | 股数 | 成本 | 类别 | 备注 |
|------|------|------|------|------|
| META | 80 | $604.78 | AI平台 | 15.3% |
| BABA | 245 | $121.69 | 非AI价值 | 8/20财报框架 |
| MSFT | 60 | $333.194 | AI软件 | |
| ADBE | 90 | $217.267 | AI软件 | 9/10财报 |
| AVGO | 55 | $416.00 | AI硬件 | 8-13新建 |
| BRK.B | 30 | $508.6 | 非AI价值 | 防御 |
| INTU | 40 | $319.49 | AI软件 | 8/25财报 |
| TSM | 30 | $416.806 | AI硬件 | GTC 15@$424 + 15@$390 |
| PYPL | 200 | $58.95 | 非AI价值 | 金融/周期 |
| CI | 40 | $271.975 | 非AI价值 | 医疗 |
| 现金 | — | $89,810.60 | 现金 | 29.2% 超目标 |

8-13分布（旧价，待重算）：AI平台15.3 / AI软件21.6 / AI硬件11.8 / 非AI22.2 / 现金29.2
偏差预告：现金🔴超目标；AI硬件⚠️低配；非AI⚠️低配；AI软件⚠️略超

### 来源A — portfolio-latest 待执行/观察
- TSM 买15股 @$424（纪律价，开盘曾探$423.12未接）
- TSM 买15股 @$390（30天，8-8 checklist加仓区上限）
- BABA 8/20：云>40%+FCF改善=加仓；跌破$105或1260H升级NS-CMIC=清仓
- INTU 8/25 超预期=加仓信号
- ADBE 9/10 持有观察
- CRM 8/26 已清仓，仅跟踪

### 来源F — 已Read的memory文件 → 提取ticker
| memory文件 | 提取的ticker |
|------------|--------------|
| user-portfolio-holdings.md | META BABA MSFT ADBE AVGO BRK.B INTU TSM PYPL CI CRM CRCL ACN UBER QCOM TLN RARE BR |
| never-assume-holdings.md | （流程，无新ticker） |
| portfolio-action-20260812-result.md | META PYPL BABA CRCL ACN MSFT CI EOG NRG TXT CRDO LMT ZTS |
| next-crcl-nbis-research-20260730.md | CRCL NBIS AUR TEM BTBT OKLO ACHR LEU RCAT IONQ |
| next-crcl-nbis-search-v2.md | CRDO LEU CRWV ALAB MU ORCL CRSP APLD IREN RKLB HOOD SOFI APP TTD JOBY VRT COHR HUT GTBIF |
| nbis-crcl-loop-final-17rounds.md | DOCS CRDO LEU FOUR DUOL |
| market-scan-aug11-v2.md | META PYPL CRCL RARE TSM PLTR DDOG SNOW HUBS WDAY GEV HEI NRG LMT |
| sector-scan-consumer-financial-industrial-20260811.md | META AXP NOC GOOGL V MA JPM GM DIS RKLB TSLA AAPL FI HOOD COIN ETN TER EMR ROK FTNT PANW CRWD ZS OKTA RTX WMT COST SBUX NKE CHKP |
| search-diversity-enriched.md | （流程） |
| baba-research-20260811.md | BABA（待续读） |
| intu-research-20260807.md | INTU |
| avgo-research-20260806.md | AVGO |
| tsm-research-20260808.md | TSM |
| qcom-research-20260806.md | QCOM |
| fico-research-20260807-v2.md | FICO |
| uber-lilu-research-20260809.md | UBER |
| orcl-research-20260801.md | ORCL |

**反复出现未执行标的（优先纳入候选）**：NBIS, CRDO, LEU, FICO, QCOM, GOOGL, AXP, NOC, AUR, TEM, BR（曾错记，未买）

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| 持仓研究分批≤8 Agent | 用户曾停29个 |
| 搜索用 WebSearch + mcp__web-search__search | fallback链+hook要求MCP至少1次 |
| 分布百分比一律脚本生成 | [[tool-before-mental-math]] |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| recommended-buys.txt 已有今日失败残留（# no new buys，理由是配额） | 本轮作废，从零重跑，禁止沿用 |

## Resources
- reports/portfolio-latest.md
- prompt.md
- tools/fetch_quotes.py
- tools/financial_rigor.py
