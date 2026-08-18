# 瓶颈猎手 — AI全链路瓶颈扫描 2026-08-17（光学 / 先进封装 / 存储链专题）

**执行方式**：bottleneck-hunter subagent 零复用重验；8次 Brave/Google News 搜索（记录于 .claude/.workflow/search-log.txt）+ 美股8只估值快照（fetch_quotes.py + stockanalysis.com）+ 台股3只行情/PER/月营收（tools/twstock_data.py，FinMind）+ financial_rigor.py 验算
**数据截止**：美股行情=2026-08-14收盘（8-17为周一，撰写时美股未开盘）；台股行情=**2026-08-17当日收盘**（欣兴+9.8%为最新信号）；新闻=2026-08-15～17周末增量 + 8月上旬关键证据
**与8-16基线关系**：增量对比。所有评级基于本轮现搜证据重验，不复用旧结论。本轮聚焦Layer 2-3光学/封装/存储链。
**定位声明**：学习与研究用途，非投资建议；低置信结论已标注。

---

## 一、零复用重验结果：8-16基线六瓶颈逐项判定

### 瓶颈评级总表（六标准：集中度/扩产周期/替代难度/产能利用率/需求增速/客户验证）

| # | 环节 | 评级 | 8-17新证据（日期） | vs 8-16 |
|---|------|------|-------------------|---------|
| S1 | **EML/CW激光器** | **S 维持** | ①LITE CEO Hurlston 7-08 RAISE Summit：InP短缺可能"比DRAM/NAND更严重"（Tom's Hardware/XenoSpectrum 8-03转述）②LITE EML+pump激光器**供给缺口>30%**（5月与7月两次同口径重申）③NVIDIA/超大规模客户订单量级从电信时代"数百件"跳到"**数亿件**"④LITE第5厂（NC Greensboro）**2028年中**才量产——扩产周期>2年实证 ⑤FCC拟禁中国光模块（8-05 TechTimes：涉美国AI数据中心60%光模块供应，且西方替代产能反而需要中国铟）——地缘维度加固 | **维持S，证据加固** |
| S2 | **InP衬底+铟原料** | **S 维持（满🔴）** | ①InP价格Q4'26拟再涨10%+、创纪录，买家"cash-rich but empty-handed"（finance.biggo 8-17周末报道）②LITE警告InP链是"narrow supply chain from raw materials to lasers"③2026年6英寸衬底转换年（良率爬坡=有效供给短期更紧）④Reuters：中国对InP出口管制威胁AI数据中心部署 | **维持S，Layer3原料端持续加固** |
| S3 | **HBM/DRAM** | **S 维持**；**NAND拆出降级A-** | ①DRAM单颗创纪录$20、RAM价格累计+63%（tech-insider 8月）②ADATA董事长：Q3'26合约价DRAM +30%、NAND +40%，AI榨干消费级供给（Wccftech）③2027年DRAM+HBM三大厂售罄维持（TweakTown/SeekingAlpha/TechPowerUp 8月初多源）④**反向**：TrendForce——**NAND供给增速2027超需求、2H27短缺缓解**；Tom's Hardware——涨价开始触到消费端承受力上限、Q3后动能趋缓 | **HBM维持S；NAND单独降A-（解除时点首次明确：2H27）** |
| S4 | **CoWoS先进封装** | **S- 维持（降级中）** | ①TSMC警告AI芯片（含封装）短缺将持续数年、2026年价格仍涨（TechTimes 8月）②TSMC自认CoWoS供给"接近需求"（8-12 VP口径维持）③Intel EMIB借CoWoS紧张获得客户切入点（247wallst/Chosunbiz 8月）——替代供给出现 | **维持S-：售罄但边际不再收紧，替代路线（EMIB/OSAT）显形** |
| S5 | **ABF载板/积层膜** | **S 维持，信号升级（地缘维度新增）** | ①**味之素8-14宣布：对中国大陆ABF膜供应削减30%**（ChemNet 8-14；finance.biggo 8-17跟进）——95%份额+对华断供=地缘单点故障②ABF膜Q3'26提价~30%维持③欣兴3037今日（8-17）**+9.8%**、PER升至74.6——市场开始为断供定价④台系三雄7月营收：欣兴+43.7%/南电+50.2%/景硕+35.9%（月月加速）⑤BT载板+玻纤布拟涨20%（TrendForce 8月）——载板族涨价扩散 | **维持S，为六个环节中今日最强（TSMC点名+断供+量价齐升三重）** |
| A+ | **MOCVD/外延设备** | **A+ 维持** | Veeco年内InP设备订单>$250M维持（GlobeNewswire确认）；光模块市场2026预期$39B（StockTitan 8月）——设备订单与终端市场互验；Q1'26财报"mixed"（Investing.com）提醒订单≠收入 | **维持A+，等Q2'26订单连续性** |

### 新瓶颈扫描（过去7天）

| 环节 | 信号 | 来源/日期 | 判定 |
|------|------|----------|------|
| **高端MLCC** | AI服务器抽干高端MLCC：交期飙至**20周**、2H26大概率短缺、日韩厂BB ratio创疫情后新高、太阳诱电已涨价、**短缺可能拖到2028** | TrendForce / finance.biggo / Chosunbiz（8月上中旬） | **新增A级瓶颈**。但标的（村田6981.T/太阳诱电6976.T/三星电机）均大市值多元化，瓶颈纯正度低→投资相关性A- |
| **BT载板/特殊玻纤布** | AI景气+短缺下BT载板、玻纤布拟涨20% | TrendForce（8月） | **新增B+**（涨价扩散信号，非硬单点） |
| **FCC对华光模块禁令风险** | 禁令若落地将切断美国AI数据中心60%光模块供应；西方替代产能扩建反而依赖中国铟 | TechTimes 8-05 | **地缘变量**：若落地→S1/S2急剧升级+西方光模块商（AAOI/FN/COHR）订单重估；概率与时间未定，标注低置信 |
| 韩华ABF替代 | Hanwha E-ssential 2026年推出ABF膜挑战味之素垄断 | DigiTimes（8月） | 反向验证证据（见下表），非新瓶颈 |

---

## 二、vs 8-16 变化汇总（本轮核心增量）

1. **S5 ABF获"断供级"新证据**：味之素对华削减30%（8-14）——从"涨价瓶颈"升级为"地缘单点故障"；欣兴当日+9.8%说明市场正在定价。但注意：断供对象是中国大陆，对台/日/韩载板厂实为**利好**（需求外溢），对中国先进封装是打击。
2. **NAND从S3拆出降级A-**：TrendForce首次给出明确解除时点（供给增速2027超需求、2H27缓解）。**DRAM/HBM维持S**（2027售罄多源维持），存储内部结构分化：HBM/DRAM窗口到2027末，NAND窗口到2H27。这直接影响WDC/SNDK的瓶颈溢价时限。
3. **S1/S2证据链继续加固**：LITE CEO"比存储更严重"警告+缺口>30%两次重申+第5厂2028年中才投产（扩产周期实证>2年）+FCC禁令风险（低置信但方向性利好西方光链）。
4. **CoWoS替代路线显形**：Intel EMIB借紧张切入——S-降级趋势确认。
5. **MLCC为新发现的A级瓶颈**（交期20周、或拖至2028），但无可投资的纯瓶颈小市值标的。

---

## 三、机会看板排名表（强制估值检查完成）

美股=8-14收盘（stockanalysis.com，PS/PE为TTM口径）；台股=8-17收盘（twstock_data.py）；汇率NT$31.5/US$估算。

| 排名 | 公司 | 代码 | 市值 | 年收入(TTM) | PS | PE / fPE | 瓶颈环节 | 评级 | 最新增速 | 信号 | 估值判断 |
|------|------|------|------|------------|-----|----------|---------|------|---------|------|---------|
| 1 | Coherent | COHR | $63.8B | $7.12B | **9.0** | 79 / 35 | EML激光双寡头 | S1 | +34%（Q1'26） | ★★★★ | **合理偏低** |
| 2 | Veeco | VECO | $3.2B | $0.68B | **4.7** | 141 / **21.7** | InP MOCVD设备 | A+ | +17%转正 | ★★★★ | **合理** |
| 3 | Micron | MU | $1.10T | $90B | 12.2 | 21.9 / **6.8** | HBM/DRAM | S3 | +346% | ★★★ | **偏高（周期顶定价）** |
| 4 | SanDisk | SNDK | $244.5B | $20.2B | 12.1 | 22.3 / **7.6** | NAND（AI/eSSD） | A-（降级后） | NAND Q3 +40%价 | ★★★ | 偏高（fPE低但窗口2H27收窄） |
| 5 | Western Digital | WDC | $183.4B | $12.9B | 14.2 | **21.0 / 25.3** | HDD nearline（AI冷数据） | A- | 高位持平 | ★★★ | 合理偏贵（**fPE倒挂**：市场已预期盈利见顶回落） |
| 6 | 欣兴 Unimicron | 3037.TW | $58.4B | NT$1.42T(估) | ~7(估) | 74.6 / — | ABF载板全球第1-2 | S5 | +43.7%（7月） | ★★★ | 偏高（三雄中最便宜；今日+9.8%不追） |
| 7 | Fabrinet | FN | $20.4B | $4.2B | 4.8 | 49 / 33 | 1.6T光模块代工 | S1链 | +39% | ★★★ | 合理（绿-黄） |
| 8 | Amkor | AMKR | $14.7B | $7.4B | 2.0 | 26 / 22 | 先进封装OSAT | S4/S5 | +26% | ★★★★ | 低估（延续8-16） |
| 9 | Applied Opto. | AAOI | $12.7B | $0.60B | 21.3 | — / 49.9 | 垂直整合光模块（EML自制） | S1侧翼 | EML短缺免疫主题 | ★★ | **偏高（红灯边缘：PS>20且盈利薄）** |
| 10 | Lumentum | LITE | $82.1B | $3.01B | 27.2 | 亏 / 42.8 | EML份额第1 | S1 | +109% | ★★ | **透支（市值/TAM=234%）** |
| 11 | AXT | AXTI | $5.2B | $0.125B | 41.8 | 1139 / 51.5 | InP衬底第1 | S2 | +165% | ★★ | **透支（市值/TAM=437%）** |
| 12 | 南电 NanYa | 8046.TW | $26.6B | NT$434亿(估) | ~8(估) | **152** / — | ABF载板 | S5 | +50.2% | ★★ | 透支边缘 |
| 13 | 景硕 Kinsus | 3189.TW | $15.1B | NT$281亿(估) | ~9(估) | **168** / — | ABF/BT载板 | S5 | +35.9% | ★★ | 透支边缘 |
| — | 味之素 | 2802.T | ¥5,721/股 | — | — | — | ABF膜>95%份额 | S5核心 | 提价30%+断供红利 | ★★★ | 非美/日股账户可及性受限，仅备案 |

**红灯验算（financial_rigor.py）**：
- LITE：$82.06B ÷ 光学元件TAM ~$35B(2026E) = **234%**（红线：>20%）——增速+109%>100%可豁免PS规则，但TAM规则独立触发。10年25xPE退出检验：需净利$3.28B（当前TTM亏损/微利，TTM收入$3.01B×20%净利率=$0.6B）→ 0名义回报需净利CAGR 18.6%，10%年化需收入$42.5B（今天的14倍）→ **无安全边际**
- AXTI：$5.24B ÷ InP衬底TAM ~$1.2B(2028E，按JX 10x扩产反推) = **437%** → 红灯
- AAOI：PS 21.3 + fPE 49.9 + 毛利率仅28.9%（同业COHR 37.5%/LITE 44.6%）——EML免疫主题（8-04 TechTimes）已被市场计入，盈利质量不支撑
- WDC：fPE 25.3 > PE 21.0（**远期倒挂**=市场预期盈利见顶）——与TrendForce"NAND 2H27缓解"互验，HDD盈利顶部已在预期内
- MU/SNDK：fPE 6.8/7.6看似极低，但这是**周期股顶部特征**（远期EPS按峰值外推），黄灯不是绿灯
- 台股三雄：PER 75-168，营收+36~50%加速可部分解释，但南电/景硕PBR 17/10.7已计入2027-28盈利兑现

---

## 四、一页纸摘要（Top 3）

🎯 **Coherent（COHR）— S1 EML瓶颈中唯一"PS<10+盈利"的入口（延续并加固8-16判断）**
- 为什么是瓶颈：EML双寡头之一、NVIDIA $2B投资+多年采购承诺锁定（3-02）；LITE证实行业缺口>30%
- 为什么是这家：PS 8.96（LITE的1/3）、fPE 35.2、毛利率37.5%；10年25x退出需净利$2.55B（当前$0.81B，CAGR 12.2%即可保本，13.8%达10%年化）——S级环节中安全边际检验最轻的美股
- 本轮增量：NAND/存储链降级后，光学成为"瓶颈最硬+估值最低"组合的环节
- 风险：LITE宣称UHP领先2年；硅光/CPO长期泄压；FCC禁令若反转
- 结论：**值得深入研究（延续8-16触发区$280-300已兑现上移，现价$325.8不再追，回调挂单）**

🎯 **Veeco（VECO）— InP军备竞赛卖铲人，估值仍是设备股中最低档**
- 为什么是瓶颈：InP扩产必买MOCVD/IBD，年内订单>$250M、2026出货2027放量；光模块市场2026 $39B预期支撑终端
- 为什么是这家：PS 4.7 / fPE 21.7；10年25x退出需净利$128M（FY1预期$147M已超）——**唯一"FY1预期即覆盖保本线"的标的**
- 本轮增量：Q1'26"mixed"财报提示订单→收入有时滞，需Q2订单连续性
- 风险：设备=一次性capex，2028扩产潮后回归周期；TTM PE 141仍微利
- 结论：**维持观察名单首位，Q2'26财报（8月底）是加仓/放弃决策点**

🎯 **Micron（MU）— S3 HBM维持S但价格已按周期顶定价；只挂单不追（纪律延续）**
- 为什么是瓶颈：2027年DRAM+HBM售罄维持多源确认；DRAM $20/颗创纪录、Q3合约+30%
- 为什么是这家：HBM三强、fPE 6.8、毛利率72.6%；PE 21.9<25意味着"盈利零增长十年也有正回报"的静态安全垫
- 本轮增量（利空）：TrendForce明确NAND 2H27缓解+消费端承受力见顶——存储族内部分化，DRAM/HBM窗口到2027末但**市场已在预定价2028供给潮**（memory股"售罄中下跌"悖论维持）
- 风险：2028三厂+长鑫供给潮；fPE 6.8按峰值EPS外推的周期陷阱
- 结论：**维持8-15/8-16纪律：挂单$780-850，不追现价$971.7**

---

## 五、反向验证：每个瓶颈如何被绕过 / 何时解除

| 瓶颈 | 绕过路线 | 解除时点 | 证据 |
|------|---------|---------|------|
| S1 EML/CW激光 | ①硅光/CPO（但光源仍需InP——只泄压不解除）②NVIDIA扶持第二来源（已投Scintil/Ayar）③TSMC COUPE把CW激光集成进代工（3年+）④AAOI等垂直整合自制DFB | LITE第5厂2028年中+COHR扩产→2027末-2028初逐步正常化 | XenoSpectrum 8-03：扩产措施"2026-2028年陆续见效" |
| S2 InP衬底 | ①JX 10倍/住友3.1倍/AXT翻倍扩产（2027-28落地）②6英寸化降本 ③Fraunhofer InP-on-GaAs ④中国云南锗业系进入 | 2027-28（经典"短缺→过剩"剧本，参考2021-23 GaAs） | JX 6-16公告/TrendForce 8-06 |
| S3 HBM/DRAM | 2028供给潮：三星P4/海力士M15X/美光爱达荷+纽约/长鑫 | DRAM/HBM：2027售罄后2028松动 | TradingKey 8-04/GS |
| S3' NAND（降级后） | 供给增速2027超需求 | **2H27明确缓解**（TrendForce本轮新证） | TrendForce 8月 |
| S4 CoWoS | TSMC 35k→130k wpm（2026末）；Intel EMIB切入；Amkor/日月光承接外溢 | 2027（TSMC自认接近需求） | TechTimes/247wallst 8月 |
| S5 ABF | ①韩华E-ssential 2026进入（首个人工第二源）②中国莲花控股1.03亿元投资国产ABF（8-17）③玻璃基板2028+ | 2027-28（韩华爬坡+国产替代）；断供反而延长非中国买家的紧张 | DigiTimes/finance.biggo 8-17 |
| A+ MOCVD | 无需绕过（设备端受益于所有扩产）；风险是订单2028后枯竭 | 扩产潮结束即周期回落（2028） | Veeco IR |
| A MLCC（新） | 村田/太诱/三星电机扩产+涨价触发需求端工程变更降规格 | 2027-2028 | TrendForce/biggo 8月 |

**聪明人为什么不买（各环节bearish一句版）**：S1——LITE市值已是TAM的2.3倍，买LITE=为2028年解除后的世界付今天的钱；S2——AXTI 437% TAM同前；S3——fPE<7是周期顶外推，2028供给潮是明牌；S4——TSMC自己说接近平衡；S5——台股三雄PER 75-168已把2027盈利兑现计入；A+——设备订单是一次性的。

---

## 六、行动建议

| 标的 | 建议动作 | 理由 |
|------|---------|------|
| COHR | 深入研究维持；现价$325.8不追，回调$280-300挂单 | S级瓶颈×最低PS入口×安全边际检验最轻 |
| VECO | 观察名单首位；8月底Q2财报为决策点 | fPE 21.7+订单能见度，等收入连续性 |
| MU | 仅挂单$780-850，不追$971 | 周期顶纪律（LRN-012延续） |
| SNDK | 观察不追 | NAND瓶颈2H27解除已被TrendForce明示，fPE 7.6是峰值外推 |
| WDC | 观察不追 | fPE倒挂=盈利见顶预期内生化 |
| 欣兴3037 | 观察；今日+9.8%后不追，等月营收连续性（8月营收9-10披露） | S5最强但PER 74.6已计入较多 |
| AMKR/FN | 维持8-16判断（低估/合理） | 本轮无新负面证据 |
| LITE/AXTI/AAOI/南电/景硕 | 暂不追踪（红灯/透支） | 瓶颈最硬=估值最满，纪律执行 |
| MLCC（村田/太诱） | 备案观察 | 新A级瓶颈但无纯正小市值标的 |

## 七、来源清单（本轮新增）

- S1/S2：[XenoSpectrum：LITE警告InP危机"比存储更严重"、缺口>30%、Greensboro 2028年中](https://xenospectrum.com/en/lumentum-inp-ai-optics-shortage/)（8-03）；[MLQ：LITE需求超供给30%](https://mlq.ai/news/lumentum-says-ai-laser-demand-exceeds-supply-by-more-than-30-as-inp-capacity-lags/)；[Yahoo Finance：CEO预测"bigger than memory"](https://finance.yahoo.com/technology/ai/articles/ai-shortage-coming-one-ceo-145315907.html)；[Reuters：中国InP出口管制](https://www.reuters.com/)；[finance.biggo：InP价格Q4再涨10%+创纪录、买家"cash-rich but empty-handed"](https://finance.biggo.com/)
- S3存储：[TweakTown：2027 DRAM+HBM全部售罄](https://www.tweaktown.com/)；[TrendForce：NAND供给2027超需求、2H27缓解](https://www.trendforce.com/)；[TechPowerUp：NAND短缺2027终结](https://www.techpowerup.com/)；[Tom's Hardware：涨价触承受力上限但Q3仍涨](https://www.tomshardware.com/)；[Wccftech：ADATA Q3 DRAM+30%/NAND+40%](https://wccftech.com/)；[tech-insider：DRAM $20/颗、RAM +63%](https://tech-insider.org/)
- S4/S5封装：[ChemNet：味之素对华ABF削减30%（8-14）](https://news.google.com/rss/articles/CBMiUEFVX3lxTE1qSUhzTThNTjNDdEhrUHdyaURZOWdRVy1VaG04SWVCS0dWS1VBaGYyamRvdnpFSzhQQVZ5WkM5T2NlVGNTYVVxOTJ4MjR3UDU3?oc=5)；[finance.biggo：莲花控股1.03亿元国产替代（8-17）](https://finance.biggo.com/)；[DigiTimes：韩华2026挑战ABF垄断](https://www.digitimes.com/)；[TechTimes：TSMC警告AI芯片短缺持续数年](https://www.techtimes.com/)；[247wallst/Chosunbiz：Intel EMIB借CoWoS紧张切入](https://247wallst.com/)；[TrendForce：BT载板+玻纤拟涨20%](https://www.trendforce.com/)
- MLCC新瓶颈：[TrendForce：高端MLCC BB ratio疫情后新高、2H26短缺风险](https://www.trendforce.com/)；[finance.biggo：交期20周、或拖至2028](https://finance.biggo.com/)；[Chosunbiz：太阳诱电涨价](https://www.chosunbiz.com)
- 地缘：[TechTimes：FCC对华光模块禁令将切60%供应、西方替代需中国铟（8-05）](https://www.techtimes.com/articles/322942/20260804/applied-optoelectronics-stock-climbs-eml-shortage-immunity-before-q2-report.htm)
- 行情：stockanalysis.com（美股8-14收盘）；FinMind via tools/twstock_data.py（台股8-17收盘）；Yahoo via fetch_quotes.py（日股2802.T ¥5,721 / 4062.T ¥21,580 / 5016.T ¥4,000，8-14收盘）

**信息充分度自评**：行业格局A（8次搜索多源交叉，关键断供事件有双源+日期）｜估值A（美股8只全字段+台股3只当日实时PER）｜瓶颈解除时点B+（NAND首次有明确时点2H27；InP/EML仍为区间估计）｜MLCC细节B（交期/涨价有多源，份额数据未逐厂核实）｜FCC禁令概率C（仅单源，标注低置信）
