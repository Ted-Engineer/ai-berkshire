# B组 半导体设备/材料/测试数据包 — 美股H2 2026科技扫描

- 采集Agent: Agent-B（半导体设备/材料/测试）
- 采集时间: 2026-08-08（周六，北京时间）；行情基准日: 2026-08-07（周五）美股收盘
- 数据源: stockanalysis.com / Yahoo Finance / macrotrends / gurufocus / MarketBeat / investing.com / 公司IR / CNBC / Reuters / Barron's / Fortune（下文逐项标注）
- 性质: 仅供学习研究，非投资建议。不同来源口径（GAAP vs non-GAAP、爬取日期）存在差异，均已注明。

## 一、核心数据总表（2026-08-07 收盘）

| # | 代码 | 公司 | 8/7收盘($) | 市值 | TTM PE | Forward PE | 最近季营收YoY | YTD | 1年涨幅 | 存储/HBM关联度(1-5) |
|---|------|------|-----------|------|--------|------------|---------------|------|---------|---------------------|
| 1 | LRCX | Lam Research | 305.77 | $382.6B | ~53.5 | 33.2 | +30%（FQ4'26, 6月季） | +78.6% | +200.5% | 5 |
| 2 | AMAT | Applied Materials | 527.48 | $418.8B | ~49.5 | 34.5 | +11%（FQ2'26, 4月季） | +101.5% | +190.0% | 4 |
| 3 | KLAC | KLA | 193.22 | ~$252B | ~52.7 | 35.9 | +15%（FQ4 FY26, 6月季） | +59.0% | +111.2% | 3 |
| 4 | ONTO | Onto Innovation | 276.00 | $13.7B | ~131 | 35.9 | +35.3%（Q2'26, 6月季） | +74.8% | +213.6% | 4 |
| 5 | CAMT | Camtek | 149.67 | ~$7.0B | ~158(GAAP) | 36.1 | +2.5%（Q1'26, 3月季） | +40.7% | +61% | 4 |
| 6 | FORM | FormFactor | 115.21 | ~$9.0B | ~79 | 33-39 | +31.9%（Q2'26, 6月季） | +106.5% | +292.7% | 5 |
| 7 | TER | Teradyne | 384.89 | $60.2B | ~52.8 | 40.4 | +104%（Q2'26, 6月季） | +98.8% | +267.4% | 4 |
| 8 | ENTG | Entegris | 145.55 | $22.2B | ~72.6 | 32.5 | +11.5%（Q2'26, 6月季） | +72.8% | +101.3% | 3 |
| 9 | MKSI | MKS Instruments | 291.31 | $19.7B | ~46.3 | ~24 | +28.3%（Q2'26, 6月季） | ≈+64%(估算) | +245.8% | 3 |
| 10 | AEIS | Advanced Energy | 341.39 | ~$13.5B | ~60.2 | 33.8 | +30.0%（Q2'26, 6月季，创纪录） | +63.2% | ≈+119%(估算) | 4 |
| 11 | ICHR | Ichor Holdings | 65.33 | $2.45B | N/A(GAAP TTM亏损) | 55.3 | +24%（Q2'26, 6月季） | +254.5% | +311.6% | 3 |
| 12 | ACLS | Axcelis | ≈138.2 | ~$4.3B | ~42 | 35.7 | +10.6%（Q2'26, 6月季） | +72.0% | +72.0% | 3 |
| 13 | VECO | Veeco | ≈51.6 | ~$3.0B | ~136 | 32.5 | +16.5%（Q2'26, 6月季） | +80.6% | +167.9%(市值口径) | 3 |

### 字段口径与来源备注
- 价格: MarketBeat/macrotrends/investing.com/公司IR 交叉核对（8/7收盘或最近收盘）。KLAC 为10:1拆股调整价（2026-06-12生效，Yahoo Finance 2026-06-12）。
- 市值: Yahoo Finance（8/7盘中快照）/ stockanalysis.com；KLAC、AEIS、VECO 为按收盘价×股本估算，已注明。
- TTM PE: 以 Yahoo Finance GAAP TTM 为主；ONTO/CAMT/VECO 的GAAP TTM EPS 受一次性项目压低，与 macrotrends 等口径差异大（已标注）。ICHR GAAP TTM 亏损，PE=N/A。
- Forward PE: stockanalysis.com / gurufocus / Yahoo Finance（8月初快照）。
- 营收YoY: 各公司最近一次财报（日期见下文每股点评）；AMAT 下次财报 2026-08-13（FQ3）。
- YTD: 基于2025-12-31收盘计算（LRCX $171.18、AMAT $261.83、ONTO $157.86、ENTG $84.25、TER $193.56、AEIS $209.24，Yahoo/macrotrends历史数据）；KLAC/ICHR/FORM/VECO/ACLS 引 MarketBeat（拆股调整）；MKSI 按1月初≈$177估算。
- 1年涨幅: investing.com / stockanalysis.com / stocktitan（8月初快照，爬取日期不同有±5pct差异）。

## 二、专节：The Information 报道事件（2026-07-27）

**事件内容（已核实）**：2026-07-27（周一），The Information 发布独家报道：一家中国国有背景（上海）公司已开始制造/初步量产国产沉浸式DUV光刻机（对标ASML核心产品），并计划今年生产约5台、2027年约20台（CNBC 2026-07-28 "China's reported chip breakthrough comes with big caveats"；The Information 简报 2026-07-27 "ASML Shares Slide After Information Report on China Producing DUV Tool"）。

**当日市场反应（2026-07-27）**：
- ASML：-5.8%，收 $1,654.62，为6月以来最低（Barron's；Investors.com 收 $1,655.26）。
- AMAT：收跌约4%（盘中一度跌超6.5%），收 $516.89（AMAT IR历史股价；Techmeme/investing.com）。
- LRCX：-4.5%（investing.com）；KLAC 同步下挫；AMAT/LRCX/KLAC 盘中跌幅5-7%（aiweekly 7/27）。

**后续发酵**：
- 7/28-29 抛售扩大：AMAT 7/28 -7.8%（$476.46）、7/29 -8.4%（$436.45），7/30 大幅反弹+15%至 $501.77（AMAT IR；heygotrade）。CNBC 7/29：20只最大芯片股自7/24收盘以来蒸发约$1.3万亿市值。
- 反驳/降温：Reuters Breakingviews 7/28 "ASML's China chip threat looks overdone"；CNBC 7/28 指出报道存在"big caveats"（年产5-20台远低于ASML年出货约百台以上DUV）；J.P. Morgan 称抛售"过头"（Barron's）。
- 大背景：SOX（费城半导体指数）2026年7月累跌21%，为2008年10月以来最差单月（Fortune 8/2）；Morningstar 7/30：全球半导体指数H1 2026涨60%后自6月峰值回撤约17%。

**对本组含义**：报道直接打击光刻机（ASML），对刻蚀/沉积/量测（AMAT/LRCX/KLAC）为间接情绪与估值冲击，而非订单基本面变化；7月底的财报季（LRCX/TER/KLAC/AEIS 等均超预期）后设备股已显著反弹。中国DUV国产化若真实推进，中期反而可能加速中国存储/逻辑扩产，但出口管制与竞争格局仍是估值压制因素。


## 三、每股简评（约80字：H2催化剂 + 最大风险）

**LRCX（Lam Research，$305.77，评分5）**：NAND刻蚀/沉积龙头，存储资本开支最纯受益者。FQ4'26营收$6.72B创纪录（+30% YoY），beat-and-raise；CSBG服务业务$7.2B创新高（7/29财报）。H2催化：NAND conversion、HBM4扩产、中国存储厂复产。风险：中国收入占比高、出口管制，7月自高点回撤近30%（52周高$438.50），估值仍处历史高位。

**AMAT（Applied Materials，$527.48，评分4）**：平台型设备龙头，HBM混合键合/先进封装（Wafer-on-Wafer）领先。公司指引CY2026半导体设备业务增长超30%。H2催化：8/13 FQ3财报、台积电资本开支$52-56B（+30%）传导、HBM4。风险：中国收入敞口大，7/27-29三日累跌约20%显示情绪脆弱，估值对利空敏感。

**KLAC（KLA，$193.22，评分3）**：量测/检测垄断者（7/28完成10:1拆股后交易）。FY26营收$13.58B（+11.7%），FQ4 +15%，9月季指引$4.0B，上调CY2026 WFE展望至low-$150B。H2催化：先进制程良率管控需求、HBM堆叠检测。风险：三巨头中估值最贵（TTM ~53x），中国敞口，7月回撤深（52周高$307.37）。

**ONTO（Onto Innovation，$276.00，评分4）**：HBM量测/检测核心标的。Q2'26营收$343.1M创纪录（+35.3%），全年指引+30%以上至超$13亿；Dragonfly VPA获头部HBM厂超$240M订单（2/18）。8/6盘后一度+11%。H2催化：HBM4爬坡、先进封装量测。风险：GAAP TTM EPS被一次性项目压低致PE虚高，8/7冲高回落显示获利盘重，大客户集中。

**CAMT（Camtek，$149.67，评分4）**：HBM/先进封装检测弹性股。Q1'26营收$121.7M（+2.5%，基数效应），公司指引2H26营收环比1H26增25%以上（5/12）。H2催化：8/10 Q2财报、Eagle/APG设备放量、HBM4检测。风险：GAAP TTM PE ~158x极贵（EPS受一次性税务项目压低），8/10财报不及预期即杀估值，小市值高波动。

**FORM（FormFactor，$115.21，评分5）**：HBM探针卡最纯标的。Q2'26营收$258.2M创纪录（+31.9%），连续两季+30%以上，DRAM/HBM探针卡驱动（7/29）。H2催化：HBM4探针卡认证放量、存储厂DRAM扩产。风险：一年+293%后估值依赖HBM4转换节奏，客户集中于SK海力士系，7月曾单日大幅波动，认证延迟即重创。

**TER（Teradyne，$384.89，评分4）**：半导体测试双寡头之一。Q2'26营收$1.33B（+104%），其中半导体测试+128%，AI相关占比超60%，并上调下半年指引（7/28）。H2催化：HBM/AI芯片测试需求、SOC测试新品周期。风险：4/28曾因指引不及预期单日-19%，测试资本开支波动大，TTM PE ~53x已充分定价AI景气。

**ENTG（Entegris，$145.55，评分3）**：半导体材料/耗材平台。Q2'26营收$883.2M（+11.5%）超预期，上调全年行业增速展望至7-8%，先进逻辑与存储材料需求同步修复（8/4）。H2催化：HBM层数增加带来的前驱体/过滤材料用量提升。风险：增速低于设备同业，6/22历史高点$183.84回撤约21%，材料业务与稼动率挂钩、周期滞后。

**MKSI（MKS Instruments，$291.31，评分3）**：真空/RF电源/光子平台。Q2'26营收$1.248B（+28%），半导体业务指引环比高个位数、同比+25%以上，数据中心/光互联（CPO）成新引擎（8/5）。H2催化：存储扩产带动真空与RF电源需求、硅光子订单。风险：财报后8/7回落约3%显示预期已高，Atotech并购遗留整合与杠杆问题，业务多元摊薄存储纯度。

**AEIS（Advanced Energy，$341.39，评分4）**：等离子电源/功率转换。Q2'26营收$574.1M创纪录（+30%），半导体收入+33%，年内第二次上调全年指引；数据中心电源爆发（8/3）。H2催化：NAND conversion刻蚀功率电源、e-datacenter（HVDC/AI电源）。风险：5/1曾创新高$388.93后7月一度跌至$252，波动极大；存储资本开支节奏变化直接冲击订单。

**ICHR（Ichor Holdings，$65.33，评分3）**：流体输送子系统（刻蚀/沉积设备核心部件）。Q2'26营收$294.8M（+24%），扭亏为盈（调整EPS $0.34），但营收低于一致预期$300.2M、利润率恢复偏慢，财报后大跌（8/3）。H2催化：LRCX/AMAT设备出货放量带动部件需求、NAND扩产。风险：利润率兑现是生死线，客户集中，YTD +254%后估值容错低。

**ACLS（Axcelis，≈$138.2，评分3）**：离子注入设备。Q2'26营收$215.2M（+10.6%），超预期（营收+4.9%、EPS+17.8% beat），功率半导体回暖+存储/先进逻辑注入需求改善（8/6）。H2催化：HBM/DRAM相关注入订单、功率半导体复苏。风险：中国收入占比高且政策敏感，Q2利润率环比收缩，52周高$193.78回撤约29%。

**VECO（Veeco，≈$51.6，评分3）**：激光退火/先进封装设备。Q2'26营收$193.5M（+16.5%，超指引），全年指引上调至$780-810M，先进封装与硅光子产能2027年目标翻倍，部分产品2026收入翻倍（8/5）。H2催化：硅光子/先进封装（与HBM相关）、激光退火。风险：GAAP盈利薄（TTM PE ~136x），订单块状波动，硅光子商业化节奏不确定。

## 四、机读数据（JSON）

```json
[
  {"ticker":"LRCX","price":305.77,"mcap_b":382.6,"ttm_pe":53.5,"fwd_pe":33.2,"rev_growth_yoy":30,"ytd_pct":78.6,"one_year_pct":200.5,"memory_exposure_score":5,"notes":"NAND刻蚀/沉积龙头；FQ4'26 +30%创纪录并上调；H2看NAND conversion/HBM4；风险=中国敞口+高估值（52周高$438.50回撤约30%）"},
  {"ticker":"AMAT","price":527.48,"mcap_b":418.8,"ttm_pe":49.5,"fwd_pe":34.5,"rev_growth_yoy":11,"ytd_pct":101.5,"one_year_pct":190.0,"memory_exposure_score":4,"notes":"平台型设备；CY2026设备业务指引+30%以上；8/13财报；风险=中国敞口+7/27-29三日累跌20%的情绪脆弱性"},
  {"ticker":"KLAC","price":193.22,"mcap_b":252.4,"ttm_pe":52.7,"fwd_pe":35.9,"rev_growth_yoy":15,"ytd_pct":59.0,"one_year_pct":111.2,"memory_exposure_score":3,"notes":"量测垄断；6/12完成10:1拆股；FY26 +11.7%、9月季指引$4.0B、WFE展望上调；风险=估值最贵+中国敞口"},
  {"ticker":"ONTO","price":276.00,"mcap_b":13.7,"ttm_pe":131.4,"fwd_pe":35.9,"rev_growth_yoy":35.3,"ytd_pct":74.8,"one_year_pct":213.6,"memory_exposure_score":4,"notes":"HBM量测核心；Q2创纪录+35%、指引+30%以上；Dragonfly VPA获头部HBM厂$240M+订单；风险=TTM PE虚高+大客户集中"},
  {"ticker":"CAMT","price":149.67,"mcap_b":7.0,"ttm_pe":157.6,"fwd_pe":36.1,"rev_growth_yoy":2.5,"ytd_pct":40.7,"one_year_pct":61.0,"memory_exposure_score":4,"notes":"HBM/先进封装检测；指引2H26环比+25%以上；8/10财报；风险=GAAP TTM PE极高+小市值高波动"},
  {"ticker":"FORM","price":115.21,"mcap_b":9.0,"ttm_pe":79.0,"fwd_pe":36.0,"rev_growth_yoy":31.9,"ytd_pct":106.5,"one_year_pct":292.7,"memory_exposure_score":5,"notes":"HBM探针卡最纯标的；连续两季营收+30%以上创纪录；风险=HBM4认证节奏+客户集中+一年近3倍后波动大"},
  {"ticker":"TER","price":384.89,"mcap_b":60.17,"ttm_pe":52.8,"fwd_pe":40.4,"rev_growth_yoy":104,"ytd_pct":98.8,"one_year_pct":267.4,"memory_exposure_score":4,"notes":"测试双寡头；Q2 +104%（半导体测试+128%）、AI占比超60%、上调H2指引；风险=测试capex波动（4/28曾单日-19%）"},
  {"ticker":"ENTG","price":145.55,"mcap_b":22.2,"ttm_pe":72.6,"fwd_pe":32.5,"rev_growth_yoy":11.5,"ytd_pct":72.8,"one_year_pct":101.3,"memory_exposure_score":3,"notes":"材料/耗材平台；Q2超预期并上调行业增速展望至7-8%；风险=增速低于设备同业+距6/22高点$183.84回撤约21%"},
  {"ticker":"MKSI","price":291.31,"mcap_b":19.7,"ttm_pe":46.3,"fwd_pe":24.9,"rev_growth_yoy":28.3,"ytd_pct":64.0,"one_year_pct":245.8,"memory_exposure_score":3,"notes":"真空/RF/光子；Q2 +28%、半导体业务指引同比+25%以上、CPO新引擎；风险=财报后回落+Atotech整合与杠杆"},
  {"ticker":"AEIS","price":341.39,"mcap_b":13.5,"ttm_pe":60.2,"fwd_pe":33.8,"rev_growth_yoy":30.0,"ytd_pct":63.2,"one_year_pct":119.0,"memory_exposure_score":4,"notes":"等离子电源+数据中心电源；Q2创纪录+30%、年内第二次上调指引；风险=波动极大（$388.93→$252→$341）"},
  {"ticker":"ICHR","price":65.33,"mcap_b":2.45,"ttm_pe":null,"fwd_pe":55.3,"rev_growth_yoy":24,"ytd_pct":254.5,"one_year_pct":311.6,"memory_exposure_score":3,"notes":"流体子系统；Q2 +24%扭亏但营收miss一致预期、利润率恢复慢致财报后大跌；风险=利润率兑现+客户集中"},
  {"ticker":"ACLS","price":138.2,"mcap_b":4.3,"ttm_pe":41.9,"fwd_pe":35.7,"rev_growth_yoy":10.6,"ytd_pct":72.0,"one_year_pct":72.0,"memory_exposure_score":3,"notes":"离子注入；Q2超预期（营收+4.9%/EPS+17.8% beat）；风险=中国敞口+利润率收缩+距52周高$193.78回撤约29%"},
  {"ticker":"VECO","price":51.61,"mcap_b":3.0,"ttm_pe":135.8,"fwd_pe":32.5,"rev_growth_yoy":16.5,"ytd_pct":80.6,"one_year_pct":167.9,"memory_exposure_score":3,"notes":"激光退火/先进封装/硅光子；Q2超预期、全年指引上调至$780-810M；风险=GAAP盈利薄+订单块状波动"}
]
```

注：ICHR ttm_pe 为 null（GAAP TTM 亏损）；ACLS 价格为基于 Yahoo YTD(+72.03%, as of 8/7) 的估算值；AEIS/VECO 市值为收盘价×股本估算；MKSI YTD 为基于1月初约$177的估算值。所有数据点均来自公开网络来源（见正文标注），采集于 2026-08-08。
