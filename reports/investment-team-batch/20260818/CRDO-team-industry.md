# CRDO 四大师验证 · 行业维度（芒格视角）——AEC/光模块/CPO 技术路线竞争

- **日期**：2026-08-18（周二，美东尾盘；本机 2026-08-19 凌晨完成）
- **数据截止**：2026-08-18 美股尾盘行情 + 当日新闻
- **角色**：AI Berkshire 行业研究员（芒格视角），v5.4 调仓执行 · CRDO 单维度验证，不复用旧结论
- **当日关键行情**（Yahoo Finance，尾盘）：CRDO $243.49（**-13.9%**，前收 $282.82；52周区间 $86.49–308.67）｜COHR -12.1%｜MRVL -8.8%｜AVGO -3.4%｜NVDA -2.4%｜纳指 -1.31%
- **检索通道**：curl（Google News RSS / Yahoo API）15+ 次查询 + 10+ 篇正文抓取，双源验证关键数字；缺口在文末标注

---

## 一、今日光模块暴跌对 AEC 的含义：同跌，不是利好，也不是路线证伪

**结论先行：今日是「利率 + AI 货币化预期修正 + 拥挤仓位去化」的系统性杀估值，AEC 与光模块属于同一个「AI 互连 beta」，同跌且 CRDO 跌得更深（-13.9% vs COHR -12.1%）。市场没有在铜与光之间做切换投票。**

暴跌三重触发（24/7 Wall St 当日两篇 + IBD 实时直播，双源一致）：

1. **Anthropic ARR 低于耳语**：周末 Anthropic 告知投资者 7 月底年化收入 $65B，低于 Gavin Baker 在 All-In Podcast 透露的 $80B+ 耳语；Reuters 报道 Anthropic 自估 2028 年收入 $190–200B，同样低于 Baker/David Sacks 预期的 $400–500B exit ARR。AI 收入端的"证伪压力"直接打击 AI 硬件支出预期。
2. **WSJ 表外承诺报道**：九大科技公司持有约 **$3 万亿表外承诺**（多为 AI 相关），增速快于传统 capex（过去一年约 $600B），约为租赁+长期借款的 3 倍。AI 支出的"表外杠杆化"引发可持续性担忧——而这笔钱"正是喂饱光模块/互连供应链的钱"。
3. **Fabrinet 财报"好但减速"**：FY26Q4 营收 $1.316B（+45% YoY）创纪录、non-GAAP EPS $4.10（上年 $2.65），但 Q1 指引 $1.375–1.425B 仅隐含温和环比增长；叠加 $56.7M 非上市股权损失、FCF -$36.9M。股价 **-20.85%**（收 $473.80），创六季最大财报日跌幅（约为历史平均的 2.2 倍），拖累 MRVL -8%、APH -7%、COHR -12%、LITE -10.1%、GLW -8.2%、AXTI -14.9%。
4. **利率背景**：30 年期美债收益率周一触及 5.31%（多年新高），10Y 4.7%，压制长久期成长股。

**芒格式判读**：注意昨天（8/17）还在涨——"AI 网络股周一大涨：Marvell +8%、Credo +8.82%（收 $282.82）、Ciena 跟涨"（24/7 Wall St + Insider Monkey 双源）。48 小时内 +8.8% → -13.9%，基本面什么都没变。变的是人的情绪和仓位。这不是产业信号，是市场先生日常报价。**铜与光的产业竞争格局，今天一天没有发生任何变化。**

对 AEC 路线的真正含义（分三层）：
- **短期（本周）**：无独立利好。CRDO 是 AI 互连高 beta 品种，光模块跌它跌更多；9/1 财报前波动放大。
- **中期（结构性）**：光模块暴跌的深层焦虑是 NVIDIA 转 CPO/LPO 后可插拔光模块的份额问题（见第三节）——这个焦虑不伤铜，反衬机柜内铜的地位在 Rubin 世代更稳固。
- **逆向信号**：光链（COHR/LITE/FN）过去一年涨 276%/736% 后的预期出清，与 CRDO forward P/S 18.09（行业 5.36，Zacks）共享同一个"高估值脆弱性"。同跌提醒我们：这不是"谁赢谁输"的市场，是"钱从 AI 硬件撤出"的市场。

---

## 二、物理分层：AEC vs 可插拔光模块 vs CPO 的"轨距"之争

技术分层（SemiVision《The AI Interconnect War: Copper Fights Back Against Optics》2026-03-13，与 Counterpoint 交叉验证）：

| 介质 | 原理 | 有效距离（224G 时代） | 功耗/成本特征 | 阵营 |
|---|---|---|---|---|
| PCB 走线 | 板内 | 厘米级 | 最低 | 所有 |
| DAC（无源铜） | 纯铜+连接器 | **~1m 或更短** | 最便宜、零 DSP 功耗 | NVIDIA NVL 机柜背板 |
| ACC（有源铜） | 两端线性均衡器 | ~2–2.5m（1.6T ACC 约 2.5W） | 低功耗、均衡能力有限 | Astera 等 |
| **AEC（有源电缆）** | 内嵌 DSP/retimer 补偿插损 | 机柜内/相邻机柜短距 | "用 DSP 买距离"；400G/800G 最广泛量产方案 | **Credo**（垂直整合）、Marvell（DSP 供线缆商） |
| AOC（有源光缆） | 两端光收发 | 5–30m | 贵、功耗高，短距不经济 | 传统光阵营 |
| 可插拔光模块 | OSFP 等 | 机柜间/集群 | 800G/1.6T 主力；DSP 功耗是瓶颈 | 中际旭创/Coherent/Fabrinet 代工 |
| LPO（线性直驱光） | 去 DSP、靠交换机侧均衡 | 中距 | 省约 25–30% 功耗 | Rubin 世代 NIC 端方向 |
| CPO（共封装光学） | 光引擎与交换 ASIC 同基板 | 跨柜/远距 | 每 bit 能耗最低；贵、良率难 | NVIDIA Quantum-X/Spectrum-X、Broadcom |

**芒格第一性原理**：这场"路线之争"其实是物理常识——**短距用铜（便宜、低功耗、低延迟），长距用光（无衰减上限）**。争议从来不是"谁消灭谁"，而是**边界线画在哪一米**。224G SerDes 每代把铜的可达距离砍半，于是边界线向铜内侧移动；CPO 把光的功耗砍半，于是边界线向光侧移动。两边都在蚕食"可插拔光模块"这个中间地带——这就是 2026 年真正的产业叙事：**不是铜 vs 光，而是"半导体化的互连"（DSP/retimer/硅光）vs "传统分立互连"**。

---

## 三、NVIDIA Rubin 世代的互连选择（决定 AEC 需求的主变量）

NVIDIA 官方技术博客《Vera Rubin POD》（2026-03-16）+ Counterpoint《From Blackwell to Feynman》（2026-04-02）双源：

**Vera Rubin POD 全景**：40 机柜、1.2 千万亿晶体管、约 20,000 颗 die、1,152 颗 Rubin GPU、60 EF、10 PB/s 总 scale-up 带宽；2H 2026 出货。五种机柜：VR NVL72（计算）、LPX 推理柜（256 LPU）、Vera CPU 柜、BlueField-4 存储、Spectrum-6 网络柜（102.4 Tb/s、512 lane、200G CPO）。

**三阶段路线图（关键）**：

1. **Blackwell/Blackwell Ultra（现在）**：GB200/300 NVL72 机柜内铜（NVLink spine = 4 个预集成铜缆 cartridge，约 5,000 根铜缆、2 英里长）；scale-out 用可插拔光模块；Ultra 世代 CPO 交换机（Quantum-X800/Spectrum-X800，144×800G）成为"性能首选"。
2. **Vera Rubin（2H26 出货）**：**机柜内继续全铜**——第六代 NVLink 3.6 TB/s/GPU、260 TB/s/柜；跨柜 NVL576（8 柜）改用 **CPO 化 NVLink6 交换机**（微环调制器+远程激光器+OSFP-XD）；scale-out NIC 端转向 **LPO**（DSP 移入 NIC/交换机）。
3. **Feynman（2028）**：**scale-up 原生 CPO**——硅光集成到 GPU 封装（初代用远程激光器保可靠性），约 2,304-GPU 全光 pod；scale-out 1.6→3.2 Tb/s（ConnectX-10）；NVLink8 可能是 CPO 电分组交换/OCS/混合（NVIDIA 已与 Lumentum 签 **$2B** OCS/MEMS 协议、与 Marvell 结盟）。同时 NVIDIA 在 OFC26 发起 **OCI MSA** 开放标准（Gen1 4 波长、Gen2 8 波长），自建供应链话语权。

**对供应商的含义（Counterpoint 原文观点）**：可插拔光模块厂商将逐步被挤出插座，机会退守为 OCI 标准下的第二源部件（激光器/光纤/连接器）；**铜在 Vera Rubin 世代（机柜内）地位稳固，但 Feynman 世代光上 scale-up + 铜的物理极限构成 2028 年后的长期压缩**。

**AEC 在此格局中的真实位置**（必须诚实）：NVIDIA NVL 机柜内用的是 **DAC+cartridge 背板**（被动铜），不是 AEC。Credo 的 AEC 主战场是 **hyperscaler 以太网生态**（Google/Meta/AWS 等非 NV 专属集群的机柜内/相邻机柜短距以太网互连）——恰恰是 Broadcom Tomahawk 交换芯片的地盘，也是 OpenAI/Anthropic 等自建以太网集群（超以太网联盟 UEC 路线）的地盘。**NVDA 转 CPO 主要威胁的是可插拔光模块厂商；AEC 的威胁来自 Broadcom 生态（见第四节）。** 这也解释了今日盘面：光模块（NV 链）跌 12–20%，CRDO（以太网链）跌 13.9%——同跌是 beta，跌幅接近是因为估值都贵。

---

## 四、Broadcom 进入 AEC 的威胁时间表

可验证证据（弱，已标注）：
- **IP 层面已在场内（单一来源，需谨慎）**：雪球 2025-08-27 帖提及"credo 年初发起的对 aph（Amphenol）联合诉讼……aec 这块最早是 credo 联合博通"——即 Credo 与 Broadcom 曾就 AEC 专利对 Amphenol 联合维权。若属实，**Broadcom 已持有 AEC 相关专利组合，"从 IP 到产品"只差商业决策**。【缺口：诉状原文未核，标为低置信度】
- **能力层面毋庸置疑**：Broadcom 拥有业界最强的 224G SerDes 与 Tomahawk 6（支持长距 DAC）、Jericho 机架规模交换，2026-03-12 OFC 2026 官方新闻稿标题为"Broadcom Showcases Industry-Leading Solutions for Scaling AI Infrastructure"。【缺口：正文被反爬拦截，未确认是否包含 AEC/retimer 新品】
- **产品层面：截至 2026-08-18，公开可检索范围内没有"博通品牌 AEC 量产"公告**。当前 AEC 竞争格局：Credo（垂直整合：自研 DSP+自产电缆，份额领先）、Marvell（向线缆商供 AEC DSP）、Astera Labs（ACC/AEC）、Amphenol/Molex（组装）。

**威胁时间表（芒格式推断，标注为观点而非事实）**：

| 时间窗 | 观察点 | 信号 |
|---|---|---|
| 2026H2 | 9/2 AVGO 财报电话；10 月 OCP 峰会 | 管理层是否点名"互连/铜缆"为新营收支柱；是否发布 Tomahawk 配套 retimer/AEC 参考设计 |
| 2027H1 | OFC 2027（3 月） | 是否官宣 AEC DSP 或交换机+AEC 捆绑方案 |
| 2027H2 起 | 财务交叉验证 | CRDO 毛利率跌破 65%（FY26 为 68.1%）或 hyperscaler 订单分流，即为份额被侵蚀的硬信号 |
| 缓冲因素 | — | Broadcom 重心在 $70B AI 网络市场的交换机+定制 XPU 大盘（Morgan Stanley 口径，经富途/Moomoo 转述），AEC 市场（CRDO FY27 铜线收入约 $1B+ 量级）对其收入弹性小；Credo 的垂直整合成本优势+ZeroFlap 可靠性数据是换供应商的摩擦成本 |

**反过来想**：杀死 AEC 的从来不是光，是三件事——(1) SerDes 被集成进交换机/GPU 封装（消灭独立 retimer），NVIDIA Feynman 正在做；(2) Broadcom/Marvell 价格战，未发生；(3) 铜的物理极限在 448G 时代（约 2028+）把 AEC 也推出机柜。**三个杀手都在 2028 年前后到期**——这给了 Credo 约 6-8 个季度的窗口期去完成"铜→光（>$600M 光收入目标）→scale-in（OmniConnect）"的平台化转型。

---

## 五、Scale-up / Scale-out / Scale-in 演变与 Credo 的卡位

1. **Scale-up（机柜内/跨柜成"一颗大 GPU"）**：NVLink6 铜主内（NVL72）、CPO 主跨柜（NVL576）；以太网阵营（UEC/博通）用交换机+DAC/AEC 组网追赶。AEC 的机会在以太网 scale-up：224G 时代 DAC 只剩 ~1m，相邻机柜（2-4m）就是 AEC 的独占领地。
2. **Scale-out（集群间）**：Rubin 世代 NIC 端 LPO 化、交换机端 CPO 化——可插拔光模块份额承压，但总带宽随 pod 规模（NVL72→576→1152→2304）指数扩张，**量增对冲份额减**。
3. **Scale-in（新兴维度，Credo 主动开辟）**：2026-08-10 Credo 宣布向 OCP 捐赠 **OmniConnect scale-in 互连方案**，发起 OCP 开放芯粒经济（OCE）轻量串行互连（LSI）工作流，瞄准推理"内存墙"：内存解聚合+芯粒到芯粒通信，缓解对 HBM 的依赖（Credo 官网新闻室）。这是把"互连"从机柜间推进到封装/内存层级——如果 LSI 成为 OCP 标准，Credo 从"卖电缆的"升级为"定义轨距的"。
4. **市场量级**：Morgan Stanley 测算 AI 网络市场迈向 **$70B**，铜缆"仍在收割早期红利"（富途/Moomoo 转述，正文未读，标为单一转述源）。CRDO FY27 收入指引增速 >80%，其中光产品 >$600M（ZeroFlap 光模块、硅光 PIC、光 DSP 各 $100M+），**增量约一半来自光、一半来自铜（AEC+retimer）**——公司自身已对冲"单路线风险"。

---

## 六、CRDO 基本面快照（行业维度所需最小集）

- Q4 FY26（截至 2026 年 5 月）：营收 $437M（+157% YoY）、净利 $169M（+362%）；non-GAAP 毛利率 68.3%、经营利润率 49.6%、净利率 51.9%
- FY26 全年：营收 $1.3B（+206%）、毛利率 68.1%
- Q1 FY27 指引（9/1 公布实际值）：营收 $465–475M（隐含 +108–113% YoY）、GAAP GM 66.9–68.9%、non-GAAP GM 67–69%、opex $86–90M
- FY27 展望（Zacks 综合）：收入 +80% 以上、毛利率大致持平、non-GAAP 净利率 ~50%、opex +50%（低于收入增速）
- 卖方：BofA $340、Stifel $350、Barclays $300、TD Cowen **今日暴跌中**上调至 $300（自 $260）、Evercore ISI 初覆 Outperform（$325）、GS $250、JPM $250、Mizuho $290、Susquehanna $250；Zacks Rank #3（Hold）；对冲基金 Q1'26 持仓 59 家（环比 69 家减少）、合计 $1.9B（-24%）
- 空头论点时间线（Seeking Alpha 标题链）：2026-02-04《AI 与 Credo 的铜缆正在"分手"》（光威胁论）→ 04-12《"光学威胁"创造了我梦寐以求的买入机会》→ 05-20《不合时宜的逆转是大警告》→ 06-12《不要追着赢家跳崖》→ 06-17《断裂点可能越来越近》。**多空分歧点恰好就是本报告的主题：铜的窗口期还剩多长。**

---

## 七、十年格局推演（芒格视角）

**反过来想，总是反过来想**：假设 2035 年回望，AI 集群互连会是什么样？
- 物理定律不变：机柜内（<3m）只要功率密度允许就永远是铜的（成本/功耗/延迟三杀光）；跨柜和楼层间是光的（CPO/光背板）；数据中心间是相干光+波分。**分层共存是终局，不是某条路线一统江湖。**
- 但"产品形态"会换代：DAC→AEC→（448G 时代）背板 retimer+光背板混合；可插拔光模块→LPO/CPO。**每一代换形态，就重新洗一次牌**——过去 10 年每次洗牌都把 SerDes/DSP 能力最强者推上台（Broadcom 拿走交换机，Credo 拿走 AEC，NVDA 正在拿走 CPO）。
- NVIDIA 的垂直整合（自研 CPO+OCI 标准+$2B Lumentum/Marvell 协议）是所有第三方互连厂商头上的长期利率——**它不消灭供应商，它消灭供应商的定价权**。
- Credo 的十年赌注：从"AEC 单品"变成"铜+光+scale-in 全互连平台"（FY27 光收入 >$600M、OmniConnect 进 OCP）。若成功，它就是以太网生态（Google/Meta/AWS/自建集群）对抗 NV 一体化的"军火商"；若失败，2028-2030 年被 Broadcom（以太网侧）与 Feynman CPO（NV 侧）双向挤压，退回利基。
- **Lollapalooza 提醒**：当下对 CRDO 有利因素在汇聚（Rubin 2H26 出货、以太网 scale-up 兴起、光收入放量、今日 TD Cowen 逆势上调目标价），但 18x forward P/S 需要连续多个 80%+ 增长季度来喂养——**好公司≠任何价格都好**。芒格会说：用 $244 买一门 68% 毛利率、50% 净利率、还能翻倍增长的生意，需要确信的不是增长率，而是"窗口期长于市场定价的隐含假设"。

---

## 八、1–6 个月催化剂表

| 日期 | 事件 | 对 CRDO/AEC 的看点 | 方向 |
|---|---|---|---|
| 8/19–8/22 | 暴跌后企稳与否 | 30Y 美债能否回落至 5.3% 下方；Anthropic/WSJ $3T 叙事发酵程度 | 双向 |
| **8/26（三）** | **NVDA Q2 FY27 财报**（7/29 官宣日历） | Rubin 2H26 出货爬坡表述；网络收入（NVLink/Spectrum-X/IB）；CPO 进度；BofA 称可能开启"多季度上调周期"；$733B AI 支出背景 | 偏正面 |
| 8/27（四） | MRVL 财报 | 以太网互连增速是否持续跑赢定制硅（AEC DSP 需求佐证） | 偏正面 |
| **9/1（二，盘后）** | **CRDO Q1 FY27 财报** | 实际 vs 指引 $465–475M/GM 67–69%；Q2 指引（验证 H2 inflection）；光收入 >$600M 路径；管理层对 Broadcom/竞争的回应；3 大客户集中度 | 高波动、双向 |
| **9/2（三）** | **AVGO Q3 FY26 财报**（8/3 官宣） | 定制 XPU+网络（AI 需贡献约 72% 增长）；是否提及铜缆/retimer/AEC 布局——**Broadcom 威胁时间表的第一个官方观察点** | 双向（对 AEC 或偏威胁） |
| 10 月（预计） | OCP Global Summit 2026 | OmniConnect scale-in/LSI 工作流进展；Broadcom 是否发布 AEC/retimer 产品；UEC 规范演进 | 双向 |
| 11–12 月 | Vera Rubin NVL72 出货爬坡 | 机柜内铜用量兑现；以太网 scale-up 招标（AEC 订单能见度） | 偏正面 |
| 2027H1（3 月） | OFC 2027 | CPO/LPO 规模化节奏（光阵营对铜的边界挤压速度）；CRDO 光产品（ZeroFlap/PIC/光 DSP）进展 | 双向 |

---

## 九、行业维度评分（芒格视角，10 分制）

**7 / 10**

| 子项 | 分 | 理由 |
|---|---|---|
| 赛道空间与持续性 | 8 | AI 网络 $70B（MS 口径）；GPU 越多互连越多，互连密度随 SerDes 代际翻倍——需求侧是物理学驱动的长坡 |
| 路线地位（AEC 短中期） | 7.5 | 224G 时代 DAC 缩短至 ~1m，AEC 独占 1–4m 机柜/邻柜生态位；Rubin 机柜内全铜背书；但 448G 后（2028+）边界收缩 |
| 竞争格局 | 5.5 | Broadcom 能力在而产品未至（悬顶之剑）；Marvell/Astera 贴身；NVIDIA 垂直整合压缩长期定价权 |
| 公司卡位（行业维度内的 CRDO） | 8 | 垂直整合+68% 毛利率验证议价力；铜+光+scale-in 三线对冲单路线风险 |
| 估值容错（行业研究员只提一句） | 5 | 18x forward P/S 已计入大量乐观预期，行业再好也买不出安全边际 |

**一句话（芒格式）**：这是一个"边界由物理定律划定、赢家由 SerDes 能力决定"的好行业里的好卡位，但窗口期（到 2028 年 Feynman/448G 换代）与估值容错同时在倒数——**今日暴跌没有改变任何产业事实，只是把"市场先生愿意付的价格"从荒谬降到了昂贵。**

---

## 十、数据缺口与来源声明

**缺口（诚实标注）**：
1. Broadcom OFC 2026 新闻稿正文被反爬拦截（403），未能确认其 AEC/retimer 产品细节——Broadcom 威胁时间表含推断成分；
2. "Credo+博通联合诉 Amphenol"仅雪球单一转述源，未核对诉状原文，低置信度；
3. Morgan Stanley $70B AI 网络市场测算为富途/Moomoo 中文转述，原报告未读；
4. CRDO 股本/精确市值未能从 Yahoo API 取得（按 ~1.68 亿股估算市值约 $41B，单源估算）；
5. NVDA 财报精确日期 8/26 未从新闻稿原文直接确认（7/29 官宣存在 + 多篇预览称"下周"，周三 8/26 与历次节奏一致——高置信但非一手）；
6. 部分 Seeking Alpha 空头文章仅有标题（付费墙），论点以标题+Zacks 交叉推断。

**主要来源**（关键数字双源验证）：
- 24/7 Wall St（8/18 两篇：Optics Stocks Drop on Anthropic News；Fabrinet Drops After Earnings）+ Yahoo Finance/IBD 实时直播（跌幅互证）
- Yahoo Finance API（CRDO/NVDA/AVGO/MRVL/COHR 价格；Insider Monkey 财报前瞻；AVGO 9/2 官宣）
- NVIDIA Developer Blog《Vera Rubin POD》（2026-03-16）+ Counterpoint Research《From Blackwell to Feynman》（2026-04-02）+ SemiVision Substack《The AI Interconnect War》（2026-03-13）（路线图三源交叉）
- Zacks（FY27 展望）、stockanalysis.com/TipRanks（目标价与 OmniConnect 公告索引）、Credo 官网新闻室（OmniConnect/OCP）
- 行情数据截止 2026-08-18 美东尾盘；本报告为学习研究用途，非投资建议。
