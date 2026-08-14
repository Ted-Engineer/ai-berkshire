# Agent-A（存储链）数据采集 — 美股 H2 2026 科技扫描

- 采集人：Agent-A（存储链）
- 采集时间：2026-08-08 01:15–02:00 北京时间（周六）
- 数据截止：2026-08-07（周五）美股收盘
- 工具：内置 web_search（英文 query）；每项数据均标注来源域名与数据日期
- 重要提示：本次存储板块处于史诗级超级周期，各数据源（尤其 TTM PE、8/6 收盘价）存在口径冲突，冲突处均已注明；无法核实的字段标注 N/A。

## 〇、四股横向速览（8/7 收盘口径）

| 标的 | 8/7 收盘 | 市值 | TTM PE | Forward PE | P/B | 最近季营收 YoY | YTD | 1年 | 平均目标价 |
|---|---|---|---|---|---|---|---|---|---|
| MU 美光 | $856.97 (yahoo) | ~$968B（8/7 推算；8/6 $995.5B stockanalysis） | 19.9 | 6.1 | 9.9 | +346% (FQ3) | +199.7% | +641.4% | $1,554.5 |
| SNDK 闪迪 | ~$1,214.83 (statmuse) | ~$180B (yahoo) | 17.1（口径分歧大） | 5.9 | ~15.3 | +372% (FQ4) | +397% | +2,738% | $2,116.6 |
| WDC 西数 | ~$456.6 (coinbase/public) | ~$157B（推算） | 18.6（口径分歧大） | 28.8 (8/5 gurufocus) | 19.4 | +44% (FQ4) | +147.7% | +592.4% | $665.3 |
| STX 希捷 | $789.99 (marketchameleon) | ~$179B（8/7 推算） | 60.8 | 23.6 | 152.9 | +48% (FQ4) | +181.6% | +475.9% | $1,141.8 |

---

## 一、MU（美光 Micron）

| # | 字段 | 数据 | 来源 | 数据日期 |
|---|---|---|---|---|
| 1 | 最新价（8/7 收盘） | $856.97（开 904.65 / 高 904.65 / 低 847.02，量 1,339 万股） | finance.yahoo.com（历史价格） | 2026-08-07 |
| 2 | 市值 | $995.53B（8/6）；按 8/7 收盘推算 ~$968B（856.97 × 1.13B 股） | stockanalysis.com；推算 | 2026-08-06 / 08-07 |
| 3 | TTM PE | 19.89（macrotrends 20.10、gurufocus 19.96 交叉印证） | stockanalysis.com；macrotrends.net；gurufocus.com | 2026-08-06/07 |
| 4 | Forward PE（含 FY EPS 一致预期） | 6.11（gurufocus 8/7 为 5.63）；隐含 FY2027（截至 2027-08）一致 EPS ≈ $144–149（markets.com 6/29 引 $149.40）。注：FY2026 EPS 一致预期 3 月时仅 $54.81（Bloomberg，via itiger），已被大幅上修；simplywall.st 显示 FY2026 EPS 预期 $72.75（偏旧） | stockanalysis.com；gurufocus.com；markets.com；itiger.com；simplywall.st | 2026-08-07 / 06-29 / 03-21 |
| 5 | P/B | 9.88 | gurufocus.com | ~2026-08-07 |
| 6 | 最近一季营收 YoY / 超预期 | FQ3 FY26（6/24 公布）：营收 $41.46B，YoY +346%（约三倍/四倍于上年），超预期 $35.84B 约 +15.7%；non-GAAP EPS $25.11；毛利率 84.9%；FQ4 指引 $50B ± $1B | investors.micron.com；mlq.ai；cnbc.com；tradethepool.com；stocktitan.net | 2026-06-24 |
| 7 | YTD / 1 年涨幅 | YTD +199.65%（yahoo，截至 8/7）；1 年 +641.42%（investing.com；financecharts 总回报口径 720.31%） | finance.yahoo.com；investing.com；financecharts.com | 2026-08-07 |
| 8 | 分析师目标价 | 平均 $1,554.51（56 家，marketwatch，8 月）；tipranks 平均 $1,570；最高 $2,200（tipranks/investing.com，43 家口径平均 $1,507.79） | marketwatch.com；tipranks.com；investing.com | 2026-08-07 |
| 9 | H2 2026 催化剂 | ① FQ4 财报 9/23（指引 $50B，料创纪录）；② HBM4 放量（Nvidia/Google）；③ FY27 capex 大幅高于 $27B 的扩产落地；④ DRAM 长约/LTA 定价谈判；⑤ FQ1 FY27 财报 12 月 | finance.yahoo.com（财报日历）；stocktitan.net；perplexity.ai；ig.com | 2026-06/07 |
| 10 | 最大风险 | 存储价格周期见顶回落（TrendForce 已指 Q3 涨幅收窄）；FY27 capex 失控式抬升；股价 1 年 +641% 后的拥挤交易；AI capex 消化期 | trendforce.com；investing.com（分析） | 2026-07 |
| 11 | 供需证据 | 2026 年 HBM 全部售罄、多年期长约锁量（仅能满足关键客户 50–65% 需求）；FQ3 DRAM ASP 环比 +低 60s%；FY26 capex 从 $20B 上调至 ~$27B、FY27 更高；宣布 ~$200B 级 AI 投资计划 | investing.com；longbridge.com；seekingalpha.com；perplexity.ai；finance.yahoo.com | 2026-02/05/06/07 |

**简评（MU）**：存储超级周期核心受益者，FQ3 营收 $41.46B（YoY +346%）创纪录，2026 年 HBM 全部售罄并锁长约，FQ4 指引 $50B；forward PE 仅约 6 倍，但股价一年已涨 641%，风险在周期价格反转与 FY27 capex 超预期抬升。

---

## 二、SNDK（闪迪 SanDisk）

| # | 字段 | 数据 | 来源 | 数据日期 |
|---|---|---|---|---|
| 1 | 最新价（8/7 收盘） | ~$1,214.83（statmuse.com"昨日收盘"，8/8 抓取；MarketWatch 8/7 盘中 11:40 $1,234.07 继续走低）。⚠️ 8/6 收盘各源冲突：stockanalysis/yahoo $1,295.06(+2.9%) vs macrotrends $1,258.58 vs tradingeconomics $1,292(-4.33%)；8/7 无官方收盘价源，中等置信度 | statmuse.com；marketwatch.com；stockanalysis.com；macrotrends.net；tradingeconomics.com | 2026-08-07 |
| 2 | 市值 | $179.90B（yahoo 估值面板）；morningstar $184.5B（146M 股）；流通股 149M（stockanalysis） | finance.yahoo.com；morningstar.com；stockanalysis.com | 2026-08-07 |
| 3 | TTM PE | 17.06（stockanalysis，8/7，对应 TTM EPS ~$73.76）；⚠️ 口径分歧大：yahoo 41.52、macrotrends 19.64（8/6）、gurufocus 49.26（8/5）、companiesmarketcap 41.3（GAAP 基数/并表期差异） | stockanalysis.com；finance.yahoo.com；macrotrends.net；gurufocus.com；companiesmarketcap.com | 2026-08-05/07 |
| 4 | Forward PE（含 FY EPS 一致预期） | 5.92（stockanalysis，8/7）；对应 FY2027（截至 2027-06）一致 EPS ≈ $213（seekingalpha 估算表：212.95），营收一致预期 ~$50B（+155%，fool 7/23；5 月时仅 $41B）；FQ1 FY27 单季 EPS 一致预期 $41.45–42.28 | stockanalysis.com；seekingalpha.com；fool.com；public.com；futunn.com | 2026-08-07 / 07-23 |
| 5 | P/B | ~15.3（companiesmarketcap，2026-08）；gurufocus 15.43（BVPS $93.09，2026-03 季）；roic.ai 6.83 / finbox 10.1 为不同口径 | companiesmarketcap.com；gurufocus.com | 2026-08 |
| 6 | 最近一季营收 YoY / 超预期 | FQ4 FY26（8/5 盘后公布）：营收 $8.97B，YoY +372%、QoQ +51%，超指引上限 $8.25B、超预期 $8.32B；non-GAAP EPS $39.25 vs 预期 $34.59；GAAP EPS $43.97（净利 $6.90B）。但 FQ1 FY27 指引 $10.3–10.8B 低于市场预期，股价随后承压（单日一度 -6.8%） | investor.sandisk.com；investing.com（电话会实录）；perplexity.ai；qz.com；finance.yahoo.com | 2026-08-05/06 |
| 7 | YTD / 1 年涨幅 | YTD +397.2%（statmuse，基于 8/7 收盘）；yahoo 8/7 面板显示 +416.75%（基于 8/6 收盘口径）；1 年 +2,738.48%（investing.com；52 周区间 $41.00–2,354.39）；H1 2026 曾涨 726% 为标普第一（forbes 7/23） | statmuse.com；finance.yahoo.com；investing.com；forbes.com | 2026-08-07 |
| 8 | 分析师目标价 | 平均 $2,116.64（22 家，investing.com）；tipranks $2,397.27、zacks $2,389.42、marketbeat $1,853.14（26 家）；最高 $3,050–3,169（Bernstein 8 月上调至 $3,000） | investing.com；tipranks.com；zacks.com；marketbeat.com；schwab network | 2026-08-07 |
| 9 | H2 2026 催化剂 | ① 8/13 投资者日（Investor Day）；② FQ1 FY27 财报 11/5（EPS 一致预期 $41.45）；③ NAND Q3 合约价 QoQ +10–15%（TrendForce）/模块厂口径 +35–40%（ADATA）；④ AI/企业级 SSD 需求；⑤ 标普 500 权重/纳入效应 | perplexity.ai；public.com；investing.com；trendforce.com | 2026-07/08 |
| 10 | 最大风险 | 指引稍不及预期即暴跌（波动率全场最高，距 52 周高点 $2,354 已回撤约 48%）；纯 NAND 单一敞口；峰值盈利上的低 PE 可能是"周期顶"假象；拥挤交易与获利盘 | qz.com；finance.yahoo.com；investing.com | 2026-08 |
| 11 | 供需证据 | NAND 合约价 Q2 2026 QoQ +70–75%（TrendForce，via elinfor 4/28），Q3 再 +10–15%（TrendForce 7/3）；FQ1 FY27 指引营收 QoQ +15–20% 印证涨价延续；行业 HBM 挤占 DRAM/NAND 产能 | trendforce.com；elinfor.com；investor.sandisk.com | 2026-04/07/08 |

**简评（SNDK）**：纯 NAND 弹性标的，FQ4 营收 $8.97B（YoY +372%）、EPS $39.25 大超预期，但 FQ1 指引 $10.3–10.8B 不及预期引发回调；forward PE 约 6 倍很便宜，前提是 NAND 涨价持续；指引反复与拥挤交易是最大风险。

---

## 三、WDC（西部数据 Western Digital）

| # | 字段 | 数据 | 来源 | 数据日期 |
|---|---|---|---|---|
| 1 | 最新价（8/7 收盘） | ~$456.6（coinbase.com"today"价；public.com 8/7 盘后 8PM ET $456.88）。⚠️ 未找到 8/7 官方收盘价源，标注为约值；8/6 收盘 $451.52（-13.03%，财报后大跌；marketwatch/macrotrends/cnn 三源一致）。另注：8/6 收盘亦有源冲突（yahoo 面板 462.15 vs marketwatch/macrotrends 451.52），采信三源一致的 451.52 | coinbase.com；public.com；marketwatch.com；macrotrends.net；cnn.com | 2026-08-06/07 |
| 2 | 市值 | $155.63B（google finance，8/6 收盘口径）；流通股 344.68M（SEC proxy，4/23）→ 8/7 口径 ≈ $157B（推算）；此前 aaii $178.9B（8/5，跌前）、tradingeconomics $169.34B | finance.google.com；sec.gov；aaii.com；tradingeconomics.com | 2026-08-05/07 |
| 3 | TTM PE | 18.58（yahoo，EPS TTM $24.30）；⚠️ 口径分歧：fullratio 27.84（8/5）、companiesmarketcap 24.0、gurufocus 32.52（8/2）、public 31.47（8/3）——GAAP/非 GAAP 与季度滚动差异 | finance.yahoo.com；fullratio.com；companiesmarketcap.com；gurufocus.com | 2026-08-02/07 |
| 4 | Forward PE（含 FY EPS 一致预期） | 28.76（gurufocus，8/5，跌前口径）；FY2027（截至 2027-06）一致 EPS $20.32、营收 $19.13B（seekingalpha 估算）→ 按 8/7 价 ~$456.6 折算 ≈ 22.4x（推算） | gurufocus.com；seekingalpha.com | 2026-08-05 / 推算 |
| 5 | P/B | 19.42（macrotrends，8/1）；gurufocus 16.87、finbox 12.15、roic.ai 6.13（口径差异） | macrotrends.net；gurufocus.com；finbox.io；roic.ai | 2026-08-01 |
| 6 | 最近一季营收 YoY / 超预期 | FQ4 FY26（8/5 盘后公布）：营收 $3.75B，YoY +44%，超预期 $3.70B；non-GAAP EPS $3.56 vs 一致预期 $3.29–3.31；GAAP 毛利率 54.1%；FY26 营收 $12.92B（+36%）；FQ1 FY27 指引 $4.0–4.2B、EPS ~$3.85–4.00（超预期 ~12%）。但超预期仍跌：8/6 单日 -13%（期望过高） | investor.wdc.com；marketbeat.com；simplywall.st；tickeron.com；seekingalpha.com；finance.yahoo.com | 2026-08-05/06 |
| 7 | YTD / 1 年涨幅 | YTD +147.70%（yahoo 估值面板，8/7）；1 年 +592.39%（nerdwallet，截至 8/2）；financecharts 12 个月总回报 +522.21%、totalrealreturns +586.37%（截至 8/4） | finance.yahoo.com；nerdwallet.com；financecharts.com；totalrealreturns.com | 2026-08-02/07 |
| 8 | 分析师目标价 | 平均 $665.25（24 家，investing.com）；WSJ 平均 $674.17 / 中位 $650（7/7–8/6 窗口）；marketbeat 平均 $536.96（25 家）；最高 $1,050（investing.com/wsj/marketbeat 一致） | investing.com；wsj.com；marketbeat.com | 2026-08-06/07 |
| 9 | H2 2026 催化剂 | ① FQ1 FY27 财报 11/5；② 2026 年产能售罄 + 2027/28 长约执行；③ nearline 大容量盘（100TB 竞赛）与 HAMR/CMR 新品；④ CFO 强调 AI 推理带来"需求持久性"；⑤ 超大规模云厂商 2027 capex 计划 | finance.yahoo.com；investing.com；futunn.com；tickeron.com | 2026-08 |
| 10 | 最大风险 | 高预期脆弱性（beat 仍 -13%）；HDD 长期需求可持续性 / QLC SSD 替代争议；超大规模客户集中；高波动（beta ~2.2）；跌后估值仍依赖 capex 周期延续 | seekingalpha.com；wsj.com；robinhood.com；futunn.com | 2026-08 |
| 11 | 供需证据 | CEO Irving Tan：2026 年产能基本售罄，前 7 大客户全部签了 firm PO，2027/28 已有客户签长期合约；AI 巨头买光 2026 供应；公司称进入"多年需求上行" | reddit.com（转引管理层表态）；gizmodo.com；tradingeconomics.com | 2026-02/07 |

**简评（WDC）**：纯 HDD 标的，FQ4 营收 $3.75B（YoY +44%）超预期但股价因期望过高单日大跌 13%；2026 产能售罄、2027/28 长约在手；FY27 一致 EPS $20.3 对应约 22x，风险在 HDD 需求可持续性与高波动。

---

## 四、STX（希捷 Seagate）

| # | 字段 | 数据 | 来源 | 数据日期 |
|---|---|---|---|---|
| 1 | 最新价（8/7 收盘） | $789.99（-7.4%，marketchameleon.com 明确注明 as of 8/7）；8/6 收盘 $852.95（macrotrends/cnn/tradingview 一致） | marketchameleon.com；macrotrends.net；cnn.com | 2026-08-06/07 |
| 2 | 市值 | $189.85B（yahoo，8/6 收盘口径）；流通股 226.64M（google finance）→ 8/7 口径 ≈ $179B（推算）；tradingeconomics 160.16B（6 月季，旧） | finance.yahoo.com；finance.google.com；tradingeconomics.com | 2026-08-06/07 |
| 3 | TTM PE | 60.82（yahoo，8/7）；google finance 61.35（EPS $13.90，8/6）；gurufocus 60.97（8/5）；macrotrends 57.08（8/6）；10 年中位数 15.7，历史极值（gurufocus） | finance.yahoo.com；finance.google.com；gurufocus.com；macrotrends.net | 2026-08-05/07 |
| 4 | Forward PE（含 FY EPS 一致预期） | 23.64（yahoo，8/7）→ 隐含 FY27 EPS ≈ $33–36；FQ1 FY27 指引 non-GAAP EPS $7.30 ± $0.20（季度环比加速）；simplywall.st 提示按 $820 价仍有 37x forward（口径更保守） | finance.yahoo.com；seagate.com；simplywall.st | 2026-08-07 / 07-28 |
| 5 | P/B | 152.87（macrotrends，7/29）；heygotrade 170.2x（价 $845.35 口径）——长期回购致股东权益极薄 | macrotrends.net；heygotrade.com | 2026-07-29 |
| 6 | 最近一季营收 YoY / 超预期 | FQ4 FY26（7/28 公布）：营收 $3.6B（精确 $3.63B vs 预期 $3.49B），YoY +48%，non-GAAP 毛利率 52.7%（环比 +570bps）；non-GAAP EPS $5.71 vs 预期 $5.09–5.10（超预期约 +12%）；FY26 营收 $12.2B（+34%）、净利 $3.2B；FQ1 FY27 指引营收 $4.1B ± $0.1B（超预期） | seagate.com；investing.com（电话会实录）；247wallst.com；zacks.com；investors.seagate.com；perplexity.ai（10-K 摘录） | 2026-07-28 |
| 7 | YTD / 1 年涨幅 | YTD +181.62%（yahoo 面板，8/7）；1 年 +475.93%（investing.com；52 周区间 $144.75–1,145.00）；上半年 YTD 曾 +250%（247wallst 6/30） | finance.yahoo.com；investing.com；247wallst.com | 2026-08-07 |
| 8 | 分析师目标价 | 平均 $1,141.82（22 家，zacks）；public.com $903.43；BofA $1,150、Citi $1,150、Evercore $1,000、Morningstar $900（7 日上调）；最高 ~$1,150；另有 perplexity 引"平均 >$1,000" | zacks.com；public.com；seekingalpha.com；perplexity.ai | 2026-08-06/07 |
| 9 | H2 2026 催化剂 | ① FQ1 FY27 财报（google finance 显示 9/24，待确认，惯例为 10 月下旬）；② HAMR 爬坡 + 50TB 认证（2027）；③ 长约覆盖 2027/2029 的能见度；④ 数据中心收入动能（Q3 曾 +55%）；⑤ nearline 提价继续 | finance.google.com；tomshardware.com；investors.seagate.com；investing.com | 2026-07/08 |
| 10 | 最大风险 | TTM PE 60x 为历史极端（10 年中位 15.7x）；HAMR 执行与产能爬坡风险（5 月 CEO 供货警告曾引发暴跌）；需求周期反转；8/7 单日 -7.4% 显示高波动脆弱性 | gurufocus.com；fool.com；marketchameleon.com | 2026-08 |
| 11 | 供需证据 | nearline 产能完全分配至 2027 年（CFO，4/30）；2026 日历年 nearline 已全部售罄（CEO，2/26）；大部分 nearline 已签至 2027 和 2029 的长约（Tom's Hardware 7/29）；管理层上调"最低 20% 年收入增长"目标 | trefis.com；seekingalpha.com；tomshardware.com；heygotrade.com | 2026-02/04/07 |

**简评（STX）**：FQ4 营收 $3.6B（YoY +48%）超预期，FQ1 指引 $4.1B/EPS $7.3 强劲；nearline 产能分配至 2027、长约覆盖至 2029，能见度极高；但 TTM PE 61x 处历史极端，HAMR 执行与周期反转是主要风险。

---

## 五、背景：SK Hynix（HBM/DRAM 供需风向标）

| 事件 | 数据 | 来源 | 日期 |
|---|---|---|---|
| Q2 2026 财报（史上最强） | 营收 ₩79.32 万亿（QoQ +51%、YoY +257%）；营业利润 ₩60.54 万亿（YoY +557%，低于一致预期 ₩64 万亿）；净利润 ₩93.92 万亿；营业利润率 76%；财报次日股价一度 -10% | investing.com（公司财报）；news.skhynix.com；reuters.com | 2026-07-28/29 |
| 2026 全年售罄 | 2026 年 DRAM/HBM/NAND 全部产出已售罄（2025-10-28 Q3 电话会首次宣布）；执行副总裁 Kim Woo-hyun："2026 年 HBM、DRAM、NAND 产能被完全预订" | reuters.com；bostk.com（SK 集团博客） | 2025-10/11（持续有效） |
| HBM 产能挤占 | 2026 年 HBM 约占 DRAM 晶圆产能 25%、需求 YoY +70%，常规 DRAM/NAND 供给被持续挤出 | investing.com | 2026-02-25 |

**含义**：供给端（SK Hynix/三星/美光产能向 HBM 倾斜 + 2026 售罄）是本轮 DRAM/NAND/HDD 全面涨价的根源；H2 2026 供给依旧偏紧，涨价与长约能见度延续至 2027 甚至 2029。

## 六、供需/涨价证据汇总（跨标的）

- TrendForce（2026-07-03）：Q3 2026 常规 DRAM 合约价 QoQ +13–18%（涨幅较 Q2 收窄）；NAND 合约价 QoQ +10–15%。
- TrendForce（2026-07-08）：威刚 ADATA 预计 Q3 DRAM 采购价 +20–30%、NAND +35–40%。
- Q2 2026 NAND 合约价已 QoQ +70–75%（TrendForce，via elinfor.com，2026-04-28）；DRAM 现货 2026 年 1 月曾单月 +60–70%（cnbeta）。
- MU FQ3：DRAM ASP 环比 +低 60s%（cnbc.com/yahoo，6/24）。
- HDD：WDC 2026 售罄 + 2027/28 长约；STX nearline 分配至 2027、长约至 2029；HDD 行业"AI 巨头买光 2026 供应"（gizmodo）。
- Capex：MU FY26 ~$27B（自 $20B 上调）、FY27 大幅增加（perplexity/seekingalpha）；SK Hynix 称产能已被预订一空。

## 七、数据冲突与置信度说明

1. SNDK 8/6–8/7 收盘价：各源互相矛盾（详见上文），8/7 采用 statmuse $1,214.83（中等置信），8/6 采用 yahoo/stockanalysis $1,295.06；
2. WDC 8/7 收盘：无官方收盘源，采用 coinbase/public 盘后 ~$456.6（约值）；8/6 采用 marketwatch/macrotrends/cnn 三源一致的 $451.52；
3. TTM PE 各源分歧普遍很大（GAAP/非 GAAP/滚动期/数据陈旧），表内均列出多源区间；
4. MU 1 年涨幅价格口径 +641%（investing.com），市值/总回报口径 +716–720%；
5. STX FQ1 财报日期（google finance 显示 9/24）与惯例不符，标注"待确认"。

---

## JSON 汇总

```json
[
  {
    "ticker": "MU",
    "price": 856.97,
    "mcap_b": 968.4,
    "ttm_pe": 19.89,
    "fwd_pe": 6.11,
    "pb": 9.88,
    "rev_growth_yoy": 346,
    "ytd_pct": 199.65,
    "one_year_pct": 641.42,
    "target_avg": 1554.51,
    "notes": "8/7收盘$856.97(yahoo历史)。市值为8/7推算(856.97x1.13B股)，stockanalysis 8/6为$995.53B。FQ3 FY26营收$41.46B超预期15.7%；2026 HBM售罄+长约；FY27 EPS一致预期~$144-149。FQ4财报9/23，指引$50B。目标价最高$2200。风险：周期反转+capex抬升。"
  },
  {
    "ticker": "SNDK",
    "price": 1214.83,
    "mcap_b": 179.9,
    "ttm_pe": 17.06,
    "fwd_pe": 5.92,
    "pb": 15.3,
    "rev_growth_yoy": 372,
    "ytd_pct": 397.2,
    "one_year_pct": 2738.48,
    "target_avg": 2116.64,
    "notes": "8/7收盘~$1214.83(statmuse，中等置信；8/6各源冲突：1295.06/1258.58/1292)。TTM PE口径分歧大(17.1~49)。FQ4营收$8.97B(+372%)、EPS$39.25超预期，但FQ1指引$10.3-10.8B不及预期。FY27 EPS一致~$213。催化剂：8/13投资者日、11/5财报。最高目标价$3000+(Bernstein)。"
  },
  {
    "ticker": "WDC",
    "price": 456.6,
    "mcap_b": 157.4,
    "ttm_pe": 18.58,
    "fwd_pe": 28.76,
    "pb": 19.42,
    "rev_growth_yoy": 44,
    "ytd_pct": 147.7,
    "one_year_pct": 592.39,
    "target_avg": 665.25,
    "notes": "8/7收盘~$456.6为约值(coinbase/public盘后，无官方源)；8/6收盘$451.52(-13%，财报超预期仍跌)。市值为推算(344.68M股)。fwd_pe 28.76为gurufocus 8/5跌前口径；按FY27 EPS一致$20.32约22.4x。2026产能售罄+2027/28长约。最高目标价$1050。"
  },
  {
    "ticker": "STX",
    "price": 789.99,
    "mcap_b": 179.0,
    "ttm_pe": 60.82,
    "fwd_pe": 23.64,
    "pb": 152.87,
    "rev_growth_yoy": 48,
    "ytd_pct": 181.62,
    "one_year_pct": 475.93,
    "target_avg": 1141.82,
    "notes": "8/7收盘$789.99(-7.4%，marketchameleon)；8/6收盘$852.95。市值为8/7推算(226.64M股)。FQ4营收$3.6B(+48%)、EPS$5.71超预期12%；FQ1指引$4.1B/$7.30。nearline分配至2027、长约至2029。P/B极高系回购致权益薄。最高目标价~$1150(BofA/Citi)。"
  }
]
```
