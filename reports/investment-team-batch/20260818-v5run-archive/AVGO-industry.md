# AVGO（博通）行业深度重研——定制ASIC份额战争与AI资本开支的传导风险

**角色**：行业研究员（芒格视角） | **组合背景**：55股、7.1%仓位、止损$346、FQ3财报9/2盘后（AI≥$16B→加仓区解禁；Q4指引<$18B→减半）
**数据截止**：2026-08-18 12:30 UTC（美股盘前，AVGO盘前$386.50，8/17收盘$392.43，市值$1.87T）
**研究方法**：gnews通道17次独立搜索+Tom's Hardware等6篇全文抓取+Yahoo/stockanalysis行情（Brave与内置搜索429至8-22，全程未使用训练知识冒充数据）

---

## 0. 核心结论（芒格式一句话）

> 博通正从"Google TPU独家实现者"演变为"前沿算力的银行+代工实现层"——它把最大的客户风险（Google多元化）换成了最大的金融风险（为OpenAI级客户融资建产能）。生意本质极好（60%+ ASIC设计份额、订单看到2028、FY27 AI收入>$100B），但生态位正在被四家竞争者从Google侧蚕食，且需求端第一次出现了"债务依赖"的结构性裂缝。**这不是卖出生意的时刻，但也不是可以闭眼加仓的时刻——9/2财报必须同时回答"AI加速"与"谁在付钱"两个问题。**

---

## 1. 定制ASIC vs GPU的份额战争（核心战场）

### 1.1 总量与渗透率：方向确凿，具体数字部分存疑

| 指标 | 数值 | 来源 | 可信度 |
|---|---|---|---|
| 2026全球AI服务器出货增速 | >28% YoY，ASIC服务器占比上升 | TrendForce 2026-01-20新闻稿标题（TechPowerUp/TrendForce双源转载） | 高（方向） |
| "ASIC服务器占比27.8%" | **未能独立验证**——TrendForce原文正文无法直接抓取（站点仅保留近5条新闻稿），27.8%具体口径无法双源确认 | 数据缺口 | 低 |
| AI服务器计算ASIC出货量2027 | 较2024/25**增长约2倍（triple）** | Counterpoint Research 2026-01-25 | 高 |
| 博通ASIC代工设计份额（2027） | "AI服务器计算ASIC伙伴领导地位延续至2027"（标题级）；**具体60%/Marvell 25%的拆分数字无法从Counterpoint原文直接验证（官网404），60/25口径仅见转述** | Counterpoint 2026-01-27（Seeking Alpha转载标题） | 中 |
| ASIC需求 vs GPU需求 | 高盛：**2027年ASIC需求将与GPU相当** | Motley Fool转述高盛，2026-05-25 | 中高 |
| 定制芯片增速 vs Nvidia | 2026年ASIC出货增速约为GPU增速的3倍 | Tech Times转述，2026-05-26 | 中 |

### 1.2 单量对比（Fubon Research，2026-07-30，经Tom's Hardware全文核实）

- Google计划**2028年部署12–15M颗TPU v9**（四计算die设计，产能消耗较2027年翻倍以上）；Fubon认为"仅靠台积电无法达成，Intel Foundry产能是必须"
- Nvidia数据中心AI GPU出货：**2026年约820万颗 → 2028年约1,240万颗**
- **推论：若Fubon兑现，2028年单一客户Google的ASIC出货量将追平或超过Nvidia全市场GPU出货**——这是"GPU vs ASIC终局"最硬的一个量化锚点

### 1.3 各路线量产状态（2026-08核实）

| 路线 | 状态 | 关键事实 |
|---|---|---|
| Google TPU v7 Ironwood | 量产部署中 | 第七代，训练/推理同构 |
| Google TPU v8（8t/8i） | 2026-04-22 Cloud Next发布，年内交付 | 首次拆分训练（8t，9,600颗/superpod，3D Torus）与推理（8i，Boardfly拓扑，288GB HBM3e）双芯片；台积电N3+HBM3e |
| OpenAI Jalapeño | 工程样片已在目标频率/功耗下运行实验室负载（GPT-5.3-Codex-Spark），9个月开发周期 | 2026-06-24官宣；单一巨型计算die+6颗HBM+I/O die的reticle级推理ASIC |
| Meta MTIA | 通过2029多年期协议锁定；新"Iris"芯片通过测试（2026-07-17）；四款新MTIA以六个月节奏发布 | 首期>1GW，多代际数十万颗量级 |
| Amazon Trainium | Project Rainier（印第安纳Trainium 2超集群）运行中，仍是Anthropic主训练伙伴 | Anthropic同时向AMD采购2GW MI450 |
| Microsoft Maia | 存在于路线图但声量小；Microsoft将"大规模"部署AMD Helios机架 | 数据缺口：Maia代际细节本轮未获可靠来源 |
| Google "Frozen v2" | 传闻中：把Gemini架构刻进硅片，目标6-10倍tokens/watt | 传闻级，未证实 |

### 1.4 芒格视角判读

定制ASIC的经济学（单位推理成本、功耗、与自身workload的贴合）已在推理侧跑赢通用GPU（TrendForce 2026-03-20："CSP在2H26加速ASIC推进，MediaTek/GUC/Alchip受益"）。但注意不对称性：**ASIC赢的是"已知workload的规模化推理"，GPU仍守住"前沿训练+生态长尾"**。Google自己在Cloud Next上同场发布Vera Rubin NVL72实例，说明连最激进的ASIC拥趸也在对冲。博通横跨两边（ASIC实现层+以太网网络），这是它比纯GPU或纯ASIC公司更稳的生态位——前提是客户不让它失去实现层独占。

---

## 2. Google TPU生态的供应商格局演变（最大单点风险）

### 2.1 时间线（全部经Tom's Hardware等核实）

| 时间 | 事件 | 对博通份额的含义 |
|---|---|---|
| 2015–2025 | 博通独占TPU硅实现（TPU v1–v7） | 100% |
| 2025-12 | **MediaTek加入v8代设计伙伴**，结束博通十年独占 | v8：训练博通/推理MediaTek参与的拆分格局（8i引入MediaTek） |
| 2026-04-19 | The Next Web：Google与**Marvell**洽谈新AI推理芯片（与博通TPU计划并行） | 推理侧第二稀释 |
| 2026-04-20 | The Next Web：**"四伙伴供应链"成型——博通、MediaTek、Marvell（+Intel代工/封装）**，在推理侧挑战Nvidia | 议价权结构性下降 |
| 2026-06-22 | eciks：Google升级版**Triggerfish（v8i迭代）交MediaTek**，3倍内存提升 | 推理代际流失的实证 |
| 2026-06-24 | 财报电话会：Hock Tan公开承认Google"**looking elsewhere**" | 管理层亲口确认 |
| 2026-07-30 | Fubon：v9（2028，12–15M颗）需Intel Foundry产能；Intel已获**2028年>300万颗TPU封装订单** | 制造端多元化 |
| 2026-08-16 | SemiAnalysis（经Tom's Hardware）：Google联手**AMD**开发v10代TPU之一（CPU IP/SoIC封装，面向RL/agentic负载） | 第五个伙伴，训练/推理边界再模糊 |

### 2.2 对冲力量（不要只看坏消息）

- 同一份4/7证券文件：博通承诺**设计并供应Google未来代际TPU直至2031年**，并对Google下一代AI机架供应网络等部件（supply assurance agreement）——即博通在"芯片实现"外的**网络/机架层锁定了2031**
- 6/3电话会：订单backlog延伸至**2028年**，"XPU与网络需求insatiable"
- Mizuho（Vijay Rakesh，4月）：仅Anthropic安排一项，估算博通2026年AI收入$21B、**2027年$42B**

### 2.3 判读

Google生态是"一客多供"的经典采购策略：训练大die的先进制程实现（博通最强）短期无人替代，但**推理ASIC（量更大、技术门槛更低）正在系统性流向MediaTek/Marvell**。v8代博通仍握训练+共同设计；v9博通份额视Intel Foundry分流程度；v10引入AMD后，博通在Google内部的份额轨迹大概是"训练高、推理降、总体缓降但绝对量随蛋糕翻倍而上升"。芒格会问：十年后Google还需要外部实现伙伴吗？——只要TPU年出货到千万颗级，Google没有动机把6,000mm²级3.5D封装的设计运营全部内化（博通2026年发布的XDSiP平台正是这个门槛的护城河），但**单价与利润率会被多供竞争压缩**。

---

## 3. 新客户管线：XPU管线的真实增量

### 3.1 六大客户承载$100B（FY27）

Hock Tan 3/4电话会：AI芯片收入2027年将"显著超过$100B"；8/11 Motley Fool：Tan重申该预测，**六大客户承载几乎全部**。已公开可对应的四席：Google、Meta、OpenAI、Anthropic（经Google TPU三方安排）；市场普遍推测含ByteDance（数据缺口：后两位未获本轮来源直接确认）。

### 3.2 OpenAI（最大增量，也是最大融资悬念）

- 2025-10：**10GW定制芯片共同开发+约$10B订单**（Tom's Hardware："mystery $10B customer"即OpenAI）
- 2026-05-07：**$18B芯片交易因Microsoft融资问题停滞**（finance.biggo.com标题；博通当日-4%）——这是"AI融资脆弱性"第一次直接打到博通订单簿
- 2026-06-24：Jalapeño官宣（详1.3）；CRN："绕开Nvidia供应链"
- 2026-06-03电话会：博通计划为OpenAI部署**1.3GW算力，并搭建compute financing platform（算力融资平台）**——博通自己开始当出资方
- Tom's Hardware（2026-02-24）："OpenAI负担不起自建数据中心，于是接管硬件"——设计在手，融资在外

### 3.3 Anthropic（结构性新增）

- 2026-04-07证券文件：博通2027年起向Anthropic供应**约3.5GW Google TPU算力**（叠加2026年已有的1GW Google Cloud安排）；Anthropic年化收入run-rate已超$30B（2025年底约$9B），1,000+企业客户年 spend>$1M
- AWS/Project Rainier仍是主训练伙伴；Anthropic另购2GW AMD MI450——Anthropic是多供策略的执行者，博通是其"Google栈批发商"

### 3.4 Meta

- 2026-04-16：多年期协议**供应MTIA至2029年**（tech-insider口径：$35B规模extension），首期>1GW、多GW演进；博通同时供应Meta以太网scale-up/out/across网络
- Hock Tan退出Meta董事会转任顾问（利益冲突），但仍"指导Meta定制硅路线图"——深度绑定反而加强
- 7/17：Meta新"Iris"芯片通过测试；另据报道Meta将为特定workload采用AMD MI400、并探索租出闲置AI算力（后者曾引发AI板块下跌）
- Meta同时被报探索采购Google Cloud TPU（Nvidia回应"乐见"但暗讽独占平台）——**Meta在GPU/自研ASIC/他厂ASIC间三头下注**

### 3.5 苹果/特斯拉

数据缺口：本轮检索未获两家与博通AI芯片新合作的可靠增量报道（苹果AI服务器芯片传闻、特斯拉自研均无新实证）。不计入管线。

### 3.6 判读

管线质量极高：**美国三大前沿实验室中的两家（OpenAI、Anthropic）以博通为实现层**，加上Google/Meta两大自研锚。但注意三个"折扣"：Jalapeño要到2027年才是收入主力；$18B OpenAI订单证明**订单≠收入，融资才是兑换中介**；六客户集中度意味着任何一家资本开支转向都会放大于博通。

---

## 4. 网络业务：守土之战打响了

| 维度 | 事实 | 来源 |
|---|---|---|
| 市场规模 | 1Q26数据中心以太网交换市场**+39.8%至$15.4B** | IDC（2026-06-17） |
| **格局突变** | **Nvidia按收入登顶以太网交换第一**（收入+193% YoY）；博通让出榜首 | IDC/SDxCentral/富途（三源一致） |
| 博通武器 | Tomahawk 6（102.4T，2025-06出货）；Jericho系列；**3.5D XDSiP**（6,000mm²堆叠、12 HBM）服务XPU；Wi-Fi 8双芯片 | Tom's Hardware/StorageReview |
| Nvidia武器 | Spectrum-X随GPU系统搭售；Beth Kindig估算其光学/CPO战略~$4B且"CPO改变一切"；Vera Rubin NVL72实例已上Google Virgo fabric | Medium/Tom's Hardware |
| CPO竞赛 | IDTechEx（2026-03-11）：Nvidia与博通**两条CPO路线并跑**，博通为先行者之一 | IDTechEx |
| 第三方 | Cisco 102.4T Silicon One G200/G300（2026-02）；Marvell Teralynx系列持续投标 | The Register |
| 生态联盟 | 博通参与Microsoft/Meta/OpenAI主导的**统一光学计算互连多源协议**（scale-up） | Tom's Hardware（Meta交易报道内） |

**判读**：博通在"商业硅"（merchant switch silicon）仍是份额王，但IDC口径按系统收入计，Nvidia凭GPU搭售已夺收入第一——这预示AI网络的价值正从芯片向"系统级fabric"迁移。博通的对策（Jericho AI fabric、CPO、与Meta的scale-up以太网、多源光学联盟）方向正确，但**网络业务的护城河宽度在收窄，而非扩大**。趋势force 2025-10的InfiniBand vs Ethernet分析框架仍成立：以太网scale-up是博通主场，Nvidia用NVLink守scale-up、用Spectrum-X攻scale-out——两端正在对方腹地交火。

---

## 5. AI资本开支的融资脆弱性传导（本报告最重要的一节）

### 5.1 融资依赖的证据链（按时间）

| 时间 | 事实 | 来源 |
|---|---|---|
| 2025-11 | BofA警告"AI繁荣现金告罄"；OpenAI的合作伙伴背负**近$100B债务** | Economic Times |
| 2025-11~2026-03 | "Big Tech回到债市"（Amazon领衔）；大型科技公司AI债从2025年9月的~$370B争论升至**2026-06的$750B**（Bloomberg/AOL口径） | AOL/Barron's/247wallst |
| 2026-04 | Oracle签2.8GW电力协议同期**裁员3万人**；循环融资质疑（Oracle-OpenAI-Nvidia三角） | ibtimes |
| 2026-06-13 | **高盛：$1.8T表外敞口是AI超周期的"定时炸弹"**（SPV/融资租赁类） | 富途/Økonomisk Ugebrev |
| 2026-07-20 | Seeking Alpha："**买hyperscaler卖半导体——轮动已经开始**" | Seeking Alpha |
| 组合锚 | Microsoft FY27资本开支指引**$190B**（4/30财报） | Yahoo Finance |

### 5.2 传导到博通backlog的兑现风险排序

博通backlog延伸至2028（6/3电话会）。若2027年融资收紧，按脆弱度排序：

1. **OpenAI相关产能（最高风险）**：$18B交易已因Microsoft融资停滞过一次；博通不得不自建1.3GW+融资平台——**当设备商开始给客户放贷，等于把客户的信用风险搬上自己的资产负债表**（芒格：看管理层把风险藏到哪儿去了）。Jalapeño收入2027年才放量，正撞融资紧缩假设窗口。
2. **Anthropic 3.5GW（中高风险）**：文件明示"以Anthropic持续的商业表现为前提"（contingent on continued commercial performance）——$30B run-rate很好，但2027年才起供，条件性条款是显性风险。
3. **Meta MTIA（中低风险）**：Meta自身现金流（FY25资本开支自担+经营现金流~$100B级）几乎不需外部融资；且有"租出算力"的变现退路；协议至2029。
4. **Google（最低风险）**：净现金资产负债表+TPU是搜索/云主业的成本项；即便2028年12-15M颗的量级打折，Intel Foundry分流的是封装不是博通设计费。
5. **网络与VMware（基本无关此风险）**：网络随所有AI capex走但客户分散；VMware是存量订阅现金流。

**量化敏感性（粗算）**：若OpenAI+Anthropic相关2027年增量（Mizuho口径合计~$40B+）打五折，博通FY27 AI收入从">$100B"落到~$80B——按当前~$1.87T市值、TTM收入$75.5B、~65x TTM PE（forward非GAAP约25x，stockanalysis口径），这个下修足以解释为何6/4财报后单日-12.6%：**市场已经开始为"订单质量"而非"订单数量"定价。**

---

## 6. VMware软件业务

| 维度 | 事实 | 来源 |
|---|---|---|
| EU监管 | **2026-07-15：博通因VMware许可变更面临EU反垄断正式审查**（注意：本轮未发现"败诉判决"的实证——任务前提中的"EU败诉"未获来源支持，现存事实是审查开启） | Yahoo Finance |
| 日本 | 2026-07-04：**日本关闭**博通VMware反垄断调查（未处罚结案） | PYMNTS/CPI |
| 行业投诉 | CISPE（2025-10）红色警报；EU云商投诉高达**1,000%涨价**（2026-03 trendingtopics "Broadcom Bullies"） | The Register/trendingtopics |
| 司法 | 2025-07：荷兰法院强制博通在85%涨价反弹后支持VMware迁移（不利判例） | Network World |
| 财务 | FQ2'26（6/3）：**软件销售疲软引发股价大跌**（CNBC），尽管AI翻倍 | CNBC/qz |
| 渠道 | 2026-01：VMware伙伴计划改革瞄准EMEA | SDxCentral |
| 事件 | VMware Explore 2026拉斯维加斯8/31–9/3（3/18官宣2026系列；8/17 hpcwire披露400+场次/labs/认证） | Yahoo/hpcwire |

**判读**：VMware的授权模式转型（永久→订阅）在财务上已被证明是提款机，但它的代价是把监管与舆论风险货币化了：EU正式审查是真实尾部（最坏情形：罚款+强制许可条款调整，参照既往科技反垄断案可达年收入几厘米级）；日本结案是正面对照。FQ2软件疲软说明转型红利期（老客户被迫迁订阅的一次性冲高）开始让位于续约经济的真实增速。VMware对组合的意义是"现金流压舱石+估值底"，而非增长引擎——只要EU不走到结构性补救，7.1%仓位的软件部分不构成卖点。

---

## 7. 芒格"生态学"：十年后的AI芯片格局

**第一层（确定性最高）**：推理算力将像电力一样分层计价——前沿训练（Nvidia+Google自研双寡头）、规模化推理（ASIC主导， hyperscaler自持）、长尾/初创（云租赁）。2028年Google TPU 12-15M颗 vs Nvidia 12.4M颗（Fubon）是这个分层的第一个交汇点。

**第二层**：GPU不会输掉"编程模型与生态"，ASIC不会输掉"单位经济"。终局更像今天的数据中心网络：**没有赢家通吃，但有生态位租金**——Nvidia收生态租金，博通收"把巨兽想法变成硅"的实现租金，台积电/Intel收制造租金。

**第三层（博通的生态位）**：博通十年后的位置取决于三件事——(a) 3.5D封装/XDSiP级的设计复杂度门槛是否持续高于MediaTek/Marvell能达到的水平（目前是）；(b) 它是否守得住"网络+ASIC打包"的粘性（Meta协议是样板）；(c) **它是否管住了当financier的冲动**。历史上最好的设备公司死于两件事：客户集中度+应收账款。博通目前两条都沾边。

**芒格式风险清单**：反过来看——什么会杀死博通？不是Nvidia，是(a) 2027年AI债市场一次真正的信用事件冻结neocloud与OpenAI级客户的提货；(b) Google把设计彻底内化+Intel 14A工艺成熟；(c) EU对VMware的结构性判决叠加软件增速失速。三者单独都不是致命，叠加才是。当前概率排序：a > b > c。

---

## 8. 1–6个月催化剂时间表（方向倾向）

| 日期 | 事件 | 方向倾向 | 关注点 |
|---|---|---|---|
| 2026-08-26（三）盘后 | **Nvidia FQ2'27财报**（已多源确认8/26） | 中性偏正 | BofA预期~$95B级beat+多年上修周期；若Rubin需求/NVL72出货超预期→博通网络与ASIC叙事同涨；若数据中心指引谨慎→"卖半导体"轮动加剧 |
| 2026-08-31–09-03 | **VMware Explore 2026**（拉斯维加斯） | 中性偏正 | 私有云+AI平台故事对冲EU审查舆情；注意任何许可模式让步信号 |
| 2026-09-02（三）盘后 | **博通FQ3'26财报**（stockanalysis确认日期） | 高波动、两线决策 | 两线：AI收入≥$16B→加仓区解禁；Q4指引<$18B→减半。额外必听：Google v8/v9份额表述、OpenAI 1.3GW与融资平台进展、backlog/2028口径是否维持、软件增速与EU审查表态 |
| 2026-09–10 | SemiAnalysis/供应链月度追踪 | 偏负 | Google-AMD v10合作细节、MediaTek Triggerfish爬坡数据（GF证券30/6：市场低估MediaTek-Google合作） |
| 2026-10下旬 | **hyperscaler Q3财报/capex季**（MSFT、GOOGL、META、AMZN） | 关键验证 | MSFT FY27 $190B capex执行、Meta MTIA提货节奏、Google TPU capex口径；任何一家砍capex=直接冲击 |
| 2026-10 | OCP Global Summit+Intel Foundry direct | 中性 | CPO/Tomahawk 6生态 vs Spectrum-X；Intel 18A/EMIB对TPU封装分流进展 |
| 2026-10~11 | EU反垄断审查程序进展 | 尾部风险 | 是否升级为正式指控/补救措施提案 |
| 2026-12上旬 | 博通FQ4'26+FY27指引 | 决定性 | $100B AI收入路线图的首个正式年度指引锚点 |
| 持续 | AI债市场（$750B+）与高盛$1.8T表外敞口发酵 | 系统性 | 任何一笔高调违约/降级即触发"融资脆弱性→backlog折价"重定价 |

---

## 9. 行业格局评分卡（芒格五维，10分制）

| 维度 | 评分 | 理由 |
|---|---|---|
| 生意本质（ASIC实现层+网络+软件现金流） | **9** | 三重现金流、设计门槛6,000mm²级、backlog至2028 |
| 产业趋势顺风（ASIC渗透） | **8** | 2027 ASIC≈GPU需求（高盛）；2028 Google单客户追平Nvidia出货（Fubon） |
| 竞争格局变化 | **5**（恶化中） | Google四→五供应商、Nvidia夺以太网交换收入第一、MediaTek/Marvell/AMD三面渗透 |
| 客户质量与集中度 | **6** | 六客户承载$100B；最大增量（OpenAI）已演示过融资停摆；博通变身放贷方 |
| 融资环境依赖度 | **4**（本季最大边际恶化） | $370B→$750B AI债、$1.8T表外、卖半导体轮动已启动 |
| **综合** | **6.4/10** | 极好的生意×正在变贵的环境；仓位维持合理，加仓需财报两线解锁 |

## 10. 操作倾向（一句话）

**维持55股/7.1%仓位跨财报，不加不减；9/2两线兑现即按纪律执行（AI≥$16B且Q4指引≥$18B→分批加至8%；Q4指引<$18B→减半），同时把"博通为OpenAI融资"的资产负债表细节列为加仓前的否决性检查项。**

---

## 11. 来源清单

**全文抓取核实（Tom's Hardware，canonical URL）**
1. Google TPU v8拆分：tomshardware.com/tech-industry/semiconductors/google-splits-its-tpu-into-two-chips-for-the-first-time-with-training-and-inference-variants（2026-04-27）
2. Anthropic 3.5GW/Google 2031：tomshardware.com/tech-industry/broadcom-expands-anthropic-deal-to-3-5gw-of-google-tpu-capacity-from-2027（2026-04-07）
3. Meta至2029+Hock Tan退董事会：tomshardware.com/tech-industry/artificial-intelligence/broadcom-to-supply-meta-with-custom-silicon-through-2029-...（2026-04-16）
4. Google-AMD v10（SemiAnalysis）：tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-...（2026-08-16）
5. Fubon 12-15M TPU 2028：tomshardware.com/tech-industry/artificial-intelligence/google-could-build-more-ai-accelerators-than-nvidia-sells-in-2028-...（2026-07-30）
6. Jalapeño官宣：tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-...（2026-06-24）

**搜索标题级来源（gnews，17次检索，日志见.claude/.workflow/search-log.txt）**
- Counterpoint（2026-01-25/27）：ASIC出货2027年增至三倍；博通保持ASIC伙伴领导地位至2027
- TrendForce（2026-01-20）：2026 AI服务器出货+28%，ASIC占比上升；（2026-03-20）CSP 2H26加速ASIC推进
- IDC经SDxCentral/富途/Trusted Tech（2026-06-17~27）：1Q26以太网交换$15.4B +39.8%，Nvidia收入登顶（+193%）
- 高盛经Motley Fool（2026-05-25）：2027 ASIC需求匹敌GPU；富途/Økonomisk Ugebrev（2026-06-13）：$1.8T表外敞口
- AOL/Bloomberg系（2026-06-22）：Big Tech $750B AI债；Economic Times（2025-11-30）：OpenAI伙伴~$100B债；BofA（2025-11-12）：现金告罄警告
- CNBC（2026-06-03）：FQ2软件疲软+AI指引不变，股价大跌；qz（06-04）：AI收入翻倍股价下跌；Moomoo（06-03）：backlog至2028、Google "looking elsewhere"、OpenAI 1.3GW+融资平台
- Motley Fool（2026-08-11）：Tan重申FY27 AI>$100B、六客户；tech-insider（2026-08-10）：AI芯片收入$10.8B/超$30B backlog（单源，低置信）
- Mizuho（经Tom's Hardware 4/7文内）：Anthropic安排2026 $21B/2027 $42B
- VMware：Yahoo Finance（2026-07-15）EU审查；PYMNTS（07-04）日本结案；trendingtopics（03-20）1,000%涨价投诉；Network World（2025-07-01）荷兰法院；Network World（2025-10-29）拒不让步；SDxCentral（2026-01-05）EMEA伙伴改革；hpcwire（08-17）Explore 2026细节
- 行情：query1.finance.yahoo.com AVGO 1y日线（2026-08-18拉取）；stockanalysis.com/stocks/avgo/（市值$1.87T、PE 65.3、Forward PE 24.9、PT $527.88、财报日9/2）

## 12. 局限性声明

1. **数据缺口**：27.8% ASIC服务器占比、Counterpoint 60%/25%份额拆分、FQ2'26 AI收入精确值（$10.8B为单源转述）、VMware分部利润率、Microsoft Maia代际——均未能双源核实，已在正文标注低置信。
2. 任务前提中的"EU反垄断败诉"未获来源支持；现存事实为2026-07-15 EU正式审查开启（可能此前提有误或指荷兰法院2025-07判例）。
3. gnews仅提供标题+日期；部分转述型媒体（tech-insider、biggo、247wallst）可靠性低于一手来源，已降权处理。
4. Google/博通/Meta官方协议金额多为媒体或分析师口径（Mizuho、Fubon、GF Securities），非公司披露。
5. 本报告为学习研究用途，非投资建议。Brave/内置搜索429（8-22恢复），全部检索经gnews通道完成，日志已追加至search-log.txt。
