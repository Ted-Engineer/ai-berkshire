# AVGO（Broadcom）风险维度重研 —— 李录视角（风险评估师）

- **报告日期**：2026-08-18（周二，美东盘中）
- **数据截止**：2026-08-18 13:36 ET（CNBC报价API：AVGO $381.31，当日-2.83%，开盘$384.32，最低$377.01，前收$392.43；与用户口径$381.56盘中时点一致，双源验证通过）
- **持仓**：55股 @$416.00，仓位6.9%，浮亏-8.3%；止损$346；FQ3财报2026-09-02盘后（公司官方PR 8/3确认日期）
- **事件规则（v5.4）**：FQ3 AI收入≥$16B→解禁加仓区；AI<$15B→次日减半；Q4指引<$18B或竞争实锤→减半
- **方法**：全部实时搜索（Bash curl：gnews RSS / CNBC queryly API / SEC EDGAR / 247wallst / TrendForce / CNBC报价API / Bing RSS / Mojeek / DDG），22条搜索日志见附录；关键数据双源；缺口显式标注；本报告为学习研究，非投资建议

---

## 0. 执行摘要（李录式三句话）

1. **需求与订单没有问题，钱的结构有问题**：FQ3 AI指引$16B（公司自设门槛）、RPO $164.6B、Apple 2031长约、四大云厂2026 capex合计冲向$700B+；但8/14 BofA把"表外融资工具2029年或达$370B"摆上桌，市场开始为"谁来付钱"重新定价——这正是6/4以来-15%→反弹→8/14再-6%的本质。
2. **竞争是真实的，但砸在2028年，不在9/2**：MediaTek以336G SerDes实锤拿下Google TPU v9（2027年发布），Broadcom押注的448G架构因信号完整性/功耗/散热推迟（2nm DSP产能要到2028-29）——最优质客户的第一个代际失守，时间缓冲约5-7个季度，FY26/FY27收入不受影响，FY28起承担份额侵蚀。
3. **裁决：持有6.9%，财报前不加不减，机械规则全部保留**：-8.3%浮亏处于AI半导体正常波动带内（该股6/4单日-15%），论点未被证伪；两周内信息劣势最大的时刻不做摊薄也不做逃命，把决策权交给9/2的三个数字（AI收入、Q4指引、FY27措辞）。

---

## 1. 管理层风险

### 1.1 Hock Tan关键人风险
- **年龄与依赖**：Hock Tan约73岁（1953年生），2025年薪酬$205.28M（InfotechLead 8/16），为全美最高薪CEO之一。Broadcom的BD驱动型商业模式（逐个客户谈判、逐代设计赢取）高度个人化——这是"能力型创始人折价"。
- **正面信号**：4/14主动退出Meta董事会（CNBC：在Meta扩大与Broadcom的芯片合作同时辞任董事）——清理利益冲突、聚焦主业，是治理加分项；6/5 Bloomberg访谈称AI订单是"leap of faith"，坦率而非粉饰。
- **负面/未决**：无公开继任计划（检索未果，标缺口）。李录标准：买Hock Tan的公司等于买"这个人的资本配置与谈判能力"，$64.9B债务+$29B表外担保的帝国离开此人折价20%不夸张。
- **评级：中高风险（6/10），但可被"深度团队+合同锁定"部分对冲**（Apple 2031、Meta 2029等多年期合同绑定的是公司不是个人）。

### 1.2 内部人交易（SEC Form 4一手核验）
| 人物 | 日期 | 交易 | 一手来源 |
|---|---|---|---|
| Henry Samueli（董事/联合创始人） | 6/24 | 10b5-1计划卖出23,253股@$377.61 + 33,346股@$378.51等（媒体合计约$250M，Investing.com 6/26） | EDGAR Form 4（0001104659-26-078348） |
| 同上 | 6/17-18 | 信托间赠与（G代码，非现金） | 同上 |
| Mark Brazeal（首席法务官） | 7/8 | 卖出25,000股@$379.19 | EDGAR Form 4（0001730168-26-000066） |
| Gayla Delly（董事） | 7/10 | 赠与500股（非现金） | EDGAR Form 4 |
- **判读**：Samueli减持后仍持有约36.9M股（约$140亿），减持占其持股<2%；全部为10b5-1规则化操作；12/25 CEO亦有$100M+规则减持（TradingView标题级）。**模式=例行变现，非知情人恐慌**。注意内部人卖价$377-379恰是现价区域——该位置是"内部人认可的价值带"而非出货顶。
- **评级：低-中风险（4/10）**。

### 1.3 13F机构动向
- **Q1'26（5月中披露）**：Druckenmiller的Duquesne新进AVGO 195,955股（约$60.65M），同步新进Intel、加仓Arm，构成"AI算力多元化篮子"（247wallst 8/16正文）。
- **Q2'26（8/14后披露）**：Reuters 8/15"机构对科技宠儿转向谨慎"；biggo 8/18标题"Nvidia与Broadcom遭大玩家大幅减持"（正文未取，标题级证据，标缺口）。Druckenmiller Q2动向：清Micron/Intel、买Amazon，**对AVGO处置未见报道（缺口）**。
- **判读**：聪明钱在Q1追高建仓、Q2部分获利了结——与股价从~$500高点回落一致。机构持仓拥挤度下降对9/2反而略偏正面（边际卖压释放）。
- **评级：中性（5/10）**。

---

## 2. 9/2财报风险矩阵（信息推理链）

### 2.1 证据链（18条，全部8/18实时检索）

**需求/交付侧（支持达标）**
- **E1 指引自设门槛**：6/3电话会Tan明确FQ3 AI收入"triple to $16 billion"（CNBC 6/3正文）——v5.4的$16B线就是公司指引线，非外部臆测。
- **E2 交付记录**：FY26连续超指引——FQ1 AI $8.4B（+106%，超"翻倍"承诺）；FQ2 AI $10.8B（+143%）；FQ2收入$22.19B超自定$22B指引；FQ3收入指引~$29.4B（当时LSEG共识$28.53B）（CNBC 3/4与6/3正文，双篇交叉）。
- **E3 概率市场**：Polymarket给"本季AI收入>$15B"94%、">$16B"78%（247wallst 8/14正文转述；单一详细来源，标注）。
- **E4 订单簿**：10-Q披露剩余履约义务（RPO）$164.6B，**含FQ2新签的custom AI accelerators长约**，约30%（≈$49B）未来12个月确认（SEC 10-Q一手，avgo-20260503）。
- **E5 客户capex全面上调**：Alphabet 2026 capex上调至最高$205B（Reuters 7/22 + AOL 8/18双源）；Amazon $220B（TradingView 8/12标题）；Meta最高$135B（CNBC 4/14正文）；Google Cloud积压$514B（Motley Fool 8/16标题）。
- **E6 客户合同矩阵（全部官方）**：4/7 Google TPU长约+Anthropic获3.5GW Google TPU算力（CNBC）；4/14 Meta MTIA至2029、初始1GW、2027多GW、首款2nm AI芯片（CNBC+SEC背景）；**7/6 Apple 2031多年期custom ASIC扩约（SEC 8-K一手，Item 8.01）**；6/24 OpenAI联合发布Jalapeño推理芯片（2027部署1GW+，VentureBeat/stocktitan/OpenAI官方多源标题）。
- **E7 管理层措辞轨迹**：3/4"significantly in excess of $100B in 2027"+"已锁定供应链"；6/3电话会原话"reiterate our AI semiconductor revenue guidance to be in excess of $100 billion"（FY27口径，CNBC正文）；**8/11-12 Yahoo/AOL双标题确认"Hock Tan Reaffirmed $100B Forecast, Six Customers Carry Nearly All of It"（正文未取、场合未证实→缺口）**。措辞从未软化，且六大客户（Google、Meta、OpenAI、Anthropic+2未具名，Apple 8-K暗示其中之一）结构未变。
- **E8 卖方preview**：Mizuho 8/10重申Outperform并上调估计（"AI ASIC最佳卡位+显著折价+管线扩张+宽技术护城河"，CNBC Analyst Calls正文）；Morgan Stanley 7/14重申Overweight（MediaTek担忧压制股价六个月但不改核心AI赢家地位，Moomoo标题）；BofA 8/14债务警报的同时亦承认"selloff targets the financing structure rather than underlying demand"（247wallst正文）。

**风险/结构侧（压制估值）**
- **E9 表外融资实锤**：10-Q后续事件：6/8安排"投资人伙伴"承接AI racks采购与对客户的租赁协议，Broadcom对客户租赁义务提供**5年期backstop，最大敞口$29B**（SEC一手）；BofA（Tom Curcuruto）：该工具在20GW规模下2029年中senior debt或达**$370B**，其中2027年单年发行约$150B（247wallst/Benzinga转述，双标题源）。
- **E10 竞争实锤与缓冲**：Commercial Times/TrendForce 6/23：MediaTek以336G私有SerDes拿下Google TPU v9大单；Google原拟448G架构因信号完整性/功耗/散热受阻，Broadcom押注448G"暂时失去领先地位"；448G光DSP需2nm、有意义产能2028-29才上量。v9于2027年发布→收入冲击FY28+。digitimes 6/12"Google TPU订单由MediaTek/Marvell/Broadcom瓜分"；TweakTown 6/24确认"Triggerfish 2027"；Wedbush 8/5称MediaTek EMIB良率评论"完全确认"Google封装订单转向Intel。
- **E11 光模块链传导（情绪面）**：6/16 SemiAnalysis"CPO延迟"报告单日重创美股光通信（6/23 AAOI-13%/COHR-9%/LITE-8%；6/29光子学普跌；8/10 COHR再-11.6%获利了结，247wallst正文）——AVGO是CPO核心玩家（Tomahawk 6集成CPO），光链情绪恶化会放大AVGO财报前的beta。
- **E12 内部人减持**（见1.2）：6-7月内部人在$377-379带规则化减持，无增持对冲。
- **E13 13F减持迹象**（见1.3）：Q2大机构trim。
- **E14 关键人溢价**（见1.1）：Hock Tan 73岁+$205M薪酬结构。
- **E15 技术面破位**：8/5 Tony Zhang（CNBC Pro）确认突破$400、目标$500前高、fwd P/E 20.8x vs 行业36.5x；**8/14 -6%（BofA警报日）收$390.69后，8/18盘中$381.31已跌破$400突破位**——技术结构从"突破"退回"破位"，财报前多空都在等催化剂。
- **E16 软件侧连续失速**：FQ1 infra software $6.80B（miss $7.02B）、FQ2 $7.18B（miss $7.32B，仅+9%）——VMware引擎第二曲线降速；6/3宣布转向"chips only"（放弃整机AI系统方案）=单GW内容量下降，模型变轻。
- **E17 大客户政治暴露**：3月初Trump政府将Anthropic列为"供应链风险"并指示机构停用（CNBC FQ1正文内述）——AVGO六客户之一的政策尾部。
- **E18 当日市况**：8/18 Nasdaq100 -1.53%、Nikkei -3.82%（247wallst实时行情）——全球risk-off，AVGO当日-2.83%，财报前两周波动被放大。

### 2.2 概率估计（v5.4三口径）

| 事件 | 估计 | 依据与校准 |
|---|---|---|
| **P(FQ3 AI ≥ $16B)** | **≈80%** | Polymarket 78%（E3）+ 指引达成记录（E2）+ 供给已锁定（E7）+ RPO覆盖（E4）；略上修因FY26三连超 |
| P(FQ3 AI ≥ $15B) | ≈94% | 与Polymarket一致；"次日减半"触发概率~6% |
| **P(Q4 AI指引 ≥ $18B)** | **≈70%** | 轨迹$8.4→10.8→16要求Q4环比+12.5%即$18B；FY26全年$54-56B隐含Q4 $19-21B（eciks标题$56B佐证）；扣分项：racks/租赁过渡、"bookings非即时交付"、chips-only内容量下降（E16） |
| **P(FY27维持"显著>$100B"或更强)** | **≈75%** | 措辞从未软化（E7三时点）+Apple 2031/Meta多GW/OpenAI 1GW+/Anthropic 3.5GW全部落在FY27；软化至"约$100B"≈20%（融资约束下主动降杠杆表述），撤回量化≈5% |

### 2.3 三情景（9/2盘后至T+3）

| 情景 | 概率 | 触发条件 | 价格反应 | 目标带 |
|---|---|---|---|---|
| **A 强验证** | **30%** | AI≥$16.5B（超指引3%+）；Q4指引≥$19B；FY27上调或给出>$120B量化；软件企稳 | +12%~+20% | **$427-458** |
| **B 符合预期** | **50%** | AI $16.0-16.5B；Q4 $17.5-19B；FY27原样重申">$100B"；软件继续温吞 | -3%~+6% 宽幅震荡 | **$370-404** |
| **C 失速** | **20%** | AI<$16B（其中<$15B约6%）或Q4指引<$18B或FY27措辞软化/融资警报升级 | -10%~-18% | **$313-343**（触及$346止损区上沿） |

期望收益≈0.30×(+15%)+0.50×(+1%)+0.20×(-14%)≈**+2.2%**——微正、左尾肥（20%概率-14%）。这就是"高事件风险+浮亏"持仓的数学本质：**赔率不差，但分布不对称地依赖9/2的三个数字**。

### 2.4 赔率行动映射（v5.4三档）——"-8.3%浮亏+财报两周前"的持仓裁决

- **档1｜持有不加不减（现价$381执行）**：论点未证伪（E1-E8全数在线），浮亏来自情绪与信用结构重定价（E9/E11/E15）而非需求破坏；6/4单日-15%的波动带内，-8.3%不构成信息。财报前两周是信息劣势最大的窗口——**李录：不懂的钱不赚，等不起的钱不赌**。
- **档2｜解禁条件不放宽**：9/2 AI≥$16B仅"解禁"，**真正加仓需同时Q4指引≥$18B**（双条件防"达标即巅峰"）；达标后右侧加仓上限7.5-8%，留一半子弹等Q4兑现。仅AI达标而Q4<$18B→维持6.9%不加。
- **档3｜机械防御（全部保留，不辩论）**：AI<$15B→次日减半（P≈6%）；Q4<$18B→减半；"竞争实锤"定义收窄为**当期代际订单公开转移**（TPU v8被夺/OpenAI或Meta公告转单）；TPU v9属已知前瞻风险（2028年兑现），不触发档3。收盘价破$346→次日减半。
- **裁决**：**维持55股/6.9%过财报**。不因浮亏行动（那是成本锚定偏差），不因FOMO抢跑（那是赌博），用事件规则替代预测。

---

## 3. 信用传导风险（表外/客户融资）

- **结构拆解（SEC一手）**：6/8安排=investor partner购买"基于Broadcom定制AI加速器的AI racks"+对客户的租赁协议；Broadcom对客户租赁义务5年backstop，**最大敞口$29B**；违约救济=承接租赁或出售racks。本质：**类卖方信贷——把硬件"卖"给靠租赁杠杆获取算力的客户，收入前置、风险后置**。
- **规模推演（BofA情景，247wallst转述）**：20GW规模下2029年中vehicle senior debt $370B、2027年单年发行$150B——AVGO自身不背主债务，但backstop或有敞口若按首单比例（$29B对应首期GW数）外推，量级可达数百亿至千亿级。
- **资产负债表现状（5/3/26）**：现金$19.6B；短债$2.25B+长债$62.66B=总债务$64.9B，净债≈$45B；**应收$10.8B（较年初+51%）、存货$4.3B（+91%）**——营运资本占用陡升，是racks模式"先发货后收款"的账面印记；FQ2净利$9.31B（+88%），FCF转化率约50%（Zhang 8/5）。
- **系统性同构**：NVDA与Blackstone/Apollo的$500B融资计划（同日BofA称其担忧"overblown"却点燃AVGO卖压——市场在挑软柿子）；NVDA为OpenAI俄亥俄数据中心backing $105B融资；四云厂capex $135-220B——**"循环融资"已成8月华尔街主题词**（BofA 8/10 NVDA点评原文提及circular financing concerns）。
- **李录判读**：FY26内可控（投资级评级+现金$19.6B+季度FCF约$8-11B），**2027-28是真考场**：若AI收入增速低于债务扩张速度、或任一大客户租赁违约，评级-估值双杀会叠加情景C。收确认认质量：AR+51%与存货+91%必须在FQ3财报里被解释，否则按收入质量折价处理。**评级：FY26低（3/10）/ FY27-29中高（7/10）**。

---

## 4. 竞争风险量化（MediaTek时间缓冲）

- **已发生（实锤级）**：TPU v9（Triggerfish，2027年上市）大单→MediaTek（336G私有SerDes，Commercial Times 6/23）；2025/12已报道MediaTek获两代Google TPU订单（TechNode）；Google封装或转Intel（Wedbush 8/5，Moomoo标题）；digitimes 6/12："MediaTek、Marvell、Broadcom瓜分Google TPU"。6/4 biggo标题量化："Broadcom承认Google旁落，市值蒸发$286B"（正文未取，标题级）。
- **根因（能力面警示）**：Broadcom押注448G SerDes下一代架构，因信号完整性/功耗/散热延期；448G光DSP需2nm、有效产能2028-29才上量——**一次真实的技术路线踏空**，证明护城河在SerDes代际切换处存在被跨越的缝隙。
- **时间缓冲量化**：v9于2027年发布、2028年才放量。Broadcom在手：TPU v7/v8（2026当期）+Anthropic 3.5GW（经Google TPU）+OpenAI Jalapeño（2027 1GW+）+Meta MTIA 2nm（合同至2029）+Apple（至2031）+未具名第6客户。**FY26/FY27 Google口径收入不受v9影响；FY28起Google份额或从~满额降至50-60%**。粗算：若FY28 Google相关AI收入~$40B、份额-30pct，收入风险≈$12B，约占FY28E AI总收入10-12%。
- **对冲证据**：Counterpoint（1/26）：2027年Broadcom仍占custom AI芯片60%份额、ASIC出货2027年3倍于2024；Marvell同期在PCIe SerDes领先Broadcom一个cadence（TrendForce 3/13）——竞争是三强常态而非单点塌方。
- **评级：当期低（4/10）/ FY28+中高（7/10）；缓冲5-7个季度**。

---

## 5. 10年确定性（李录框架）

**确定的部分**：
- 生意本质="AI时代最深的接口IP库+SerDes/封装工程能力+大客户切换成本"，Apple 2031/Meta 2029长约是十年可见度的法定锚；
- 双引擎：AI半导体（FY26E $54-56B，+180%）+基础设施软件（$28B+/年run-rate，VMware现金流牛）；
- FCF机器（~50%转化）+回购授权$10B+股息$0.65/qtr；
- ASIC结构性渗透（云厂去NVDA单源依赖是十年趋势，Broadcom是最大受益者）。

**不确定的部分**：
- 客户是六个比Broadcom更强势的对手——自研+双源是它们的既定策略，TPU v9已示范；
- SerDes代际（448G失手一次）与先进封装路线是可再生风险；
- 关键人：Hock Tan之后是否还是Broadcom？
- 融资周期：$370B表外工具把AVGO与2027-29信用周期捆绑；
- 政策：Anthropic案例显示大客户政治暴露可在一周内反转。

**结论：确定性7/10**——"能力护城河"而非"品牌/网络效应护城河"，五到七年难被替代，十年维度必须接受至少一次代际份额丢失与一次信用周期冲击。以$381计，fwd P/E约20.8x（行业36.5x）已在为这些风险付折扣，10年持有的赔率成立，但需以"仓位上限+事件规则"承认不可知部分。

---

## 6. 证伪线与仓位终审

### 6.1 $346止损评估
- 现价$381.31距$346为-9.3%；恰处情景C区间（$313-343）上沿——**保留**。
- 执行细则（终审）：**以收盘价确认**（避免盘中插针，如8/18日内低$377距止损仅8%）；若因系统性暴跌（非AVGO特有消息）触及，允许T+1复核一次，滑点容忍2%，最多一次，不做第二次"再看一天"。
- 李录注：$346本质是"论点证伪的价格投影"——AI节奏破位+融资恶化+竞争当期化的三重叠加区，不是任意数。

### 6.2 事件规则终审
1. **AI<$15B→次日减半**：保留（P≈6%）。无辩论、无条件、不引用"长期"。
2. **AI≥$16B→解禁加仓区**：保留但**加双条件**——真正加仓需Q4指引≥$18B同步达标；否则只解禁不加（防"达标即巅峰"，FQ2就是前例：AI +143%照样-15%，因为预期结构变了）。
3. **Q4指引<$18B或竞争实锤→减半**：保留；"实锤"定义收窄为**当期代际订单公开转移证据**（v8被夺/客户公告转单/管理层在电话会确认当期份额损失）。TPU v9（2027产品）与Wedbush封装评论不构成触发。
4. **FY27措辞监视（新增建议）**：若9/2电话会把"significantly in excess of $100B"降格为"约$100B"或撤回量化，即使AI/Q4达标，也不加仓并下调目标价15%——措辞变化是Tan式管理层的先行指标（12/25"AI翻倍"、3/26"$100B+"、6/26重申，措辞链条从未回退过，一旦回退即是信号）。

### 6.3 6.9%仓位终审
- **维持55股过9/2，财报前零操作**。理由：期望+2.2%微正但左尾-14%@20%——这个分布下"加仓=赌财报、减仓=交税给波动"，持有是唯一不依赖预测的选择。
- 事件后重构：情景A→右侧加至7.5-8%（分两笔，首笔不超半）；情景B→6.9%不动，等Q4；情景C→机械减半至~3.5%或止损离场，不抄底。
- **综合风险评分：6.5/10**（事件风险8/10；信用结构FY27+视角7/10；竞争当期4/10、远期7/10；关键人6/10；10年确定性7/10；当期财务稳健3/10低风险）。

---

## 附录A：缺口标注（诚实清单）
1. **期权IV未获取**：Yahoo options API返回401 Invalid Crumb（被拦），无法读取9/2到期IV/straddle隐含变动——以Polymarket概率（94%/78%）+COHR链put/call比作情绪替代，**AVGO自身期权定价缺口**。
2. **8/11 $100B重申正文未获取**：仅Yahoo（8/11 08:01 GMT）与AOL（8/12）双标题+摘要级确认；发言场合未证实。
3. **Q3卖方精确共识EPS/收入**：Seeking Alpha/Investing.com付费墙；以6/3时点LSEG共识（收入$28.53B）+公司指引替代。
4. **Duquesne Q2'26对AVGO处置**：qz.com正文未读；biggo 8/18"大玩家减持"仅标题级。
5. **digitimes/biggo正文**：digitimes付费墙；biggo未取得URL。
6. **Hock Tan继任计划**：公开检索无果。
7. **EDGAR 13F全量扫描**未做（以Reuters/247wallst报道替代）。
8. **gnews跳转解码不可用**（batchexecute接口变更）——以出版商直达URL+CNBC queryly API绕过。
9. $370B/20GW情景为BofA单一分析师推演（Benzinga标题为第二源），非公司指引。

## 附录B：双源验证表（关键数据）
| 数据 | 源1 | 源2 |
|---|---|---|
| 现价$381.31/-2.83% | CNBC报价API（8/18 13:36ET） | 用户给定$381.56（盘中时点差） |
| FQ3 AI指引$16B | CNBC 6/3正文 | 247wallst 8/14正文；CNBC Pro 8/5 |
| FQ2 AI $10.8B（+143%） | CNBC 6/3正文 | 247wallst 8/14/8/16正文 |
| $29B backstop | **SEC 10-Q一手**（Note 11后续事件） | 247wallst 8/14（引BofA） |
| RPO $164.6B | **SEC 10-Q一手** | —（一手权威，单源可接受） |
| 财报日9/2 | 公司官方PR标题（Yahoo 8/3） | 用户v5.4给定 |
| Alphabet capex $205B | Reuters 7/22标题 | AOL/Fool 8/16-18 |
| Meta 1GW/合同2029 | CNBC 4/14正文 | CNBC 4/15分析文 |
| Apple扩约至2031 | **SEC 8-K 7/6一手** | —（8/18当日新闻未见跟进报道，一手权威） |
| MediaTek TPU v9/336G | TrendForce 6/23正文（引Commercial Times） | TweakTown 6/24；digitimes 6/12标题 |
| 内部人减持明细 | **SEC Form 4一手**（6/24、7/8） | Investing.com 6/26标题 |
| Polymarket 94%/78% | 247wallst 8/14正文 | —（单一详细来源，已标注） |

## 附录C：搜索日志（22条，全部2026-08-18执行）
```
13:29 ET | v54-AVGO-risk/env | date baseline confirmed (2026-08-18 US intraday)
13:35 ET | v54-AVGO-risk/gnews | Broadcom AVGO earnings preview September
13:35 ET | v54-AVGO-risk/gnews | Broadcom AI revenue quarter
13:38 ET | v54-AVGO-risk/gnews | Hock Tan broadcom
13:38 ET | v54-AVGO-risk/gnews | Broadcom insider selling Form 4
13:40 ET | v54-AVGO-risk/gnews | Broadcom MediaTek custom chip competition
13:44 ET | v54-AVGO-risk/bing-rss | Hock Tan Reaffirmed $100B article URL resolve (低相关结果)
13:48 ET | v54-AVGO-risk/cnbc-queryly | Broadcom FQ2 June weak software sales AI unchanged
13:48 ET | v54-AVGO-risk/cnbc-queryly | Broadcom Hock Tan $100 billion
13:52 ET | v54-AVGO-risk/cnbc-queryly | Meta gigawatt custom chips Tan board
13:55 ET | v54-AVGO-risk/sec-edgar | AVGO submissions (Form4/10-Q/8-K index)
14:02 ET | v54-AVGO-risk/gnews | Broadcom optical transceiver selloff Coherent
14:15 ET | v54-AVGO-risk/mojeek | Hock Tan Reaffirmed $100B URL resolve (空结果)
14:20 ET | v54-AVGO-risk/sec-edgar | 10-Q avgo-20260503 融资工具/backstop条款
14:30 ET | v54-AVGO-risk/sec-edgar | Form 4 x3 内部人明细 (6/24,7/8,7/10)
14:35 ET | v54-AVGO-risk/curl-yahoo-opt | AVGO options IV → 401 Invalid Crumb 被拦（缺口）
14:35 ET | v54-AVGO-risk/gnews | Alphabet capex 2026 raises
14:35 ET | v54-AVGO-risk/gnews | MediaTek TPU Google orders
14:40 ET | v54-AVGO-risk/trendforce | MediaTek TPU v9 336G SerDes 正文
14:46 ET | v54-AVGO-risk/cnbc-quote-api | AVGO live quote $381.31@13:36ET
14:50 ET | v54-AVGO-risk/gnews | Broadcom earnings date September 2 (官方PR确认)
14:50 ET | v54-AVGO-risk/gnews | Broadcom 13F institutional Q2
14:50 ET | v54-AVGO-risk/gnews | Broadcom OpenAI gigawatt custom accelerator
14:55 ET | v54-AVGO-risk/curl-probe | openai.com(000失败)/tradingkey(410) → 缺口
15:00 ET | v54-AVGO-risk/sec-edgar | 8-K 7/6 Apple 2031 + 6/11,6/18债务tender
```

*本报告为AI Berkshire投研学习用途，非投资建议。李录视角为方法论模拟。*
