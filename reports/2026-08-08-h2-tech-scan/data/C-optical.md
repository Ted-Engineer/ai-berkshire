# C腿：光通信与光模块/互连 —— H2 2026 美股科技扫描数据包

- 采集时间：2026-08-08（周六，北京时间，Get-Date 确认）
- 美股最近完整交易日：2026-08-07（周五）
- 采集方式：web_search 英文查询；主要来源 stockanalysis.com / macrotrends / Yahoo Finance / gurufocus / MarketBeat / investing.com / Reuters / CNBC / 公司IR
- 重要口径说明：免费数据源快照存在滞后（部分站点的"8/6收盘"实为8/5数据），且 GAAP 与 non-GAAP EPS 差异大；关键字段均标注来源与日期，冲突处并列列出。多数标的未能检索到 8/7（周五）精确收盘价，表中以可验证的最新收盘价+日期为准，严禁外推。

## 一、总表（11 只标的）

| Ticker | 最新价（日期） | 市值 | TTM PE | Forward PE | 最近一季营收YoY | YTD涨幅 | 1年涨幅 | 来源/备注 |
|---|---|---|---|---|---|---|---|---|
| COHR | $355.83（8/6收盘，Yahoo历史页） | ~$69.6B（区间$65.4-74.0B） | 135.5（stockanalysis） | 43.4（stockanalysis；SeekingAlpha 61.3） | +21%（FQ3 FY26 营收$1.81B，pro-forma +27%） | +103.49%（Yahoo，截至8/7） | +188.37%（investing.com） | 市值：SeekingAlpha $65.4B@8/5收盘$334.22；Yahoo $73.5B、stockanalysis $74.0B口径不同。8/7收盘价未检索到 |
| LITE | $838.06（8/6收盘，Yahoo OHLC+macrotrends） | ~$65B（838.06×77.8M股） | 125.7（Yahoo；public.com 144.7、MarketBeat 155.2） | 47.3（gurufocus 8/4，FY27口径；FY26口径>120x，TradingKey） | +90%（FQ3 FY26 营收$808.4M） | +141.22%（Yahoo，截至8/7） | +666.09%（investing.com） | 52周区间$108.71-$1,085.68；较历史高点回撤约23% |
| FN | $543.95（8/6收盘，macrotrends/eToro） | ~$19.5B（public.com $19.0B@8/5） | 45.4（macrotrends 8/6；Yahoo 47.95） | 30.5（gurufocus 8/6） | +39.3%（FQ3 FY26 营收$1,214.3M vs $871.8M） | +22.59%（Yahoo，截至8/7） | +58.13%（MarketWatch） | 8/7盘中区间$502.00-547.57、开$509.50（investing.com），收盘未检索到；FQ4财报8/17 |
| AAOI | $140.90（8/6收盘，+13.43%，Yahoo历史页） | ~$10.0B（Yahoo $9.97B；macrotrends $10.56B@8/6） | N/A（GAAP亏损，TTM EPS -$0.65） | N/A | +86%（Q2 2026 营收$191.9M，8/6发布，创纪录） | +297.10%（Yahoo，截至8/7） | +434.74%（Yahoo，截至8/7） | 8/6财报后单日+13.4%；Q2净亏-$22.78M（GAAP），800G收入$12.8M环比翻倍；全年收入目标>$1B；beta 3.79 |
| GLW | $157.18（8/6收盘，macrotrends） | $135.4B（Yahoo） | 72.4（Yahoo；stockanalysis 73.1） | 42.8（stockanalysis） | 核心营收+17%（Q2核心$4.74B；光通信板块营收$2.07B +32%） | +80.12%（Yahoo，截至8/7） | +145.67%（SeekingAlpha；FinanceCharts 12月总回报+154.6%） | 7/28因Q3指引跳水（详见事件专节）后已收复全部失地（8/6收盘$157.18 > 7/27收盘$143.29） |
| POET | $9.00（8/6收盘，Yahoo历史页，+5.50%） | ~$1.5B（Yahoo $1.51B；MarketWatch $1.47B） | N/A（亏损，TTM EPS -$0.84） | N/A | +202%（Q1 2026营收$50.3万，极小基数） | +16.3%（Saxo，截至8/4，滞后） | +36.3%（Saxo，截至8/4） | 8/7盘前$9.11（MarketWatch）；Q2财报预计8/11-8/12；纯期权型标的，收入可忽略 |
| CIEN | $403.76（8/6收盘，Ciena官方IR报价） | ~$58B（Robinhood $59.7B@$413.92） | 118.5（macrotrends 8/6；Yahoo 125.7） | 45.7（Yahoo；gurufocus 39.4@8/2） | +40%（FQ2 FY26 营收$1.57B） | +73.14%（MarketBeat） | +328.91%（MarketBeat；Yahoo +321.98%） | FQ2 EPS $1.64超预期$1.46，FY26指引上调至$6.3B；6/4财报超预期却跌14%（利好钝化=拥挤信号） |
| ALAB | $331.50（8/6收盘，macrotrends） | $54.6B（macrotrends 8/7；Robinhood $56.8B） | ~210（Yahoo 210.3@7/31；Robinhood 216.4） | ~105（Yahoo 105.3；gurufocus 102.9） | +104%（Q2 2026 营收$392.4M，8/4发布） | +110.03%（Yahoo，截至8/7） | +104.46%（Yahoo，截至8/7） | 8/7盘中~$338（indmoney）；Q3指引$540-560M远超预期；光引擎/定制芯片尚未出货 |
| CRDO | $236.37（8/6收盘，stockanalysis，+2.58%；Yahoo历史/macrotrends显示$230.43，口径冲突） | $41.9B（macrotrends 8/7） | 88.1（public.com 8/3） | N/A（无直接来源） | FY26 Q4营收$437M +157%（全年$1.3B +206%，财年4月止） | +65.94%（Yahoo，截至8/7） | +95.82%（investing.com；stockanalysis 52周+108.93%） | 52周区间$86.49-$308.67；AEC在scale-up互连份额领先 |
| MRVL | $210.54（8/6收盘，Yahoo/macrotrends） | $184.4B（MarketWatch/Google） | 72.7（stockanalysis；macrotrends 89.0、Google 72.1） | 46.4（stockanalysis） | +28%（FQ1 FY27 营收$2.42B创纪录，数据中心占76%） | +148.12%（Yahoo，截至8/6） | N/A（未检索到直接来源） | 6月纳入标普500；FY27全年指引+40%至~$11.5B；6/24见顶$316后回撤约33% |
| AVGO | $420.56（8/6收盘，macrotrends；8/7盘中$422.01-429.58，Robinhood报~$428.05） | ~$2.0T（MarketWatch；Yahoo $1.85T口径滞后） | 64.8（Yahoo） | 20.8（Yahoo） | +48%（FQ2 FY26 营收$22.2B；AI半导体$10.8B +143%） | +22.7%（FinanceCharts总回报；Slickcharts价格+21.5%） | +41.3%（FinanceCharts 12月总回报；investing.com价格+35.9%） | 下季指引~$29.4B（CNBC 6/3报道，待核实）；Tomahawk 6/CPO是1.6T核心卡位 |

## 二、Lumentum 8/11（周二）FQ4 FY2026 财报：市场预期

- 财报时间：2026-08-11（周二），盘后；为光模块板块本周最重要事件（COHR 8/12 周三盘后紧随其后）
- EPS 预期：~$2.97（MarketBeat 8/4，13位分析师）/ $2.99（Zacks共识，区间$2.94-3.07）；部分口径给出GAAP稀释$2.62（TrustWaves，称同比+718.8%）
- 营收预期：~$987.7M（MarketBeat）；公司指引$960M-$1,010M，中值$980M——指引发布时高于当时买方一致预期$936.6M（Sherwood 8/6）
- 上季基数（FQ3，5/6发布）：营收$808.4M +90% YoY，GAAP EPS $1.99（去年同期-$0.64）；FQ4指引GAAP毛利率41.5-43.5%（MarketBeat）
- 全年口径：Zacks共识FY26 EPS $8.21；FY27 EPS $16.67（预期增长159.7%，MarketBeat）——forward PE的分歧（47x vs >120x）主要来自采用FY26还是FY27 EPS
- 超预期信号：Zacks ESP +0.46%（Yahoo 7/21）——略偏正面；卖方关注点：EML激光器供需、1.6T订单能见度、CPO/外部光源（UHP激光器据MLQ.ai将在H2 CY2026放量拐点）

## 三、事件专节：7/28 康宁指引冲击与板块回调

**事件经过（已确认）**
1. 2026-07-28 盘前，康宁发布Q2财报：核心营收$4.74B +17%、核心EPS $0.78 +30%，业绩本身不差（GAAP营收$4.505B）；光通信业务营收$2.07B +32%、光通信净利$438M +77%（Investing.com 7/28）。
2. 但Q3指引偏弱：预计营收$4.9-5.0B，低于市场预期的~$5B；管理层表示AI光通信业务增速将放缓（Reuters 7/28）。股价盘前一度跌约17-20%（Yahoo Finance/TradingView报道盘前$143→约$118），当日蒸发市值$23.2B（Reuters标题"暴跌超20%"；CNBC口径"plunging 12%"，盘中修复后收跌幅度小于盘前）。
3. 传染效应（7/28当日，Quartz）：Ciena -5.9%、Coherent -5.7%、Lumentum -4.7%；Benzinga同期报道三只光通信股齐跌。背景是此前交易极度拥挤——康宁在7/28之前年内已涨约64%（Investing.com 7/28），COHR 7/2也出现过-9.57%的单日大跌（StockInvest/Trefis）。
4. 随后一周（7/29-8/6）板块V型修复：Truist于8/3升级评级并点名亚马逊合作（Yahoo 8/3）；GLW 8/3收$146.64、8/4单日+9.04%收$159.89（公司IR）、8/6收$157.18，已完全收复7/28跌幅；COHR 8/6收$355.83（+6.42%）、LITE 8/6收$838.06、AAOI财报后+13.4%。

**解读（供主报告参考）**
- 本次事件不是需求破坏，而是"增速二阶导"问题：康宁AI光业务环比增速放缓触发高估值板块的去拥挤；但一周内收复失地说明资金对AI光互连的中期逻辑并未动摇。
- 风险提示：该事件证明板块对任何"指引不及预期"高度敏感，LITE 8/11、COHR 8/12财报若指引低于买方预期，重演7/28式回调的概率不低；尤其LITE现价较52周高点已回撤约23%，拥挤度部分释放但TTM PE仍在125x以上。

## 四、1.6T 光模块 H2 2026 放量（必查项）

- MarketDesk（2026-02）：H2 2026是1.6T真正的放量拐点——GB300服务器全面切换1.6T，超大规模云厂商认证已完成；800G→1.6T切换是H2主线。
- IDTechEx（2026）：2026被定义为"1.6T之年"（Year of 1.6T）。
- TheValueist：1.6T爬坡发生在H2 CY2026与CY2027，线性直驱（LPO/LRO）方案约占25%份额。
- MapYourTech（2026初）：1.6T已进入量产爬坡阶段。
- SemiAnalysis：CPO交换机H2 2026上市，单口1.6T（144×800G）——CPO时间表曾是6/29光互连板块另一次回调的诱因（Barron's 7/3）。
- 行业量化（LinkedIn行业报告引用）：光收发器市场2025约$8.42B→2026预测$9.15B；800G及以上2026出货约6,300万只。（注：该口径偏窄，仅供量级参考）
- 结论：多源一致确认1.6T在H2 2026进入放量期，800G→1.6T切换是板块H2最确定的催化剂；scale-up互连（ALAB/CRDO的AEC、MRVL/AVGO的scale-up fabric、CIEN的scale-across）是第二增长曲线。

## 五、每股简评（约80字）

- **COHR（$355.83，YTD +103%）**：800G/1.6T收发器+激光器双轮驱动，FQ3营收+21%且Q4指引$1.91-2.05B，8/12财报是下一个方向性事件；TTM PE 135x、7月两次单日近10%波动，弹性与风险同高。
- **LITE（$838.06，YTD +141%）**：EML激光器卡位全部800G/1.6T模块，FQ3营收+90%，8/11财报指引$960M-1.01B已高于当时共识；一年涨约6.7倍后较峰值回撤23%，财报前博弈激烈，波动率极高。
- **FN（$543.95，YTD +23%）**：光模块代工龙头，FQ3营收+39%，深度绑定英伟达系1.6T放量，是板块中业绩确定性最强、估值最温和（fwd PE ~30x）的"卖铲人"，但8/7盘中一度跌超6%显示获利盘压力。
- **AAOI（$140.90，YTD +297%）**：Q2营收+86%创纪录、800G收入环比翻倍、全年目标>$1B，财报后单日+13%；但GAAP仍亏损、持续稀释、beta 3.8，是高贝塔期权而非基本面锚。
- **GLW（$157.18，YTD +80%）**：7/28指引冲击的震源，光业务Q2仍+32%且与亚马逊绑定，一周收复失地证明需求未破坏；fwd PE 43x，指引波动是最大变量，板块风向标。
- **POET（$9.00，市值$1.5B）**：光互插器概念+设计推进叙事驱动，Q1营收仅$50万、持续亏损稀释，8/11前后财报无实质业绩支撑，纯情绪标的，波动极端（6月曾近腰斩又反弹）。
- **CIEN（$403.76，YTD +73%）**：FQ2营收+40%、FY26指引上调至$6.3B，DCI+scale-across受益者；但6/4超预期却跌14%说明预期打满，TTM PE 118-126x，财报后"利好钝化"风险是板块缩影。
- **ALAB（$331.50，YTD +110%）**：Q2营收+104%、Q3指引$540-560M大超预期，PCIe retimer+AEC卡位scale-up；trailing PE 210x/fwd ~105x，光引擎与定制芯片尚未贡献收入，估值透支了两年增长。
- **CRDO（$236.37，YTD +66%）**：FY26营收+206%、AEC在scale-up互连领先，是ALAB最直接对手；PE 88x在互连股中反而最低，风险在于客户集中与巨头自研挤压，8/6两口径收盘价冲突需复核。
- **MRVL（$210.54，YTD +148%）**：定制AI加速器+DCI光互连双引擎，FY27指引+40%至$11.5B，6月入标普；但较6月峰值$316回撤33%，定制ASIC毛利率与竞争是核心争议，fwd PE 46x。
- **AVGO（$428盘中，YTD +23%）**：AI半导体季度$10.8B +143%，Tomahawk 6/102.4T与CPO直接定义1.6T生态，fwd PE ~21x是11只中最便宜；市值~$2T后弹性下降，是板块的"指数锚"而非弹性来源。

## 六、板块级风险汇总

1. **估值拥挤度（最大风险）**：11只中多数TTM PE>70x（LITE 126x、ALAB ~210x、CIEN 118-126x、COHR 135x、CRDO 88x、MRVL 73-89x、GLW 72x），AAOI/POET亏损；7/28康宁事件与6/29 CPO时间表回调证明任何增速放缓信号都会触发剧烈去拥挤。
2. **康宁指引的板块含义**：AI光业务增速二阶导放缓已被定价一次；若LITE 8/11或COHR 8/12的指引下台阶，可能引发第二波。
3. **技术路线风险**：CPO若提前放量，可插拔模块厂（COHR/AAOI/FN下游）面临路线切换；LPO/LRO侵蚀DSP（MRVL）与retimer价值量。
4. **个股风险**：AAOI/POET亏损+稀释+高beta；MRVL较峰值-33%的动量损伤；FN 8/7盘中急跌显示拥挤获利盘；CRDO数据源冲突提示小盘数据质量风险。

## 七、JSON（机读）

```json
[
  {
    "ticker": "COHR",
    "price": 355.83,
    "mcap_b": 69.6,
    "ttm_pe": 135.5,
    "fwd_pe": 43.4,
    "rev_growth_yoy": 21,
    "ytd_pct": 103.49,
    "one_year_pct": 188.37,
    "notes": "8/6收盘;8/7收盘N/A;FQ3营收+21%至$1.81B;8/12盘后财报,指引$1.91-2.05B;1.6T收发器放量;7/28康宁事件当日-5.7%;TTM PE口径冲突(135-178)"
  },
  {
    "ticker": "LITE",
    "price": 838.06,
    "mcap_b": 65,
    "ttm_pe": 125.7,
    "fwd_pe": 47.3,
    "rev_growth_yoy": 90,
    "ytd_pct": 141.22,
    "one_year_pct": 666.09,
    "notes": "8/6收盘;8/11盘后财报,EPS预期$2.97-2.99,营收预期$987.7M,公司指引$960M-1.01B高于当时共识$936.6M;EML卡位1.6T;较峰值回撤23%;fwd PE口径FY27=47x,FY26>120x"
  },
  {
    "ticker": "FN",
    "price": 543.95,
    "mcap_b": 19.5,
    "ttm_pe": 45.4,
    "fwd_pe": 30.5,
    "rev_growth_yoy": 39.3,
    "ytd_pct": 22.59,
    "one_year_pct": 58.13,
    "notes": "8/6收盘;8/7盘中$502-547.57收盘N/A;FQ3营收$1,214.3M +39.3%;FQ4财报8/17;英伟达系1.6T代工;板块最低估值"
  },
  {
    "ticker": "AAOI",
    "price": 140.9,
    "mcap_b": 10,
    "ttm_pe": null,
    "fwd_pe": null,
    "rev_growth_yoy": 86,
    "ytd_pct": 297.1,
    "one_year_pct": 434.74,
    "notes": "8/6收盘,财报后+13.4%;Q2营收$191.9M创纪录,800G收入$12.8M环比翻倍;GAAP净亏-$22.78M,TTM EPS -$0.65;全年目标>$1B;beta 3.79,稀释风险"
  },
  {
    "ticker": "GLW",
    "price": 157.18,
    "mcap_b": 135.4,
    "ttm_pe": 72.4,
    "fwd_pe": 42.8,
    "rev_growth_yoy": 17,
    "ytd_pct": 80.12,
    "one_year_pct": 145.67,
    "notes": "8/6收盘;7/28 Q3指引$4.9-5.0B低于预期~$5B引发-17~20%盘中暴跌并拖累COHR/LITE/CIEN,一周收复失地;Q2核心营收+17%,光通信+32%;板块风向标"
  },
  {
    "ticker": "POET",
    "price": 9,
    "mcap_b": 1.5,
    "ttm_pe": null,
    "fwd_pe": null,
    "rev_growth_yoy": 202,
    "ytd_pct": 16.27,
    "one_year_pct": 36.3,
    "notes": "8/6收盘;8/7盘前$9.11;Q1营收仅$50.3万(小基数+202%),TTM EPS -$0.84;Q2财报约8/11-8/12;YTD/1年为Saxo 8/4滞后口径;纯概念高波动"
  },
  {
    "ticker": "CIEN",
    "price": 403.76,
    "mcap_b": 58.1,
    "ttm_pe": 125.7,
    "fwd_pe": 45.7,
    "rev_growth_yoy": 40,
    "ytd_pct": 73.14,
    "one_year_pct": 328.91,
    "notes": "8/6收盘(公司IR);FQ2营收$1.57B +40%,EPS $1.64超预期,FY26指引上调至$6.3B;6/4超预期却跌14%=拥挤信号;DCI+scale-across"
  },
  {
    "ticker": "ALAB",
    "price": 331.5,
    "mcap_b": 54.6,
    "ttm_pe": 210.3,
    "fwd_pe": 105.3,
    "rev_growth_yoy": 104,
    "ytd_pct": 110.03,
    "one_year_pct": 104.46,
    "notes": "8/6收盘;8/7盘中~$338;Q2营收$392.4M +104%,Q3指引$540-560M大超预期;PCIe retimer+AEC卡位scale-up;光引擎/定制芯片未出货;估值透支"
  },
  {
    "ticker": "CRDO",
    "price": 236.37,
    "mcap_b": 41.9,
    "ttm_pe": 88.1,
    "fwd_pe": null,
    "rev_growth_yoy": 157,
    "ytd_pct": 65.94,
    "one_year_pct": 95.82,
    "notes": "8/6收盘口径冲突:stockanalysis $236.37(+2.58%) vs Yahoo/macrotrends $230.43,需复核;FY26(4月止)营收$1.3B +206%,Q4 $437M +157%;AEC scale-up领先;fwd PE无直接来源"
  },
  {
    "ticker": "MRVL",
    "price": 210.54,
    "mcap_b": 184.4,
    "ttm_pe": 72.7,
    "fwd_pe": 46.4,
    "rev_growth_yoy": 28,
    "ytd_pct": 148.12,
    "one_year_pct": null,
    "notes": "8/6收盘(YTD截至8/6);8/7盘前$216.19;FQ1 FY27营收$2.42B创纪录+28%,数据中心占76%;FY27指引+40%至~$11.5B;6月入标普;较6/24峰值$316回撤33%;1年涨幅N/A"
  },
  {
    "ticker": "AVGO",
    "price": 420.56,
    "mcap_b": 2000,
    "ttm_pe": 64.8,
    "fwd_pe": 20.8,
    "rev_growth_yoy": 48,
    "ytd_pct": 22.7,
    "one_year_pct": 41.3,
    "notes": "8/6收盘,8/7盘中$422.01-429.58(Robinhood报$428.05);市值~$2.0T(Yahoo $1.85T滞后);FQ2 FY26营收$22.2B +48%,AI半导体$10.8B +143%;CNBC报下季指引~$29.4B待核实;Tomahawk6/CPO定义1.6T"
  }
]
```

---
*采集人：Agent-C（光通信与互连）；本文件仅供研究，非投资建议。未检索到的字段一律标注 N/A/null，未做任何外推。*