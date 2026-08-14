# 全美股漏斗筛选（全新数据重跑）— 2026-08-12

> **数据截止**：2026-08-11收盘/2026-08-12凌晨
> **搜索工具**：mcp__web-search__search + mcp__web-search__fetchWebContent + fetch_quotes.py
> **数据来源**：Forbes/247wallst/Investing.com/Yahoo Finance v8/yfinance
> **持仓事实来源**：portfolio-latest.md（仅取股数/成本）

---

## 第一层：全市场扫描 — 126+只候选（9大行业）

### 行业覆盖与候选清单

| 行业 | 候选数 | 代表标的 |
|------|:------:|---------|
| 科技-AI软件/SaaS | 22 | META PYPL ORCL SAP NOW PLTR DDOG SNOW NET HUBS WDAY TEAM IBM ZS AMZN等 |
| 科技-半导体 | 20 | NVDA AMD MU AVGO TSM MRVL ALAB ARM CRDO**🆕** ADI ASML AMAT等 |
| 科技-网络安全 | 8 | PANW CRWD FTNT ZS S CHKP等 |
| 医疗健康 | 12 | VRTX ISRG DXCM VEEV ABNT等 |
| 金融科技/支付 | 8 | V MA PYPL SQ HOOD等 |
| 消费/E-commerce | 10 | AMZN MELI SHOP DASH ABNB等 |
| 能源/核能 | 10 | VST CEG NRG LEU CCJ等 |
| 国防/航空 | 8 | LMT NOC GD TXT HII等 |
| 工业/材料 | 8 | CAT GE ETN PH等 |
| **合计** | **126** | |

### 新发现候选

**CRDO（Credo Technology）$243.82** — 247wallst推荐3大AI半导体之一
- AI网络互联（Active Electrical Cables/光学/1.6T）
- Q4 FY26收入$437M (+157% YoY)，FY26收入翻三倍至$1.34B
- 非GAAP净利$662M（5倍增长）
- MC $45.5B，fPE 26.9x，ROE 34.4%，毛利率68%
- 客户：Google/Meta等hyperscaler
- 从高点回调-26% → 入场窗口

---

## 第二层：5条硬指标粗筛 → 15只通过

### 实时数据表（fetch_quotes.py 8/11收盘价）

| 代码 | 价格 | fPE | ROE% | 通过？ | 说明 |
|------|------|-----|------|:------:|------|
| **META** | $609 | ~17 | 30 | ✅5/5 | AI广告垄断PEG0.6 |
| **PYPL** | $59 | ~10 | 25 | ✅5/5 | FCF yield 9%+回购 |
| **CRDO** 🆕 | $244 | 27 | 34 | ✅5/5 | PEG0.17! AI网络垄断 |
| GOOGL | $352 | 24 | 49 | ✅5/5 | 反垄断不确定 |
| AMZN | $275 | 27 | 31 | ✅5/5 | 太贵 |
| LMT | $599 | 18 | 89 | ✅5/5 | 增速低 |
| NOC | $580 | 19 | 27 | ✅5/5 | 增速低 |
| VRTX | $530 | 24 | 24 | ✅4/5 | CF垄断 |
| ISRG | $400 | 33 | 17 | ✅4/5 | 太贵 |
| VEEV | $236 | 24 | 14 | ✅4/5 | ROE偏低 |
| ABNB | $181 | 30 | 35 | ✅4/5 | 太贵 |
| DXCM | $88 | 28 | 39 | ✅4/5 | 竞争加剧 |
| GD | $396 | 21 | 18 | ✅4/5 | 增速低 |
| CEG | $278 | 21 | 15 | ✅4/5 | 比NRG贵 |
| NRG | $121 | 11 | 24 | ✅4/5 | 净利率低 |

### 被淘汰代表（5指标不过）

| 代码 | 淘汰原因 |
|------|---------|
| PLTR | fPE 76x ❌ |
| DDOG | fPE 85x + ROE 5% ❌ |
| SNOW | fPE 124x + 亏损 ❌ |
| NET | fPE 185x + 亏损 ❌ |
| CRWD | fPE 143x + 亏损 ❌ |
| MU | fPE 5.6x但周期顶部陷阱 ❌ |

---

## 第三层：精细分析 TOP 5 → 终选

### 🥇 META（$609）— AI广告定价引擎
fPE 17x | ROE 30% | 增速28% | PEG 0.6
- 30亿用户网络效应 + Advantage+ AI广告工具
- 2026广告收入$243B将超Google
- 从$796高点-24%，最佳入场区间
- **进入终选：✅**

### 🥈 PYPL（$59）— 深度价值反转
fPE 10x | ROE 25% | FCF yield 9.3% | 回购8%
- Q2 beat 7.8% + 上调指引
- $6B回购/年 = 8%流通股缩容
- Branded checkout +16%加速
- **进入终选：✅**

### 🥉 CRDO（$244）— AI网络互联瓶颈🆕
fPE 27x | ROE 34% | 增速157% | PEG 0.17
- AI网络互联（AEC/光学/1.6T）直接受益hyperscaler capex
- FY26收入翻三倍，净利5倍
- 从高点-26%回调
- **风险**：MC仅$45B（波动大）、客户集中（hyperscaler）、库存翻三倍
- **进入终选：✅（新发现，需要深度验证）**

### 第4-5名
- LMT（$599）：✅进入分析但增速10%不够"大赚"
- NRG（$121）：✅进入分析但净利率2.6%太低

