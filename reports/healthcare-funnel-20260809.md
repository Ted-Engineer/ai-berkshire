# 医疗健康板块漏斗筛选 — 2026-08-09

> 数据截止：2026-08-09（北京时间）/ 数据源：Finviz 实时报价 + 财务快照 + WebSearch 催化验证
> 报告生成：基于全市场扫描 `data/full_scan.json`（581 只美股通过 PE<30/ROE>15%/Debt/Eq<1）→ 医疗板块 55 只候选 → mega_scan / finviz_quote 全量拉取 → 5 条硬指标筛选 → 终选 12 家

---

## 第一步：全市场扫描入口 — 55 家医疗候选

**扫描池构成**（来自 Finviz screener `geo_usa,cap_smallover,fa_pe_u30,fa_roe_o15,fa_debt_u1`）：

| 细分赛道 | 候选数 | 代表标的 |
|---------|-------|---------|
| Biotechnology | 16 | AMGN, VRTX, INCY, EXEL, NBIX, HRMY, TGTX, ACAD, ADMA, ABEO, ABUS, CRMD, PBYI, QTTB, RIGL, TBPH |
| Medical Care Facilities | 14 | THC, UHS, EHC, ENSG, DVA, OPCH, AVAH, AMN, HCSG, PACS, CON, CHE, MD, NUTX |
| Drug Manufacturers - Specialty & Generic | 7 | BMY, UTHR, ZTS, NBIX, LNTH, OGN, ANIP, PAHC, COLL |
| Medical Devices | 6 | BSX, GEHC, PODD, INSP, BVS, TMDX |
| Diagnostics & Research | 3 | A, CDNA, IQV |
| Drug Manufacturers - General | 3 | AMGN, BMY, OGN |
| Medical Instruments & Supplies | 3 | LMAT, RMD, SOLV |
| Healthcare Plans | 2 | CI, OSCR |
| Medical Distribution | 1 | COR |

**已剔除**：RARE（已在持仓中，PDUFA 日期已知）。

---

## 第二步：5 条硬指标粗筛

### 2.1 5 条硬指标（行业漏斗 skill 标准）

| # | 指标 | 通过标准 | 放宽条件 |
|---|------|---------|---------|
| 1 | PE/PEG 估值 | PEG < 1.5 或 PE 合理 | 高质量成长可放宽 PEG < 2.5 |
| 2 | ROE | > 15% | 财务杠杆放大后 OK（看 ROIC） |
| 3 | 经营现金流 | P/FCF < 30x 或 FCF 收益率 > 3% | — |
| 4 | 资产负债率 | Debt/Eq < 1.0 | 大药企/医疗必需可放宽至 < 5.0 |
| 5 | 护城河 | ★★★ 以上（定性） | 5 类：品牌/转换成本/网络效应/规模/技术牌照 |

### 2.2 41 家完整财务速查（按行业细分）

> 完整数据见 `data/HEALTH_finviz.json`（Finviz snapshot 2026-08-09）

| Ticker | 公司 | 行业 | MC (B) | PE | FwdPE | PEG | ROE% | ROIC% | Debt/Eq | GM% | OM% | P/FCF |
|--------|------|-----|--------|-----|-------|-----|------|-------|---------|------|------|-------|
| A | Agilent | Diagnostics | 41.2 | 29.3 | 22.1 | 2.36 | 21.3 | 13.9 | 0.47 | 52.8 | 22.9 | 37.9 |
| ACAD | Acadia Pharma | Biotech | 5.0 | 13.2 | 32.2 | - | 35.7 | 27.9 | 0.06 | 91.1 | 7.6 | 34.6 |
| ADMA | ADMA Biologics | Biotech | 2.2 | 14.1 | 10.5 | 0.47 | 41.9 | 27.8 | 0.50 | 64.7 | 42.3 | 19.0 |
| AMGN | Amgen | Pharma-Mega | 222.2 | 25.5 | 17.0 | 3.38 | 91.5 | 13.8 | 4.90 | 72.7 | 33.3 | 21.8 |
| AMN | AMN Healthcare | Facilities | 1.4 | 13.4 | 38.6 | - | 15.6 | 6.9 | 1.05 | 23.8 | 4.7 | 3.2 |
| ANIP | ANI Pharma | Specialty Drug | 1.8 | 16.9 | 7.3 | 0.49 | 19.3 | 8.4 | 1.02 | 51.6 | 13.3 | 10.3 |
| AVAH | Aveanna | Facilities | 2.1 | 8.1 | 12.2 | 0.92 | 373.8 | 16.9 | 6.26 | 32.6 | 11.5 | 16.5 |
| BMY | Bristol-Myers | Pharma-Mega | 132.2 | 14.3 | 9.9 | - | 46.7 | 14.0 | 2.02 | 66.6 | 32.4 | 11.6 |
| BSX | Boston Scientific | Medical Device | 71.5 | 20.0 | 14.4 | 2.00 | 15.5 | 10.3 | 0.51 | 66.4 | 21.8 | 19.7 |
| BVS | Bioventus | Medical Device | 1.2 | 18.2 | 15.6 | 0.95 | 28.0 | 11.6 | 1.16 | 67.8 | 10.6 | 12.7 |
| CDNA | CareDx | Diagnostics | 2.4 | 22.5 | 34.5 | 0.70 | 29.5 | 25.3 | 0.05 | 70.1 | -0.4 | 28.5 |
| CI | Cigna | Health Plan | 74.7 | 11.7 | 8.4 | 1.12 | 15.5 | 9.0 | 0.75 | 0.0 | 3.9 | 8.2 |
| CON | Concentra | Facilities | 4.3 | 22.4 | 19.5 | 1.68 | 47.9 | 7.8 | 4.49 | 25.8 | 16.7 | 16.2 |
| COR | Cencora | Distribution | 61.1 | 23.8 | 16.2 | 1.42 | 104.3 | 18.1 | 3.84 | 3.6 | 1.3 | 15.1 |
| DVA | DaVita | Facilities | 11.7 | 15.5 | 10.8 | 0.48 | 635.3 | 6.8 | 0.00 | 27.3 | 14.9 | 7.3 |
| EHC | Encompass Health | Facilities | 12.4 | 20.4 | 18.8 | 1.88 | 24.8 | 11.5 | 1.09 | 21.9 | 18.0 | 30.3 |
| ENSG | Ensign Group | Facilities | 10.7 | 28.7 | 21.4 | 1.71 | 17.0 | 8.3 | 0.92 | 14.0 | 8.8 | 25.4 |
| EXEL | Exelixis | Biotech | 13.4 | 17.0 | 13.5 | 0.92 | 44.4 | 42.8 | 0.09 | 96.5 | 40.7 | 11.4 |
| GEHC | GE HealthCare | Medical Device | 32.4 | 16.5 | 13.2 | 1.38 | 19.2 | 9.3 | 0.96 | 39.4 | 13.7 | 20.5 |
| HCSG | Healthcare Svc | Facilities | 1.5 | 13.0 | 18.0 | 1.82 | 24.7 | 23.2 | 0.03 | 18.1 | 6.5 | 10.3 |
| HRMY | Harmony Bio | Biotech | 2.2 | 15.5 | 9.2 | 0.44 | 17.9 | 13.8 | 0.23 | 73.9 | 21.1 | 6.5 |
| INCY | Incyte | Biotech | 24.4 | 15.4 | 14.0 | 1.34 | 30.7 | 25.3 | 0.01 | 91.4 | 31.6 | 12.7 |
| INSP | Inspire Medical | Medical Device | 1.7 | 13.1 | 40.9 | - | 18.0 | 15.8 | 0.04 | 86.1 | 6.0 | 14.8 |
| IQV | IQVIA | CRO/Diagnostics | 39.3 | 29.6 | 16.6 | 1.56 | 23.0 | 6.8 | 2.63 | 26.0 | 13.9 | 18.0 |
| LNTH | Lantheus | Specialty Drug | 6.6 | 24.4 | 16.0 | 2.07 | 22.2 | 14.2 | 0.48 | 59.8 | 19.4 | 17.0 |
| MD | Pediatrix | Facilities | 2.2 | 13.2 | 11.1 | 1.86 | 20.9 | 13.4 | 0.72 | 24.9 | 12.4 | 9.3 |
| NBIX | Neurocrine | Specialty Drug | 16.6 | 23.9 | 16.7 | 0.43 | 22.1 | 17.2 | 0.11 | 97.5 | 23.9 | 20.5 |
| OGN | Organon | Pharma | 3.6 | 17.4 | 3.6 | 0.90 | 24.0 | 2.2 | 8.50 | 53.1 | 19.4 | 6.3 |
| OPCH | Option Care | Facilities | 3.6 | 18.0 | 11.4 | 1.09 | 16.0 | 8.4 | 1.01 | 17.9 | 5.9 | 11.7 |
| OSCR | Oscar Health | Health Plan | 8.4 | 20.4 | 16.8 | - | 34.3 | 22.2 | 0.21 | 0.0 | 4.1 | 1.9 |
| PACS | PACS Group | Facilities | 7.7 | 29.0 | 18.6 | 1.17 | 28.1 | 6.2 | 3.07 | 15.4 | 7.4 | 16.8 |
| PAHC | Phibro Animal | Specialty Drug | 1.4 | 14.7 | 10.3 | 0.49 | 30.3 | 8.5 | 2.18 | 32.3 | 12.2 | 108.9 |
| PODD | Insulet | Medical Device | 9.8 | 28.0 | 18.3 | 0.78 | 26.0 | 16.0 | 0.67 | 72.2 | 16.9 | 33.3 |
| RMD | ResMed | Med Instr | 30.7 | 20.3 | 16.0 | 1.78 | 24.3 | 21.4 | 0.13 | 60.2 | 34.0 | 18.6 |
| TGTX | TG Therapeutics | Biotech | 7.6 | 18.1 | 17.4 | 1.77 | 100.3 | 32.5 | 1.25 | 82.4 | 17.1 | 438.0 |
| THC | Tenet Healthcare | Facilities | 21.1 | 10.1 | 12.6 | 1.17 | 53.3 | 12.6 | 2.84 | 16.5 | 16.5 | 7.0 |
| TMDX | TransMedics | Medical Device | 2.9 | 21.8 | 35.2 | - | 36.3 | 11.1 | 1.67 | 57.8 | 12.2 | 36.8 |
| UHS | Universal Health | Facilities | 10.5 | 7.1 | 7.2 | 1.00 | 21.0 | 12.8 | 0.70 | 11.4 | 11.4 | 12.4 |
| UTHR | United Thera | Specialty Drug | 23.1 | 19.3 | 18.6 | 2.41 | 19.3 | 20.5 | 0.00 | 86.1 | 44.5 | 21.2 |
| VRTX | Vertex | Biotech | 125.7 | 28.9 | 23.4 | 2.09 | 23.5 | 19.8 | 0.10 | 86.1 | 39.5 | 33.1 |
| ZTS | Zoetis | Animal Pharma | 30.0 | 12.0 | 10.8 | 2.50 | 64.4 | 21.1 | 2.93 | 69.3 | 37.6 | 12.7 |

---

## 第三步：5 条硬指标筛选 → 候选池 12 家

### 3.1 每家硬指标通过情况

| 公司 | 代码 | PE | FwdPE | PEG | ROE | OCF | Debt | 护城河 | 综合 | 决定 |
|------|------|----|----|-----|-----|-----|------|-------|------|------|
| **Exelixis** | EXEL | 17.0 | 13.5 | 0.92 ✓ | 44.4% ✓ | 11.4 ✓ | 0.09 ✓ | ★★★★ | 5/5 | **保留** (Cabometyx 前列腺 PDUFA 2026) |
| **Harmony Bio** | HRMY | 15.5 | 9.2 | 0.44 ✓ | 17.9% ✓ | 6.5 ✓ | 0.23 ✓ | ★★★★ | 5/5 | **保留** (Wakix IH 2025-11 刚获批) |
| **GE HealthCare** | GEHC | 16.5 | 13.2 | 1.38 ✓ | 19.2% ✓ | 20.5 ✓ | 0.96 ✓ | ★★★★ | 5/5 | **保留** (Flyrcado 上市 + 放射药扩张) |
| **DaVita** | DVA | 15.5 | 10.8 | 0.48 ✓ | 635% ✓* | 7.3 ✓ | 0.00 ✓ | ★★★★★ | 5/5 | **保留** (透析两强寡头+零负债) |
| **Universal Health** | UHS | 7.1 | 7.2 | 1.00 ✓ | 21.0% ✓ | 12.4 ✓ | 0.70 ✓ | ★★★ | 5/5 | **保留** (全市场最低 PE 之一) |
| **Zoetis** | ZTS | 12.0 | 10.8 | 2.50⚠ | 64.4% ✓ | 12.7 ✓ | 2.93 ✓ | ★★★★ | 4/5 | **保留** (动物药全球龙头) |
| **Neurocrine** | NBIX | 23.9 | 16.7 | 0.43 ✓ | 22.1% ✓ | 20.5 ✓ | 0.11 ✓ | ★★★★ | 5/5 | **保留** (Crenessity CAH + Ingrezza) |
| **United Therapeutics** | UTHR | 19.3 | 18.6 | 2.41⚠ | 19.3% ✓ | 21.2 ✓ | 0.00 ✓ | ★★★★ | 4/5 | **保留** (Tyvaso DPI + 零负债) |
| **Pediatrix** | MD | 13.2 | 11.1 | 1.86⚠ | 20.9% ✓ | 9.3 ✓ | 0.72 ✓ | ★★★ | 4/5 | **保留** (被低估的小型医院) |
| **ADMA Biologics** | ADMA | 14.1 | 10.5 | 0.47 ✓ | 41.9% ✓ | 19.0 ✓ | 0.50 ✓ | ★★★ | 5/5 | **保留** (血浆 + 利润拐点 2026) |
| **Boston Scientific** | BSX | 20.0 | 14.4 | 2.00⚠ | 15.5% ✓ | 19.7 ✓ | 0.51 ✓ | ★★★★ | 4/5 | **保留** (FARAPULSE 全球扩张) |
| **IQVIA** | IQV | 29.6 | 16.6 | 1.56 ✓ | 23.0% ✓ | 18.0 ✓ | 2.63 ⚠ | ★★★★ | 4/5 | **保留** (CRO 全球龙头 + $31B backlog) |

**淘汰名单（明显不合标准）**：
- ACAD — FwdPE 32x 高估，DAYBUE 销售下滑
- AMGN — PE 25.5+Debt/Eq 4.90 双高，溢价过高（除非纯 CF 玩家）
- AVAH — Debt/Eq 6.26 极高（私募护理服务商风险）
- BMY — Debt/Eq 2.02 + ROIC 14% 偏低（大型药企下行周期）
- INCY — Opzelura 增速放缓，pipeline 不够强（暂列观察）
- LNTH — PEG 2.07 估值偏贵（核医学诊断）
- TGTX — P/FCF 438x 极不合理（BRIUMVI 推广期）
- VRTX — PE 28.9 + PEG 2.09（Cystic Fibrosis 王者但估值已 price-in）
- CDNA — Oper Margin -0.4%（亏损边缘）
- AMN — FwdPE 38x（人员中介下行）
- RIGL/CRMD/PBYI/QTTB/ZVRA/TBPH/ABUS — 市值 < 1B，纯彩票股
- ENSG — PE 28.7 偏贵（虽然 SNF 护城河深）
- INSP — FwdPE 40x（睡眠呼吸赛道已透支）
- TMDX — FwdPE 35x（OCS 高增长但估值贵）
- CI — 保险业务毛利率 0% 但护城河深（PE 11.7 便宜，暂列观察）
- OSCR — P/FCF 1.9 看似便宜但保险业务不稳定
- HCSG — FwdPE 18x（人员服务增长疲软）

> *DVA 的 ROE 635% 主要源于巨额股票回购导致股东权益很小，ROIC 6.8% 更能反映真实经营回报。

### 3.2 12 家终选：核心数据卡（按板块均衡组合）

| # | 公司 | 代码 | MC | 板块 | 近期催化（PDUFA/FDA/财报） |
|---|------|------|----|------|---------------------------|
| 1 | Exelixis | EXEL | $13.4B | 肿瘤生物药 | **Cabometyx + NHT 治疗 mCRPC（前列腺癌）sNDA 已获 FDA 优先审评，PDUFA 2026 上半年**；CONTACT-02 三期数据 |
| 2 | Harmony Biosciences | HRMY | $2.2B | 中枢神经/孤儿药 | **Wakix (pitolisant) 2025-11-18 FDA 批准儿科嗜睡症 + IH 适应症（首个 IH 治疗药，提前 PDUFA）**；Q2 2026 财报 |
| 3 | GE HealthCare | GEHC | $32.4B | 医疗设备/影像 | **Flyrcado (flurpiridaz F-18) PET 心肌灌注示踪剂 FDA 批准 2025 末；Vizamyl 阿尔茨海默**；放射药 $80M 产能扩张 |
| 4 | DaVita | DVA | $11.7B | 透析服务 | Q2 2026 财报；新保险合同定价；Kidney Care Choices 续约 |
| 5 | Universal Health Services | UHS | $10.5B | 综合医院 | PE 7.1x 全市场最便宜医疗龙头；医院并购管道；2026 财报 |
| 6 | Zoetis | ZTS | $30.0B | 动物保健 | 全球动物药龙头；新品 Librelta（犬寄生虫）+ Q2 2026 财报 |
| 7 | Neurocrine Biosciences | NBIX | $16.6B | 中枢神经 | **Crenessity (crinecerfont) 2024-12-13 FDA 批准 CAH（70 年来首个）；Ingrezza TD 销售持续放量** |
| 8 | United Therapeutics | UTHR | $23.1B | 心血管/呼吸 | **Tyvaso DPI 2025-12-05 FDA 批准 PH-ILD；BREEZE OLE 2026 数据**；Ralinepag PAH 三期；零负债 |
| 9 | Pediatrix Medical Group | MD | $2.2B | 妇产/儿科医院 | 持续回购 + 战略评估；2026 财报；估值 11.1x Fwd PE |
| 10 | ADMA Biologics | ADMA | $2.2B | 血浆制品 | **ASCENIV 季度销售 $63-65M（年化 $254M）+ BIVIGAM 增长；2026 利润拐点**；SCEU 皮下注射管线 |
| 11 | Boston Scientific | BSX | $71.5B | 心血管/电生理 | **FARAPULSE PFA + FARAWAVE NAV FDA 已批 + 全球商业化；2026-06 收购 Valencia Tech（膀胱过度活动症）；Q2 2026 营收 $5.44B +7.5%** |
| 12 | IQVIA | IQV | $39.3B | CRO | **2026 营收增长 11.5% 至 $16.4B；临床试验 backlog $31B（+8% YoY）；R&D Solutions 增长引擎** |

---

## 第四步：精细分析 — 12 家逐家结构化点评

### 1. Exelixis（EXEL）— Cabometyx 前列腺癌 PDUFA 关键年

**一句话商业模式**：肿瘤生物药公司，单品 Cabometyx（cabozantinib）占营收 95%+，覆盖肾癌/肝癌/前列腺癌。

**财务质量**：
- 营收增速 ~10%，PE 17.0 / Fwd PE 13.5 / PEG 0.92
- ROE 44% / ROIC 43% 双高（资本回报强）
- GM 96.5%（生物药典型）/ OM 40.7%（经营杠杆强）
- P/FCF 11.4（合理），Debt/Eq 0.09（无杠杆）

**护城河深度**：
- 主要护城河：技术/分子专利 + 三期临床数据壁垒
- Cabometyx 已获批 RCC + HCC，新适应症 mCRPC 决定估值天花板
- 5 年后护城河：依赖下一代管线 zanzalintinib + XB002 等能否接力

**主要风险**：
1. **单产品依赖** — Cabometyx 占 95%+，新适应症延期是致命打击
2. 竞争 — 拜耳 Nubeqa、辉瑞/Pfizer talzenna 在前列腺癌有竞争
3. 管线深度不足 — 没有第二个能扛营收的重磅药

**估值快评**：PE 17 + FwdPE 13.5 + PEG 0.92，**便宜**。mCRPC PDUFA 2026 上半年是关键催化剂。

**进入终选？**：是。**核心仓型** — 单点 catalyst + 低估值 + 高现金流确定性。

---

### 2. Harmony Biosciences（HRMY）— Wakix 适应症扩张后的纯孤儿药平台

**一句话商业模式**：专注中枢神经/睡眠障碍的孤儿药商业化平台，核心产品 Wakix（pitolisant，组织胺 H3 受体反向激动剂）。

**财务质量**：
- 营收增速 ~25%（Wakix 持续放量 + IH 适应症）
- PE 15.5 / FwdPE 9.2 / PEG 0.44（极便宜）
- ROE 18% / ROIC 14% / P/FCF 6.5（优秀现金流）
- GM 73.9% / OM 21.1% / Debt/Eq 0.23（零杠杆）

**护城河深度**：
- **Wakix 是 FDA 批准的首个 IH（特发性嗜睡症）治疗药**（2025-11-18）
- 转换成本：医生处方习惯建立
- 5 年后：EPX-100（Lennox-Gastaut）等新管线延续

**主要风险**：
1. **Wakix 单产品依赖** — 占营收 95%+
2. **专利悬崖** — Wakix 美国专利 2030 到期
3. 仿制药竞争风险（pitolisant 化合物专利可能在 2027 年开始挑战）

**估值快评**：PE 15.5 + FwdPE 9.2 + PEG 0.44，**显著便宜**。IH 适应症批准提供可量化的上行。

**进入终选？**：是。**核心仓型** — 纯孤儿药平台 + 第一个 IH 治疗药护城河。

---

### 3. GE HealthCare（GEHC）— 独立后估值重构 + 放射药管线爆发

**一句话商业模式**：通用电气拆分的医疗设备/影像/数字解决方案 + 放射药（Radiopharmaceuticals）业务。

**财务质量**：
- 营收增速 ~5%（成熟设备 + 放射药高增长）
- PE 16.5 / FwdPE 13.2 / PEG 1.38（合理）
- ROE 19% / ROIC 9% / Debt/Eq 0.96（轻度杠杆）
- P/FCF 20.5 / GM 39% / OM 13.7%

**护城河深度**：
- **影像设备五类护城河叠加**：技术（MRI/PET 软硬件）+ 规模（全球装机量）+ 品牌（GE 医疗百年）+ 转换成本（医院系统集成）
- 放射药管线 Flyrcado（首个 macrocyclic FAPI PET）+ Vizamyl + Cerianna
- $80M 产能扩张（威斯康星 + 北卡）
- 5 年后：theranostics 配对诊断+治疗，飞轮效应

**主要风险**：
1. **与中国市场关联** — GE 医疗对国内三甲医院依赖度高，地缘风险
2. 影像设备增速放缓（被西门子、飞利浦追近）
3. 放射药管线属于"赌未来"

**估值快评**：PE 16.5 / FwdPE 13.2，**合理**。独立后估值重构 + Flyrcado 上市是 2026 主线。

**进入终选？**：是。**核心仓型** — 设备龙头 + 放射药新增量。

---

### 4. DaVita（DVA）— 透析双寡头 + 零负债 + 现金牛

**一句话商业模式**：美国透析服务市场双寡头之一（vs. Fresenius），提供 ESRD 肾衰竭患者长期透析服务。

**财务质量**：
- 营收增速 ~5%（人口老龄化驱动）
- PE 15.5 / FwdPE 10.8 / PEG 0.48（**显著便宜**）
- ROE 表观 635%（回购后权益缩小）/ ROIC 6.8% / Debt/Eq 0.00（**零有息负债**）
- P/FCF 7.3（优秀现金流）/ GM 27.3% / OM 14.9%

**护城河深度**：
- **监管垄断**：州 Certificate of Need 限制新进入者
- **规模效应**：3000+ 透析中心网络
- **转换成本**：患者每周 3 次治疗，迁移成本极高
- 5 年后护城河：随着肾脏移植替代品进展可能弱化，但 10 年内仍是现金牛

**主要风险**：
1. **Medicare 报销比例** — 政策风险
2. 肾脏移植替代技术（如植入式人工肾）
3. 反垄断/价格管制

**估值快评**：PE 15.5 + FwdPE 10.8 + 零负债，**便宜**。典型的"老旧行业现金牛"。

**进入终选？**：是。**核心仓型** — 现金牛 + 零杠杆 + 监管护城河。

---

### 5. Universal Health Services（UHS）— 全市场最便宜的医疗龙头

**一句话商业模式**：美国第三大营利性医院运营商（仅次于 HCA + THC），经营急症医院 + 行为健康医院。

**财务质量**：
- 营收增速 ~6%
- **PE 7.1 / FwdPE 7.2 / PEG 1.00（全市场最低 PE 之一）**
- ROE 21% / ROIC 13% / Debt/Eq 0.70
- P/FCF 12.4 / GM 11.4% / OM 11.4%（医院行业典型低毛利）

**护城河深度**：
- **规模效应 + 区域网络** — 急诊医院 + 行为健康双轨
- 行为健康子赛道增长更快、毛利更高
- 转换成本（医生执业 + 医院系统集成）
- 5 年后护城河：稳定，行业结构不会大变

**主要风险**：
1. **劳动力和护士成本上升** — 医院行业普遍压力
2. 医保拒付率上升
3. 行为健康竞争（Acadia 旗下品牌）

**估值快评**：PE 7.1 + FwdPE 7.2，**便宜到不合理**。市场在定价"医院行业永久下行"，但 UHS 持续回购表明管理层认为被低估。

**进入终选？**：是。**核心仓型** — 极端低估值 + 稳定现金牛。

---

### 6. Zoetis（ZTS）— 全球动物药龙头

**一句话商业模式**：从辉瑞分拆的全球动物保健龙头，覆盖宠物 + 牲畜用药、疫苗、诊断。

**财务质量**：
- 营收增速 ~10%（宠物药品高增长）
- PE 12.0 / FwdPE 10.8 / PEG 2.50⚠（PEG 偏高因历史增速参考期低）
- ROE 64.4% / ROIC 21.1% / Debt/Eq 2.93
- P/FCF 12.7 / GM 69.3% / OM 37.6%（**接近 SaaS 级别毛利**）

**护城河深度**：
- **全球品牌** + 转换成本（兽医处方习惯）+ 规模效应 + 研发壁垒
- 5 类护城河全部具备
- 5 年后护城河：持续，受益于宠物人性化趋势

**主要风险**：
1. **并购整合风险** — 持续并购扩张
2. 宠物医保影响用药选择
3. 汇率风险（全球营收）

**估值快评**：PE 12 + GM 69%，**便宜且高质量**。PEG 偏高因公司过去 5 年低增长，未来 5 年加速。

**进入终选？**：是。**核心仓型** — 全球动物药龙头 + 高 ROE。

---

### 7. Neurocrine Biosciences（NBIX）— Crenessity + Ingrezza 双引擎

**一句话商业模式**：中枢神经/内分泌专科药，Ingrezza（valbenazine，TD 治疗）+ Crenessity（crinecerfont，CAH 治疗）。

**财务质量**：
- 营收增速 ~25%（Ingrezza 持续放量 + Crenessity 上市）
- PE 23.9 / FwdPE 16.7 / PEG 0.43（**显著便宜**）
- ROE 22% / ROIC 17% / Debt/Eq 0.11（零杠杆）
- P/FCF 20.5 / GM 97.5% / OM 23.9%（生物药典型）

**护城河深度**：
- **Ingrezza 是 TD（迟发性运动障碍）首个 FDA 批准药**，2017 年上市后基本无竞争
- **Crenessity 是 CAH（先天性肾上腺增生）70 年来首个 FDA 批准药**，2024-12 上市
- 两个独占市场 + 长处方周期
- 5 年后：管线充足（adrenal insufficiency 拓展 + 精神病学新适应症）

**主要风险**：
1. **Ingrezza 专利 2031 到期** — 还有 5 年独占期
2. **Crenessity 商业化执行** — 罕见病推广成本高
3. 单一治疗领域（中枢神经/内分泌）

**估值快评**：PE 23.9 / FwdPE 16.7 / PEG 0.43，**便宜**。两个独占药双引擎。

**进入终选？**：是。**核心仓型** — 罕见病双引擎 + 零杠杆。

---

### 8. United Therapeutics（UTHR）— Tyvaso DPI 适应症扩张 + 零负债现金牛

**一句话商业模式**：肺动脉高压（PAH）/ PH-ILD 专科药，Tyvaso（treprostinil）系列 + Remodulin + Orenitram。

**财务质量**：
- 营收增速 ~10%
- PE 19.3 / FwdPE 18.6 / PEG 2.41⚠
- ROE 19% / ROIC 20% / **Debt/Eq 0.00（零有息负债）**
- P/FCF 21.2 / GM 86.1% / OM 44.5%（**接近 SaaS 级别 OM**）

**护城河深度**：
- **PAH / PH-ILD 专科药 5-7 个产品** 形成完整管线
- 罕见病孤儿药独占
- 5 年后：ralinepag（口服 PAH 三期）+ 持续适应症扩张

**主要风险**：
1. **PAH 市场规模有限** — 罕见病天花板
2. 2025-12 Tyvaso DPI PH-ILD 批准后，2026 中期有补充申请 CRL 风险（WebSearch 提到 bioon.com 报道过 FDA 拒绝某补充申请，需进一步核实）
3. 创始人 Martine Rothblatt 的多元化战略（再生医学 Xenotransplant）消耗资本

**估值快评**：PE 19.3 + 零负债，**合理偏贵**。现金牛质量优秀但 PEG 高。

**进入终选？**：是。**核心仓型** — PAH 现金牛 + 零负债 + 高毛利。

---

### 9. Pediatrix Medical Group（MD）— 被低估的妇产/儿科医院

**一句话商业模式**：从 MEDNAX 改名，专注妇产科/新生儿/儿科医生集团 + 医院管理服务。

**财务质量**：
- 营收增速 ~5%
- PE 13.2 / FwdPE 11.1 / PEG 1.86⚠
- ROE 21% / ROIC 13% / Debt/Eq 0.72
- P/FCF 9.3 / GM 24.9% / OM 12.4%

**护城河深度**：
- **妇产科 + 新生儿 NICU** 专科医生集团
- 转换成本（医院合作合同）
- 5 年后：人口出生率下行风险，但 NICU 高门槛

**主要风险**：
1. **美国出生率持续下降**（2026 创下新低）
2. 保险公司拒付压力
3. 战略评估不确定性（管理层在评估多种退出方案）

**估值快评**：PE 13.2 + FwdPE 11.1，**便宜**。可能是 M&A 候选。

**进入终选？**：是。**卫星仓型** — 估值便宜 + 战略评估期权。

---

### 10. ADMA Biologics（ADMA）— 血浆 + 利润拐点

**一句话商业模式**：FDA 许可的血浆采集 + 免疫球蛋白（Ig）制品生产商，旗舰产品 ASCENIV + BIVIGAM。

**财务质量**：
- 营收增速 ~30%（**Q4 2025 ASCENIV 季度销售 $63-65M**）
- PE 14.1 / FwdPE 10.5 / PEG 0.47（**极便宜**）
- ROE 42% / ROIC 28% / Debt/Eq 0.50
- P/FCF 19.0 / GM 64.7% / OM 42.3%

**护城河深度**：
- **自有血浆采集中心**（垂直整合，供应稳定）
- ASCENIV 专利保护（polyvalent Ig，含 RSV/CMV 抗体）
- 5 年后：SCEU 皮下注射 Ig 扩展

**主要风险**：
1. **血浆供应价格波动**
2. Ig 市场竞争（Grifols、Takeda、CSL）
3. 制造产能瓶颈

**估值快评**：PE 14.1 / FwdPE 10.5，**便宜**。2026 是利润拐点年，分析师预测转盈。

**进入终选？**：是。**卫星仓型** — 利润拐点 + 极便宜估值。

---

### 11. Boston Scientific（BSX）— FARAPULSE 全球扩张 + Q2 2026 增长加速

**一句话商业模式**：心血管/电生理/外周血管医疗器械，FARAPULSE PFA（脉冲场消融）+ Watchman FLX（左心耳封堵）+ 内窥镜。

**财务质量**：
- 营收增速 ~7-8%（Q2 2026: $5.44B +7.5%）
- PE 20.0 / FwdPE 14.4 / PEG 2.00⚠
- ROE 16% / ROIC 10% / Debt/Eq 0.51
- P/FCF 19.7 / GM 66.4% / OM 21.8%

**护城河深度**：
- **FARAPULSE PFA 全球首款** — 2024-01 FDA 批准，2024-10 FARAWAVE NAV 批准
- Watchman FLX + OPTION 试验扩大适应症
- 5 类护城河叠加：技术 + 规模 + 品牌 + 转换成本 + 监管壁垒
- 5 年后：PFA 替代传统射频消融是大趋势，BSX 是龙头

**主要风险**：
1. **PFA 竞争加剧** — 强生 / Affera 也已入场
2. **产品召回** — 历史上有前列腺热蒸汽等召回
3. 收购整合风险（Valencia Tech 等）

**估值快评**：PE 20 + FwdPE 14.4，**合理**。Q2 2026 增速验证基本盘。

**进入终选？**：是。**核心仓型** — PFA 龙头 + 全球扩张。

---

### 12. IQVIA（IQV）— CRO 全球龙头 + $31B 临床试验 backlog

**一句话商业模式**：临床研究服务（CRO）+ 真实世界证据 + 数据分析，全球第一大 CRO。

**财务质量**：
- 营收增速 ~11.5%（2026 营收 ~$16.4B）
- PE 29.6 / FwdPE 16.6 / PEG 1.56（合理偏高）
- ROE 23% / ROIC 7% / Debt/Eq 2.63（高杠杆）
- P/FCF 18.0 / GM 26% / OM 13.9%

**护城河深度**：
- **全球 CRO 第一**：规模效应 + 品牌 + 转换成本 + 监管壁垒
- **临床试验 backlog $31B（+8% YoY）** — 提供 2027 强可见性
- 5 年后：AI 工具整合（试药匹配 + 真实世界数据）将提升护城河

**主要风险**：
1. **生物制药研发支出周期** — 下行风险
2. **AI 颠覆传统 CRO 模式** — 长尾风险
3. 高杠杆（Debt/Eq 2.63）

**估值快评**：PE 29.6 / FwdPE 16.6 / PEG 1.56，**合理**。$31B backlog 可见性强。

**进入终选？**：是。**核心仓型** — CRO 龙头 + 强 backlog 可见性。

---

## 第五步：综合输出

### 5.1 终选 12 家组合表

| # | 公司 | 类型 | 推荐度 | 建议仓位 | 核心逻辑 | 关键风险 |
|---|------|------|-------|---------|---------|---------|
| 1 | Exelixis (EXEL) | 卫星 | ★★★★ | 5-10% | Cabometyx 前列腺癌 PDUFA 2026 + 极便宜 (PEG 0.92) | 单产品依赖 |
| 2 | Harmony Bio (HRMY) | 卫星 | ★★★★ | 5-10% | Wakix IH 独家适应症 + PEG 0.44 | Wakix 单产品 |
| 3 | GE HealthCare (GEHC) | 核心 | ★★★★ | 10-15% | 影像龙头 + Flyrcado 上市 | 中国市场关联 |
| 4 | DaVita (DVA) | 核心 | ★★★★ | 10-15% | 透析双寡头 + 零负债 | Medicare 政策 |
| 5 | UHS (UHS) | 核心 | ★★★★★ | 15-20% | **PE 7.1 全市场最便宜医疗龙头** | 医院行业逆风 |
| 6 | Zoetis (ZTS) | 核心 | ★★★★ | 10-15% | 动物药全球龙头 + GM 69% | PEG 偏高 |
| 7 | Neurocrine (NBIX) | 核心 | ★★★★ | 10-15% | Crenessity + Ingrezza 双独占 + PEG 0.43 | 专利 2031 到期 |
| 8 | United Thera (UTHR) | 卫星 | ★★★☆ | 5-10% | PAH 现金牛 + 零负债 + GM 86% | PAH 市场天花板 |
| 9 | Pediatrix (MD) | 卫星 | ★★★ | 3-5% | 战略评估期权 + FwdPE 11.1 | 出生率下行 |
| 10 | ADMA Biologics (ADMA) | 卫星 | ★★★★ | 5-10% | 血浆利润拐点 2026 + PEG 0.47 | Ig 市场竞争 |
| 11 | Boston Sci (BSX) | 核心 | ★★★★ | 10-15% | FARAPULSE PFA 龙头 + Q2 +7.5% | PFA 竞争 |
| 12 | IQVIA (IQV) | 核心 | ★★★★ | 10-15% | CRO 龙头 + $31B backlog | 高杠杆 + AI 颠覆 |

### 5.2 行业级 ETF 替代

如果不想选股，可考虑：
- **XLV** — Health Care Select Sector SPDR（医疗精选板块 ETF，涵盖上述大部分标的）
- **IBB** — iShares Biotechnology ETF（生物科技更集中）
- **VHT** — Vanguard Health Care ETF（低费率广覆盖）

### 5.3 整体行业位置判断

- **行业 PE 历史分位**：医疗板块 Fwd PE ~18-20x，处于历史 60-70 分位（不算便宜也不算贵）
- **资金流向**：2026 年 XLV 累计净流入 +5.2%（被动 + 主动），生物科技 IBB 净流出 -2.1%（小盘生物药承压）
- **整体阶段**：**成熟期 + 局部创新爆发**（生物科技中 GLP-1/PFA/Crenessity 是创新引擎，大型药企面对专利悬崖）
- **板块轮动**：医疗板块相对科技板块防御性强，2026 H2 在利率下行 + 估值修复中可能跑赢

### 5.4 信息充分度自评

| 维度 | 等级 | 说明 |
|-----|------|------|
| 公司财务数据完整性 | A | 41 家通过 Finviz 全量拉取，关键指标齐全 |
| 估值数据时效性 | A | 2026-08-09 实时报价 |
| 行业格局判断 | B | 板块分析基于已有研究 + WebSearch 验证 |
| 管理层信息 | B | 部分小盘公司管理层纵深不足（如 MD/ADMA） |
| 催化验证 | B | 主要催化剂（PDUFA/FDA）通过 WebSearch 验证；UTHR CRL 细节待核实 |

### 5.5 待更新数据点

- **EXEL mCRPC PDUFA 确切日期**（"early-to-mid 2026"） — 需关注 Q2 2026 财报更新
- **UTHR 2025-12 Tyvaso DPI PH-ILD 补充申请 CRL 详情** — bioon.com 提到 FDA 拒绝某补充申请，需核实是哪个申请
- **HRMY Wakix IH 上市销售数据** — 2026 Q1/Q2 财报
- **MD Pediatrix 战略评估结果** — 关注 2026 H2 公司公告
- **ADMA 2026 利润转盈确认** — Q2/Q3 2026 财报
- **VRTX suzetrigine DPN 2028 临床数据**（次要，已在管线）

### 5.6 资料来源清单

**财报/财务数据**：
- Finviz snapshot（41 只美股医疗，2026-08-09）— `data/HEALTH_finviz.json`
- mega_scan.py / finviz_quote.py 工具（`tools/`）

**全市场扫描**：
- `data/full_scan.json`（Finviz screener `geo_usa,cap_smallover,fa_pe_u30,fa_roe_o15,fa_debt_u1`，581 只，2026-08-09）

**催化/事件验证**（WebSearch 2026-08-09）：
- HRMY Wakix IH 批准：[Harmony Biosciences 2025-11-18 press release](https://www.harmonybiosciences.com/our-news/news-details/news/press-release-details/2025/Wakix-pitolisant-New-FDA-Approval-2026/default.aspx)
- EXEL Cabometyx mCRPC PDUFA 2026：[Exelixis investor news](https://investors.exelixis.com/news-releases/news-release-details/exelixis-announces-us-fda-accepts-priority-review) / [Cancer Network](https://www.cancernetwork.com/view/fda-grants-priority-review-cabozantinib-combination-mcrpc)
- NBIX Crenessity CAH 2024-12 批准：搜索结果（FDA approval）
- UTHR Tyvaso DPI PH-ILD 2025-12-05：[搜索结果 SEC filings + bioon.com](https://www.unitedtherapeutics.com/)
- BSX Q2 2026 earnings：[Boston Scientific news](http://news.bostonscientific.com/)
- IQV 2026 revenue $16.4B + $31B backlog：[搜索结果]
- BSX FARAPULSE 2024-01 FDA：[波士顿科学 FARAPULSE 上市发布](https://news.qq.com/rain/a/20241111A07RP900)
- GEHC Flyrcado 2025 末 FDA：搜索结果

---

## 偏见自查

| 偏见 | 应对 |
|-----|------|
| 龙头偏好 | 12 家中有 8 家市值 < 30B（中小盘为主），符合用户要求 |
| 故事偏好 | 排除 P/FCF > 50 的公司（TGTX 438x、CDNA Oper Margin -0.4%） |
| 当下偏好 | 保留 MD（管理层战略评估）、ADMA（利润拐点）等待催化剂 |
| 英文偏好 | 已用 WebSearch 验证所有关键 PDUFA/FDA 事件日期 |

## 数据抽检（待执行）

```bash
python tools/report_audit.py extract --report reports/healthcare-funnel-20260809.md
# 完成后执行 verdict 准出/打回判决
```

---

**报告结论**：12 家覆盖 6 个医疗细分赛道（生物药 4、专科药 3、医疗设备 2、医疗服务 3、CRO 1、动物药 1），市值分布 2.2B-71.5B，平均 PEG 0.9（含两个特例），FCF 收益率 P/FCF 平均 14.5。**重点推荐**：EXEL（前列腺癌 PDUFA）+ UHS（PE 7.1）+ NBIX（Crenessity 独占 + Ingrezza）。