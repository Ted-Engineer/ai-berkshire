# APLD 四大师验证 · 行业维度（芒格视角）——AI 数据中心"代建/中立房东"行业格局与生态位

- **日期**：2026-08-19（第5班执行）；**数据截止**：2026-08-18 美股收盘行情 + 当日新闻（本机 `date` 确认）
- **角色**：AI Berkshire 行业研究员（芒格视角）。本次**不复用** `APLD-checklist-20260819.md` 的任何结论，全部基于本轮独立检索。
- **当日行情**（Yahoo chart API，8/18 收盘）：APLD **$28.51（-8.6%）**，52周 $13.16–50.73（较高点 -44%）｜CRWV $93.17（**-12.1%**）｜NBIS $248.43（-7.6%）｜DLR $195.25（-1.3%）｜EQIX $1,085.09（-1.1%）｜VRT $272.54（-6.8%）。APLD 市值约 $8.2B（StockTitan 口径）。
- **检索通道**：curl 17 次 Google News RSS + Yahoo chart API 6 ticker + StockTitan（APLD/BW 两页官方 PR 摘要）+ jina-reader 正文 5 篇（TechCrunch / POWER Magazine 等）；关键数字双源交叉，缺口文末标注。webReader/WebFetch/DDG 多次被配额或反爬拦截，已标注。

---

## 〇、芒格开场：先把"生态位"画对，再谈竞争

芒格看行业不看"赛道"，看**生态学**：谁吃谁、谁给谁打工、利润沉淀在哪一层。AI 算力基础设施在 2026 年 8 月已经分化出四个清晰的营养级：

| 生态位 | 代表 | 收入本质 | 承担的核心风险 | 8/18 表现 |
|---|---|---|---|---|
| **算力零售商（自运营云）** | CRWV、NBIS、新入场的 Meta Compute / SpaceX-xAI | 买 GPU＋机房→按时辰卖算力 | 技术迭代（GPU 3年折旧）、定价权、客户集中 | CRWV **-12.1%**、NBIS -7.6% |
| **中立房东 / 代建商（Powered Land）** | **APLD**、Chirisa+Blue Owl、Prime、Fermi | 卖"已通电的土地＋壳＋交付"，15 年 take-or-pay | 电力交付、融资杠杆、续约议价权反转 | APLD -8.6% |
| **零售 Colo / 互联 REIT** | DLR、EQIX | 城市核心区位＋互联生态＋零售机柜 | 增长太慢（不是杠杆） | DLR -1.3%、EQIX -1.1% |
| **设备/电力 EPC 商** | VRT、B&W、Bloom | 卖铲子：散热、电源、燃气电站 EPC | 订单周期、无长期租金现金流 | VRT -6.8%、B&W 8/18 -3.5% |

**8/18 这个大跌日本身就是一次天然的生态位实验**：同一天、同一个利空（Meta Compute 扩张预期＋全球芯片抛售，见 yellow.com《Meta Compute Plan Hits AI Stocks As Global Chip Selloff Deepens》与 MarketWatch、Motley Fool 多篇双源），离"算力零售"越近的层跌得越狠（CRWV -12% > NBIS -7.6% > VRT -6.8% > APLD -8.6%），而 DLR/EQIX 几乎免疫（-1%）。市场用脚投票的排序与芒格的食物链分析完全一致：**威胁沿"卖算力→卖时间→卖铲子→卖区位"逐层衰减**。

一个刺眼的细节：APLD 的**合同现金流结构**（15 年 take-or-pay，见下）本应让它像 DLR 一样抗跌，但它跌得像 neocloud。这说明市场当前仍把它定价在"AI 故事股"生态位，而不是"电力基础设施"生态位——合同与股价的分离，既是机会（错定价），也是警示（它还不是 DLR，融资与执行风险使然）。这部分属于财务维度，此处不展开。

---

## 一、行业格局：APLD 的"AI Factory"模式在四个生态位中的坐标

### 1.1 APLD 的资产版图（本轮检索重建，全部官方口径）

来自 StockTitan 收录的 APLD 官方 PR 摘要（与 Reuters、DCD、Fierce Network、Pulse 2.0、eciks 等媒体双源）：

| 园区 | 位置 | 规模 | 状态/租约 | 目标投运 |
|---|---|---|---|---|
| Polaris Forge 1（Ellendale） | 北达科他 Ellendale | 400MW 签约 IT 负载，已 live 175MW（B2 一期 75MW 已 RFS） | **全部租出**；含 CoreWeave 250MW 旧约＋MOU 将 B3 租约转给 CoreWeave 子公司（待其获投资级评级） | ELN-04（150MW）由 $1.59B 7.000% 2031 票据融资在建 |
| Polaris Forge 3 | 北达科他 Center（Oliver County） | 园区 430MW，已签 300MW | 美国高投资级 hyperscaler，15 年 take-or-pay，**$7.5B** 基础期（续约至 $18.2B）；当日股价 +21.5% | **2027-08**（MDU 电力协议已签，待 ND PSC 批准） |
| Delta Forge 1 | 路易斯安那 Rapides Parish | 园区 430MW（$3.6B 投资），已签 300MW | 同一美国高投资级 hyperscaler | 在建（Cleco 为其建 756MW 燃气电厂） |
| Delta Forge 2（第五园区） | 未取得位置披露 | 已签 210MW | 同一 hyperscaler，15 年，**$5.2B** 基础期（30 年含续约 $12.7B；Reuters 双源确认） | **2028-Q1** |

**组合汇总（DF2 签约后官方口径）**：签约 IT 负载 **1.4GW**；电网功率规模 **约 2.15GW**；基础期合约租金 **$36B**（含全部续约 **$86B**）；**约 70% 合约收入来自美国投资级 hyperscaler**；同一高投资级客户三连签 810MW / 约 $20.2B。FY26（截至 2026-5-31）：营收 $611.3M（+167%），调整后 EBITDA $107.2M，NOI $90.4M。另：原自有 GPU 云业务已分拆为 **ChronoScale（Nasdaq: CHRN）**，APLD 保留约 96%——公司结构上已把自己"提纯"为房东。

芒格注意到的行业信号：**APLD 已把"自运营云"生态位剥离**（ChronoScale），只留"中立房东"。这与下节巨头的垂直整合方向正好构成镜像——行业在向"要么纯卖时间、要么纯卖算力、不做中间态"分化。

### 1.2 与 CRWV/NBIS（自运营）对比：一层之隔，风险差一个数量级

- **收入形态**：CRWV/NBIS 卖 GPU 时辰（随行就市，The Register 报道 NBIS 承诺"快速 1GW 电力计划"；IO Fund 质疑其循环融资结构）；APLD 卖 15 年 take-or-pay（对手方违约才伤得到它）。
- **技术风险**：GPU 三年一代（TechCrunch 引用的泡沫论者最锋利的一点是"押在快速折旧芯片上的万亿赌局"）——这颗雷在 CRWV/NBIS 的资产负债表上，不在 APLD 的。APLD 的壳设计要跟随液冷/功率密度升级，但改造周期是"建筑级"而非"芯片级"。
- **但租户质量与算力零售商的存亡挂钩**：APLD 最大的老租户是 CoreWeave（Ellendale 250MW＋B3 转让 MOU）。若 Meta Compute 把 neocloud 定价打穿，CoreWeave 的租约虽是 take-or-pay，长期续约与新增需求会受损。**APLD 对 neocloud 的敞口＝合同期内的现金流免疫＋合同期外的需求传染**。约 70% 收入已换成投资级 hyperscaler，正是在主动降低这层传染。

### 1.3 与 DLR/EQIX（REIT 零售 colo）对比：批发 vs 零售，两条时间轴

- DLR/EQIX 的资产在城市核心＋互联枢纽，卖的是"生态与区位"，增速慢但 8/18 证明其防御性（-1%）。美国 colo 市场 2026 规模约 $72.4B，由 EQIX/DLR 领跑，QTS、Iron Mountain 跟进（Research and Markets databook，DCD 转引）。
- APLD 卖的是**边缘电网的批发功率**（北达科他、路易斯安那），单租户、超大规模、15 年期。这不与 REIT 正面竞争，反而互补：hyperscaler 在核心城自建/租 REIT，把训练这种"电力密集、延迟不敏感"的负载扔到偏远大园区。**芒格式表述：REIT 卖的是"地段"，APLD 卖的是"瓦特"；地段不稀缺，当下的瓦特稀缺。**

### 1.4 与 VRT（设备商）对比：卖铲子的没有房东命

VRT：$15B 收入 backlog、液冷主导、2026 上半年 +107%（Seeking Alpha / Globe and Mail 双源）。设备商吃的是"建设量"的一次性订单，吃不到 15 年租金的复利；但也没有融资杠杆与交付罚款风险。B&W 是同一层的电力版：为 APLD 做 ≥1GW 燃气 EPC（见下节），自己 Q2 2026 营收 +130%、backlog +533% 至 $2.6B、pipeline $14B+。**行业每一层都在boom，但利润的"久期"完全不同：设备商赚快钱，房东赚慢钱，neocloud 赌命。**

---

## 二、核心问题：Meta Compute 与 Google-Intersect 的垂直整合——中立房东被绕过了吗？

**结论先行：没有。恰恰相反，2026 年的两起标志性垂直整合事件，一件打击的是 APLD 的"邻居"（算力零售商），一件证明的是 APLD 的"商品"（可交付电力）仍是全行业瓶颈。但诚实的芒格必须同时写出反例条款。**

### 2.1 事实链 A：Meta Compute——巨头下场卖算力，neocloud 被正面攻击

双源事实链（TechCrunch 2026-07-01 正文＋Bloomberg/CNBC/MarketWatch/Fool/Fierce 多源标题）：

1. **2026-05-27**（CNBC）：扎克伯格公开表示自建云业务"definitely on the table"。
2. **2026-07-01**（Bloomberg 独家，TechCrunch 跟进正文）：Meta 筹建云基础设施业务，出售算力与模型访问，名为 **Meta Compute**，由基础设施负责人 Santosh Janardhan、超级智能实验室 Daniel Gross、总裁 Dina Powell McCormick 领衔；考虑复制 CoreWeave 模式卖"裸算力"，并效仿 AWS 出售托管模型（含新闭源模型 Muse Spark）。
3. **动机**：Meta 对 AI 基建的累计承诺已达 **$182.9B**（2026Q1 10-Q，SEC 文件），在路易斯安那 Richland Parish、俄亥俄（"曼哈顿大小"，年内投运）自建巨型园区；自家模型外部需求不足，于是把**过剩算力货币化**——TechCrunch 点题："AI 竞赛的赢家可能不是模型最好的人，而是拥有数据中心的人。"
4. **先例**：SpaceX/xAI 已先行（2026-05）：Anthropic **买断 Colossus 1 全部算力**，随后又与 Google、Reflection AI 签约；SemiAnalysis 推演 SpaceX 2027 年达 10GW、$300B ARR、微软为最大买家。
5. **市场后果**（多源一致）：Meta 确认推进当日 Meta +9%（CNBC）；CRWV/NBIS/IREN 应声大跌（Fool《Should Nebius and CoreWeave Investors Be Scared》、techi《Nebius Lost $12 Billion in a Day》、247wallst《Meta 想用主权级规模埋葬 CoreWeave》）；8/18 在芯片抛售中继续被压制（yellow.com）。

**芒格判读**：Meta Compute 的经济学是"边际成本定价的巨头过剩产能"——Meta 的算力是自用的沉没成本，外卖价可以低到只覆盖运营，这是对 CRWV/NBIS 这类"以算力差价为生"公司的出清式打击。**但对 APLD 无害甚至有利**：第一，Meta 每卖一小时算力，都在扩大"已通电容量"的价值，而 Meta 自己的新园区（El Paso 与 BlackRock 合资 $14B 园区，PR Newswire/Yahoo 双源）从拿地到通电同样要排电力队；第二，Meta Compute 卖的是推理/训练服务，它不卖"给竞争对手的对手盘提供中立场地"——**中立性本身是产品**：OpenAI/Anthropic/xAI 不可能租 Meta 的机房，hyperscaler 之间互不租，neocloud 又没有 $2B 一栋的信用去 project-finance 自建——**中立房东是这群互相戒备的猛兽唯一共用的水坑**。

### 2.2 事实链 B：Google-Intersect——巨头把"发电商"直接买下来

双源事实链（POWER Magazine 2026-06-04 长文正文＋Alphabet 官方公告/DCD/PV-Tech/POWER/Utility Dive 标题群）：

1. **2024-12**：Google＋TPG Rise Climate 向 Intersect Power 注资超 $800M，目标 2030 年前催化 $200 亿清洁能源＋共置数据中心投资。
2. **2025 年末宣布、2026-03 交割**：Alphabet 以 **$4.75B 现金＋承债**全资收购 Intersect（获得多 GW 开发管线与整建团队；存量运营资产剥离给 TPG 等）。
3. **2026-06-04**：首个收购后项目 **Meitner Energy Center**（得州 Panhandle Gray/Roberts 两县）开工——**1GW+ 风光储＋场内燃气 firming 与数据中心共址**，"Day One 清洁能源为主、少数燃气兜底"；Google 同时在得州已有 6,200MW+ PPA，2026 年又加签 Clearway 1.17GW、TotalEnergies 1GW 光伏、Sunraycer 400MW、Linea 500MW；配套 Missouri CCF、Nevada 地热 CTT、Minnesota 铁-空气储能 CEAC、1GW 需求响应、白宫 Ratepayer Protection Pledge。
4. 行业解读（avanzaenergy 等评论，与 POWER 事实层分离）："power-first"模式宣告 PPA 时代式微——**巨头不再向第三方买电、也不再等第三方建园，直接把电力开发商变成自己的部门**。

**芒格判读——这是对"中立房东"的真问题，必须两面写**：

- **利好面（当下被验证）**：Google 为了不排队，花 $4.75B 买发电商＋自建共址园区——这**反向证明了"可交付的电力＋土地"是何等稀缺**，稀缺到全球最有钱的公司宁愿买下整个开发商。APLD 手里 2.15GW 电网功率＋已签 MDU/Cleco/B&W 电力合约，正是同一商品的在售库存。Google 模式普及得越快，全行业对"谁能立刻交货"的定价就越高——APLD 2026 年连签 $20.2B 三连约（同一投资级客户），就是这种定价的体现。
- **风险面（10 年维度）**：如果 Intersect 式"自持电力部门"成为四巨头标配，2028-2030 年后巨头新增产能可以完全不经过中立房东——**第三方园区会从"必需品"退化为"补充产能"**，续约（2040 年代）时的议价权将反转。APLD 的 15 年 take-or-pay 恰好把这个风险推到了 2041 年——**它卖的本质是"电力稀缺窗口期的批发时间"，窗口关闭前锁死合同，是这门生意的全部要义**。

**芒格反转问句**（自答）："如果我是扎克伯格，有 $182.9B 承诺和自建电力团队，为什么把下一 GW 给 APLD？"——因为 Meta 自己的园区从排队到通电要面对的是：得州 **474GW 的并网申请池**（Utility Dive：得州已因该数字**暂停审批新数据中心**）、全国性的互联积压（MarketScale/WEF/American Action Forum 多源），而 APLD 的北达科他/路易斯安那功率是**已排到队、已有 ESA、燃气已在 B&W 订单表上的现货**。**在电力市场，时间比价格贵。**

---

## 三、电力先手：2.15GW 电网功率＋≥1GW 自备气电的稀缺性时间窗

### 3.1 APLD 电力资产盘点（双源：官方 PR 摘要＋DCD/IIR/Cleco/B&W 公告）

- **电网侧**：组合电网功率约 **2.15GW**（DF2 官方 PR 口径）。Polaris Forge 3 与 **Montana-Dakota Utilities（MDU）签电力服务协议**，满负荷 430MW，目标 2027-08 投运（MDU 已为 PF1 服务，三年给北达客户回馈 $38.4M 电费抵扣——政治善缘资产）。
- **燃气侧**：与 **Babcock & Wilcox 签 $2.4B 协议＋LNTP**，设计安装 **"One Gigawatt"级**自备燃气电站（B&W 官方标题；DCD 标题"more than 1GW"；采用 **Siemens Energy 20 台汽轮发电机组**，B&W 另已为 12–15 个月交付窗口再锁定 1GW 机组产能）；路易斯安那侧 **Cleco 为 Delta Forge 建 756MW 燃气电厂**（DCD 报道＋Cleco 官方 PR 双源）。任务书所称"1.2GW 自备气电"未获第二来源精确口径，**按"≥1GW（B&W LNTP）+ 第三方 756MW（Cleco）"如实标注**。
- **在途扩张**：已在北达科他 Oliver County 考察第三个数据中心选址（Valley News Live），MDU/PSC 流程并行。

### 3.2 窗口的稀缺性证据（为什么"先手"值钱）

1. **得州 474GW 互联申请池→州层面暂停新数据中心审批**（Utility Dive）——最大市场化电力市场开始排斥新负荷，排队位置变成硬通货。
2. **燃气 EPC 产能全球紧俏**：B&W 自己 pipeline $14B+、为交付锁定 1GW 机组需排队 12–15 个月；Bloom/Chirisa/CoreWeave 在伊利诺伊搞微电网自保（Data Center Frontier/Microgrid Knowledge 双源）——**整个行业在用"分布式燃气"绕开电网，而 APLD 两头都占**（既有大电网 ESA，又有自备气电）。
3. **政策双向风险**：参议院民主党调查燃气数据中心（Latitude Media）、WIRED 质疑新增燃气 DC 排放"超过整个国家"——**政治是这门生意最大的外生变量**，北达科他（共和党州、低电价、欢迎投资）与路易斯安那（Cleco 合规大电厂路线）选址本身是一种监管套利。

### 3.3 竞品的电力打法对照（谁在抢同一张入场券）

| 竞品 | 2026 动向（来源） | 与 APLD 的功率差 |
|---|---|---|
| **Fermi America**（Rick Perry） | 得州 Big Spring"Hypergrid"——规划**世界最大私有电网**（Hart Energy）；曾有一笔 $150M 交易告吹、后找到首个大客户（WSJ/ConstructConnect 双源） | 愿景大于交付：仍在找客户阶段，APLD 已 $36B 合约在手 |
| **Chirisa Generation** | 与 Blue Owl/PowerHouse 的 **$5B JV** 进入下一期、另获 $750M 融资建 CoreWeave 园区（PR Newswire/DCD）；弗吉尼亚园区三周两起火灾（DCD）——交付质量风险暴露 | 资金雄厚但执行口碑受损；APLD 连续按期 RFS（B2 一期 75MW on schedule，Yahoo 转引） |
| **Prime Data Centers** | Sacramento 第二栋动工、区域扩产、获 Grain 投资（Business Wire/Sacramento Business Journal） | 城市级批发（几十 MW 级），不在 GW 级电力先手竞赛同一条起跑线 |
| **Crusoe** | 战略转向**模块化"grab-and-go"数据中心**（Forbes），此前一次暂停曾打击 Bloom（TechStock²） | 从"大园区"退向"快部署"，侧面印证大园区电力之难 |
| **DLR/QTS/IRON（REIT 系）** | 靠资本市场与存量土地扩产（colo databook） | 城市核心为主，边缘大功率赛道让给 APLD/Fermi/Chirisa |

**任务书所列"修正案数字"未能定位**：公开信息中查无此名的数据中心开发商（疑为音译/笔误），**标注为缺口**；已按实际主力竞品（Fermi/Chirisa/Prime/Crusoe）完成覆盖。

芒格对窗口的判断：**电力先手是一条"会折旧的护城河"**。它不来自技术垄断，来自排队位置＋行政许可＋燃气机组订单这三个会随时间贬值的资产：电网扩容（FERC 加速令已出）与燃气 EPC 产能扩张（B&W backlog +533% 说明供给正在赶来）都会在 2028–2030 年收窄缺口。**APLD 的战略本质是在窗口关闭前把每个 GW 都焊进 15 年 take-or-pay。** 窗口期长度 = 行业估值的核心变量。

---

## 四、芒格"生态学"：10 年 AI 园区终局推演（2036 年回头看）

**情景 A：铁路化（主观概率 ~50%）**
AI 园区重演 19 世纪铁路+土地公司剧本：四巨头自持"干线"（核心自有园区），中立房东持有"支线与仓储容量"；15 年 take-or-pay 像铁路长期运输合约一样成为基础设施固收资产。APLD 们演化为**未注册的电力 REIT**，估值从 AI beta 切换到收益率曲线。特征：巨头 capex 增速放缓但绝对值维持，租约到期续约率>80%。这个情景下今天的 APLD 便宜得离谱。

**情景 B：全闭环（~30%）**
Google-Intersect 模式普及：每家巨头内化"发电商＋EPC＋园区"，2028 年后新增 GW 不再外流；中立房东退化为次级补充产能，2040 年代续约时议价权反转（租约重定价 downward）。特征：观察指标是**巨头收购电力开发商的频率**（2026 年已见一例）与**APLD 新签约租户中投资级占比是否维持**。部分对冲：APLD 已有 $36B 基础期合约把重定价推到 2041+。

**情景 C：需求断崖/折旧陷阱（~20%）**
TechCrunch 引用的泡沫论成真：终端 AI 收入（Anthropic ARR 低于耳语、WSJ $3T 表外承诺等，见同期 CRDO 行业报告的双源记录）撑不住万亿 capex，take-or-pay 对手方寻求重组。**APLD 的防御**：约 70% 收入来自美国投资级 hyperscaler——但芒格要冷冷补一句："投资级"在同一个 capex 周期里是**相关性强、非独立的**信用；四巨头同时砍 capex 时，"分散"是幻觉。Ellendale 的 CoreWeave 租约是组合中最脆的一块。

**芒格三问收尾**：
1. *10 年后这个行业还在吗？*——在，且更大：AI 用电力像人用卡路里，推理时代只增不减。
2. *利润归谁？*——归"许可与瓦特"的持有者，不归壳，更不归转售算力的人。
3. *APLD 在食物链哪一层？*——**卖批发时间的商人**：不赌技术路线、不赌模型胜负，赌的是"未来 15 年美国电力交付会比今天更稀缺"这一件事。这件事当前被 474GW 排队池、B&W 12 个月机组交期和得州暂停令共同证实着。

---

## 五、行业维度评分（芒格口径）

**总评分：★★★★☆（4/5）——"电力稀缺窗口期的高质量批发房东生态位；扣一星给窗口会关闭与巨头闭环化的双向不确定性"**

| 分项 | 评分 | 一句话依据 |
|---|---|---|
| 需求确定性（5 年内） | ★★★★★ | $36B 基础期合约已锁；巨头 $182.9B 级承诺与 474GW 排队池 |
| 竞争强度 | ★★★☆☆ | Fermi/Chirisa/Prime/Crusoe 同向扩产，但 GW 级电力先手者屈指可数 |
| 生态位安全性（被绕过风险） | ★★★★☆ | Meta Compute 打的是 neocloud 不是房东；但 Google-Intersect 展示了 10 年后的绕行路径 |
| 时间窗久期 | ★★★☆☆ | 燃气 EPC 产能与 FERC 加速正在赶来，2028–30 窗口收窄概率大 |
| 周期/政策脆弱性 | ★★★☆☆ | 参议院燃气调查、表外杠杆疑虑、take-or-pay 信用的周期相关性 |

（注：此为**行业生态位**评分，不含 APLD 公司层面的融资/稀释/治理判断——那属于 checklist 与财务维度，本轮不涉及。）

---

## 六、催化剂表

| 预计时点 | 事件 | 方向 | 依据 |
|---|---|---|---|
| 2026-09 前后 | ND PSC 对 PF3－MDU 430MW 电力协议的批准裁决 | 批准＝+/否决＝- - | MDU ESA 需 PSC 批准（官方 PR） |
| 2026 H2 | Oliver County 第三园区选址落地/预签约 | + | Valley News Live 报道考察中 |
| 2026 H2–2027 | Meta Compute 正式商用与定价公布 | 间接：压制 CRWV/NBIS → APLD 中立性溢价提升；但若引发 AI capex 信心恶化则全体承压 | Bloomberg 7/1、CNBC |
| 2027 年中 | B&W/Siemens 20 台机组到货安装（12–15 个月窗口） | +（自备电力落地） | B&W Q2 2026 PR |
| 2027-08 | Polaris Forge 3 初始运营（300MW/首笔 $7.5B 计租） | ++（NOI 跃升） | 官方 PR |
| 2028-Q1 | Delta Forge 2 初始运营（210MW/$5.2B） | + | Reuters 双源 |
| 不定期 | 得州 474GW 排队池的政策决议 / ERCOT 新负荷规则 | 收紧＝电力先手资产升值 | Utility Dive |
| 不定期 | 参议院对燃气数据中心的调查进展 | 负面尾部 | Latitude Media |
| 不定期 | 巨头再收购电力开发商（第二个"Intersect"） | 情景 B 概率上修的信号 | POWER/Alphabet 公告 |
| 不定期 | CoreWeave 获投资级评级（触发 B3 租约转让 MOU） | +（租户信用升级） | 官方 PR |

---

## 七、数据来源与缺口标注

**主要来源**（关键数字均双源）：APLD 官方 PR（经 StockTitan Rhea-AI 摘要：FY26 业绩、$36B/1.4GW/2.15GW/810MW-$20.2B、$1.59B 票据、CHRN 分拆、MDU ESA、DF2 $5.2B）× Reuters（DF2）× DCD/Fierce/Pulse2/eciks（PF3、DF1）；B&W 官方 PR 摘要（1GW LNTP、Siemens 20 机组、$2.4B×IIR）× DCD 标题；Cleco 官方 × Louisiana Illuminator/WBRZ（$3.6B、Rapides Parish）；TechCrunch 正文（2026-07-01）× Bloomberg/CNBC/MarketWatch/Fool（Meta Compute 全链）；POWER Magazine 正文（2026-06-04）× Alphabet 公告/DCD/PV-Tech（Intersect $4.75B、Meitner 1GW+）；Utility Dive（474GW/得州暂停）× MarketScale/WEF/American Action Forum（互联积压）；Hart Energy × WSJ/ConstructConnect（Fermi）；PR Newswire × DCD（Chirisa/Blue Owl $5B JV）；Business Wire × Sacramento Business Journal（Prime）；Forbes × TechStock²（Crusoe 转向）；Yahoo chart API（6 标的收盘价）。

**缺口（诚实标注）**：
1. **"1.2GW 自备气电"未获双源**：可核实为 B&W"≥1GW"LNTP＋Cleco 第三方 756MW；1.2GW 精确口径未在公开 PR 中找到。
2. **"修正案数字"（疑似竞品名）无法定位**：公开信息查无此公司，疑为音译/笔误，未做任何猜测性替代结论。
3. **大租户身份未披露**：SEC 与 PR 均未具名"美国高投资级 hyperscaler"，本报告不做任何具名推断。
4. **Delta Forge 2 的具体位置**未在所获来源中披露（仅知为第五园区）。
5. **8/18 跌幅归因**：多源媒体（yellow.com/MarketWatch/Fool）指向"Meta Compute＋芯片抛售"，但无官方归因，属合理推断非定论。
6. **WSJ（Fermi 客户身份）、Bloomberg 原文、Seeking Alpha 全文**等付费墙未读，仅用标题级信息并已标注。
7. **工具受阻记录**：webReader/WebFetch 配额耗尽（至 8/22）、DDG/Bing 反爬拦截、DCD 正文多次超时——改用 jina-reader＋StockTitan 完成正文级验证，均已在 search-log.txt 留痕。
8. B&W 财报中出现的"Base Electron 数据中心项目"（Q2 贡献 $100.7M 营收）名称存疑（疑为转写歧义），未用于本报告任何结论。

---

*本报告为学习与研究用途，不构成投资建议。芒格语录位置：反过来想——这个行业的死法是"电力不再稀缺"；盯着 474GW 排队池什么时候清空，就知道了。*
