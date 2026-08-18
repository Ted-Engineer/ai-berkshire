# 瓶颈猎手 — AI全链路瓶颈扫描 2026-08-16（Layer 2-3 alpha 环节聚焦）

**执行方式**：bottleneck-hunter subagent 独立执行；12次 mcp__web-search__search（全部记录于 .claude/.workflow/search-log.txt）+ 美股13只实时报价（finviz_quote.py）+ 台股15只行情/PER/月营收（tools/twstock_data.py，FinMind）
**数据截止**：行情=2026-08-14收盘（8-16为周日，8-14为最后交易日）；新闻=2026-08-16；台股月营收=2026年7月（8-10前强制披露）
**与8-15版关系**：增量重跑。核心任务：①验证8-15六大S级瓶颈是否仍成立（需现搜证据）②扫描新瓶颈/评级变化 ③强制估值检查 ④补上台/日/欧标的（本轮新增台股15只月营收交叉验证，这是对8-15纯美股口径的最大补强）
**定位声明**：本项目为学习与研究用途，非投资建议；低置信结论均已标注

---

## 一、趋势确认：AI基建2026资本开支

| 指标 | 数值 | 来源 |
|------|------|------|
| 2026 Big-4 hyperscaler capex | ~$725B（Amazon $200B / Google $185B / Meta $125B / Microsoft $120B），较2025年$410B **+77%** | valueaddvc（2026-08更新版） |
| 2026 Big-5（含Oracle） | ~$775-800B（Q1'26财报确认） | alcapitaladvisory |
| 2026 全球AI capex | **>$1万亿**（GS：hyperscaler口径$794B低估总量约$200B——非hyperscaler AI投资被漏统） | Goldman Sachs官方insights |
| 加速性判断 | 2026需求增速+77% vs 关键环节供给增速：CoWoS年化扩产~80%（但85%+已被预定）、HBM/DRAM 2027产能已售罄、EML交期推过2027 → **需求>供给仍成立至2027**；2027 capex增速共识降至+22-25%（GS/Reuters） | 多源 |

**已发生验证事件（≥3个，全部为2026年内实际发生）**：
1. **[2026-08-13] TSMC 7月营收同比+45%**（NVIDIA/AMD/Apple订单加速），同日台积电先进封装VP何军表态：CoWoS产能连续三年翻倍、供给已"非常接近"需求——瓶颈正从CoWoS向ABF载板转移（slicast / finance.biggo / xenospectrum）
2. **[2026-08-03/04] 三星/海力士/美光2027年DRAM+HBM产能全部售罄**（DigiTimes系），NAND至2026年8月的产能也近乎订满，客户以预付款锁量（sammyfans / TradingKey / tweaktown）
3. **[2026-08-11 AMC] Lumentum 6月季（FQ4）营收$1.01B、同比+109%**，全品类激光器需求爆发；野村8-12全球AI趋势报告确认EML/CW激光供需失衡持续（techflowpost / ainvest）
4. [2026-03-02] NVIDIA向Lumentum与Coherent各承诺**$2B（合计$4B）EML产能锁定**，并投资Scintil Photonics与Ayar Labs（TechTimes 2026-05-27回溯）
5. [2026-08-05] Veeco再获LUMINA+ MOCVD订单（InP激光制造）；年内累计InP相关设备订单**>$250M**，2026开始出货、2027显著放量（Veeco IR / convergedigest）

**趋势确认：✅ 可追踪**（全球AI capex >$1T、+77%增速、多环节2027售罄交叉印证）

---

## 二、供应链物理拆解（Layer 0-4）

```
Layer 0：AI训练/推理服务（模型API、Agent）
Layer 1（定价充分）：GPU/ASIC、HBM、服务器整机、数据中心REIT
│
├─ Layer 2（本轮主扫描区）：
│   ├─ 网络互联：800G/1.6T光模块（2026市场$25-35B；1.6T细分$1.1B→$1.8B、+69%）
│   ├─ 光通信核心：EML/CW激光器（NVIDIA $4B锁定；交期>2027；200G远紧于100G）
│   ├─ 半导体材料：InP衬底（2"价格$800→$2,300-2,500，+~200%）/GaAs/SOI
│   ├─ 先进封装：CoWoS（2026售罄、50-78周交期）+ ABF载板/积层膜（TSMC点名"第二约束"）
│   ├─ PCB/CCL：高频高速覆铜板（台光电7月营收+129%——AI服务器CCL量价齐升）
│   ├─ 测试：Probe Card（FORM Q1 +32%；台系精测+50%/旺矽+67%）
│   ├─ 散热/冷却：CDU/冷板（direct-to-chip交期拉长至Q4'26；台系双鸿7月+117%）
│   └─ 电力连接：变压器/GSU/母线（GSU交期130-210周；HV最高60个月）
├─ Layer 3：
│   ├─ 外延设备：MOCVD/IBD（Veeco $250M+订单；Aixtron为另一极）
│   ├─ 高纯金属：铟（中国2025-02限制至今未解——四种受控小金属中唯一仍全面受限）/镓(+123%)/锗(+203%)
│   └─ 特气/靶材（B级维持，事件性冲击为主）
└─ Layer 4：电力（核电PPA/气轮机槽位2028-29）、冷却水、土地并网许可（电网4-5年 vs 数据中心<18月错配）
```

---

## 三、瓶颈地图（六标准评估）+ 与8-15对比

六标准：供给集中度/扩产周期/替代难度/产能利用率/需求增速/客户验证周期（🔴越多越紧）

### S级瓶颈（≥4🔴，单点故障级）

| # | 环节 | 今日证据（日期） | 六标准快评 | 主要供应商 | vs 8-15 |
|---|------|----------------|-----------|-----------|---------|
| S1 | **EML/CW激光器** | NVIDIA $4B锁定LITE/COHR（3-02）；交期推过2027；200G EML远紧于100G；LITE 6月季+109%；野村8-12确认失衡持续；硅光只能部分泄压（仍需InP光源） | 🔴🔴🔴🔴🔴（替代难度🟡，硅光是部分替代） | LITE、COHR、三菱电机、住友电工 | **维持S，证据加固** |
| S2 | **InP衬底+铟原料** | 2"光通信级衬底$800→$2,300-2,500（+~200%，2025初→2026-04）；铟是中国四种出口受限小金属中唯一仍全面受限者；JX ¥120B/4年扩至10倍、住友电工¥18B扩至3.1倍（FY2028）——扩产本身证明缺口 | 🔴🔴🔴🔴🔴🔴（今日唯一满🔴） | AXTI、JX金属(5016.T)、住友电工(5802.T) | **维持S，且从Layer3原料端（铟）加固** |
| S3 | **HBM/DRAM** | 2027年三大厂DRAM+HBM全部售罄（8-03/04）；NAND至8月订满；客户仅获申请量60-70%；新供给2028才可能松动 | 🔴🔴🔴🔴🔴（替代难度🟡） | MU、海力士、三星 | **维持S；注意：股价与基本面背离（memory股近期下跌）** |
| S4 | **CoWoS先进封装** | 2026售罄、交期50-78周、2026-27产能85%+已锁定、NVIDIA独占~60%（~595k片/年）；**但TSMC VP 8-12表态"供给已非常接近需求"、瓶颈转移至ABF**；产能35k→130k wpm（2024末→2026末） | 🔴🔴🔴🔴（供给集中度🔴、验证🔴；**产能利用率由🔴转🟡边缘**） | TSMC准独家（+Amkor/日月光二线） | **S→S-（降级中）**：仍售罄但边际不再收紧 |
| S5 | **ABF载板/积层膜** | **TSMC VP 8-12点名：ABF将成为仅次于memory的第二大约束**；台系三雄7月营收同比：欣兴+43.7%/南电+50.2%/景硕+35.9%（加速中）；味之素ABF膜份额>95%、Q3'26提价~30%（8-15证据） | 🔴🔴🔴🔴🔴（替代难度🟡，玻璃基板是远期威胁） | 味之素(2802.T)、Ibiden(4062.T)、欣兴(3037.TW)、南电(8046.TW)、AT&S | **维持S，获TSMC官方背书=6个S级中今日信号最强** |
| S6 | **变压器/GSU/大型电力设备** | GSU交期130-210周、HV Tier1最高60个月；LPT 120周+积压未清（mid-2026）；Hitachi Energy +$250M扩产；数据中心<18月 vs 电网4-5年错配未解；但Powermag质疑部分为"恐慌性自致短缺"，台系中兴电7月营收仅+3.8%（收入确认滞后） | 🔴🔴🔴🔴（需求增速🟡-🔴之间：数据中心电力需求年增~25-30%） | GEV、Hitachi Energy、西门子能源、HD现代电气、HUBB、中兴电/士电 | **维持S（交期证据），但收入端验证滞后，评级内部分歧加大** |

### A级瓶颈

| # | 环节 | 今日证据 | vs 8-15 |
|---|------|---------|---------|
| A+（新） | **MOCVD/外延设备（Layer 3）** | Veeco年内InP激光制造设备订单>$250M（MOCVD+IBD+湿法），2026出货、2027放量；3-02与8-05两笔公告+"全球光通信龙头"复购——这是"InP军备竞赛的卖铲人" | **新增A+**：8-15未单列（当时归在S2注脚） |
| A3↑ | **液冷/CDU/冷板** | direct-to-chip交期拉长至Q4'26（sourcebyspec 7月版）；市场$4.07B(2026)→$27.65B(2033)、CAGR 31.5%；GS：2026年76% AI服务器液冷；台系量验证：双鸿7月+116.7%、奇鋐+57.4%、健策+91.0% | **A→A+（上调）**：8-15称"未发现硬短缺证据"，本轮找到交期拉长+台股营收爆发双证据 |
| A2 | CPO共封装光学 | 2026放量元年但商业稳定拐点不早于H2'27；真约束仍是上游EML/InP | 维持A |
| A1 | 铀浓缩/HALEU | 维持8-15判断（LEU获DOE $900M+约$2.3B合同；兑现集中2028+）。注意LEU股价YTD -21.7%（AI核电叙事降温）但近1月+29.3% | 维持A |
| A-↑ | **Probe Card测试卡** | FORM Q1'26营收+32%至$226.1M、净利三倍至$20.4M；行业报告市场规模上修至$3.5-5.5B（HBM测试强度左移，"结构性摆脱周期性"）；台系精测7月+49.9%、旺矽+66.5% | **B→A-（上调）**：量价证据足以升半级 |

### B级瓶颈（观察）

| # | 环节 | 判断 |
|---|------|------|
| B1 | 模拟/电源IC、企业存储 | GlobX：2026短缺已扩散至"加速器周围的一切"——高速网络、企业存储、模拟/电源IC；无单点供应商，B级观察（受益者MPS/安森美/英飞凌，非纯瓶颈） |
| B2 | 高频高速CCL（玻纤布/树脂） | 台光电7月营收+129.4%（M6/M8 CCL量价齐升），但PER 96已充分定价；上游特殊玻纤布（日东纺）值得关注，B+ |
| B3 | 特气/氦 | 维持8-15：事件性（卡塔尔）而非结构性 |
| B4 | GaAs/SOI传统衬底 | 维持：温和增长，非硬瓶颈 |

**与8-15对比变化汇总**：
- **维持S（证据加固）**：EML激光器、InP衬底（新增铟原料受限证据）、HBM、ABF载板（获TSMC官方点名）
- **降级中**：CoWoS S→S-（TSMC自认供给接近需求，瓶颈向ABF转移——**这是本轮最重要的边际变化**）
- **上调**：液冷/CDU A→A+（找到交期+台股营收双证据）；Probe Card B→A-
- **新增**：MOCVD/外延设备 A+（Veeco $250M+订单链）；铟原料受控（并入S2加固）
- **信号背离警示**：memory股在"2027售罄"基本面下反而下跌——市场开始对2028供给潮预定价

---

## 四、公司筛选与估值检查（硬门槛）

### 4.1 美股看板（finviz，8-14收盘；PS=TTM；增速=最新季YoY）

| Ticker | 公司 | 市值 | PS | PE | fPE | 最新季增速 | 估值灯 | 信号强度 | 瓶颈 |
|--------|------|------|-----|-----|-----|-----------|--------|---------|------|
| **COHR** | Coherent | $63.8B | 9.0 | 79.2 | 23.1 | +33.8% | 🟢-🟡 | ★★★★ | S1 EML |
| **AMKR** | Amkor | $14.7B | **2.0** | 26.5 | 21.5 | +25.6% | 🟢 | ★★★★ | S4/S5封装链 |
| **VECO** | Veeco | $3.2B | **4.7** | 143.9(TTM微利) | 16.5 | +16.5% | 🟢-🟡 | ★★★★ | A+ MOCVD |
| **HUBB** | Hubbell | $27.0B | 4.3 | 30.3 | 22.6 | +15.3% | 🟢 | ★★★★ | S6电力 |
| **FN** | Fabrinet | $20.4B | 4.8 | 49.0 | 33.1 | +39.3% | 🟢-🟡 | ★★★ | S1链制造 |
| **MU** | Micron | $1,097B | 12.2 | 22.0 | **6.3** | +345.7% | 🟡 | ★★★ | S3 HBM |
| **VRT** | Vertiv | $113.1B | 9.9 | 66.5 | 32.1 | +24.1% | 🟡 | ★★★ | A+液冷 |
| **ONTO** | Onto Innovation | $16.3B | 14.5 | 124.1 | 29.5 | +35.3%(QoQ年化口径) | 🟡 | ★★★ | S5检测 |
| **FORM** | FormFactor | $10.3B | 11.4 | 90.2 | 35.1 | +31.9% | 🟡 | ★★★ | A-探针卡 |
| **MTSI** | MACOM | $24.2B | 20.8 | 101.8 | 37.3 | +35.8% | 🟡 | ★★★ | S1二线 |
| **LITE** | Lumentum | $72.1B | 23.9 | 亏损(TTM) | 28.0 | +109.3% | 🔴 | ★★（红灯封顶） | S1 EML |
| **AXTI** | AXT | $5.4B | **42.7** | 4389 | 36.8 | +164.8% | 🔴 | ★★（红灯封顶） | S2 InP |
| **GEV** | GE Vernova | $283.2B | 6.9 | 30.4 | **42.7** | +21.8% | 🔴 | ★★ | S6 |
| **LEU** | Centrus | $3.8B | 8.0 | 86.8 | 67.1 | +14.0% | 🔴 | ★★ | A1 HALEU |

**红灯依据（用financial_rigor.py验算）**：
- LITE：市值$72.1B ÷ 光学元件TAM约$35B(2026) = **206%**，远超"TAM 20%"红线；虽增速+109%>100%可豁免PS规则，但"市值>TAM 20%"这一条独立触发红灯。近1月+31%、YTD+151%，8-11财报后单日+5.2%
- AXTI：市值$5.4B ÷ InP衬底TAM（2028E约$1.2B，按JX 10倍扩产反推）= **446%**；PS 42.7且近1月+79%、YTD+399%——典型"瓶颈最硬=估值最满"
- GEV：fPE 42.7 > PE 30.4（远期高于即期=市场定价2027 EPS下滑），2027 EPS一致预期约-19%
- LEU：PE 86.8>80且增速仅+8.5%，无法用PEG自洽

### 4.2 台股看板（twstock_data.py，8-14收盘；月营收=2026年7月，8-10披露）

| 代码 | 公司 | 市值(≈USD) | PER | PBR | 7月营收YoY | 趋势(5→6→7月) | 瓶颈环节 | 估值灯 |
|------|------|-----------|-----|-----|-----------|--------------|---------|--------|
| 3324.TW | 双鸿Auras | $3.0B | **23.3** | 7.1 | **+116.7%** | +94%→+62%→+117% | A+液冷冷板 | 🟢 |
| 3016.TW | 嘉晶EPI | $0.94B | 85.4 | 5.7 | +51.4% | +37%→+41%→+51% | S2 GaAs/InP外延 | 🟡 |
| 2455.TW | 全新VPEC | $2.2B | 93.0 | 19.2 | +45.1% | +47%→+24%→+45% | S2 InP外延晶圆 | 🟡 |
| 6510.TW | 精测Chun | $3.1B | 70.5 | 9.7 | +49.9% | +34%→+40%→+50% | A-探针卡 | 🟡 |
| 1513.TW | 中兴电CDC | $2.7B | **19.1** | 4.0 | +3.8% | +4%→+8%→+4% | S6重电/GIS | 🟢（量未启动） |
| 3037.TW | 欣兴Unimicron | $53.1B | 67.9 | 13.1 | +43.7% | +32%→+36%→+44% | S5 ABF载板 | 🟡 |
| 8046.TW | 南电NanYa | $26.8B | 153.4 | 17.1 | +50.2% | +36%→+50%→+50% | S5 ABF载板 | 🟡 |
| 3189.TW | 景硕Kinsus | $14.4B | 159.9 | 10.2 | +35.9% | +33%→+32%→+36% | S5 ABF载板 | 🟡 |
| 2383.TW | 台光电EMC | $70.1B | 96.4 | 37.9 | **+129.4%** | +115%→+121%→+129% | B+高频CCL | 🔴（PBR 38） |
| 3017.TW | 奇鋐AVC | $40.3B | 43.1 | 23.0 | +57.4% | +61%→+66%→+57% | A+散热/CDU | 🟡 |
| 3653.TW | 健策 | $22.6B | 109.6 | 30.2 | +91.0% | +38%→+58%→+91% | A+冷板/均热片 | 🔴 |
| 6223.TW | 旺矽MPI | $20.0B | 137.9 | 39.7 | +66.5% | +58%→+65%→+67% | A-探针卡 | 🔴 |
| 3081.TW | 联亚LandMark | $8.2B | **218.6** | **49.8** | **+176.5%** | +119%→+128%→+177% | S2 InP激光外延 | 🔴 |
| 1503.TW | 士电 | $3.3B | 27.3 | 2.7 | +15.1% | +8%→-11%→+15% | S6变压器 | 🟢（量温和） |
| 3533.TW | 嘉泽Lotes | $6.1B | 21.0 | 4.7 | +18.6% | +9%→+17%→+19% | S6连接器 | 🟢（量温和） |

（汇率按NT$31.5/US$估算，标注"≈"；台股月营收同比是瓶颈"量"验证的最快公开信号）

**台股月营收三重含义**：
1. **S5 ABF量验证成立**：三雄7月+36~50%且逐月加速——与TSMC"ABF第二约束"表态互为印证（8-15仅有日系提价证据，本轮补上台系量的证据）
2. **A+液冷从故事变数据**：双鸿+117%/奇鋐+57%/健策+91%——8-15"未发现硬短缺"的判断被7月数据推翻，支持上调
3. **S6变压器收入端未启动**：中兴电+3.8%/士电+15%——GSU交期160周是订单/backlog口径，转化为营收要到2027；这解释了为何"瓶颈最紧的环节"在台股重电上看不到营收爆发（低PER反而是市场对"有订单无营收"的定价）

---

## 五、交叉验证

### 5.1 正向验证矩阵

| 验证项 | 结果 | 证据 |
|--------|------|------|
| 客户签约 | ✅强 | NVIDIA $4B锁定LITE/COHR产能；NVIDIA占TSMC 2026 CoWoS需求~60%；memory预付款锁2027 |
| 收入体现 | ✅强 | LITE +109%/MU +346%/AXTI +165%/FORM +32%；台股7月营收表（15只中13只加速） |
| 涨价 | ✅强 | InP衬底2" +200%（$800→$2,300-2,500）；味之素ABF膜+30%；镓+123%/锗+203%；memory全线涨价 |
| 交期 | ✅强 | EML>1年（推过2027）；CoWoS 50-78周；GSU 130-210周；direct-to-chip冷却拉长至Q4'26 |
| 扩产capex | ✅强 | JX ¥120B(10x)/住友¥18B(3.1x)/Hitachi+$250M/TSMC CoWoS 35k→130k wpm/Veeco $250M+设备订单 |
| 第三方 | ✅ | TrendForce(8-06 InP)/Nomura(8-12 EML)/TSMC VP(8-12 ABF)/GS(capex>$1T)/DigiTimes(2027售罄) |

### 5.2 反向验证（芒格式否定，逐瓶颈）

**S1 EML激光器**：聪明人为什么不买？——LITE市值已达光学元件TAM的2倍，NVIDIA有动机扶持第二来源（已投Scintil/Ayar）；台积电COUPE把CW激光集成进代工流程是长期"去LITE/COHR化"路线。瓶颈何时解除？LITE/COHR自扩+EML交期2027末正常化。需求-50%敏感度：LITE PS 23.9会先杀估值再杀盈利。**结论：瓶颈真实但价格已透支（红灯名单）**。

**S2 InP衬底**：绕过路线？Fraunhofer 150mm InP-on-GaAs、大尺寸化降本；中国衬底（云南锗业系）在涨价刺激下会进入。供给冲击：JX 10倍+住友3.1倍+AXT翻倍扩产全部2027-28落地=经典"短缺→过剩"剧本（参考2021-23 GaAs）。AXTI在YTD+399%后买入=为别人的扩产买单。**结论：S级最纯正，但美股纯度标的AXTI红灯；台股联亚PER 218/PBR 50更极端**。

**S3 HBM**：2028供给潮（三星P4/海力士M15X/美光爱达荷+纽约/长鑫）是共识；MU fPE 6.3x=市场已在为2028崩溃定价——"售罄至2027"与"股价下跌"并存说明聪明钱在卖基本面最好的时刻（周期股纪律）。**结论：维持8-15纪律——只挂单不追（触发区$780-850）**。

**S4/S5 CoWoS→ABF**：TSMC自己说CoWoS接近平衡——瓶颈溢价将向ABF迁移；ABF的远期威胁是玻璃基板（2028+）。台股三雄PER 68-160已计入加速，欣兴相对最便宜。**结论：方向确认，选估值最低环节入口（ONTO fPE 29.5/欣兴PER 68）而非追纯度**。

**S6变压器**：Powermag质疑部分短缺是"自致危机"（恐慌性双订）；Ayr Energy宣称把HV交期从3-5年压到6-12个月；HD现代/西门子能源/日立2027-28新厂。台股中兴电PER 19+营收+3.8%=市场尚未为backlog定价——这是"左侧"特征，但需等收入拐点（月营收连续2月>20%）。**结论：S级维持，但把HUBB（绿灯）作为主入口、中兴电列入观察**。

**A+ MOCVD（VECO）**：设备订单是一次性资本开支而非经常性收入——InP扩产潮2028结束后VECO回到周期股原形；TTM仍微利（PE 144）。但PS 4.7/fPE 16.5提供了安全垫，订单能见度到2027。**结论：新观察标的，等待Q3订单连续性验证**。

**A+液冷**：Vertiv产能2026年底翻倍=自家解除瓶颈的时点；超大规模客户自研CDU+Boyd/Motivair/nVent竞争。双鸿PER 23却给出+117%营收增速——市场将其视为"机壳厂"而非"液冷厂"的定价错配是本轮台股最佳风险回报。**结论：双鸿(3324.TW)绿灯入观察，VRT维持黄灯**。

---

## 六、瓶颈机会排名表

| 排名 | 公司 | 代码 | 市值 | 年收入(TTM) | PS | PE/fPE | 瓶颈环节 | 评级 | 份额 | 最新增速 | 信号 | 估值判断 |
|------|------|------|------|------------|-----|--------|---------|------|------|---------|------|---------|
| 1 | Coherent | COHR | $63.8B | $7.1B | 9.0 | 79/23 | EML激光+光模块 | S1 | EML双寡头之一(~30%) | +33.8% | ★★★★ | 合理偏低（绿-黄） |
| 2 | Amkor | AMKR | $14.7B | $7.4B | 2.0 | 26/22 | 先进封装OSAT | S4/S5 | OSAT全球第2 | +25.6% | ★★★★ | **低估（绿）** |
| 3 | Veeco | VECO | $3.2B | $0.68B | 4.7 | 144/17 | InP外延设备MOCVD/IBD | A+(新) | MOCVD两强之一(vs Aixtron) | +16.5%(转正) | ★★★★ | 合理（绿-黄，订单驱动） |
| 4 | 双鸿 | 3324.TW | $3.0B | NT$31.7B | ~2.3(估) | 23/— | 液冷冷板/散热模组 | A+ | 台系冷板双雄之一 | +116.7% | ★★★★ | **低估（绿）** |
| 5 | Hubbell | HUBB | $27.0B | $6.2B | 4.3 | 30/23 | 电网/变压器硬件 | S6 | 北美电网设备前列 | +15.3% | ★★★★ | 合理（绿） |
| 6 | Fabrinet | FN | $20.4B | $4.2B | 4.8 | 49/33 | 1.6T光模块制造 | S1链 | NVIDIA光模块主力代工 | +39.3% | ★★★ | 合理（绿-黄） |
| 7 | Micron | MU | $1,097B | $90B | 12.2 | 22/6.3 | HBM/DRAM | S3 | HBM三强(~20-25%) | +345.7% | ★★★ | 周期顶定价（黄） |
| 8 | 欣兴 | 3037.TW | $53.1B | NT$1.37T | ~7(估) | 68/— | ABF载板 | S5 | ABF载板全球第1-2 | +43.7% | ★★★ | 已计入较多（黄） |
| 9 | Onto | ONTO | $16.3B | $1.1B | 14.5 | 124/30 | ABF在线检测 | S5 | 载板检测近垄断 | +35.3% | ★★★ | 偏高（黄） |
| 10 | FormFactor | FORM | $10.3B | $0.9B | 11.4 | 90/35 | HBM探针卡 | A- | 探针卡全球第1 | +31.9% | ★★★ | 偏高（黄） |
| — | Lumentum | LITE | $72.1B | $3.0B | 23.9 | 亏/28 | EML激光 | S1 | EML份额第1(~40%) | +109.3% | ★★ | **透支（红）** |
| — | AXT | AXTI | $5.4B | $0.13B | 42.7 | 4389/37 | InP衬底 | S2 | InP衬底第1(~50%+) | +164.8% | ★★ | **透支（红）** |
| — | 联亚 | 3081.TW | $8.2B | NT$35B | ~15(估) | 219/— | InP激光外延 | S2 | InP外延关键供应商 | +176.5% | ★★ | **透支（红）** |
| — | GE Vernova | GEV | $283.2B | $41.3B | 6.9 | 30/43 | 气轮机/电力设备 | S6 | 气轮机西方三强 | +21.8% | ★★ | 透支（红，fPE倒挂） |
| — | Centrus | LEU | $3.8B | $0.47B | 8.0 | 87/67 | HALEU铀浓缩 | A1 | 美国唯一本土商业化 | +14.0% | ★★ | 透支（红） |

（"年收入"美股取finviz TTM Sales；台股取近12月营收加总估算；份额为公开资料估计值，标"估"）

### 前五名一页纸摘要

---

🎯 **Coherent（COHR）— 光学双S级瓶颈（EML激光+数据中心光模块）中最便宜的入口**
- 为什么是瓶颈：EML双寡头之一，NVIDIA $4B产能锁定的两个对象之一；交期推过2027
- 为什么是这家：PS 9.0（vs LITE 23.9）、fPE 23.1、最新季+33.8%——S级环节中唯一"PS<10且远期盈利"的美股
- 催化剂：近1-3月：8月中下旬FQ4'26财报（EML出货爬坡）；3-12月：200G EML放量、InP 6英寸转进
- 风险：LITE宣称UHP领先其2年；台积电COUPE硅光集成是3年+替代路线
- 关键数据：$63.8B / $7.1B / PS 9.0 / fPE 23.1 / +33.8% / 瓶颈业务（光通信）占比~70%
- 安全边际检验：10年25x PE退出需净利$6.6B（当前$0.8B，CAGR 23.4%）——在瓶颈延续至2027+情景下可达成，**有条件安全边际**
- 结论：**值得深入研究（观察触发区$280-300延续8-15建议）**

🎯 **Amkor（AMKR）— 全场估值最低的先进封装标的（PS 2.0）**
- 为什么是瓶颈：CoWoS外溢订单的最大承接者（OSAT第2），2.5D封装+ABF载板自供
- 为什么是这家：PS 1.97/PE 26.5全场最低；$2.5-3B capex扩AI封装产能；台积电产能溢出直接受益
- 风险：OSAT竞争激烈毛利低；CoWoS若2027缓解则外溢逻辑反转
- 安全边际：10年25x退出需净利$1.52B（当前$0.55B，CAGR 10.8%）——要求最低
- 结论：**值得深入研究**

🎯 **Veeco（VECO）— InP军备竞赛的卖铲人（本轮新发现）**
- 为什么是瓶颈：InP激光扩产必须买MOCVD/IBD设备，Veeco年内订单>$250M、2027放量
- 为什么是这家：PS 4.7/fPE 16.5；MOCVD两强之一（vs Aixtron）；客户复购（"全球光通信龙头"3月与8月两下单）
- 风险：设备=一次性capex，2028扩产潮结束后回归周期股；TTM微利
- 结论：**加入观察名单，等Q3'26订单与收入连续性**

🎯 **双鸿 Auras（3324.TW）— 台股液冷量价齐升+估值错配**
- 为什么是瓶颈：direct-to-chip交期拉长至Q4'26；冷板/散热模组7月营收+116.7%
- 为什么是这家：PER 23.3/PBR 7.1给出+117%增速——被按"机壳厂"定价的液冷核心供应商
- 风险：Vertiv产能2026底翻倍后2027行业性过剩；ODM自研
- 结论：**加入观察名单（台股流动性需用大额挂单纪律）**

🎯 **Hubbell（HUBB）— 唯一"绿灯+S级瓶颈"的美股（延续8-15）**
- 电网/变压器硬件，PS 4.3/fPE 22.6/目标价$573 vs 现价$511
- 风险：变压器只占部分业务；新产能2027-28释放
- 结论：**维持8-15触发区$430-470挂单，不追高**

---

### 行动建议

| 标的 | 建议动作 | 理由 |
|------|---------|------|
| COHR | 执行 /investment-team 深入研究 | S级瓶颈×最低估值入口×NVIDIA绑定 |
| AMKR | 执行 /investment-team 深入研究 | S级链×全场最低PS×盈利 |
| VECO | 观察名单，等Q3订单验证 | A+新瓶颈但收入兑现在2027 |
| 3324.TW 双鸿 | 观察名单 | A+液冷量价齐升×PER 23 |
| HUBB | 维持挂单$430-470 | 绿灯但高于触发区 |
| MU | 仅挂单$780-850（fPE~5x） | 周期顶纪律（LRN-012） |
| TSM | 维持持仓+挂单$390/400 | S4降级但不改持仓逻辑 |
| LITE/AXTI/3081.TW/GEV/LEU/2383.TW | 暂不追踪（红灯） | 瓶颈最硬=估值最满 |

---

## 七、候选登记与状态

- 本轮新登记候选（池内原缺）：AXTI、ONTO、FORM、VECO、FN、3324.TW、3016.TW、6510.TW、1513.TW、3081.TW（含红灯标的——登记供后续监控，不代表推荐）
- 已在池（核查）：LITE、COHR、MU、GEV、VRT、HUBB、LEU、AMKR、PWR、ETN、NVT、CCJ、AVGO、TSM
- 非美股瓶颈龙头备案：味之素(2802.T)、Ibiden(4062.T)、JX金属(5016.T)、住友电工(5802.T)、Soitec(SOI.PA)、IQE(IQE.L)、Technoprobe(TPRO.MI)、Aixtron(AIX.DE)、HD现代电气(267260.KS)

## 八、来源清单（主要）

趋势/capex：[Goldman Sachs >$1T](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)、[valueaddvc $725B](https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once)、[alcapital $775-800B](https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html)

EML/激光：[TrendForce](https://www.trendforce.com/presscenter/news/20251208-12823.html)、[TechTimes NVIDIA $4B锁定](https://www.techtimes.com/articles/317281/20260527/ai-data-center-optical-component-shortage-nvidias-4b-laser-lockup-pushes-rivals-past-2027.htm)、[Nomura/LITE +109%](https://www.techflowpost.com/en-US/article/33273)、[convequity硅光泄压](https://www.convequity.com/notes-light-is-the-future-pt-2/)、[ainvest LITE/COHR/FN](https://www.ainvest.com/news/lighting-fiber-lumentum-coherent-fabrinet-capitalizing-optical-transceiver-boom-2507/)

InP/铟：[TrendForce 8-06](https://www.trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/)、[InP价格3倍](https://finance.biggo.com/news/xsiIxJ0Bh5an-7GhIww3)、[JX ¥120B/10x](https://www.jx-nmm.com/english/newsrelease/fy2026/20260616_02.html)、[住友¥18B/3.1x](https://en.wedoany.com/shortnews/356703.html)、[铟唯一全面受限](https://www.geopoliticalmonitor.com/critical-minerals-global-indium-supply-demand/)、[Ga/Ge涨价](https://www.useluminix.com/reports/industry-analysis/china-rare-earth-export-controls-2026-us-defense-ai-chip-supply-impact)、[11-27管制暂停到期](https://www.materialsdispatch.com/en/blog/china-november-2026-export-control-cliff)

HBM：[sammyfans 2027售罄](https://www.sammyfans.com/2026/08/03/ai-demand-books-all-2027-dram-hbm-supply/)、[TradingKey 8-04](https://www.tradingkey.com/analysis/stocks/us-stocks/262073096-mu-samsung-sk-hynix-secured-dram-2027-ai-memory-tradingkey)、[memory股下跌悖论](https://marketwise.com/investing/why-micron-sk-hynix-samsung-stock-is-tumbling-during-memory-shortage/)

CoWoS/ABF：[TSMC +45%与ABF第二约束](https://slicast.com/commentary/tsmc-2026-08-12)、[TSMC VP何军表态](https://finance.biggo.com/news/18911103-c55c-4611-b80a-b6d155ed9dbe)、[5.5x良率98%](https://xenospectrum.com/en/tsmc-cowos-memory-abf-bottlenecks/)、[CoWoS 50-78周/85%锁定](https://siliconanalysts.com/analysis/cowos-lead-times-ai-bottleneck-2026)、[CoWoS瓶颈至2028](https://www.aiexpert.news/en/ticker/ai-chip-shortage-moves-upstream-cowos-packaging-bottleneck-deepens-into-2028)

变压器：[GSU 130-210周](https://megagridsupply.com/learn/transformer-lead-times-2026)、[HV 60个月](https://www.gridreadiness.com/blog/power-transformer-lead-times-ai-data-center-2026.html)、[Powermag自致危机论](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)、[Hitachi+$250M](https://www.sourcebyspec.com/news/global-transformer-shortage-2026-lead-times-capacity-adds-and-sourcing-levers.html)

液冷：[direct-to-chip拉长至Q4](https://www.sourcebyspec.com/news/liquid-cooling-supply-shortage-2026-lead-times-risk-map-and-sourcing-cues.html)、[市场31.5% CAGR](https://www.sourcebyspec.com/news/liquid-cooling-supply-chain-2026-cdu-bottlenecks-coolant-specs-and-component.html)、[GS 76%液冷](https://axis-intelligence.com/data-center-liquid-cooling-statistics/)

MOCVD/设备：[Veeco LUMINA+订单8-05](https://ir.veeco.com/news-and-events/news-details/2026/Veeco-Announces-LUMINA-MOCVD-System-Order-for-Manufacturing-Indium-Phosphide-Lasers/default.aspx)、[$250M+订单](https://convergedigest.com/veeco-lands-250m-in-orders-for-inp-laser-manufacturing-equipment/)、[3-02多系统订单](https://ir.veeco.com/news-and-events/news-details/2026/Veeco-Books-Multi-System-Lumina-and-Spector-Orders-for-Manufacturing-Indium-Phosphide-InP-based-Optical-Components/default.aspx)

探针卡：[FORM Q1 +32%](https://www.stocktitan.net/sec-filings/FORM/10-q-formfactor-inc-quarterly-earnings-report-fd4f2595365c.html)、[$3.5-5.5B市场上修](https://www.hdinresearch.com/news/1320)

其他：[GlobX短缺扩散至模拟/电源IC](https://globx.eu/blog/supply-chain-insight/ai-infrastructure-semiconductor-supply-chain-2026)、[1.6T市场+69%](https://www.stalwartresearchinsights.com/product/16t-optical-transceiver-industry-outlook-2026-2036)、[1.6T采购10M→20M](https://www.szwecent.com/why-1-6t-optical-transceivers-overtake-800g-in-2026-ai-clusters/)

行情数据：finviz.com（美股，8-14收盘）；FinMind via tools/twstock_data.py（台股，8-14收盘+2026年7月月营收）

**信息充分度自评**：行业格局A（12次搜索多源交叉+台股15只月营收量的验证）｜估值A（finviz+twstock实时快照，PS/PE/fPE全字段）｜瓶颈解除时点B（JX/住友/Vertiv扩产投产节奏未逐厂核实）｜汇率C（NT$31.5为估算值）
