# F组数据采集报告：美股互联网 / 金融科技 / 高动量股（H2科技扫描）

- **采集Agent**: Data Agent-F（互联网/金融科技/动量股）
- **报告日期**: 2026-08-08（周六，北京时间）
- **数据截止**: 2026-08-07（周五）美股收盘；部分字段为8/6收盘（已逐条标注）
- **采集方式**: web_search（英文query），优先来源 stockanalysis.com / macrotrends / slickcharts / Yahoo Finance / investing.com / MarketWatch / gurufocus / 公司IR
- **纪律**: 搜索不到的字段一律写 N/A；来源冲突时取多数源并注明；Yahoo"trailing returns"模块的正负号在抓取中丢失，凡涉及YTD符号均用第二个独立来源交叉验证（方法见文末）

---

## 0. 市场快照（交叉验证背景）

| 指标 | 数值 | 来源/日期 |
|---|---|---|
| S&P 500 YTD（总回报） | +13.38%（价格回报+12.63%） | slickcharts，截至8/6收盘 |
| Nasdaq 100 YTD | +16.33% | slickcharts，截至8/6收盘 |
| 道指 YTD | +12.11% | slickcharts，截至8/6收盘 |
| 比特币现价 | ~$64,098（低迷） | coinbase.com，8/7-8/8 |
| 市场结构 | 2026年主线=存储/光模块/AI硬件（SNDK、DELL、MU、STX、INTC等）；7月高估值科技深度回调（MarketWatch 7/17：约19只科技股7月跌超25-30%）；互联网/消费平台普遍跑输指数 | MarketWatch/slickcharts/investors.com |

---

## 1. 主数据表（13只标的）

> 价格说明：优先取8/7收盘；仅有8/6收盘的以(8/6)标注；"≈"表示8/7盘中/估算值（来源为报价页"当前价"，非官方收盘确认）。

| Ticker | 最新价($) | 市值 | TTM PE | Fwd PE | P/FCF | 最近一季营收YoY | YTD | 1年 |
|---|---|---|---|---|---|---|---|---|
| MELI | 1,826.25（MarketWatch 8/7；8/6收盘1,830.00） | ~$92.7B（Yahoo 92.78B） | 49.9（stockanalysis/gurufocus，8月初） | 46.1-46.3 | ~8.1x（gurufocus FCF收益率12.41%，8/1） | Q2 +50%（$10.2B，8/5发布） | **-9.15%**（Barron's） | -22.25%（Barron's；investing.com -17.66%） |
| SHOP | 147.44（8/6收盘）；8/7≈147.0（CNN，-0.40） | ~$189.7B（stockanalysis/Google Finance） | 99.5 | 70.9 | N/A | Q2 +34%（$3.58B，8/5发布） | -8.57%（MarketBeat） | -3.0%（investing.com -3.09%） |
| APP | ≈337.4（8/7，robinhood报价；8/6收盘335.67，单日-19.66%） | ~$112.3B（stockanalysis，8/6） | 25.8-26.2 | 18.6（stockanalysis；SeekingAlpha 21.3） | 30.4（macrotrends 8/2，财报暴跌前口径） | Q2 +52.8%（$1.924B，8/5盘后发布） | **≈-52.8%**（8/6收盘推算；macrotrends截至8/5为-41.25%） | -26.38%（investing.com） |
| DUOL | 122.00（8/7，eToro；8/6收盘122.58） | ~$5.7B（MarketWatch 5.72B） | 14.5-14.6 | 45.3-46.4 | N/A | Q2 +18%（$298.5M，8/5盘后发布） | ≈-37%（Perplexity/macrotrends推算） | -60.44%（stockanalysis） |
| COIN | 146.19（8/7，slickcharts；8/6收盘145.41） | ~$38.6B | N/A（TTM净亏损-$988M） | 109-128 | 22.56（stockanalysis） | Q2 ≈-19%（$1.22B vs 上年$1.5B，7/30发布） | -30.5%（slickcharts；Yahoo -33.6%） | ≈-51.7%（Yahoo；stockanalysis市值-53.1%） |
| HOOD | ≈93.37（8/7，slickcharts；8/6收盘90.71） | ~$84B（按8/7价×899.08M股） | 40.2-40.7 | 38.9 | N/A | Q2 +32%（创纪录$1.31B，7/29发布） | -20.57%（slickcharts） | -12.0%（totalrealreturns，截至8/5） |
| SOFI | ≈18.2（8/7估算，MarketWatch盘前18.18；8/6收盘18.10-18.31各源不一） | ~$23.5B | 37.9-38.4 | 24.7-25.0 | N/A | Q2 +40%（调整后净收入$1.2B创纪录，7/29发布） | ≈-25%（8/6推算；截至8/3为-33.4%，totalrealreturns） | -18.11%（totalrealreturns，截至8/3） |
| UBER | 70.47（8/6收盘；8/7未查到官方收盘价，N/A） | ~$143.9B（stockanalysis，8/6） | 15.4-17.8（各源口径不一） | 16.8-19.5 | 15.5（macrotrends 8/4；gurufocus 15.13） | Q2 +12%（$14.19B，8/5发布） | **-8.29%**（Yahoo，截至8/7；符号经"2026年抛售"新闻交叉验证） | -20.33%（TradingView） |
| SPOT | 475.07（8/6收盘；8/7盘中≈479，MarketWatch） | ~$97.7B | 26.1-33.7（各源口径不一） | 30.3-33.7 | N/A | Q2 +14%（€4.777B，8/4发布） | -16.1%（simplywall.st） | -29.78%（investing.com） |
| RDDT | ≈160.1（8/7，robinhood报价；8/6收盘153.60） | ~$30.8B | 35.2-36.6 | 25.0-26.1 | N/A | Q2 +61%（$805M，7/30发布，大超预期） | ≈-34%（Yahoo符号推断；tikr 5月末-40%） | -29.97%（investing.com） |
| PYPL | ≈59.35（8/7，robinhood报价；8/6收盘59.78，+3.19%） | ~$50.8B | 11.3 | 10.8 | N/A | Q2 +5%（$8.68B，7/28发布） | ≈-4%（估算，低置信，见注） | -13.63%（investing.com） |
| GOOGL | **355.31（8/7收盘，Yahoo历史数据确认）** | ~$4.35T（12.23B股×355.31） | 17.95 | 26.93 | 87.7（macrotrends 8/6；资本开支吞噬FCF，Q2 FCF/股-$0.48） | Q2 +24%（$119.8B，7/22发布） | **+13.8~14.3%**（Yahoo GOOG +13.79%截至8/6；slickcharts +14.30） | +77.61%（investing.com） |
| META | 585.49（8/6收盘；8/7未查到官方收盘价，N/A） | ~$1.49T（2.55B股×585.49） | 22.2 | 18.4 | 36.97（macrotrends 8/6） | Q2 +28%（$60.80B，7/29发布） | -10.63%（slickcharts） | -23.32%（investing.com） |

**注**：
1. PYPL YTD为估算：2025年全年-31.60%（slickcharts年报数据），2025-12 Forbes提及"PYPL 2025年跌约30%"→ 2025年末约$62 → 现价59.78≈YTD -4%（±3%）。置信度低。
2. APP YTD：macrotrends显示截至8/5收盘(417.80)年内-41.25%，隐含2025年末≈$711；8/6暴跌19.66%至335.67 → YTD≈-52.8%。Yahoo页面"49.08%"经多源验证为误读（与价格史矛盾），弃用。
3. SOFI 8/6收盘价各源在18.10-18.31间冲突（Yahoo/MarketWatch/macrotrends），取≈18.2中值。
4. 52周区间参考：MELI 1,495-2,548.5；APP 332.19-745.61（现价贴近年内低点）；DUOL 87.89-415.76；HOOD 63.52-153.86；GOOGL 196.60-408.61；META 520.26-796.25；RDDT 119.27-282.95；PYPL 38.46-79.22。

---

## 2. 专节：S&P 500 2026年至今（YTD）涨幅榜（动量交叉验证）

### 2.1 当前榜单（slickcharts.com/sp500/performance，抓取于2026-08-08，数据截至~8/7收盘）

| 排名 | 代码 | 公司 | YTD涨幅 |
|---|---|---|---|
| 1 | SNDK | Sandisk | +458.64% |
| 2 | DELL | Dell Technologies | +259.07% |
| 3 | MU | Micron Technology | +220.82% |
| 4 | STX | Seagate Technology | +219.05% |
| 5 | INTC | Intel | +178.81% |
| 6 | WDC | Western Digital | +162.10% |
| 7 | MRVL | Marvell Technology | +147.75% |
| 8 | AMD | Advanced Micro Devices | +128.46% |
| 9 | LITE | Lumentum Holdings | N/A（搜索片段截断，未取到数值） |
| 10-20 | — | 未能从搜索片段完整获取 | N/A |

**10-20名说明（诚实披露）**：搜索未能返回完整10-20行。根据MarketWatch H1榜单碎片与多源交叉，第10-20名大概率包含（无排序）：CIEN（Ciena）、COHR（Coherent）、MRNA（Moderna）、GNRC（Generac）、FIX（Comfort Systems）、VRT（Vertiv）、NVDA、AVGO等；其中非科技成分约3只（MarketWatch："top 20中仅3只非科技"）。**此名单不完整部分按要求标注N/A，不作编造。**

### 2.2 MarketWatch《S&P 500上半年20大牛股》（2026-06-30发布，H1口径，补充参考）

搜索仅取到表格碎片（原文付费墙）：
- SNDK：H1榜首（各源数字471%-488%不等）
- INTC：+278%（Morningstar转载版"第3名"）/ +257%（moomoo转载版"第4名"）——两转载版排名与数字略有出入
- WDC：+271%；MRVL：+251%；STX：+250%；DELL：+243%；LITE：+133%（1年+339%）
- 榜单其余确认出现的名字：MRNA（Moderna）、GNRC（Generac）、FIX（Comfort Systems）、CIEN、COHR
- 特征："除3只外全部为科技股；半导体与计算机硬件主导"（MarketWatch 6/30）；"62%的S&P 500成分股年内上涨"

### 2.3 动量交叉验证结论

1. **2026年动量主线是"存储+光模块+AI硬件"**（SNDK/MU/STX/WDC/INTC/MRVL/LITE/CIEN/COHR/DELL），与F组互联网/金融科技标的几乎无交集。
2. **7月起动量退潮**：SNDK从7/21的~707%（Yahoo sg）回落至8/7的458.6%； MarketWatch 7/17统计约19只科技股7月单月跌超25-30%。APP（-20%，8/6）、META（财报后-9.5%）、COIN（近52周低点）均为本轮回调受害者。
3. **HOOD曾在上半年短暂进入YTD前十**（stockstoearn社媒帖，约Q1口径："5. Robinhood"，当时SNDK +594%），但现YTD已转负（-20.6%）——金融科技动量已熄火。
4. 本组13只中仅 **GOOGL（+13.8%）与UBER口径的YTD为正/接近指数**（UBER -8.3%实为负），其余全部跑输S&P 500（+13.38%）。

---

## 3. 必查专节一：MELI（MercadoLibre）

### Q2 2026财报（重要更正：已发布，非8月中旬）
- **发布日期：2026-08-05（周三）盘后**（公司IR/MarketBeat/investing.com均确认）。任务假设的"8月中旬"已过时。
- **Q2业绩**：净收入+金融收入 **$10.2B，+50% YoY**（连续第30个季度增速>30%，barchart）；经营利润$683M，经营利润率6.7%（利润率压缩）。
- **预期对比**：营收超预期+4.07%，EPS超预期+5.75%（Zacks）；MarketScreener：Q2营收$10.20B vs 预期（beat）。
- **股价反应**：尽管beat，财报后下跌——8/4收盘≈$1,922.57（Morningstar prev close口径）→ 8/6收盘$1,830（约-4.8%），市场担忧利润率压缩。
- **下次财报**：Q3 2026预估 **2026-11-04**（Yahoo Finance earnings date）。

### 2026年回调原因拆解（多源）
1. **巴西竞争白热化**：公司主动下调巴西免运费门槛与take rate应对竞争（Motley Fool 5/12："Down 40%, Is It Time To Buy MercadoLibre?"）；Q4 2025财报后股价即因"巴西等关键市场竞争加剧"回落（Investor's Business Daily 2/25）。
2. **利润不及预期+投入加码**：Q4 2025利润miss（Reuters 2/24：信贷与物流投入导致利润下滑，营收+45%但股价跌超6%）；Q1 2026营收$8.85B +49%（四年最快）但EPS miss，股价年内一度-17%（tikr 6/22）。
3. **利润率压缩**：Q2经营利润率仅6.7%（信贷扩张+物流投入+补贴），是8/5财报后下跌的直接触发。
4. **宏观**：巴西高利率环境+雷亚尔汇率波动（多源提及，未找到单一定量来源，标注为定性判断）。
5. **幅度**：52周高点$2,548.50 → 3月低点约$1,495 → 现价$1,826；年初至今-9.15%（2025年末收盘$2,014.26，fool.com确认）。

### 估值锚
- 2.9x trailing P/S，"上市以来最便宜"（Reddit价值投资帖）；FCF收益率12.41%（gurufocus，8/1，10年中位数1.82%的6.8倍）；分析师共识Buy，目标价$2,327.50（public.com，12位分析师）。

---

## 4. 必查专节二：AppLovin（APP）——AXON增速与估值

### 最新增速（2026）
- **Q2 2026（8/5盘后发布）**：营收**$1,924M，+52.8% YoY**（vs 预期$1,940M，罕见miss；略低于自身指引区间$1,915-1,945M中点）；GAAP净利润$1,267M；摊薄EPS $3.76（beat）。
- **Q3指引偏软** → 股价8/6暴跌**-19.66%**（$417.80→$335.67），盘后一度-24%（Perplexity/WSJ/SeekingAlpha："AppLovin breaks investors' hearts"）。
- **增速轨迹（减速中）**：Q4 2025 +66% → Q1 2026 +59%（$1.84B，QoQ +11%）→ Q2 2026 +52.8%。
- **AXON电商化**：AXON 2.0广告引擎驱动的**电商平台于2026年6月正式上线**（SeekingAlpha 5/6指引电话会："as Axon opens in June"）；BofA 6/10重申Buy；公司称可维持约80%调整后EBITDA率（Q2指引84-85%），已回购近$7.5B股票（Yahoo 6/9）。
- **卖方预期**：2026营收~$8B、2027 ~$10B（accruedint 2025-12）；另一口径2026 +38%/2027 +29.5%（finviz 3/6）。

### 估值
- TTM PE 25.8-26.2；Fwd PE 18.6（stockanalysis）~21.3（SeekingAlpha）；PEG 0.69；P/FCF 30.4（macrotrends 8/2，暴跌前口径，暴跌后约25x）。
- gurufocus 8/5：价格$419.70 vs GF Value $511 → "适度低估"（财报前口径）。
- **股价位置**：YTD ≈ -53%（年内从~$711跌至$336）；1年 -26.4%；52周区间$332.19-$745.61，**现价几乎贴着年内最低点**。分析师共识仍为Buy、目标价$590.55（public.com，20位分析师）——多空分歧极大。

---

## 5. 每股H2催化剂 / 最大风险 / 简评（~80字）

### MELI — MercadoLibre
- **H2催化剂**：Q3财报11/4；信贷(Mercado Pago)与广告变现；墨西哥扩张；巴西份额巩固（约35%）。
- **最大风险**：巴西竞争（take rate/补贴战）持续压缩利润率；信贷资产质量在高利率下恶化；拉美宏观/汇率。
- **简评**：增速仍是50%的顶级复利机器，但利润率从"投入期"跌到6.7%吓退市场。2.9x PS+12% FCF收益率为上市以来最便宜，估值已计大量悲观；赌的是投入换规模的拐点。

### SHOP — Shopify
- **H2催化剂**：Q2大超预期（8/5，+34%，GMV +32%至$115.6B）后Q3指引亦超预期；Q3财报10月末；企业级/支付渗透提升。
- **最大风险**：估值（Fwd PE ~71x）对增速容错极低；宏观消费走弱与关税扰动中小商家。
- **简评**：财报后单日+17%、单月+22.5%，基本面重新加速（营收+34%、FCF利润率健康），是13只里少数"动量+基本面"共振者，唯估值昂贵，回调即机会型标的。

### APP — AppLovin
- **H2催化剂**：AXON电商广告6月上线后的首个完整放量季（Q3财报11月）；回购；80%+ EBITDA率。
- **最大风险**：增速减速+指引偏软破坏叙事；电商广告面对Meta/Google正面竞争；高预期下任何miss都会暴跌（已演示-20%）。
- **简评**：Q2营收+53%却因差2千万miss而暴跌20%，现价贴年内低点、Fwd PE仅18x。AXON电商是二次成长期权，但市场要先看到Q3证据。高风险高赔率。

### DUOL — Duolingo
- **H2催化剂**：Max分层订阅等变现测试；DAU +23%动能；2028年100M DAU目标；Q3财报11月初。
- **最大风险**：bookings增速被主动砍到+11%（原可+20%）；AI（ChatGPT类）对语言学习的替代担忧；SBC约占营收15%。
- **简评**：一年内从$416跌到$122（-60%），2月指引暴雷+8月Q3指引再疲软，估值杀到TTM PE 14.5x的"假便宜"（forward PE 46x）。增长换利润的再定价未完成，接刀需谨慎。

### COIN — Coinbase
- **H2催化剂**：USDC生态（平台USDC达$20B历史新高、占流通量30%+）；"Everything Exchange"衍生品/股票代币；Q3财报10月末。
- **最大风险**：加密熊市（BTC ~$64k）拖累交易量；连续亏损（Q2 EPS -$1.36，Q1 -$1.49）；监管反复。
- **简评**：YTD -30%、贴近52周低点，Q2营收-19%且亏损扩大，基本面与币价双杀。唯一的亮点是USDC与订阅服务的收入多元化，属于"赌加密周期反转"的高贝塔仓位。

### HOOD — Robinhood
- **H2催化剂**：预测市场/事件合约（Q2创纪录的核心驱动）；国际化（Bitstamp）；净入金创纪录$22B；Q3财报10月末。
- **最大风险**：交易量高度顺周期，加密/期权热度退潮即杀业绩；估值40x对增长依赖大；监管（预测市场）。
- **简评**：Q2创纪录（营收+32%、EPS +48%）但股价YTD -20.6%——市场在提前定价交易热度的均值回归。预测市场是真增量，但需证明非一次性。动量已破位。

### SOFI — SoFi
- **H2催化剂**：FY26营收指引上调至$4.75-4.85B（+32-35%）；科技平台(to-B)输出；降息利好贷款业务；Q3财报10月末。
- **最大风险**：利润指引未同步上调（财报日-10%的直接原因）；消费信贷质量；估值不便宜（Fwd PE ~25x）。
- **简评**：营收+40%创纪录、会员增长强劲，但"增收不提利"让市场两次用脚投票（4月-13%、7月-10%）。YTD约-25%~-33%。拐点要看Q3 EPS是否跟上营收。

### UBER — Uber
- **H2催化剂**：Q3财报11/3；robotaxi合作网络（自动驾驶平台化）；广告+会员(Uber One)；GB +24%的动能。
- **最大风险**：指引疲软（8/5财报后-5%）；AV竞争长期叙事压制估值；监管与司机成本。
- **简评**：Q2 GB +24%、净利+86%但营收小幅miss+指引弱，YTD -8.3%。Ackman称抛售后"no brainer"。15x PE、15x P/FCF的现金流机器，是组内估值最舒服的资产之一。

### SPOT — Spotify
- **H2催化剂**：300M付费订阅里程碑后的提价空间；播客/有声书变现；利润率扩张记录（Q2毛利率创新高）；Q3财报10月末。
- **最大风险**：利润指引不及预期（Q2财报后-4.9%的直接原因）；音乐版权成本；FX逆风。
- **简评**：用户与利润率双优（订阅+9%、MAU 777M、经营利润€655M），但营收小幅miss+保守指引压估值，YTD -16%。26-30x PE的"消费股里的成长股"，等指引转强。

### RDDT — Reddit
- **H2催化剂**：广告营收+64%动能；AI数据授权；Q3财报10月末；DAU 130M+（+18%）。
- **最大风险**：**Google搜索导流"choppy and declining"**（AI Overviews侵蚀）——Q2大超预期仍暴跌11-21%的核心原因；广告单一依赖；用户增速放缓。
- **简评**：连续第8个季度营收增速60%+、净利率31%，基本面是组内最炸裂的之一；但流量入口被AI搜索卡脖子，YTD ≈-34%。35x PE买的是"搜索脱敏"的兑现。

### PYPL — PayPal
- **H2催化剂**：**$53B/$60.50-per-share收购报价传闻**（7/15，单日+16%、单周+23%）——是否推进是最大事件变量；新CEO战略；Q2 beat+FY EPS指引上调至$5.38；agentic commerce/Fastlane。
- **最大风险**：收购若证伪则回吐涨幅；无品牌结账份额持续被Apple Pay/Stripe蚕食；增速仅+5%。
- **简评**：11x PE、FY指引上调、双底形态突破51.46（技术面），是被遗忘的价值股+并购期权。YTD≈-4%、1年-13.6%，下行靠估值托底，上行靠收购或增长叙事重建。

### GOOGL — Alphabet
- **H2催化剂**：Cloud +82%、积压订单$514B的兑现；Gemini/TPU商业化；Q3财报10月末；搜索份额企稳证据。
- **最大风险**：AI资本开支大超预期（Q2财报后股价因此回落）；FCF被capex吞噬（P/FCF 88x、Q2 FCF/股转负）；反垄断救济措施。
- **简评**：2026年大型互联网里唯一的真动量股：营收+24%、云+82%、1年+77.6%、市值$4.35T。17.9x PE买AI赢家并不贵，但"增收不增FCF"的capex叙事是H2最大变数。

### META — Meta Platforms
- **H2催化剂**：广告营收+28%的AI变现证据；Q3财报10月末；超级智能实验室模型进展。
- **最大风险**：**capex指引上调至$130-145B、Q3指引偏弱、Q2 FCF暴跌91%至$784M**（财报后-9.5%）；卖方预计2027 FCF转负至约-$24B。
- **简评**：营收端是近年最快增速，利润端却被AI开支吞没——EPS miss 14%、YTD -10.6%。18x forward PE不贵，但市场要的是"开支纪律"信号，H2走势取决于capex叙事的二次定价。

---

## 6. 数据质量与缺口声明

1. **8/7官方收盘价缺失**：UBER、META、SPOT（仅有8/6收盘）；APP、HOOD、SOFI、RDDT、PYPL、COIN的8/7价来自报价页"当前价"或slickcharts快照，非交易所收盘确认，均标"≈"。
2. **符号推断**：Yahoo"trailing returns"模块抓取的YTD数值丢失正负号。已用独立来源逐一验证：MELI（Barron's -9.15%✓）、META（slickcharts -10.63✓）、HOOD（slickcharts -20.57✓）、COIN（slickcharts -30.52✓）、SOFI（totalrealreturns -33.39✓）、UBER（MarketWatch"2026抛售"新闻✓）、RDDT（价格史推算✓）。GOOGL为正（slickcharts +14.30✓，无符号歧义）。
3. **APP YTD的Yahoo"49.08%"与价格史严重矛盾**（6月报道$469时YTD -24%），判定为组件误读，弃用；采用macrotrends年报口径推算（-52.8%）。
4. **来源冲突未完全收敛**：SOFI 8/6收盘（18.10 vs 18.25 vs 18.31）、RDDT 8/6收盘（150.87 vs 153.60）、HOOD 8/6收盘（90.71 vs 92.82，判定后者为8/5数据错位）、SHOP市值（tradingeconomics $261.8B为离群值，弃用）。
5. **N/A清单**：SHOP/DUOL/HOOD/SOFI/SPOT/RDDT/PYPL的P/FCF；LITE的YTD数值；S&P 500 YTD榜单第9-20名完整数值；UBER/META/SPOT的8/7收盘价。
6. 所有财报日期、指引、增长率均来自公司公告或主流财经媒体（Reuters/CNBC/WSJ/Yahoo/SeekingAlpha/Zacks/MarketBeat），引用见正文。

---

## 7. JSON数据（机器可读）

```json
[
  {"ticker":"MELI","price":1826.25,"mcap_b":92.7,"ttm_pe":49.9,"fwd_pe":46.2,"rev_growth_yoy":50.0,"ytd_pct":-9.15,"one_year_pct":-22.25,"notes":"Q2已于8/5发布:营收$10.2B+50%超预期但利润率压缩至6.7%股价跌;巴西竞争+信贷物流投入是回调主因;FCF收益率12.4%;下次财报11/4;价格=8/7收盘(MarketWatch)"},
  {"ticker":"SHOP","price":147.44,"mcap_b":189.7,"ttm_pe":99.5,"fwd_pe":70.9,"rev_growth_yoy":34.0,"ytd_pct":-8.57,"one_year_pct":-3.1,"notes":"Q2 8/5发布大超预期+34%,GMV+32%,股价+17%;Q3指引超预期;单月+22.5%动量回归;风险=Fwd PE~71x;价格为8/6收盘,8/7≈147.0"},
  {"ticker":"APP","price":337.4,"mcap_b":112.3,"ttm_pe":25.8,"fwd_pe":18.6,"rev_growth_yoy":52.8,"ytd_pct":-52.8,"one_year_pct":-26.4,"notes":"Q2营收$1.924B+52.8%差$16M miss+Q3指引软,8/6暴跌-19.7%;AXON电商6月上线;增速66%→59%→53%减速;现价贴52周低点;价格为8/7报价页≈值"},
  {"ticker":"DUOL","price":122.00,"mcap_b":5.7,"ttm_pe":14.5,"fwd_pe":46.4,"rev_growth_yoy":18.0,"ytd_pct":-37.0,"one_year_pct":-60.4,"notes":"Q2 beat($298.5M+18%)但Q3指引$302M疲软,8/6再跌9%;FY bookings仅+11%;2月指引暴雷后一年-60%;AI替代担忧;Max变现测试是H2看点"},
  {"ticker":"COIN","price":146.19,"mcap_b":38.6,"ttm_pe":null,"fwd_pe":109.2,"rev_growth_yoy":-18.7,"ytd_pct":-30.5,"one_year_pct":-51.7,"notes":"Q2营收$1.22B miss,EPS-$1.36亏损扩大,贴52周低点;BTC~$64k低迷;USDC平台余额$20B创新高是亮点;TTM净亏损故PE=N/A;价格=8/7 slickcharts"},
  {"ticker":"HOOD","price":93.37,"mcap_b":84.0,"ttm_pe":40.2,"fwd_pe":38.9,"rev_growth_yoy":32.0,"ytd_pct":-20.57,"one_year_pct":-12.0,"notes":"Q2创纪录:营收$1.31B+32%/EPS+48%/净入金$22B;预测市场驱动;但市场定价交易热度均值回归,YTD转负;价格=8/7 slickcharts≈值"},
  {"ticker":"SOFI","price":18.2,"mcap_b":23.5,"ttm_pe":38.0,"fwd_pe":24.7,"rev_growth_yoy":40.0,"ytd_pct":-25.0,"one_year_pct":-18.1,"notes":"Q2调整后净收入$1.2B创纪录+40%,FY营收指引上调至$4.75-4.85B(+32-35%),但利润指引未调→财报日-10%;YTD截至8/3为-33.4%后反弹;价格/市值为≈估算"},
  {"ticker":"UBER","price":70.47,"mcap_b":143.9,"ttm_pe":15.4,"fwd_pe":16.8,"rev_growth_yoy":12.0,"ytd_pct":-8.29,"one_year_pct":-20.33,"notes":"Q2 GB+24%/净利+86%但营收$14.19B小幅miss+指引弱,8/5后-5%;Ackman称抛售后no-brainer;15x PE+15x P/FCF;价格为8/6收盘(8/7 N/A);下次财报11/3"},
  {"ticker":"SPOT","price":475.07,"mcap_b":97.7,"ttm_pe":26.1,"fwd_pe":30.3,"rev_growth_yoy":14.0,"ytd_pct":-16.1,"one_year_pct":-29.8,"notes":"Q2订阅300M(+9%)/MAU 777M/利润率创新高,但营收€4.777B小幅miss+利润指引弱→-4.9%;价格为8/6收盘(8/7盘中≈479);提价与播客是H2催化"},
  {"ticker":"RDDT","price":160.1,"mcap_b":30.8,"ttm_pe":36.6,"fwd_pe":26.1,"rev_growth_yoy":61.0,"ytd_pct":-34.4,"one_year_pct":-30.0,"notes":"Q2 $805M+61%大超预期(EPS $1.25 vs $0.95),但Google搜索导流'choppy and declining'→暴跌11-21%;连续8季增速60%+;价格=8/7报价页≈值(8/6收盘153.60)"},
  {"ticker":"PYPL","price":59.35,"mcap_b":50.8,"ttm_pe":11.3,"fwd_pe":10.8,"rev_growth_yoy":5.0,"ytd_pct":-4.0,"one_year_pct":-13.63,"notes":"Q2 $8.68B+5% beat,FY EPS指引上调至$5.38;7/15传$53B($60.5/股)收购报价,单周+23%;11x PE价值股+并购期权;YTD为估算值(低置信);价格=8/7报价页≈值"},
  {"ticker":"GOOGL","price":355.31,"mcap_b":4345.0,"ttm_pe":17.95,"fwd_pe":26.93,"rev_growth_yoy":24.0,"ytd_pct":13.8,"one_year_pct":77.61,"notes":"Q2营收$119.8B+24%/Cloud+82%至$24.8B/积压订单$514B;组内唯一真动量股,市值$4.35T;风险=AI capex吞噬FCF(P/FCF~88x);价格=8/7收盘(Yahoo历史数据确认)"},
  {"ticker":"META","price":585.49,"mcap_b":1493.0,"ttm_pe":22.2,"fwd_pe":18.4,"rev_growth_yoy":28.0,"ytd_pct":-10.63,"one_year_pct":-23.32,"notes":"Q2营收$60.8B+28% beat但EPS miss 14%+Q3指引弱+capex上调至$130-145B,FCF暴跌91%至$784M→财报后-9.5%;价格为8/6收盘(8/7 N/A)"}
]
```

---
*报告结束。Agent-F，2026-08-08 01:30 (UTC+8)。所有数字均可通过文中来源复核；未标注来源的推断已显式标记"估算/≈"。*
