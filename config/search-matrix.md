# 候选发现搜索矩阵（portfolio-rebalance skill 的参数文件）

> 本文件是**搜索词库参数**：GICS 25组双视角 + AI 17赛道 + 非AI 14主题 + 7维交叉。
> 新增赛道/主题/教训驱动的搜索词只改这里，不改 skill。
> 版本：v4（2026-08-15，含端侧AI/AI数据/中国消费/黄金四个新增）

## 搜索总量硬指标

全程搜索**合计≥80次**（每次调用追加记录到 `.claude/.workflow/search-log.txt`）。
构成：GICS 25组×2视角=50 + AI赛道17×2=34 + 非AI主题≥8 + 7维补充 ≈ 95+，留冗余。

**候选池两侧均衡**：AI相关候选占比不得超过65%，非AI候选至少35%。candidates.csv 的 source 列必须标注所属清单（AI赛道#n/非AI主题#n/GICS/D1-D7/F-memory/G-生态链），报告末尾输出两侧占比统计。

---

## 一、GICS 25个二级行业组（全部搜索，每组2次：价值型1次+成长/事件型1次）

| 1级行业 | 2级行业组 | 价值型搜索词 | 成长/事件型搜索词（第二视角） |
|---------|----------|-------------|------------------------------|
| 能源 | Energy | "undervalued energy oil gas pipeline midstream stocks 2026" | "energy stocks earnings beat guidance raised 2026" / "natural gas pipeline LNG capacity expansion stocks" |
| 材料 | Materials | "undervalued chemical metals mining specialty materials stocks 2026" | "lithium uranium copper miners production growth 2026" / "specialty materials supply shortage stocks" |
| 工业 | Capital Goods | "undervalued industrial machinery defense aerospace manufacturing stocks 2026" | "defense stocks record backlog order growth 2026" / "electrical equipment grid capex beneficiary stocks" |
| 工业 | Commercial & Professional Services | "undervalued business services waste environmental printing stocks 2026" | "business services stocks high ROIC insider buying 2026" / "staffing payroll stocks hiring recovery" |
| 工业 | Transportation | "undervalued airline railroad trucking logistics shipping stocks 2026" | "shipping railroad stocks earnings recovery momentum 2026" / "airline stocks capacity discipline margin" |
| 消费者可选 | Automobiles & Components | "undervalued auto EV auto parts dealer stocks 2026" | "EV stocks deliveries growth 2026" / "auto supplier content per vehicle increase stocks" |
| 消费者可选 | Consumer Durables & Apparel | "undervalued consumer electronics household appliance luxury apparel stocks 2026" | "luxury brand pricing power revenue growth 2026" / "appliance housing recovery stocks" |
| 消费者可选 | Consumer Services | "undervalued restaurant hotel casino cruise travel stocks 2026" | "travel leisure cruise stocks earnings beat 2026" / "restaurant same store sales growth stocks" |
| 消费者可选 | Retailing | "undervalued ecommerce grocery discount retail department store stocks 2026" | "retail stocks same store sales margin expansion 2026" / "off-price discount retail traffic growth" |
| 通信服务 | Telecommunication Services | "undervalued telecom wireless tower stocks 2026" | "telecom stocks FCF dividend growth 5G monetization 2026" / "fiber broadband penetration growth stocks" |
| 通信服务 | Media & Entertainment | "undervalued streaming media gaming advertising publishing stocks 2026" | "streaming gaming stocks subscriber growth profitability 2026" / "advertising stocks digital shift share gains" |
| 消费者必需 | Staples Distribution & Retail | "undervalued grocery food retail drug store distribution stocks 2026" | "grocery drugstore stocks defensive recession stable earnings" / "food distribution volume recovery stocks" |
| 消费者必需 | Food, Beverage & Tobacco | "undervalued food beverage tobacco alcohol stocks 2026" | "food beverage dividend aristocrats pricing power 2026" / "alcohol tobacco volume recovery stocks" |
| 消费者必需 | Household & Personal Products | "undervalued household personal care beauty products stocks 2026" | "consumer staples quality moat margin stability 2026" / "beauty personal care emerging market growth stocks" |
| 医疗保健 | Health Care Equipment & Services | "undervalued medical device hospital health IT services stocks 2026" | "medical device new product cycle FDA approvals 2026" / "hospital health services volume growth stocks" |
| 医疗保健 | Pharma, Biotech & Life Sciences | "undervalued pharma biotech drug manufacturing life science tools stocks 2026" | "biotech pipeline catalysts FDA approvals 2026" / "life science tools CRO backlog growth stocks" |
| 金融 | Banks | "undervalued bank regional bank money center bank stocks 2026" | "bank stocks NIM expansion earnings growth 2026" / "regional bank merger acquisition targets 2026" |
| 金融 | Diversified Financials | "undervalued fintech payment processing asset manager exchange data stocks 2026" | "fintech transaction volume TPV growth 2026" / "exchange market data stocks moat pricing power" |
| 金融 | Insurance | "undervalued insurance P&C life reinsurance broker stocks 2026" | "insurance hard market combined ratio improvement 2026" / "specialty niche insurer high ROE 2026" |
| 信息技术 | Software & Services | "undervalued software SaaS enterprise cloud cybersecurity AI software stocks 2026" | "SaaS NRR 120% net revenue retention 2026" / "AI agent software ARR growth triple digit 2026" |
| 信息技术 | Technology Hardware & Equipment | "undervalued tech hardware server storage networking equipment stocks 2026" | "server storage networking AI demand revenue surge 2026" / "hardware margin expansion turnaround stocks" |
| 信息技术 | Semiconductors & Semi Equipment | "undervalued semiconductor design foundry memory equipment materials stocks 2026" | "semiconductor revenue growth 50% AI 2026" / "HBM memory shortage beneficiary stocks" |
| 公用事业 | Utilities | "undervalued utility electric power gas water nuclear renewable stocks 2026" | "utility data center power demand growth 2026" / "nuclear renewable capacity expansion IPP stocks" |
| 房地产 | Real Estate | "undervalued REIT industrial office residential retail data center healthcare REIT stocks 2026" | "data center REIT FFO growth 2026" / "REIT dividend yield discount to NAV stocks" |

**执行要求**：25组全部搜索（两列词各≥1次，合计≥50次）；对有潜力的方向下钻到3级（如"Semiconductors"→"Memory/HBM"单独搜）；某组无候选须标注"已扫描，无候选"。报告输出25组×双视角覆盖矩阵。

<!-- AI-TRACKS -->

---

## 二、AI侧17个赛道（GICS无法覆盖的新业态，全部搜索，每赛道≥2条不同视角词，合计≥34次）

视角A=运营商/公司本身，视角B=供应商/瓶颈，视角C=催化剂/事件，任选其二：

| # | AI赛道 | 搜索词（多视角） | 代表标的方向 |
|---|--------|----------------|-------------|
| 1 | AI Cloud / Neocloud运营商 | A:"AI cloud GPU rental neocloud providers 2026" B:"neocloud contract backlog billion deal wins" C:"coreweave nebius earnings revenue growth" | NBIS, CRWV, Lambda, Crusoe |
| 2 | AI定制芯片ASIC/推理芯片 | A:"custom AI ASIC accelerator design win stocks 2026" B:"broadcom marvell XPU customer pipeline" C:"AI inference chip vs training shift beneficiaries" | AVGO, MRVL, ALAB |
| 3 | AI网络/光模块/交换 | A:"800G 1.6T optical module demand growth 2026" B:"AI cluster networking switch CPO stocks" C:"co-packaged optics breakthrough suppliers" | ANET, CIEN, COHR, LITE, CRDO |
| 4 | HBM/存储 | A:"HBM4 capacity sold out memory stocks 2026" B:"DRAM NAND supply tightness beneficiary" C:"micron SK hynix HBM revenue growth" | MU, WDC, STX |
| 5 | 先进封装/CoWoS链 | A:"advanced packaging CoWoS capacity expansion 2026" B:"OSAT packaging substrate ABF shortage stocks" C:"chiplet hybrid bonding equipment suppliers" | TSM, AMKR, KYEC |
| 6 | 半导体设备/材料 | A:"WFE wafer fab equipment spending record 2026" B:"semiconductor materials shortage suppliers" C:"ASML AMAT KLAC backlog book-to-bill" | AMAT, LRCX, KLA, ASML |
| 7 | AI电力：燃气IPP/核电/铀 | A:"data center power gigawatt pipeline IPP stocks 2026" B:"nuclear SMR fuel uranium enrichment demand" C:"power purchase agreement AI hyperscaler signed" | VST, CEG, TLN, NRG, CCJ, LEU |
| 8 | 电网设备/变压器 | A:"transformer lead time shortage grid equipment stocks 2026" B:"transmission substation capex beneficiary" C:"electrification switchgear demand surge" | GEV, HIT(日立), ETD, PWR |
| 9 | AI散热/液冷 | A:"liquid cooling rack power density AI stocks 2026" B:"CDU cold plate immersion cooling suppliers" C:"Vertiv earnings AI backlog growth" | VRT, MODV, SMCI, nVent |
| 10 | 数据中心REIT/代建/E&C | A:"data center REIT FFO growth leasing 2026" B:"data center construction E&C backlog stocks" C:"hyperscaler capex guidance data center buildout" | EQIX, DLR, JCI, EME |
| 11 | AI Agent/应用软件 | A:"AI agent enterprise deployment ARR growth 2026" B:"agentic workflow software adoption metrics" C:"Salesforce ServiceNow Palantir AI revenue disclosure" | CRM, NOW, PLTR, SOUN |
| 12 | AI模型/基础模型生态 | A:"foundation model API token revenue growth 2026" B:"LLM training compute contract suppliers" C:"OpenAI Anthropic valuation revenue multiple" | MSFT, GOOGL, META + 供应商 |
| 13 | 物理AI/人形机器人 | A:"humanoid robot production ramp 2026 stocks" B:"robot actuator reducer sensor suppliers" C:"Tesla Optimus Figure commercial timeline" | TSLA, 供应商群 |
| 14 | 自动驾驶/Robotaxi | A:"robotaxi commercial fleet expansion 2026" B:"AV lidar compute supplier stocks" C:"autonomous driving regulatory approval milestone" | TSLA, AUR, GOOGL生态 |
| 15 | 加密矿企转AI算力 | A:"bitcoin miner AI pivot HPC hosting 2026" B:"crypto mining data center conversion capacity" C:"Hut 8 Bit Digital AI contract revenue" | BTBT, CLSK, HUT, IREN |
| 16 | 端侧AI/边缘推理芯片 | A:"AI PC AI phone NPU upgrade cycle stocks 2026" B:"edge AI inference chip smartphone PC silicon suppliers" C:"on-device AI qualcomm mediatek design win" | QCOM, MTK, 端侧传感器链 |
| 17 | AI数据/标注/合成数据 | A:"AI data labeling curation public companies 2026" B:"synthetic data training data suppliers stocks" C:"data infrastructure AI governance compliance" | 数据标注、合成数据、数据工具 |

**执行要求**：17个赛道全部搜索，每个≥2条不同视角词；任何赛道"无候选"必须标注扫描词原文；报告输出17赛道×视角覆盖矩阵。

---

## 三、非AI侧14个主题（防AI单一叙事绑架；至少8个主题各≥1次，合计≥8次）

**主题13/14为优先纳入项**：13催化剂密度高（政策+估值修复），14与AI泡沫应急规则构成对冲闭环。

| # | 非AI主题 | 搜索词示例 | 代表方向 |
|---|---------|-----------|---------|
| 1 | 老龄化/银发经济 | "aging population healthcare demand stocks 2026" / "senior living home healthcare volume growth" | 医疗服务、养老、慢病管理 |
| 2 | 国防现代化 | "defense stocks record backlog NATO rearmament 2026" / "defense electronics ammunition capacity" | LMT/NOC/HWM/欧洲军火 |
| 3 | 能源转型/电网升级 | "grid modernization capex beneficiary stocks 2026" / "energy storage battery demand growth" | 电网、储能、输配电 |
| 4 | 美国制造回岸/自动化 | "reshoring US manufacturing factory automation stocks 2026" / "industrial robot machine tool demand" | 自动化、机床、工业软件 |
| 5 | 利率长期下行受益者 | "rate cut beneficiaries stocks 2026 duration assets" / "REIT utilities relative value falling rates" | REIT、公用、长久期成长 |
| 6 | GLP-1/减肥药生态 | "GLP-1 supply chain contract manufacturing 2026" / "obesity drug volume growth suppliers" | CDMO、给药装置、原料药 |
| 7 | 水务/基建老化更新 | "water infrastructure replacement cycle stocks 2026" / "pipe valve pump municipal capex" | 水务设备、工程 |
| 8 | 农业科技/粮食安全 | "agriculture technology precision farming stocks 2026" / "fertilizer crop protection supply" | 农化、农机、种子 |
| 9 | 体育博彩/iGaming | "sports betting iGaming legalization expansion 2026" / "online gambling volume growth stocks" | 博彩运营、平台 |
| 10 | 宠物经济 | "pet economy spending growth stocks 2026" / "veterinary pet food premiumization" | 宠物食品、兽医链 |
| 11 | 奢侈品/品牌护城河 | "luxury brand pricing power heritage moat 2026" / "premium consumer resilience stocks" | LVMH系、高端消费 |
| 12 | 保险硬市场周期 | "insurance hard market pricing cycle 2026" / "P&C reinsurance underwriting margin stocks" | 财险、再保、经纪 |
| 13 | 中国/新兴市场消费复苏 | "China consumer stimulus recovery stocks 2026" / "Chinese ecommerce valuation re-rating catalysts" | 中概电商、消费、本地生活 |
| 14 | 黄金/贵金属（尾部对冲+自身动量） | "gold miners real rates tail hedge stocks 2026" / "precious metals royalty central bank buying momentum" | 金矿、贵金属权利金公司（FNV/WPM类） |


---

## 四、7维正交交叉搜索（与GICS枚举互补，每维至少1次；D6、D7必做）

枚举的局限：任何分类都"按过去的方式组织行业"。正交维度让交集自然浮现枚举会遗漏的标的。

| 维度 | 逻辑 | 搜索方式（示例） |
|------|------|-----------------|
| **D1. 量化筛选** | 财务指标横切全市场 | "stocks forward PE under 15 ROE above 20 FCF yield above 8 2026"；finviz/stockanalysis筛选器。**至少3组不同条件**：价值型（fPE<15）、成长型（收入增速>50%）、收益型（FCF yield>5%）各一组，不可全是价值型 |
| **D2. 主题/趋势** | 按投资主题横切 | 直接引用上方两份清单：AI侧17赛道（每赛道≥2视角词）+ 非AI侧14主题（≥8个）。禁止只搜泛化的"AI infrastructure beneficiaries"这类笼统词（NBIS教训） |
| **D3. 事件驱动** | 按催化剂事件搜索 | "recent spin-off stocks 2026"、"activist investor targets 2026"、"rejected acquisition target stocks"、"earnings beat guidance raised 2026" |
| **D4. 技术面/资金面** | 按价格行为搜索 | "stocks near 52 week low strong fundamentals 2026"、"oversold stocks institutional buying"、"insider buying cluster 2026" |
| **D5. 聪明钱跟踪** | 顶级投资者在买什么 | "best value investor holdings changes 2026 Q2"、"Berkshire Hathaway portfolio changes"、"top hedge fund new positions 13F" |
| **D6. 财报催化（必做）** | 最近1周财报+重大异动 | "stocks earnings beat guidance raise 2026 August"、"biggest earnings movers this week"、"revenue growth over 200% stocks 2026"、"contract backlog billion dollars AI stocks"、"analyst estimate revision upgrade momentum stocks 2026"。**搜索词不可带"undervalued"——高成长股不会出现在价值筛选器中**（NBIS教训：454%增速+$40B积压→单日+34%） |
| **D7. 持仓生态链（必做）** | 每只持仓的供应商/客户/合作伙伴 | 对每只持仓搜索 "{持仓公司} supplier vendor partner"、"who provides AI compute to {持仓公司}"（NBIS是META/MSFT的算力供应商——执行此维度必然发现） |

**执行要求**：
- 7维每维≥1次（D6、D7必做）；D1三组条件、D2十二个主题（AI≥8+非AI≥4）
- 各维度候选与GICS+赛道候选去重合并，每个候选标注发现维度
- D2主题可与上方清单复用同一搜索但不重复计数

---

## 五、候选来源A-G总表（7路并行，缺一不可）

| # | 来源 | 做什么 | 为什么 |
|---|------|--------|--------|
| A | portfolio-latest.md 待执行项 | Read持仓文件，提取"待执行""观察""计划买入"等所有未完成项 | 用户已有意图的标的最可能成交，不可遗漏 |
| B | 全市场多维搜索 | GICS 25组双视角 + 7维交叉（本文件第一、四节） | 枚举+正交双保险 |
| C | /industry-funnel | 按行业漏斗逐层精选 | 系统性覆盖行业内的候选 |
| D | /bottleneck-hunter | 供应链瓶颈套利扫描 | 非传统视角的标的 |
| E | 行业分布缺口反向映射 | 按分布偏差反向映射到GICS行业清单，对缺口行业定向搜索 | 分布偏差被定向修正（方向提示，不是搜索限制） |
| F | 用户历史关注（必选） | 三步：(1)Read MEMORY.md索引；(2)对每条相关记忆Read完整内容提取ticker；(3)特别关注反复研究但未执行的标的。输出提取清单 | 用户花最多时间研究的标的最可能成交（NBIS教训：索引有4条但未读取=零执行） |
| G | 持仓生态链反向搜索（必选） | 对每只持仓搜索核心供应商/客户/合作伙伴（=D7） | 生态链标的有已验证的商业关系（NBIS是META/MSFT算力供应商） |

**来源F执行证据**：必须展示"Read了哪些memory文件→提取了哪些ticker"。
**来源G执行证据**：必须展示"对哪些持仓搜索了供应商/客户"。

## 防错教训存档（搜索词设计的由来）

- **NBIS教训（2026-08-13前）**：所有搜索词带"undervalued"→454%增速的NBIS被价值筛选器系统性过滤。对策：25组全部配第二视角词+D6财报催化强制"高增长"词+AI赛道多视角
- **NBIS教训2**：D2只搜泛化"AI infrastructure beneficiaries"→结果全是VRT/GEV等组件商，漏掉运营商。对策：AI 15→17个细分赛道，每赛道独立搜索词
- **"只看AI"偏差**：用户历史多次要求纠正。对策：非AI主题与AI赛道平行搜索，候选池AI≤65%
