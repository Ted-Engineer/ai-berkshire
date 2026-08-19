# 瓶颈猎手 — AI全链路瓶颈扫描 2026-08-19（来源D · 第5班增量更新）

**执行方式**：bottleneck-hunter；**18次curl搜索**（16次gnews + 2次brave，全部记录于 `.claude/.workflow/search-log.txt`，标签 `819b3-D-bottleneck`）+ 美股14只收盘估值快照（fetch_quotes.py + stockanalysis.com）+ 台股5只8-18收盘估值（tools/twstock_data.py，FinMind）+ financial_rigor.py红灯验算
**数据截止**：美股=**2026-08-18收盘**；台股=2026-08-18收盘；新闻增量=8-16～8-19，四个专项变量回溯至各自源头日期（3月～8月，文中逐一标注）
**与8-18基线关系**（`AI全链-bottleneck-20260818-v54.md`）：增量更新，8-18结论仅作对比基线、本轮全部重验。基线六环节评级：EML S / InP S / HBM S / CoWoS A+ / ABF S / 玻纤 A-。**本轮核心裁决：六环节评级全部维持，无一升降级**；增量在于四个需求侧/路线侧新变量的传导判定 + InP证据链显著加固 + 电力链人力卡点新立。
**定位声明**：学习与研究用途，非投资建议；低置信结论已标注。

---

## 一、四个专项变量核查（本轮任务核心）

### 1.1 TSMC联手景硕推EMIB-like封装（源头7-30，The Information经Wccftech/TechTimes多源确认）

**事实链**：
- TSMC内部代号 **"quasi-EMIB"** 的新封装项目，与**景硕Kinsus（3189.TW）**合作开发，克隆Intel EMIB路线：有机基板内嵌局部硅桥，取代CoWoS-L的整面RDL中间层（Wccftech 7-30，源头The Information）
- Wccftech原文承认："**CoWoS-L capacity sold out through 2026 and well into 2027, lead times stretching to 78 weeks in some cases**"——TSMC被迫开第二条路线防Intel EMIB抢单
- Chosunbiz 8-03：TSMC以EMIB-like在CoWoS紧张下"retain AI chip orders"；BigGo 7-30：消息日景硕股价+7.6%
- 旁证：Microsoft Maia 300（Intel 18A+EMIB）寻求30万片封装单位、NVIDIA占TSMC封装队列60%（TechTimes 8-11）——封装争夺战从"产能"升级为"路线"

**瓶颈判定**：
1. **CoWoS A+维持且偏紧**：78周交期+售罄至2027是"紧"的强证据；良率98-99%、2029年14x reticle目标（TradingKey 8-13）、ASE SPIL斗六NT$1000亿新厂2028投产（TrendForce 8-12）是"松"的中期证据——与8-18"2027实质缓解"判断一致，不动
2. **景硕3189角色升级但估值透支**：quasi-EMIB载体=BT载板新需求曲线。但PER 160.48、PBR 10.25、52周高939现价865（概念已定价）→ **红灯维持，暂不追踪，观察名单**
3. **对TSMC的双重含义**：短期确认封装霸主地位（对手排队），长期是护城河第一道裂缝——第一次TSMC"克隆"别人而非被克隆

### 1.2 Google收购Intersect Power垂直整合"kills PPA era"（源头3月完成，6月首项目落地）

**事实链**：
- 3-10/3-11完成$4.75B收购（Energy-Storage.News/pv-tech/TPG公告）；TPG售后再设IPX Power作为独立IPP
- 5-05 Substack专题："Why Google's Intersect Acquisition Kills the PPA Era"——发电商从"卖电给hyperscaler"变为"hyperscaler自持发电资产"
- 6-04/6-05：首个收购后项目德州**Meitner Energy Center**开工：数据中心与1GW+能源colocated（DCD/Industrial Info/Latitude Media）

**瓶颈判定**：
- **物理层不变**：自建电源仍需燃机/变压器/GSU/开关设备——S-P1重型燃机S、S-P2变压器S维持且逻辑加固（自建=绕过电网排队，设备需求前置）
- **商业层结构性利空IPP/PPA中介**：hyperscaler垂直整合电力后，第三方PPA与IPP的"电力中介溢价"长期被压缩。8-18基线"电力IPP A-（已降级）"维持，且标注**逻辑侧继续恶化**
- 新信号：H&MV Engineering估值€1.4B——**HV高压工程师稀缺被称为"$1T AI数据中心建设的阻碍"**（TechTimes 8-11）。电力链瓶颈正从"设备"向"设备+工程服务+人力"扩散，S-P2的持续性获新支撑

### 1.3 Meta Compute卖冗余算力→对neocloud/IPP需求的传导（源头7-01，8月持续落地）

**事实链**：
- 7-01：Meta宣布云基础设施业务变现冗余AI算力，当日股价+9%（CNBC/Bloomberg/Reuters）
- 8-07 MarketScale：**Meta挖角AWS副总裁Dave Brown**（EC2算力核心人物）、与**Anthropic**洽谈合作——"cloud push becomes real"
- 8-06 tech-insider：Meta Cloud vs AWS/Azure竞争格局分析；富途7-01：Meta言论当日曾拖累AI硬件股，但华尔街共识"不代表算力过剩，是资本纪律"

**瓶颈判定（传导链拆解）**：
1. **对neocloud（CRWV $93.17/NBIS $248.43）**：hypserscaler自建电力（变量2）+自卖冗余算力（变量3）=两头挤压"算力中介"商业模式。neocloud的稀缺性叙事从"买不到GPU"降级为"服务差异化竞争"。**这是需求预期变量，不改变当前GPU/HBM物理售罄状态**（2027 HBM售罄证据未松动）
2. **对物理瓶颈链**：若Meta/SoftBank（7-02，10GW入美）等大规模转售冗余，边际GPU供给增加→2027-28新增供给曲线左移→S3/S4的解除时点可能提前。**判定：观察信号，暂不据此调级**——HBM 2027售罄（8-04/05三源）与Meta卖冗余并存，说明当前是结构性错配（大客户冗余≠市场过剩）
3. 反向验证：若算力真过剩，Meta不会同时维持2026年~$100B+级capex并挖AWS算力一号人物建云业务——自用转售是资本效率优化而非退出信号

### 1.4 OpenAI CFO收入评论（7-29"7月年化超Q2总量"→8-14企业收入反超消费者+$40B ARR）

**事实链**（时间线完整核实）：
- 7-29：CFO Sarah Friar告诉员工，**7月单月年化收入已超过整个Q2总量**（CNBC 7-29/30）
- 8-14闭门投资者会议（TechTimes 8-15转述）：**企业收入首次超过消费者收入**（年初60/40→8月交叉），比OpenAI自己"2026年底达平价"的指引**提前约两个季度**
- 数字：**$40B年化ARR**，7月单月环比+20%、企业客户数+32%；年初$20B→8个月翻倍；广告接近$1B run rate；1月时ARR $20B（Friar确认）
- 资本面：3-31完成$122B融资@投后$852B；IPO机密招股书5月提交、6-8公开确认，GS/MS/JPM牵头；同期两名企业业务高管离职

**瓶颈判定（需求端最强对冲证据）**：
- 8-18暴跌两大归因之一是"AI支出数学检验"（Anthropic ARR $65B miss vs $80B口径）。OpenAI $40B ARR+8个月翻倍+企业交叉证明**AI收入端在加速而非见顶**——Anthropic是单一公司预期差，非行业性miss
- **传导逻辑**：OpenAI ARR加速→Stargate等capex承诺的回收可见度提升→2027年hyperscaler/neocloud capex下修风险下降→S/A级瓶颈（InP/EML/ABF/HBM）的持续时间获得需求端支撑
- 注意量价背离信号延续（8-18已标注）：买家转向"单位智能成本"，"tokenmaxxing"结束——长期利好推理效率方向，中性偏空"无差别算力堆料"

---

## 二、瓶颈地图增量更新（vs 8-18基线：六环节全部维持）

| # | 环节 | 评级 | 8-19新证据（日期） | vs 8-18基线 |
|---|------|------|--------------------|-------------|
| S1 | **EML/CW激光器** | **S 维持** | ①**Lumentum CEO公开警告：InP短缺可能比存储芯片更严重**（BigGo 8-03）②AAOI因"EML短缺免疫"（垂直整合）被单独定价（TechTimes 8-04）③EML+CW-DFB月产能2026年超5000万只的军备竞赛口径（BigGo 6-04） | **维持S**。下游CEO亲自确认上游短缺等级 |
| S2 | **InP衬底+铟** | **S 维持（证据链显著加固）** | ①InP价格Q4'26拟再涨10%+创纪录，买家"cash-rich but empty-handed"（BigGo 8-17）②XenoSpectrum 8-17：InP衬底=AI光通信供应风险、买家签长约锁供给 ③SCMP 8-17封面级报道"Next silicon?"：AI数据中心材料价格飙升+中国供应紧缩 ④中国出口管制推InP价+250%口径（BigGo 6-11）⑤AXTI周一（8-17）领跑光学股（24/7 Wall St 8-17）；⑥FCC禁令若落地切60%光模块供应且西方替代需中国铟（TechTimes 8-05，低置信维持） | **维持S**。本轮证据最密集的环节：价格上涨+长约锁货+CEO警告+地缘挤压四线并进 |
| S3 | **HBM/DRAM** | **S 维持** | ①三大厂2027全部售罄、无新买家名额（TweakTown/TechPowerUp 8-04、SeekingAlpha 8-05）②RAM价格+63%、DDR5单颗创$20（tech-insider 8-06）③DDR5一年5倍结构分析（XenoSpectrum 8-17）④市场端"售罄中下跌"悖论延续：MU 8-18收$940.76（+0.7%） | **维持S**。供给侧零松动；Meta Compute变量=2027-28供给曲线的远期观察点 |
| S3' | NAND（拆出） | A- 维持 | 无新增证据 | 维持 |
| S4 | **CoWoS先进封装** | **A+ 维持** | 紧侧：①CoWoS-L售罈至2027、交期最长78周（Wccftech 7-30）②MSFT Maia 300寻30万单位、NVDA占队列60%（TechTimes 8-11）。松侧：③良率98-99%、2029目标14x reticle（TradingKey 8-13）④ASE SPIL斗六NT$1000亿厂2028运营（TrendForce 8-12）。路线侧：⑤**TSMC-景硕quasi-EMIB=第三条封装路线开建**（The Information 7-30） | **维持A+**（8-18已从S-降级）。quasi-EMIB既确认紧度（被迫开新路）又加速多元化（降级逻辑再确认）——双向证据同日出现，A+正好 |
| S5 | **ABF载板/积层膜** | **S 维持** | ①味之素95%份额+30%涨价+缺口延至2027（Wccftech 5-11、BigGo 5-14链延续）②TSMC 8-11点名ABF为"下一个瓶颈"（8-18已录）③味之素6-16宣布ABF大幅扩产（디지털투데이）——供给响应已启动但2027-28才落地 | **维持S**。注意：quasi-EMIB若放量，载体是BT载板而非ABF——ABF垄断地位存在远期路线风险（2028+），标注不调级 |
| A+1 | MOCVD/外延设备 | A+ 维持 | VECO 8-18收$50.91（+$0.35），市值$3.11B；**8月底Q2财报=订单连续性裁决点**（InP Q4涨价10%为订单前瞻正信号） | 维持 |
| A+2 | 液冷/CDU/冷板 | A+ 维持 | 双鸿3324 PER 22.56=一年区间最低端维持（8-18收盘978 NT$）；FinMind月营收数据仅至2026-02（**数据缺口**：7月+117%口径为8-17新闻转述，未获FinMind独立确认）；9/10八月营收披露=升级/证伪节点 | 维持 |
| A+3 | 特殊玻纤布/低Dk电子布 | A- 维持 | 证据链仍为4-5月（TrendForce 4-29、BigGo 4-17、台湾玻璃扩产5-12）；BT载板+玻纤布涨20%（8月口径延续）。8月无新松动信号 | 维持 |
| A1 | 高端MLCC | A 维持 | 无增量 | 维持 |
| S-P1 | 重型燃气轮机 | S 维持 | 无直接增量；Google-Intersect colocated自建模式（变量2）间接强化燃机需求逻辑 | 维持 |
| S-P2 | 变压器/GSU/开关设备 | **S 维持（+人力卡点新立）** | ①交期最长4年、美买家抢进口产能（pv magazine/Reuters 5-11链）②TD Economics 7-16：供应约束将拖慢美国AI建设 ③**新增：H&MV Engineering估值€1.4B，HV工程师稀缺被称"$1T建设阻碍"（TechTimes 8-11）——瓶颈从设备扩散至工程服务/人力** | 维持S。人力维度为本轮新增观察点 |
| — | 电力IPP/容量市场 | A- 维持（逻辑侧恶化） | Google-Intersect垂直整合（3月）+Meta自建自卖（7月）：hyperscaler"自持电力+自售算力"两头压缩IPP/neocloud中介价值 | 维持A-，**不排除下次扫描降级** |

**新瓶颈扫描（8-16～8-19窗口）**：未发现未跟踪的新材料/设备瓶颈类别。TSMC剩余瓶颈名单（存储+ABF）口径未变，地图继续从"封装产能"向"上游材料+电力工程"迁移。

### 瓶颈解除时间表（增量更新）

| 瓶颈 | 解除时点 | 本轮增量依据 |
|------|---------|--------------|
| S1/S2 EML/InP | 2027末-2028（维持） | LITE CEO"比存储更严重"+Q4再涨10% → 时点无提前迹象，甚至更紧 |
| S3 DRAM/HBM | 2027售罄后2028松动（维持） | 三厂2027售罄8月初三源再确认；Meta卖冗余=2027-28远期观察点 |
| S4 CoWoS | 2026底缺口10%、2027实质缓解（维持） | SPIL 2028新厂+良率98%+quasi-EMIB多元化=缓解路径清晰但不在2026 |
| S5 ABF | 2027-28（维持） | 味之素扩产已启动（6-16）但落地2027-28；quasi-EMIB路线风险在2028+ |
| A+2 液冷 | 2026底VRT产能翻倍（维持） | 无新供给信号；双鸿8月营收9/10验证 |
| S-P2 变压器 | "2028年前不会正常化"（维持） | +HV工程师稀缺：人力维度或使正常化更晚 |

---

## 三、机会看板排名表（强制估值检查完成 · 8-18收盘价）

美股=stockanalysis.com（市值/TTM收入/PE/fPE）+fetch_quotes.py收盘价；台股=FinMind 8-18收盘；汇率NT$31.5/US$。

| 排名 | 公司 | 代码 | 市值 | 年收入(TTM) | PS | PE / fPE | 瓶颈环节 | 评级 | 收入增速 | 信号 | 估值灯 |
|------|------|------|------|------------|-----|----------|---------|------|---------|------|--------|
| 1 | **Fabrinet** | FN | $17.29B | $4.64B | **3.73** | 37.0 / **26.5** | 1.6T光模块代工 | S1 | +35.7% | ★★★★ | **绿**（8-18收$482.59，较盘中低点+2.3%企稳） |
| 2 | **Amkor** | AMKR | $13.63B | $7.46B | **1.83** | 24.6 / **20.1** | OSAT CoW三巨头 | S4(A+)/S5 | +17.9% | ★★★★ | **绿**（CoW外溢+SPIL NT$1000亿扩产=行业景气再确认） |
| 3 | **Veeco** | VECO | $3.11B | $0.68B | **4.56** | 137 / **21.1** | InP MOCVD设备 | A+1 | -2.5%（TTM） | ★★★★ | **绿**（InP Q4涨价10%=订单前瞻正信号；8月底Q2财报裁决） |
| 4 | **双鸿 Auras** | 3324.TW | $2.89B | ~$1.05B(年化估) | ~2.8(估) | **22.56**（一年新低维持） | 液冷冷板/CDU | A+2 | +62~117%（新闻口径） | ★★★★ | **绿**（台股备案；FinMind月营收仅至2月，标注） |
| 5 | **Coherent** | COHR | $60.01B | $7.12B | 8.43 | 74.4 / **32.8** | EML激光双寡头 | S1 | +22.5% | ★★★ | **黄**（TAM 171.5%检验维持，见验算；收$306.43在挂单$280-300上沿之外） |
| 6 | Micron | MU | $1.06T | $90.27B | 11.8 | 22.8 / 7.0 | HBM/DRAM | S3 | +167% | ★★★ | 黄（**挂单$780-850纪律不变，$940.76不追**） |
| 7 | 奇鋐 AVC | 3017.TW | $37.6B | ~$6.7B(年化估) | ~5.6(估) | 40.46 | 液冷/机壳 | A+2 | +66%（6月口径） | ★★★ | 绿-黄 |
| 8 | TSMC | TSM | $1.93T | $139.6B | 13.8 | 27.7 / 19.1 | CoWoS/2nm/quasi-EMIB | S4(A+) | +30.6% | ★★★ | 绿-黄（quasi-EMIB=护城河裂缝的早期对冲信号；组合持有，$390/365挂单纪律不变） |
| 9 | 欣兴 Unimicron | 3037.TW | $59.6B | ~$5.7B(估) | ~9(估) | **76.23** | ABF载板第1-2 | S5 | +36%（6月口径） | ★★★ | 黄偏高 |
| 10 | AAOI | AAOI | $11.11B | $0.60B | 18.6 | 亏 / 57.1 | 垂直整合光模块 | S1侧翼 | +61.8% | ★★ | **红**（亏损+PS>15+fPE 57） |
| 11 | Lumentum | LITE | $78.34B | $3.01B | 26.0 | 亏 / 40.4 | EML份额第1 | S1 | +83.2% | ★★ | **红**（TAM 223.8%红灯维持，见验算） |
| 12 | **AXT** | AXTI | $5.28B | $0.126B | **42.1** | 1148 / **51.9** | InP衬底第1（美系） | S2 | +45.8% | ★★ | **红**（一年+5485%；InP最纯正美股标的但严重透支，见验算） |
| 13 | 景硕 Kinsus | 3189.TW | $14.6B | NT$470亿级(估) | ~10(估) | **160.48** | ABF/BT载板+**quasi-EMIB载体** | S5/S4 | +36%（7月口径） | ★★ | **红**（逻辑升级但PER 160已定价；观察名单） |
| 14 | 南电 | 8046.TW | $25.7B | NT$800亿级(估) | ~8(估) | **146.3** | ABF载板 | S5 | +50%（7月口径） | ★★ | 红-黄边缘 |

### 红灯验算（financial_rigor.py，8-18收盘口径）

- **AXTI**：PS = 5280/125.51 = **42.07**（>30红线且增速45.8%<100%不豁免）→ 红灯规则2触发；10%年化检验：需2036年净利$548M，从$3.88M起步需**年均+68.9%×10年**——不可达成；市值$5.28B ÷ InP衬底TAM（估$0.5-1B）≈ **5-10倍TAM** → 远超20%红线。**红灯确认，信号封顶★★**。注：InP逻辑本身是本轮最强，AXTI是"正确瓶颈+错误价格"的教科书案例
- **LITE**：市值/TAM = 78340/350（2026E光学TAM $35B）= **223.8%** → TAM红灯维持；增速83.2%<100%不豁免PS规则 → 双红。CEO警告（InP比存储紧）对其是基本面利好，但当前价已透支3年以上
- **COHR**：60010/350 = **171.5%** → 黄灯维持（盈利+PS 8.43+DC增速对冲）；$280-300挂单纪律不变
- **FN**：10%年化要求下，需10年后净利$1.79B（10年25x退出），从TTM $473M起步需CAGR **14.3%**——FY26 EPS +39%背景下可达成 → **绿灯**
- **AMKR**：同口径需净利CAGR ~9.8%——恰好贴线，但PS 1.83为全表最低+OSAT行业景气（SPIL扩产）提供超额概率 → 绿灯维持
- **景硕3189**：PER 160.48>80红线+PBR 10.25；quasi-EMIB催化剂7-30已兑现（当日+7.6%），当前865接近52周高939 → "利好出尽+高估值"组合，红灯维持
- 台股载板三雄（欣兴76/南电146/景硕160）：估值已计入2027-28盈利兑现，**全部不追**

---

## 四、一页纸摘要（Top 3 入口 + 2 维持 + 1 新观察）

🎯 **Fabrinet（FN）— S1链绿灯入口维持，暴跌后首日企稳**
- 8-18收$482.59，较盘中低点$471.66回升2.3%；PS 3.73/fPE 26.5为光链最低档
- 本轮增量：OpenAI $40B ARR加速（变量4）直接强化其大客户（Cisco/NVDA/Amazon）的2027订单可见度
- 10%年化退出检验需净利CAGR 14.3%——绿灯；风险：四大客户58%集中度
- 结论：**维持8-18"值得深入研究"，NVDA财报前为研究窗口**

🎯 **Amkor（AMKR）— PS 1.83+CoW外溢，行业景气再确认**
- SPIL斗六NT$1000亿扩产（8-12）+MSFT Maia 300寻30万单位（8-11）：先进封装需求池在TSMC之外继续膨胀
- TTM收入上修至$7.46B（+17.9%）；PE 24.6/fPE 20.1，全表唯一"双绿"纯度
- 结论：**维持低估判定，$54.84可分批**

🎯 **Veeco（VECO）— InP S2环的设备杠杆，催化剂在8月底**
- InP Q4'26再涨10%+买家锁长约（8-17）→ InP厂商扩产意愿强化 → MOCVD订单前瞻转正
- fPE 21.1维持绿灯；8月底Q2财报订单簿=加仓/放弃的单一裁决点
- 结论：**观察名单维持，财报前不动**

🎯 **Micron（MU）— 纪律执行**：$940.76 vs 挂单$780-850，不追（fPE 7.0为峰值EPS外推的周期陷阱特征）

🎯 **Coherent（COHR）— 黄灯纪律**：$306.43高于$280-300挂单区间，等回调；TAM 171.5%未过线

🔍 **景硕（3189.TW）— 新增观察（红灯，不买）**：quasi-EMIB是本轮唯一"角色质变"的标的（BT载板从配套变载体），若回调至PER<100且TSMC路线2027年放量验证，可重估。当前160倍PER透支

---

## 五、反向验证（芒格式否定）

| 反向问题 | 回答 | 置信度 |
|---------|------|--------|
| quasi-EMIB是不是CoWoS利空？ | 表面是（替代路线），实质确认了紧度（78周交期逼出来的）。真正受损的是ABF的远期垄断（EMIB-like用BT载体）——2028+风险，2026-27无影响 | A-（单源The Information+多转述） |
| OpenAI $40B会不会是IPO前的美化口径？ | 可能有选择性披露（闭门会议、匿名转述、两名高管同期离职），但1月$20B为Friar本人公开确认，8个月翻倍与Q2超Q1的轨迹自洽；且The Information/CNBC/TechTimes/qz多源独立 | B+ |
| Meta卖算力会不会引发算力通缩、终结瓶颈链？ | 当前证据不支持：HBM 2027售罄未松动；Meta自己还在capex扩张+挖AWS算力一号人物。但2027-28供给曲线左移是真实远期风险——已列为S3观察点，不调级 | B |
| Google自建电力会不会反而增加IPP需求（自建也要买电）？ | colocated模式下Google是设备买家不是电力买家；IPP失去的是最高信用等级的购电方。TPG拆出IPX Power恰说明资本在重构退出路径 | B |
| AXTI一年+5485%，会不会强者恒强？ | PS 42+10年需68.9%净利CAGR——数学上不成立。InP是对的，价格是错的。等回调或找VECO类设备杠杆替代 | A |
| 双鸿PER 22.6为什么没人买？ | 可能：台股流动性折价+液冷竞争格局分散（vs ABF味之素95%垄断）+7月营收+117%未经FinMind独立确认。9/10数据是试金石 | B |

---

## 六、行动建议 + 候选追加

| 标的 | 建议动作 | 理由 |
|------|---------|------|
| FN | 深入研究执行中（8-18新入口维持） | 绿灯+OpenAI收入链传导 |
| AMKR | 维持"可分批"（$54.84） | PS 1.83+行业扩产再确认 |
| VECO | 观察，8月底Q2财报=决策点 | InP涨价→设备订单传导 |
| 双鸿3324 | 台股备案观察；9/10营收>100%→升级 | PER 22.6价值异常 |
| MU / COHR | 挂单纪律不变（$780-850 / $280-300） | 周期顶/TAM黄灯 |
| 景硕3189 | **新增观察名单（红灯）**：PER<100或TSMC quasi-EMIB放量验证时重估 | 角色质变但已定价 |
| AXTI / LITE / AAOI / 南电 | 暂不追踪（红/透支） | 纪律执行 |
| neocloud（CRWV/NBIS） | 不作为瓶颈链标的；Meta/Google变量列入其论文风险清单 | 中介价值两头受挤 |

**candidates.csv追加（source=819b3-D-bottleneck，python去重）**：`FN`、`VECO` 2只（当前活跃文件无此二者——8-18班次追加后文件被后续班次归档重置，本轮重新落账）。追加后候选总数29。其余标的（COHR/AMKR/MU/GEV/VRT/AXTI未达标）不追加。

---

## 七、来源清单（本轮新增）

- 专项变量1（quasi-EMIB）：[Wccftech：TSMC Concedes Intel's EMIB…Starts Building "Quasi-EMIB" As CoWoS Remains Choked Through 2026（78周交期、售罄至2027、与景硕合作，源头The Information）](https://wccftech.com/tsmc-concedes-intels-emib-packaging-is-a-potent-contender-starts-building-quasi-emib-as-cowos-remains-choked-through-2026/)（7-30）；TechTimes 7-30（EMIB-like计划+Kinsus）；Chosunbiz 8-03；BigGo 7-30（景硕+7.6%）
- 专项变量2（Google-Intersect）：Energy-Storage.News 3-13（$4.75B完成）；TPG公告 3-10（IPX Power）；Substack 5-05（kills PPA era）；Data Center Dynamics/Industrial Info 6-05（Meitner Energy Center 1GW+ colocated）
- 专项变量3（Meta Compute）：CNBC/Bloomberg/Reuters 7-01（云业务+股价+9%）；MarketScale 8-07（挖AWS Dave Brown、与Anthropic洽谈）；Moomoo/SoftBank 7-02（10GW入美）
- 专项变量4（OpenAI）：CNBC 7-29（7月年化超Q2总量）；TechTimes 8-15（8-14投资者会：企业>消费者、$40B ARR、7月+20% MoM、IPO进程）；qz.com 8-14；thelec 8-17
- InP/EML：BigGo 8-17（Q4涨10%+、cash-rich empty-handed）；XenoSpectrum 8-17；SCMP 8-17（Next silicon?，标题级引用、正文404未获取）；BigGo 8-03（LITE CEO：InP短缺或比存储更严重）；BigGo 6-11（中国管制+250%）；24/7 Wall St 8-17（AXTI领跑）；TechTimes 8-05（FCC禁令60%）；TechTimes 8-04（AAOI EML免疫）；BigGo 6-04（EML月产能5000万只）
- CoWoS/封装：TradingKey 8-13（良率98%+、14x reticle 2029）；TechTimes 8-11（MSFT 30万单位、NVDA占60%）；TrendForce 8-12（SPIL斗六NT$1000亿、2028）；Wccftech 7-30（78周）
- ABF：Wccftech 5-11（+30%、缺口至2027）；BigGo 5-14（95%份额）；디지털투데이 6-16（味之素扩产）；digitimes 3-06（EMIB复兴IC载板投资）
- 存储：TweakTown/TechPowerUp 8-04、SeekingAlpha 8-05（2027售罄）；tech-insider 8-06（RAM +63%）；XenoSpectrum 8-17（DDR5 5x）
- 电力链：TD Economics 7-16（供应约束拖慢AI建设）；TechTimes 8-11（H&MV €1.4B、HV工程师稀缺）；pv magazine/Reuters 5-11（交期4年，基线延续）
- 行情/估值：fetch_quotes.py（美股14只8-18收盘）；stockanalysis.com（AXTI/FN/AMKR/VECO/COHR/LITE/MU/TSM/AAOI市值与PE/PS）；FinMind via twstock_data.py（台股5只8-18收盘PER/PBR/市值；月营收仅至2026-02，**如实标注数据缺口**）；financial_rigor.py（红灯验算6组）

**信息充分度自评**：四个专项变量A-（quasi-EMIB单源The Information+多转述、OpenAI多源自洽、Meta/Google时间线完整）｜InP证据链A（5个独立信源、日期明确）｜估值A（14只全字段：市值/收入/PS/PE必填项齐全）｜SCMP正文未获取（B，标题级）｜台股月营收缺口（FinMind仅至2月，7月口径依赖新闻转述，B-）｜FCC禁令概率C（单源维持）

**与调仓流程的接口**：本轮六环节评级零变动，瓶颈地图稳定；四个新变量中，变量1（quasi-EMIB）影响2028+的ABF/BT格局、变量2/3（hyperscaler垂直整合+自售算力）是neocloud/IPP论文的风险项而非当前瓶颈链的变化、变量4（OpenAI $40B）是8-18暴跌"数学检验"担忧的最强对冲。绿灯入口FN/AMKR/VECO维持，NVDA财报（下周）仍是全链多空总裁决点。
