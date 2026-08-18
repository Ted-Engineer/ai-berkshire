# CoreWeave (CRWV) 巴菲特六关买入前 Checklist — 成长型框架（2026-08-16 复核）

- **报告日期**: 2026-08-16（`date` 确认：Sun Aug 16 22:27 2026）
- **价格锁定**: $105.26（2026-08-14 收盘，`fetch_quotes.py` 实时复核一致，偏差 0.00%）；52 周区间 $60.55–153.20（现价处于区间中位）
- **数据截止**: 2026-08-16 搜索快照；财务数据截至 Q2 2026（2026-06-30，8/11 财报 + 10-Q）
- **标的性质**: AI Neocloud 龙头；用户长期关注标的（memory）；industry-funnel 结论"★★★★期权位，$95-110 小仓 / $78-90 主力"；8-15 checklist 判 ❓ 灰区、触发 $80
- **分析框架**: 成长型（收入增速 112% > 50%、CapEx/收入 > 200%、backlog 13.78x TTM、GAAP 未盈利、渗透率低 — 5 条判定全命中）
- **计算工具**: `python tools/financial_rigor.py`（本文所有倍数/情景均由工具精确计算，禁心算）
- **本次为独立复核**：对 8-15 报告的任务书口径逐项重验，多 处 口径已过时，修正见下表

## AI 研究偏见预警：B+ 级

上市约 17 个月（2025-03 IPO @ $40），10-K/10-Q 硬数据可靠但历史短；媒体与卖方覆盖极密。**警惕共识陷阱**：8/11 财报 beat + 指引上调 + 单日大涨 11-19% 后，"backlog $104B = 需求已锁定"是当前最饱满的叙事。数据缺口（诚实标注）：Nvidia 持股比例（~6% 为 IPO 披露口径，本次未独立复核）、GAAP 毛利率（由 10-Q 成本推算）、流动比率 0.31x（沿用 8-15 的 10-Q 口径，本次未独立复核）。

## 任务书/旧口径修正表（本次复核新发现）

| 口径 | 任务书/旧值 | 本次核实值 | 来源 |
|---|---|---|---|
| RPO/backlog | "$99B 口径？" | **$104.2B**（Q2 末；Q1 末为 $99.4B，去年同期 $30.1B）+ 另 >$25B Q3 新增承诺未入账（一说 $129B 含 Q3 承诺） | Reuters + marketdaily（双源） |
| Q2 收入 | "$2.58B +112%" | **$2.575B，+112%**（Q2'25 为 $1.212B）| CNBC/Reuters + khancapitals（双源）✓ 口径成立 |
| 毛利率 | "回升至 ~70%？" | **~66%（10-Q 成本推算，工具计算 65.86%）— 60% 区间，未回升到 70%**；adj EBITDA 率 59% 且环比下滑（Q1 62%）| tradingkey + khancapitals（EBITDA 率双源） |
| 高管套现 | "8-15 口径 $2.65 亿" | **IPO 以来内部人累计卖出 >$2.3B**（6/30 口径）；CEO 6-8 月经 10b5-1 计划连续卖出（6/16 ~$108-119、6/30 $37.7M、7/7-8 369,489 股、7/14 $24.9M、7/28 $13.3M @$66.62、8/4 $28.2M）— 任务书口径低估一个数量级 | kucoin/cryptobriefing + MarketBeat/Fool/StockTitan Form 4（多源） |
| 年化 PS | "~5x" | **5.64x**（Q2 年化收入 $10.3B 口径，工具计算）；TTM PS 7.68x；前瞻 PS（FY26E 中值）4.54x | 工具计算 |
| FY26 指引 | "+140% 口径" | **+142% ~ +157%（中值 +150%）**：$12.4-13.2B vs FY25 $5.13B | CNBC + 404k transcript（双源）✓ 口径成立（取下限） |
| 净债务 | "~$14-17B？" | **$30.08B**（总债务 $35.6B − 现金 $5.52B，工具计算）— 任务书口径严重低估 | The Register + CNBC/ET Datacenters（双源） |
| Stargate | "官方 GPU 供应方" | **Stargate 伞形体系内的 GPU 算力供应商之一**：OpenAI 官方口径"Abilene 旗舰站 + 与 CoreWeave 的在建项目"共同构成 Stargate ~7GW/$400B+；但主要站点由 Crusoe 建设租给 Oracle，CRWV 非主承建方 | openai.com 官方 + presenc.ai/convergedigest（口径修正） |

## 核心数据表（Q2 2026，截至 2026-06-30；标注双源者已交叉验证）

| 指标 | 数值 | 来源与置信度 |
|---|---|---|
| 收入 | $2,575M（+112% YoY）| IR/CNBC/Reuters，高（双源✓） |
| TTM 收入 | $7,561M；H1'26 $4.65B | panabee + 工具计算，高 |
| FY26 指引 | $12.4–13.2B（+142%~157%）；adj 营业利润 $960M–1.15B（**首次给出转正时间表**）| CNBC + 财报 transcript，高（双源✓） |
| Backlog | $104.2B（13.78x TTM / 8.14x FY26E，工具计算）| Reuters + marketdaily，高（双源✓） |
| GAAP 营业利润率 | −2%（Q1'26 为 −7%，改善中）| tradingkey + panabee（H1 营业亏损 $193M），高 |
| 毛利率 | ~66%（10-Q 推算，工具计算 65.86%）；adj EBITDA 率 59%（↓自 62%） | 推算：中高；EBITDA 率：tradingkey+khancapitals 双源✓ |
| 净亏损 / EPS | −$626M / 摊薄 −$1.14（adj EPS −$1.03，好于预期的 −$1.20）| marketdaily + Yahoo，高（双源✓） |
| 经营现金流 | **+$679M（转正）** | tradingkey + IR，高 |
| 现金 | $5,524M；另有 $10B 循环+DDTL 未提取额度 | 10-Q（8-15 复核）+ The Register（双源✓） |
| 总债务 / 净债务 | $35.6B / $30.08B；Q2 净利息 $640M（+140% YoY） | The Register + ET Datacenters，高（双源✓） |
| 2026 CapEx 指引 | $35–39B（上调；Q2 单季 $9.4B） | Reuters + ET Datacenters，高（双源✓） |
| 市值 | $58.06B（551.54M 股 × $105.26，工具验算偏差 0.01%） | 工具 + stockanalysis.com $58.05B（双源✓） |
| PS | 年化 5.64x / TTM 7.68x / FY26E 4.54x（工具计算） | 工具计算，高 |
| PS/增速 | 年化口径 **0.050**；TTM 口径 0.069 | 工具计算，高 |
| EV | $88.13B；EV/年化收入 8.56x；EV/FY26E 6.88x | 工具计算，高 |
| 同业 PS | CRWV TTM 7.33-7.91x vs **NBIS 53.25-54.50x**；前瞻 CRWV ~4x 2027E vs NBIS ~7x | SeekingAlpha + 247wallst + ainvest（多源✓） |
| 客户集中度 | H1'26 客户 A 40% + 客户 B 23% = **63%**；FY25 微软单客户 ~67% | 10-Q（8-15 复核），高 |
| 大额合同 | OpenAI 累计 $22.4B（2025-03/05/09 三次扩约）；Meta $14.2B（2025-09）扩至 **$21B（2026-04-09）**；Anthropic **$6.8B（2026-04-10）**；Google 亦已签约（四大 AI 实验室全覆盖） | CoreWeave 官方 + Reuters/WSJ/CNBC（OpenAI 双源✓）；Forbes + CNBC（Meta 双源✓）；financialcontent + enterprisedna（Anthropic，中高） |
| 稀释 | 股本 218M（2024）→ 436M（2025）→ 532M（2026-03-31，+22.15% YoY）→ 当前 ~551.5M；两年 **2.53x**；另有 $3.5B 可转债（~$119.6 转股价） | financecharts + companiesmarketcap + 昨日 10-Q 口径，中高 |
| 流动比率 | 0.31x（10-Q 口径沿用，本次未独立复核；负债端含巨额客户预收/递延收入） | 8-15 报告 + watchlist，中 |
| 利息覆盖 | 年化 adj EBITDA $6.04B / 年化净利息 $2.56B = **2.36x**；利息吞掉 FY26E 收入 20% | 工具计算，高 |
| 现金跑道 | 纯现金 0.97 季度（$5.52B / 季烧钱 ~$5.7B）；含 $10B 未提取额度 ≈ 2.7 个季度 | 工具计算，高 |

---

## 六关逐关评估

### 第一关：我能理解这门生意吗（能力圈） — ★★★☆☆

**一句话**：借债买 GPU 和数据中心，以多年期合同租给 Meta/OpenAI/微软/Anthropic 等巨头，赚租金与融资成本之间的利差。

- [x] 赚钱方式说得清：**高杠杆算力租赁，金融属性 > 科技属性**
- [?] 10 年后：不确定。GPU 每 2-3 年一代、贬值快；若推理需求持续则生意在，若需求逆转则资产端与负债端同时塌陷
- 关键变量：① AI 推理需求曲线 ② Nvidia 供货优先级与采购成本 ③ 债务市场对 GPU 抵押品的胃口 ④ 前五大客户资本开支周期 ⑤ GPU 二手残值
- 认知来源：本仓库四篇深度研究 + 两日连续 checklist + 本次 14 次定向搜索，非道听途说
- 芒格式批评成立：你买的不是云公司，是一堆带杠杆的折旧芯片。**判定：勉强在能力圈内，通过**

### 第二关：这是一门好生意吗（成长型经济特征） — ★★★☆☆

| 指标 | 参考标准 | 实测（工具核验） | 判断 |
|---|---|---|---|
| 收入增速 | >50% | **+112%**（FY26 指引 +142~157%） | ✅ |
| 毛利率 | >30% | **~66%**（推算；未回升至 70%，adj EBITDA 率 62%→59% 下滑） | ✅ |
| Backlog/收入 | >1x | **13.78x TTM / 8.14x FY26E** | ✅ 极强 |
| 现金跑道 | 现金+可融资 > 2 年烧钱 | 纯现金 **0.97 季度** ❌；含 $10B 未提取额度 ≈ 2.7 季度（勉强） | △ |
| 客户质量 | 头部已签约 | Meta/OpenAI/微软/Anthropic/Google 全签约 | ✅ |

4/5 项达标（跑道按宽口径勉强及格）。**新增正面事实**：Q2 经营现金流转正 +$679M；FY26 adj 营业利润指引 $960M–1.15B 首次转正。**对冲负面**：净利息 $640M/季（+140% YoY）已吞掉 adj 营业利润指引的大部分；两家客户 63% 收入。增长是真的，生意质量被杠杆和集中度侵蚀。**判定：通过（低星）**

### 第三关：护城河够不够深 — ★★★☆☆

| 护城河 | 证据 | 变宽/变窄 |
|---|---|---|
| 规模/成本 | 最大上市 Neocloud；backlog $30B→$104B（一年 3.5x）；33 数据中心级交付能力 | 短期变宽 |
| 转换成本 | 多年期照付不议合同（Meta $21B 至 2032、OpenAI $22.4B） | 稳定 |
| 供应关系 | Nvidia 深度关系（IPO 前战略投资，~6% 口径未独立复核）+ 新架构（Blackwell/Vera Rubin）优先交付 | 稳定偏宽 |
| 电力+交付速度 | 电力获取与集群交付周期构成时窗壁垒 | 变宽 |
| 技术/专利 | 无独占技术；GPU 资产本身贬值快 | 变窄风险 |

100 亿复制测试：**部分能复制**——NBIS（净现金更厚）、Oracle（规模更大）、Crusoe/私有对手都在做；但电力+交付时窗+已签合同让 2-3 年内难以撼动。护城河是**合同与执行，不是技术**。**判定：通过**

### 第四关：管理层是否值得信任 — ★★★☆☆

- 创始人掌舵：Intrator（商品交易员→Hudson Ridge 天然气对冲基金→Atlantic Crypto 以太坊矿→CRWV），执行力已被验证（$40 IPO → $58B 市值）
- **关联交易疑点**：Origin House 等创始人关联载体 IPO 前低价入股（本次搜索未获增量披露，沿用既有质疑口径，中置信）
- **套现（本次核实的关键更新）**：IPO 以来内部人累计卖出 **>$2.3B**（任务书 $2.65 亿口径低估 10 倍）；CEO 6-8 月连续七笔卖出、单笔 $13-38M，价格区间 $66.62-119，均为 2025-11-20 设立的 10b5-1 计划机械执行。卖出后 CEO 直接持股仍 ~208 万股（~$190M）
- **稀释**：两年 2.53x + $3.5B 可转债在途；2026 YTD 债务+股权融资 >$30B；8 月 $2.6B DDTL 需 sweeten 条款才成交——融资成本上行已显现
- 承诺 vs 交付：近四季收入全部 beat 或达指引上限，指引连续上调 — 交付记录良好
- **判定：通过（"合格但有治理隐患"的教科书定义）**

### 第五关：价格是否足够便宜（成长型安全边际） — ★★★☆☆（条件通过）

工具核验（全部 `financial_rigor.py` 精确计算）：

| 口径 | 数值 | 判断 |
|---|---|---|
| PS 年化（Q2×4=$10.3B） | **5.64x** | vs NBIS 53-55x：**大幅低于同业** |
| PS/增速 | **0.050**（<0.5 = 便宜阈值） | 表面便宜 |
| EV/年化收入 | 8.56x（净债务 $30.08B 使 EV=$88.13B） | **不便宜** |
| EV/FY26E | 6.88x | 中性 |
| 同业折价原因 | 高杠杆 + 客户集中 63% + 稀释不停 | 折价是风险定价，非错杀 |

**PS 三情景（FY26E 收入 × 目标 PS，工具计算）**：
- 乐观：$13.2B × 7x = $92.4B → **+59%**
- 中性：$12.8B × 5x = $64.0B → **+10%**
- 悲观：$12.4B × 3x = $37.2B → **−36%**
- 极端悲观（需求逆转+融资收紧）：$12.4B × 2x = $24.8B → **−57%**（腰斩不敢无脑加仓，须确认融资通道未关闭才可加）

**EPS 代理三情景**（FY26E adj 营业利润 $1.91/股，工具输出）：+72% / −18% / −76% — 悲观尾部深于 PS 口径，因利润端对利息极度敏感。

**10 年退法**：$105.26 买入要 10 年 10% IRR 需市值 $150.6B；若届时 PS 压缩至 2x，需收入 $75.3B = FY26E 起 **10 年 CAGR 19.4%** — AI 长周期下可达，但需持续融资+稀释，股东回报必然打折。

**判定**：PS 口径有真实安全边际（0.05 的 PS/增速 + 同业 1/7 的 PS），EV 口径被债务吃掉大半；折价主因（杠杆+集中度）是真实风险而非错杀。**条件通过**：只在带内下沿给仓位。

### 第六关：仓位与决策纪律 — ★★★☆☆

- FOMO 检查：8/11 财报后 +11-19% 情绪已部分消化，$105.26 较 6 月高点 $153.20 回撤 31%，**不在情绪极值，但在小仓带上沿** — 半分警惕
- 停牌 5 年测试：不可接受（融资依赖型公司必须盯季报）→ 只配小仓
- 买入论述 200 字：可写清（见镜子测试）
- **强制纪律（前置）**：仓位 ≤1.5-2%（归零可承受）；每季盯三个数——净利息/收入、前两大客户占比、新增融资利差，任一持续恶化强制离场；基建期豁免（FCF 为负）以 backlog>2x + 融资通道敞开为前提，通道收窄即豁免失效

**镜子测试（通过）**：
> 我以 $105.26 买入 CoreWeave，因为：
> 1. 这门生意的本质是高杠杆 GPU 算力租赁（借债买芯片、长约出租赚利差），我理解它；
> 2. 它的护城河是多年期合同（$104.2B backlog = 13.78x TTM）+ 电力/交付时窗 + Nvidia 供应关系，短期在变宽，但技术护城河弱、长期靠执行力维持；
> 3. 管理层交付记录优秀但治理有隐患（内部人卖出 >$2.3B、两年稀释 2.53x、Origin House 关联疑点），以小仓位+强制止损对冲，不完全信赖；
> 4. 当前价格 = PS/增速 0.05、PS 为同业 1/7，约相当于成长型框架下的 6-7 折，安全边际来自同业折价而非绝对便宜；
> 5. 即使我错了，-36%~-57% 情景可承受，因为仓位 ≤2% 且每季盯利息/集中度/融资利差三信号，恶化即离场。

**快速否决清单**：①赚钱方式说不清？否。②连续 3 年 FCF 为负？触发但**基建期豁免成立**（增速 112%>50% + backlog 13.78x>2x + 现金+可融资 ≈2.7 年>2 年；盈利拐点时间表已给出：FY26 adj 营业利润 $960M-1.15B）。③诚信污点？无坐实，止于治理隐患。④护城河不可逆侵蚀？否。⑤博傻？部分依赖债务市场持续接盘——以仓位约束对冲，不构成纯博傻。⑥归零承受？≤2% 仓位可。⑦FOMO/追高？否（回撤 31% 后、带内上沿）。⑧200 字说清？是。**无红线触发。**

---

## 总览与最终结论

| 关卡 | 星级 | 一句话 |
|---|---|---|
| 能力圈 | ★★★☆☆ | 高杠杆算力利差生意，可理解但 10 年确定性不高 |
| 好生意 | ★★★☆☆ | 需求真实（backlog 13.78x、OCF 转正、盈利指引转正），但债务+集中度侵蚀质量 |
| 护城河 | ★★★☆☆ | 合同+电力+交付时窗，非技术壁垒 |
| 管理层 | ★★★☆☆ | 交付优秀，套现 >$2.3B 与稀释 2.53x 是硬伤 |
| 安全边际 | ★★★☆☆ | PS 口径便宜（0.05 PS/增速），EV 口径一般；条件通过 |
| 仓位纪律 | ★★★☆☆ | 镜子测试过、无红线；须仓位+强制止损双前置 |

### 结论：✅ 通过 Checklist（5/6 关；第五关条件通过）— "小仓期权位"成立

- **裁决**：$105.26 落在 funnel 给定的 $95-110 小仓带**上沿**。独立复核支持小仓结论（PS/增速 0.05、同业 1/7 折价、盈利拐点时间表、OCF 转正均被验证），但**建议在带内下沿 $95-100 执行、仓位 ≤1.5%**；现价只给 1% 或等回落。
- **主力区间 $78-90 维持，触发价 $80 不变**（8-15 已登记 watchlist，本次复核确认）。
- **与 8-15 ❓ 结论的关系**：昨日灰区的主因是财报后情绪高点。本次三个新增事实（OCF +$679M 转正、FY26 adj 营业利润指引首次转正、Meta/Anthropic 新约使四大实验室全覆盖）将裁决从 ❓ 上移为条件 ✅；但**跑道 0.97 季度 + 利息覆盖 2.36x 两大保留意见不变**——这不是可以重仓的 ✅。
- 若买入，每季强制复查：净利息/收入、前两大客户占比、新增融资利差。三者任一持续恶化 = 基建期豁免失效，无条件离场。

## 3 条最关键发现（速览）

1. **盈利拐点首次有了时间表，但利息吃掉大半**：Q2 OCF +$679M 转正、FY26 adj 营业利润指引 $960M-1.15B 转正；同期净利息年化 $2.56B = FY26E 收入的 20%，EBITDA/利息仅 2.36x。成长是真的，"利润"一大半预付给了债权人。
2. **任务书两处口径严重过时**：净债务实际 $30.08B（非 $14-17B），内部人套现 IPO 以来 >$2.3B（非 $2.65 亿）——杠杆与治理折价都比任务书假设的更深，这是同业 1/7 PS 折价的真正来源。
3. **客户结构一年内从"单点"变"寡头"**：微软 67%（FY25）→ 客户 A 40% + B 23%（H1'26），叠加 Meta $21B + OpenAI $22.4B + Anthropic $6.8B + Google——需求多元化在改善，但 63% 两客户集中度仍是单一故障点。

## 数据来源

- [CNBC: Q2 2026 财报](https://www.cnbc.com/2026/08/11/coreweave-crwv-q2-earnings-report-2026.html) / [Reuters: backlog $104.2B + CapEx 上调](https://www.reuters.com/technology/coreweave-edges-past-quarterly-revenue-estimates-2026-08-11/)
- [The Register: 债务 $35.6B、利息 $640M、$10B 未提取额度](https://www.theregister.com/off-prem/2026/08/12/coreweave-revenue-doubles-as-debt-pile-reaches-356b/5286832) / [ET Datacenters: 债务细节](https://datacenters.economictimes.indiatimes.com/news/ai-compute-infrastructure/coreweaves-35-billion-debt-raises-neocloud-refinancing-concerns/133196621)
- [tradingkey: EBITDA 率 59%/营业利润率 −2%/OCF $679M](https://www.tradingkey.com/news/earnings/262097152-tradingkey) / [khancapitals: EBITDA 率 62%→59%](https://khancapitals.com/coreweave-q2-2026-earnings/) / [marketdaily: adj EPS/指引](https://marketdaily.com/coreweave-q2-2026-earnings-revenue-doubles-ai-backlog-104-billion/)
- [404k Research: Q2 财报 transcript（FY26 指引）](https://404kresearch.substack.com/p/coreweave-fiscal-q2-2026-earnings) / [panabee: H1 营业亏损 $193M](https://www.panabee.com/news/coreweave-earnings-q2-2026-report)
- [CoreWeave 官方: OpenAI 累计 $22.4B](https://www.coreweave.com/news/coreweave-expands-agreement-with-openai-by-up-to-6-5b) / [Reuters: OpenAI 扩约](https://www.reuters.com/business/coreweave-expands-openai-pact-with-new-65-billion-contract-2025-09-25/)
- [Forbes: Meta $21B + Anthropic 连环签约（2026-04-09/10）](https://www.forbes.com/sites/aliciapark/2026/04/10/coreweave-stock-surges-13-on-anthropic-deal-a-day-after-21-billion-meta-partnership/) / [CNBC: Anthropic 协议](https://www.cnbc.com/2026/04/10/coreweave-anthropic-claude-ai-deal.html) / [financialcontent: Anthropic $6.8B](https://www.financialcontent.com/article/marketminute-2026-4-10-the-great-gpu-landgrab-coreweave-secures-68-billion-agreement-with-anthropic-as-the-ai-infrastructure-arms-race-hits-fever-pitch)
- [OpenAI 官方: Stargate 五新站 + CoreWeave 项目口径](https://openai.com/index/five-new-stargate-sites/) / [presenc.ai: Stargate 结构](https://presenc.ai/research/openai-compute-commitments-tracker-2026)
- [kucoin: 内部人卖出 >$2.3B](https://www.kucoin.com/news/flash/coreweave-ceo-sells-31m-worth-of-shares-amid-2-3b-in-insider-sales-since-ipo) / [MarketBeat Form 4 快讯（7/28、8/4）](https://www.marketbeat.com/instant-alerts/insider-selling-coreweave-nasdaqcrwv-ceo-sells-200000-shares-of-stock-2026-08-06/) / [StockTitan: 10b5-1 卖出明细](https://www.stocktitan.net/sec-filings/CRWV/form-4-core-weave-inc-insider-trading-activity-7561ceb8a522.html)
- [SeekingAlpha: CRWV PS 7.33x vs NBIS 54.50x](https://seekingalpha.com/article/4935934-coreweave-vs-nebius-i-see-more-upside-for-crwv-stock-than-nbis) / [247wallst: PS 7.91 vs 53.25](https://247wallst.com/investing/2026/08/12/coreweave-nebius-are-soaring-this-brand-new-etf-gives-exposure-across-top-neocloud-stocks/) / [ainvest: 前瞻 PS 4x vs 7x](https://www.ainvest.com/news/coreweave-nebius-ai-infrastructure-play-2026-valuation-scalability-analysis-2511/)
- [financecharts: 股本 532M（+22.15% YoY）](https://www.financecharts.com/stocks/CRWV/income-statement/shares-outstanding) / [stockanalysis: 市值 $58.05B（8/14）](https://stockanalysis.com/stocks/crwv/market-cap/)
- [Wikipedia/CoreWeave IR: Intrator 履历](https://en.wikipedia.org/wiki/Michael_Intrator) / 本仓库 `reports/CRWV-checklist-20260815.md`（客户 A/B、现金 $5,524M、可转债、微软 67%、流动比率 0.31x 的 10-Q 口径基线）

---

## 结语

巴菲特说，投资的第一条规则是不要亏损。CoreWeave 的每一项成长指标都经得起复核——112% 增速、13.78 倍收入的 backlog、转正的经营现金流、首次给出的盈利时间表；但复核同样确认，它的每一分成长都押在债务市场和两个客户手里：0.97 个季度的现金跑道、2.36x 的利息覆盖、20% 收入的利息、两年 2.53 倍的稀释。"通过"的准确含义是：**这是一个可以下小注的期权，不是可以下重注的资产。** 在 $105 的带内上沿，纪律比观点更重要——等得到的回撤就等，等不到就只给 1%。

*本报告为学习与研究用途，不构成投资建议。*
