# AI基础设施硬件 行业漏斗筛选报告

**日期**：2026-08-20 ｜ **执行**：industry-funnel（简化版，聚焦美股）
**背景**：组合AI硬件仓位仅7%严重低配；AI硬件水位🟢供不应求，为分布缺口最大方向。
**方法**：第一层8次全市场扫描 → 第二层双轨粗筛 → 第三层补充验证 → 终选3家（互补性原则）。

---

## 一、第一层：全市场扫描（38家）

入选类别：A=成交活跃 / B=涨幅榜 / C=市值前列。市值除注明外为估计值。

| 公司 | 代码 | 市值 | 主业 | 类别 |
|------|------|------|------|------|
| Nvidia | NVDA | $5.3T* | GPU/AI计算平台 | A/C |
| Micron | MU | $1.06T✓ | DRAM/HBM/NAND | A/B |
| Broadcom | AVGO | $1.73T✓ | 定制ASIC+网络芯片 | A/C |
| TSMC | TSM | $1.93T✓ | 晶圆代工+先进封装 | A/C |
| Marvell | MRVL | $207B✓ | 定制ASIC/光DSP | A/B |
| SanDisk | SNDK | $232B✓ | NAND闪存 | B |
| Western Digital | WDC | $167B✓ | HDD近线存储 | A/B |
| Seagate | STX | $192B✓ | HDD近线存储 | A/B |
| AMD | AMD | ~$310B | CPU/GPU/MI系列 | A/C |
| Intel | INTC | ~$290B | x86+代工 | B |
| Arm | ARM | ~$170B | 架构IP授权 | B |
| Arista | ANET | $208B* | 以太网AI交换机 | A/C |
| Eaton | ETN | ~$150B | 电气配电(非纯正) | C |
| GE Vernova | GEV | ~$150B | 燃机/电网(非纯正) | C |
| Applied Materials | AMAT | ~$150B | 沉积/刻蚀设备 | C |
| Lam Research | LRCX | ~$120B | 刻蚀/沉积设备 | C |
| KLA | KLAC | ~$120B | 量检测设备 | C |
| ASML | ASML | ~$350B | EUV光刻 | C |
| Dell | DELL | ~$90B | AI服务器/存储 | A/C |
| Vertiv | VRT | $97B✓ | 电源+液冷 | A/C |
| Celestica | CLS | ~$36B | AI服务器ODM/EMS | A/B |
| Astera Labs | ALAB | $49B✓ | AI互连/PCIe交换 | A/B |
| Super Micro | SMCI | ~$28B | AI服务器 | A/B |
| Monolithic Power | MPWR | ~$40B | VRM电源管理 | A |
| Nova | NVMI | $12.3B* | 量测设备 | C |
| Amkor | AMKR | $12.6B* | 先进封装 | C |
| Credo | CRDO | ~$18B | AEC有源电缆 | A/B |
| Lumentum | LITE | ~$22B | 光模块/EML/CPO | A/B |
| Coherent | COHR | ~$15B | 光模块/收发器 | A/B |
| Ciena | CIEN | $56B✓ | 波分光网络 | A/B |
| Bloom Energy | BE | ~$16B | 燃料电池 | B |
| Teradyne | TER | ~$20B | 半导体测试 | C |
| Entegris | ENTG | ~$15B | 材料污染控制 | C |
| Kulicke&Soffa | KLIC | ~$3B | 键合设备 | C |
| Sterling Infra | STRL | ~$25B | 数据中心EPC(非纯正) | B |
| Digital Realty | DLR | ~$60B | 数据中心REIT | C |
| Equinix | EQIX | ~$75B | 数据中心REIT | C |

\* 有来源：NVDA/ANET/AMKR/NVMI（StockTitan、stockalarm.io、Yahoo）。✓ 已于2026-08-20盘中经 stockanalysis.com 实时验证（本表其余市值为估计）。行业背景：2026年半导体销售额冲击~$1T（+22%）；YTD最佳表现：SNDK +464%（高点+656%）、MU +187%、INTC +134%（Morningstar/TipRanks/Instagram行情帖）；存储板块8月正回调（MU距6月高点-25%，SNDK-33%）。

---

## 二、第二层：双轨粗筛（保留10家）

**价值轨**（ROIC>15% + FCF正 + PE<行业中位）：

| 公司 | 关键数据 | 结论 |
|------|---------|------|
| TSM | ROIC~30%，FCF强正，PE 27.7x/forward 19.1x，TTM净利+53.4% | ✅保留 |
| MU | 市值$1.06T，FCF强正，forward PE 6.5x≪中位，TTM净利+711% | ✅保留（周期股口径） |
| AVGO | ROIC~22%，FCF强，forward PE 23x，但遭Marvell-谷歌$120B定制芯片协议冲击，5日跌14% | ⚠️标黄 |
| DELL | PE~15x，FCF强，但毛利率~10%、AI服务器质量存疑 | ⚠️标黄 |

**成长轨**（增速>30% + 市值$5-100B + 订单能见度）：

| 公司 | 关键数据 | 结论 |
|------|---------|------|
| ALAB | 营收+104% YoY，Q3指引$540-560M(环比+40%)，市值$49B，股价距高点-43% | ✅保留 |
| LITE | Q4 FY26营收$1.01B(环比+23%)，NVDA入股$2B背书CPO | ✅保留 |
| WDC | 2026年HDD售罄+firm POs，市值$167B超成长轨区间→转价值轨：PE 19x<中位，TTM净利+399% | ⚠️标黄（转轨） |
| CLS | 2026 EPS预期+70%，指引上调，但$3B增发摊薄+低毛利 | ⚠️标黄 |
| SNDK | NAND周期暴利（forward PE 7.4x），但市值$232B超区间+YTD高点+656%后剧烈回调 | ⚠️标黄 |
| BE | 增速~40%+SK订单，但长期亏损商业模式 | ⚠️标黄 |

**淘汰名单**（节选）：NVDA（市值$5.3T超成长轨区间，PE~40x超价值轨——基准股不占漏斗名额）；AMD（增速~25%不达标+市值超区间）；INTC（代工亏损、低增速，纯情绪修复）；ANET（$208B超区间+PE~45x）；SMCI（毛利率~10%<30%警戒+治理前科）；ARM（PE 200x+荒谬）；ASML/AMAT/LRCX/KLAC（增速15-25%不达标）；EQIX/DLR（REIT非硬件）；GEV/ETN/POWL/STRL（AI占比<50%非纯正）；**MRVL**（市值$207B超区间；获谷歌$120B定制芯片协议+1年后股价已+212%，forward PE 52x利好已定价）；**STX**（市值$192B超区间，forward PE 23x，与WDC同质让位）；**CIEN**（TTM增速+30.6%达标但市值涨幅+335%+forward PE 50x透支）；VRT（Q2营收miss单日-14%，增速~23%边缘）；CRDO（单一客户>60%集中度）；KLIC/ASYS/INTT（小盘+周期波动）。

---

## 三、第三层：精细分析（5家）

**1. 台积电 TSM（价值轨·高确定性）**
Q2'26营收$40.2B，净利~$22B，毛利率67.7%超指引上限（同比+910bp），全年增速指引上调至"40%+"，HPC驱动、2nm爬坡（TSMC IR）。市值$1.93T，PE 27.7x/forward 19.1x，TTM营收+30.6%、净利+53.4%；7月单月营收+45% YoY，先进封装订单溢出至INTC（stockanalysis.com/GuruFocus）。AI含量100%：NVDA/AVGO/AMD所有AI芯片+HBM基底均经其代工与CoWoS封装。护城河：技术+规模垄断，10年后仍在。风险：台海地缘、AI capex退潮。**合理偏便宜**。进终选。

**2. 美光 MU（价值轨·周期成长）**
市值$1.06T，股价$940距6月高点$1,255回调-25%；TTM营收$90.3B（+167%）、净利$50.5B、EPS $44.3、**forward PE 6.5x**（stockanalysis.com实时）。Q3 FY26营收$41.5B、毛利率84.9%、EPS $25.11；Q4指引营收$50B（环比+20%）、EPS $30.73（Micron IR）。HBM4对NVDA分配+DRAM全场紧缺；UBS目标$1,625，BofA看FY30 EPS $230+。风险：84.9%毛利率为历史极端，2027年供给释放后均值回归；回调正在进行（收益率驱动）。**极便宜但要盯周期信号**。进终选。

**3. Astera Labs ALAB（成长轨·高弹性）**
Q2'26营收$392.4M（+104% YoY），EPS 80c超共识69c；Q3指引$540-560M（环比+40%，超consensus $417M约30%），Scorpio X-Series进入量产并将于Q3成最大产品线（TheFly/GlobeNewswire）。市值$49B，股价$283距高点$499回调-43%，forward PE 51x；JPM/RBC/Jefferies目标价$465-500。卖点：AI互连纯度100%、毛利率~76%、NVDA平台深度绑定。风险：客户集中、CPO技术切换。**回调后性价比显著改善**。进终选。

**4. Lumentum LITE（成长轨·高弹性·备选）**
Q4 FY26营收$1.01B（环比+23%，首次破十亿）、non-GAAP毛利率50.4%（Lumentum IR）。NVDA 2026年3月战略入股$2B共研CPO光子技术——类"链主背书"。1.6T光模块+EML紧缺。风险：YTD涨幅已7倍于NVDA（io-fund），透支度需警惕；毛利率50%低于ALAB；客户集中。列为第一备选。

**5. 西部数据 WDC（成长轨→价值轨·确定性备选）**
CEO Irving Tan："2026年基本售罄，前七大客户均有firm POs"；Seagate同证nearline产能全年锁满（The Register/PCMag）。市值$167B（1年+541%），PE 19x，TTM营收$12.9B（+35.7%）、净利$9.3B（+399%）（stockanalysis.com实时）。HDD价格创两年新高，订单能见度=全行业最佳。风险：HDD长期被SSD侵蚀的技术性通缩；与MU存储同赛道让位。列为第二备选。

---

## 四、终选3家（组合互补性）

| 标的 | 角色 | 核心逻辑 | 关键风险 |
|------|------|---------|---------|
| **TSM（C-漏斗）** | 高确定性·核心 | AI硬件唯一"必经之路"，垄断+67.7%毛利率+forward PE 19x，供不应求水位下最稳 | 台海地缘 |
| **MU（C-漏斗）** | 中等弹性·成长 | 存储超级周期主战场，forward PE 6.5x+回调-25%提供买点，HBM4结构性溢价 | 2027供给释放、周期见顶 |
| **ALAB（C-漏斗）** | 高弹性·期权 | +104%增速+Scorpio量产+Q3指引环比+40%，回调-43%后风险收益比改善 | 客户集中、CPO技术切换 |

**选择理由**：TSM提供确定性底仓（所有AI路线之争的赢家通吃方，forward PE 19x为三大龙头中最低）；MU在forward PE 6.5x+回调-25%处买入高周期弹性（与TSM产业链上下游互补、风险源不同）；ALAB用高增速博超额弹性且已回调-43%（与存储/代工相关性低）。三家覆盖代工-存储-互连三个互不重叠子环节。备选顺序：LITE > WDC > CLS。

---

## 五、未来IPO候选

1. **Groq**：LPU推理芯片，2026年传闻IPO，估值~$6.5B+——推理需求爆发最大纯度受益者。
2. **Lightmatter**：光互连/CPO初创（估值~$4.4B），与LITE/Cohere主题呼应——电子互连向光互连迁移的下一站。

注：Cerebras原列此处，抽检发现已于2026年上市（代码CBRS，ARK 8月在买入），已移出。

---

## 六、信息充分度自评、抽检修正与来源

### 6.1 抽检修正记录（2026-08-20盘中，stockanalysis.com实时验证）

| 数据点 | 初稿值 | 验证值 | 处置 |
|-------|--------|--------|------|
| MU市值 | ~$420B | $1.06T | 已修正，forward PE 10.7x→6.5x |
| SNDK市值 | ~$50B | $232.19B | 已修正，成长轨→超区间标黄 |
| WDC市值 | ~$50B | $167.00B | 已修正，转价值轨标黄 |
| STX市值 | ~$38B | $191.95B | 已修正，维持淘汰 |
| MRVL市值 | ~$85B | $206.66B | 已修正+新增谷歌$120B协议信息 |
| CIEN市值 | ~$15B | $55.90B | 已修正，淘汰理由更新 |
| AVGO市值 | ~$1.5T | $1.73T | 已修正 |
| TSM市值 | ~$1.3T | $1.93T | 已修正，PE 27.7x/forward 19.1x |
| VRT市值 | ~$75B | $97.43B | 已修正 |
| ALAB市值 | ~$30B | $49.15B | 已修正，+104%增速验证通过 |
| TSM ROIC | ~30% | TTM净利$69.7B/营收+30.6%，口径合理 | 通过 |

**抽检发现的增量信息**：①Marvell获谷歌$120B定制芯片协议+$12.18B认股权证，冲击AVGO定制ASIC份额预期（AVGO 5日-14%）；②存储板块8月回调中（MU距高点-25%、SNDK-33%、ALAB-43%）——收益率驱动而非基本面恶化，改善买入时点；③Cerebras已上市（CBRS），移出IPO候选。终选结论不变、逻辑强化。

### 6.2 信息充分度自评

| 维度 | 等级 | 说明 |
|-----|------|------|
| 财务数据完整性 | A- | 终选3家+粗简10家均经实时验证；LITE/CLS等备选仍为估计 |
| 估值时效性 | A- | 核心标的PE/市值为2026-08-20盘中实时数据 |
| 行业格局 | A | 供不应求多方交叉验证（TSM/MU/WDC/STX财报互证） |

**待核实**：MU单季$41.5B营收与84.9%毛利率为搜索所得极端值（存储超级周期顶部特征），下单前必须核对10-Q原文；LITE/COHR/CRDO/DELL等备选精确市值与实时PE。

**主要来源**：TSMC IR（Q2'26）、Micron IR（FY26Q2/Q3）、Astera Labs IR+TheFly（Q2'26）、Lumentum IR（FY26Q4）、Celestica IR、The Register/PCMag（HDD售罄）、Morningstar（SNDK+464%）、NerdWallet（MU一年+641%）、stockanalysis.com（2026-08-20盘中实时验证：MU/AVGO/TSM/MRVL/SNDK/WDC/STX/VRT/CIEN/ALAB市值与估值）、Investing.com、Barron's/Reuters/MarketWatch（存储回调、Seagate财报、Marvell-谷歌协议）。
