# 持仓和买卖的研究任务 v4

> **执行入口**：本文件是设计文档（口径权威）。日常执行用 `/portfolio-rebalance`——流程在 `skills/portfolio-rebalance.md`，可调参数在 `config/portfolio-targets.md`，搜索词库在 `config/search-matrix.md`。修改本文件的设计后须同步到上述三处。

## 目标
基于实时行情和数据，对当前持仓逐一分析，给出明确操作建议（清仓/买入/持有/加仓/减仓），并找到最值得买入的新标的。投资期限1-6个月。

**真实目的（v4明确）**：捕捉1-6个月内可兑现的大额收益（催化剂/事件驱动），不是长期复利配置。全部框架为之服务：
- **机会优先**：行业分布是风险预算和搜索罗盘，不是收益目标——强催化剂与分布区间冲突时，优先催化剂，用硬上限+止损管理风险
- **生存前提**：短期大额收益伴随高波动，本流程不承诺盈利；目标是提高每笔的胜率与赔率、并把单笔亏损锁在可承受范围（见5.5风险预算），靠重复下注积累收益

## 核心约束
1. **持仓只数≤11只**：调仓后持有的股票数量不能超过11只
2. **明确操作信号**：每只股票给单一动词+触发条件，禁止模糊建议
3. **投资期限**：1-6个月，不做长期投资，只做短期能见得到大额利润的投资
4. **禁止复用任何旧评分/旧研究**：但凡不是本次实时搜索的就是旧的，必须全部从零重跑
5. **行业分布必须符合顶层设计**（见下方），偏离>5%必须修正
6. **WebSearch MCP fallback链**（配额用尽禁止放弃，必须换下一个）：
   - ❌ 禁止以"WebSearch配额用尽"为由跳过任何搜索步骤
   - ❌ 禁止以"搜索工具不可用"为由放弃研究
7. **异动快速反应协议**（防止隔夜大涨来不及反应）：
   - 执行prompt时，**首先**WebSearch "biggest stock movers today" / "stocks surge earnings beat today" 检查当日重大异动
   - 如发现用户关注过的标的（memory中有记录）异动>10%，**立即**纳入候选并评估
   - 如发现持仓标的的供应商/客户/合作伙伴异动>15%，评估对持仓的影响
8. **来源F（用户历史）和来源G（持仓生态链）为必选**：不可跳过、不可走过场
   - 来源F执行证据：必须展示"Read了哪些memory文件→提取了哪些ticker"
   - 来源G执行证据：必须展示"对哪些持仓搜索了供应商/客户"

---

## 行业分布顶层设计（最高优先级，每次执行必须评估）

**设计时间尺度**：基于1-6个月战略视角，但1-6个月投资期限内允许±10%战术偏离
**复审机制（两级）**：①每次执行时核验设计假设是否仍成立（5.1的✅/❌假设清单，≥2个失效触发设计复审）；②每半年全面复审目标分布本身（当前设计基于2026年8月，下次全面复审：2027年2月）

### 目标分布（v4统一口径：与"设计理由"、portfolio-latest.md、5.1模板一致）

| 类别 | 目标占比 | 硬上限 | 定义 |
|------|---------|--------|------|
| **AI平台** | **20-25%** | 30% | 自建AI基础设施+大规模AI投入的平台公司 |
| **AI软件** | **15-20%** | 25% | 以AI驱动的企业/消费软件，不自建大规模AI基础设施 |
| **AI硬件** | **25-30%** | 35% | 半导体/芯片/数据中心硬件/电力基础设施/AI Cloud运营商 |
| **非AI价值** | **15-25%** | 35% | 见"非AI价值细分"下方 |
| **现金** | **10-20%** | 30% | 战略储备 |

**AI总暴露**：50-65%（平台+软件+硬件之和），硬上限70%

**约束分级（v4：机会优先，风险靠硬上限和止损管）**：
- **硬约束（🔴强制修正）**：AI总暴露 50-65%/cap 70、非AI价值 15-25%/cap 35、现金 10-20%/cap 30、**单一非美国家敞口≤15%**（硬上限20%，含中概ADR/港股——地缘/退市/汇率尾部风险）
- **软约束（⚠️仅提示，不强制修正）**：AI平台/AI软件/AI硬件三个子区间——AI内部轮动跟随催化剂与动量，不做会计口径的均值回归
- **战术上浮通道**：某类别满足"≥2个标的双重准入通过"或"现有持仓处于盈利趋势（未触发止损）"时，允许运行至硬上限（而非区间上限）
- **让利润奔跑**：因上涨导致的超配不主动减仓，直至硬上限或出现卖出信号（止损/催化剂兑现/基本面恶化）
- **不为填格子买弱资产**：低配类别若无候选通过双重准入，允许持续低配，报告标注"等待合格标的"

### 非AI价值细分（子规则）

| 子类别 | 建议占比 | 定义 |
|--------|---------|------|---------|
| **防御价值** | 10-15% | 低波动+稳定分红（消费必需/公用事业/保险） |
| **金融/周期** | 5-15% | 金融科技/工业/能源等周期性标的 |
| **医疗** | 5-10% | 医疗保险/医疗服务/生物科技 |

**单一子类别不超过总资产的15%**（防止集中风险）
**算术约束（v4）**：三个子类区间之和（20-40%）服从非AI主区间（15-25%）——非AI总仓位接近下限时，子类下限按比例压缩；唯一硬约束为"单一子类别≤15%"

### 设计理由

**AI平台放宽到20-25%**（从v3的15-20%上调）：
- 2026年Q2 FCF恶化是CapEx集中投入期的短期现象，2-3年后基础设施建成FCF会反弹
- META TTM FCF仍有$71B（即使Q2单季-91%），MSFT云收入增长30%+支撑CapEx投入
- 优质平台（如MSFT）的"好的投资"（Azure扩张）不应与烧钱平台等同
- 巴菲特自己持有苹果占其组合40%+，说明优质平台可以重仓
- **但设定30%硬上限**：超过此比例必须减仓，防止过度集中

**AI硬件提升到25-30%**（从v3的10-15%上调）：
- 物理瓶颈是AI文明级趋势中最确定的受益者（CoWoS/HBM/电力均为S级瓶颈）
- 硬件公司"卖铲子"比平台"挖金子"更确定，且ROIC/FCF质量更高
- TSM ROIC 54.6% vs META负FCF，NVDA FCF $48.6B/Q vs META $3.3B/Q
- 李录框架：物理瓶颈=文明级趋势的咽喉
- **警示**：硬件有周期性风险（2022年半导体寒冬NVDA跌-60%），故设定30%硬上限

**AI软件维持15-20%**：
- 软件公司轻资产+高FCF转化率+定价权
- 但面临AI颠覆风险（定价模式被侵蚀），不可过重
- ADBE/INTU等PE 10-13x的低估值软件股是核心配置
- 硬上限25%：防止软件过度集中

**非AI价值下调到15-25%**（从v3的20-30%）：
- 在AI回调时提供组合保护（低相关性）
- 拆分为三个子类（防御/金融周期/医疗），防止单一行业集中度过高
- 芒格原则：组合里要有让你晚上睡得着的东西
- **2000年互联网泡沫启示**：思科（硬件）跌-89%，微软（平台）跌-60%，可口可乐（非科技）仅跌-20%

**现金降至10-20%**（从v3的15-20%下调）：
- 提升资金使用效率，长期持有>20%现金=机会成本
- 但保留10%底线作为应急储备和战术灵活性
- 硬上限30%：超过则必须部署或说明原因（如等待重大回调）

### 分类规则

**主规则**（按主业收入>50%判定）：
- **AI平台**：自建AI基础设施（数据中心/GPU集群），CapEx>$80B/年或AI CapEx占收入>20%，AI是核心战略
- **AI软件**：使用AI提升产品，但不自建大规模AI基础设施，AI CapEx占收入<10%
- **AI硬件**：制造AI基础设施所需的物理产品（芯片/存储/设备/电力/冷却）
- **非AI价值**：主业与AI无直接关联，或AI仅为次要工具

**跨类业务判定（v4确定性规则，按顺序判定，前一条能定则不启用后一条）**：
1. **主规则**：CapEx>$80B/年或AI CapEx占收入>20%，**且云/AI基础设施为第一大收入来源** → **AI平台**
2. **收入AI敏感度**：AI直接相关收入占比≥50% → 按该业务归类；30-50% → 归AI敏感度更高的类别
3. **收入增量**：AI相关占收入增量>60% → **AI硬件**（适用于代工/设备/材料）
4. 仍无法判定（50/50）→ 归AI敏感度更高类别（保守原则），报告标注"归类存疑"

**历史判例表（新例外必须写入此表，禁止当次临场改判）**：
| 标的 | 判定 | 依据 | 判定日期 |
|------|------|------|---------|
| MSFT | AI软件 | 收入与利润主体为订阅软件，AI基建服务于软件变现（对主规则的豁免） | 2026-08 |
| GOOGL | AI平台 | 自建AI基建+GCP为增长引擎，AI CapEx占收入>25% | 2026-08 |
| TSM | AI硬件 | AI占收入增量>60% | 2026-08 |

> 说明：MSFT按主规则（CapEx ~$175B>$80B）本应归AI平台，判例固定为AI软件。
> v4起AI三个子区间为软约束，分类仅用于**搜索路由与暴露监控**，不再影响强制修正——消除"分类翻转导致达标结论互换"的问题。

### 每次执行必须完成的分布评估

**在第二步（持仓分析）完成后、第三步（新候选筛选）开始前，必须执行：**

1. **计算当前分布**：将每只持仓归类，计算各类别占总资产比例
2. **对比目标**：输出对比表

| 类别 | 目标 | 当前 | 偏差 | 状态 |
|------|------|------|------|------|
| AI平台 | 20-25% | XX% | ±X% | ✅/⚠️/🔴 |
| AI软件 | 15-20% | XX% | ±X% | ✅/⚠️/🔴 |
| AI硬件 | 25-30% | XX% | ±X% | ✅/⚠️/🔴 |
| 非AI价值 | 15-25% | XX% | ±X% | ✅/⚠️/🔴 |
| 现金 | 10-20% | XX% | ±X% | ✅/⚠️/🔴 |

3. **偏离修正规则（v4：只适用于硬约束类别——AI总暴露/非AI价值/现金/单一国家敞口）**：
   - 偏差 ≤5%：✅ 合理，不需要主动修正
   - 偏差 5-10%：⚠️ 警告，在后续操作中优先修正
   - 偏差 >10%：🔴 必须修正，必须在本轮调仓中制定修正措施
   - **上行偏离=让利润奔跑**：因持仓上涨导致的超配，只要未出现卖出信号（止损/催化剂兑现/基本面恶化），允许持续至**硬上限**，不主动减仓
   - **下行偏离=不为填格子买弱资产**：低配类别无候选通过双重准入时，允许持续低配并标注"等待合格标的"
   - **AI三个子类别只做⚠️提示**（软约束，不触发🔴）——AI内部配置跟随催化剂与动量
   - **硬上限触发**（如AI总暴露>70%、单一非美国家>20%）：必须在下一轮调仓时减仓至上限以下，不可例外

4. **修正影响后续决策**：
   - 如果AI平台超配>5%：优先在此类中寻找减仓/清仓标的
   - 如果AI硬件低配>5%：优先在新候选中寻找AI硬件标的
   - 如果非AI价值低配>5%：优先在新候选中寻找非AI价值标的
   - 现金>25%时：优先寻找加仓/新建机会；现金<10%时：优先保留现金不加仓

5. **在最终方案中必须包含分布对比**：
   - 调仓前分布 vs 调仓后分布 vs 目标分布
   - 说明每项操作对分布的影响
   - 如果调仓后仍有>10%偏差，必须解释原因和后续修正计划
6. **分布表数字生成规则（防错·必读）**：
   - 所有百分比必须由**脚本计算生成并打印**（Python/financial_rigor.py），禁止手写或心算百分比——2026-08-13教训：心算 66247.5/295102 得 22.5%，实际 22.449% 应为 22.4%，把正确数字改错
   - 脚本必须输出**合计校验行**：五个互斥主类别（AI平台/AI软件/AI硬件/非AI价值/现金）精确合计=100.0%，校验不过禁止写报告
   - 小计行（AI总暴露）和子项行（中国敞口）**不参与求和**，必须在表格中视觉区分（斜体/缩进/注明"小计"），禁止与主类别行混排同格式
   - 用户质疑任何数字时：**先跑工具再回答**，禁止用口头心算回应数字质疑

---

## 零复用铁律（最高优先级，不可变通）

❌ **"本次"= 这次执行此prompt的过程，不是"这个Claude会话"**
❌ 不得以"本会话早些时候已执行/已研究/已搜索"为由跳过任何步骤
❌ 不得引用reports/下的旧报告、旧评分、旧结论
❌ 不得引用同一会话内更早对话轮次的研究结果
❌ 哪怕1小时前刚研究过同一只股票，本次执行也必须重新用WebSearch获取最新数据
❌ 每一步都必须展示真实执行证据（WebSearch搜索词、Agent ID、工具输出），不可只说"已完成"

**执行原则：如果你无法展示这一步在本次prompt执行中真实发生的证据，就等于没做。**

## Skill执行铁律（最高优先级，不可变通）

❌ **直接用WebSearch分析股票=未执行。必须通过Skill工具调用。**
❌ **不得以"WebSearch配额用尽"为由跳过skill执行——必须切换到MCP搜索工具（见核心约束#6）**
❌ **持仓分析必须启动/investment-team Agent（4个并行Agent），不得用WebSearch替代**
❌ **候选标的必须过/investment-checklist + /investment-team双重验证，缺一不可**
❌ **/industry-funnel和/bottleneck-hunter必须正式调用skill，不得用"已扫描数据"替代**
❌ **每一步skill执行必须展示真实证据：Agent ID、skill输出、financial_rigor.py结果**

**判断标准**：
- ✅ "我调用了/investment-checklist BR，Agent ID: xxx，六关全过" = 已执行
- ❌ "我用WebSearch搜索了BR的财务数据" = 未执行
- ❌ "基于之前的扫描数据，BR看起来不错" = 未执行
- ❌ "WebSearch配额用尽所以跳过了漏斗扫描" = 未执行（必须换MCP工具）

**执行原则：Skill调用是硬性要求，不是建议。无法展示skill调用证据=步骤未完成=报告无效。**

## 推荐准入铁律（最高优先级，不可变通）

❌ **任何在最终方案中推荐"买入/新建/换仓"的新标的，必须先通过 /investment-checklist 验证**
❌ **对比研究（如"A vs B谁更好"）≠ checklist验证。对比是筛选，checklist是准入——两步不可合并**
❌ **Deep Research的结论不能直接作为推荐——Deep Research推荐的标的必须再过checklist才能进最终方案**
❌ **加仓已有持仓（如META 80→95股）不需要新checklist，但换仓/新建必须跑**

### 推荐验证矩阵（最终报告必须包含）

在最终方案的执行清单前，必须输出此矩阵：

| 推荐标的 | 推荐类型 | checklist结果 | investment-team评分 | .done标记文件 | 可推荐？ |
|---------|---------|-------------|-------------------|--------------|---------|
| AVGO | 新建 | 4/6 PASS | ★★★★☆ | investment-checklist-AVGO-*.done | ✅ |
| PDD | 换仓 | 3/6 GRAY | 未执行 | ❌ 无 | ❌ 不可推荐 |
| TSM | 加仓 | 豁免（已有持仓） | — | — | ✅ |

**判断标准**：矩阵中任何一行标记 ❌ 不可推荐 = 该标的不得出现在执行清单中。

### 推荐清单文件（hook会检查）

最终方案输出前，必须创建 `.claude/.workflow/recommended-buys.txt`：
- 每行一个ticker，列出所有**新建/换仓**的标的（加仓已有持仓不需列入）
- 如无新买入推荐，写入 `# no new buys`
- hook验证：每个ticker必须有对应的 `investment-checklist-{TICKER}-*.done` 文件
- ❌ recommended-buys.txt中的ticker没有对应checklist .done = hook阻止结束

**PDD教训记录（2026-08-13）**：
本次执行中，Deep Research对比BABA vs PDD后直接推荐换仓PDD，但PDD未跑checklist。
用户发现后追问"你有深度研究PDD吗？"——补跑checklist后发现PDD是灰色地带（3/6通过，
净利润连续5季度下降+Temu核心模式被全球de minimis规则拆解），修正推荐为保留BABA。
**根因：对比研究的结论不能跳过准入验证。这条铁律就是为防止此类失误而设。**

## 执行流程

### 第一步：核实当前持仓（必须逐项确认）
- **必须先Read** `reports/portfolio-latest.md`
- **若用户提供了持仓清单，以用户数据为准**
- **写入任何文件前，必须逐项向用户确认**：股数、成本价、现金余额
- ❌ 绝不基于假设写持仓文件
- ⚠️ **提取"待执行/观察/计划买入"项**：持仓文件中所有标记为"待执行""计划""观察"但尚未执行的标的，必须在第三步作为候选来源A纳入筛选——这些是用户已有意图的标的，不可遗漏

### 第二步：持仓股分析（全部从零研究，禁止复用）
- **每只持仓股都必须在本次执行中重新启动Agent** 进行实时研究
- 必须展示Agent ID或搜索证据，证明是本次执行中新建的研究
- ❌ 不得引用任何旧文件、旧Agent结果、旧会话内容
- ❌ 不得以"刚研究过"为由跳过

**分析重点**（1-6个月视角）：
- FCF是否为正？增速？ROE？
- 有无重大催化剂（财报/新品/监管）？
- 下行风险多大（悲观场景-X%）？
- 仓位是否合理（太小<3%=机会成本，太大>25%=集中风险）？

**输出**：每只股票一句话判断 + 明确操作信号

### 第二步半：行业分布评估（必须执行，不可跳过）
- 按上方"行业分布顶层设计"的分类规则，将每只持仓归类
- 计算当前分布，输出对比表
- 标注偏差状态（✅/⚠️/🔴）
- 如果存在🔴偏差（>10%），必须在本轮调仓中制定修正措施
- 此评估结果直接影响第三步的候选筛选方向

### 第三步：新候选股筛选（必须在本次执行中真实运行）

#### 候选累积追踪（必须执行，hook会检查）

搜索过程中必须维护 `.claude/.workflow/candidates.csv` 文件：
- 格式：`ticker,company,gics_sector,source`（第一行为header）
- 每次搜索发现的新候选**立即追加**（同一ticker不重复添加）
- **下限300只**，理想350只唯一候选
- 覆盖验证：25个GICS组每组至少4只，7维搜索每维至少5只
- ❌ 候选不足300只时，Stop hook会阻止结束并要求继续搜索

#### 候选来源（6路并行，缺一不可，覆盖全美股）

| # | 来源 | 做什么 | 为什么 |
|---|------|--------|--------|
| A | **portfolio-latest.md 待执行项** | Read持仓文件，提取"待执行""观察""计划买入"等所有未完成项 | 用户已有研究结论的标的最可能成交，**不可遗漏** |
| B | **全市场多维搜索** | GICS 25二级行业组全覆盖 + 5维交叉搜索（量化/主题/事件/技术面/聪明钱） | 确保不因搜索方向偏窄而漏掉任何赛道的机会。**枚举+正交双保险** |
| C | **/industry-funnel** | 按行业漏斗逐层精选 | 系统性覆盖行业内的候选 |
| D | **/bottleneck-hunter** | 供应链瓶颈套利扫描 | 发现非传统视角的标的 |
| E | **行业分布缺口反向映射** | 根据第二步半的偏差，**反向映射**到GICS行业清单，对每个缺口行业搜索候选 | 确保分布偏差被定向修正 |
| F | **用户历史关注（必选·执行步骤强制）** | **三步执行**：(1) Read MEMORY.md索引；(2) 对每条与研究标的相关的记忆文件，Read完整内容提取ticker；(3) 特别关注曾被反复研究但未执行的标的（如"next XXX搜索"系列中的XXX本身）。输出提取的ticker清单作为候选 | 用户偏好驱动的机会，**用户花最多时间研究的标的最可能成交**。NBIS教训：记忆索引里有4条NBIS相关条目但未读取=零执行 |
| G | **持仓生态链反向搜索（必选）** | 对每只当前持仓，搜索其**核心供应商/客户/合作伙伴**作为候选。例：META的AI算力供应商→NBIS；TSM的核心设备供应商→ASML；MSFT的AI合作伙伴→OpenAI | 持仓的生态链标的具有**已验证的商业关系**，是最自然的扩展方向。NBIS是META和MSFT的算力供应商——如果执行了此来源，NBIS必然被发现 |

#### 全市场扫描覆盖范围（来源B必须覆盖）

**必须搜索全部11个GICS一级行业，不可只搜"防御价值"或"AI"**：

| GICS行业 | 代表性搜索词 | 为什么不能跳过 |
|---------|------------|--------------|
| 信息技术 | "undervalued software semiconductor stocks 2026" | AI软件/硬件候选 |
| 金融 | "undervalued fintech bank insurance payment processing stocks 2026" | **BR这类金融基建** |
| 医疗保健 | "undervalued healthcare pharma medical device stocks 2026" | 医疗候选 |
| 消费者必需 | "undervalued consumer staples FMCG stocks 2026" | 防御候选 |
| 消费者可选 | "undervalued consumer discretionary retail ecommerce stocks 2026" | 周期候选 |
| 工业 | "undervalued industrial aerospace defense manufacturing stocks 2026" | 工业/国防候选 |
| 能源 | "undervalued energy oil gas pipeline stocks 2026" | 能源候选 |
| 公用事业 | "undervalued utility power water stocks 2026" | 防御候选 |
| 材料 | "undervalued materials chemical metals mining stocks 2026" | 资源候选 |
| 房地产 | "undervalued REIT real estate stocks 2026" | 收益候选 |
| 通信服务 | "undervalued telecom media streaming stocks 2026" | 通信候选 |

#### GICS 3级细分搜索（必须执行，覆盖全部25个二级行业组）

**1级行业太粗（11个），2级行业组才25个，3级行业~74个。必须至少搜索到2级，对有前景的方向下钻到3级。**

以下为全美股GICS 2级行业组搜索清单（每个2级组一个搜索词，不得跳过）：

| 1级行业 | 2级行业组 | 搜索词 | 3级下钻方向（如2级有发现则深入） |
|---------|----------|--------|-------------------------------|
| **能源** | Energy | "undervalued energy oil gas pipeline midstream stocks 2026" | 综合油气/勘探/设备/管道/炼化 |
| **材料** | Materials | "undervalued chemical metals mining specialty materials stocks 2026" | 化工/金属/采矿/特种材料/容器包装 |
| **工业** | Capital Goods | "undervalued industrial machinery defense aerospace manufacturing stocks 2026" | 国防/航空航天/机械/电气设备 |
| | Commercial & Professional Services | "undervalued business services waste environmental printing stocks 2026" | **BR这类金融基建**/专业服务/环境服务 |
| | Transportation | "undervalued airline railroad trucking logistics shipping stocks 2026" | 航空/铁路/海运/物流 |
| **消费者可选** | Automobiles & Components | "undervalued auto EV auto parts dealer stocks 2026" | 整车/EV/零部件/经销商 |
| | Consumer Durables & Apparel | "undervalued consumer electronics household appliance luxury apparel stocks 2026" | 家电/电子/奢侈品/服装 |
| | Consumer Services | "undervalued restaurant hotel casino cruise travel stocks 2026" | 餐饮/酒店/赌场/旅游 |
| | Retailing | "undervalued ecommerce grocery discount retail department store stocks 2026" | 电商/超市/折扣/百货 |
| **通信服务** | Telecommunication Services | "undervalued telecom wireless tower stocks 2026" | 运营商/基站/宽带 |
| | Media & Entertainment | "undervalued streaming media gaming advertising publishing stocks 2026" | 流媒体/游戏/广告/出版 |
| **消费者必需** | Staples Distribution & Retail | "undervalued grocery food retail drug store distribution stocks 2026" | 超市/药店/批发 |
| | Food, Beverage & Tobacco | "undervalued food beverage tobacco alcohol stocks 2026" | 食品/饮料/烟草/酒精 |
| | Household & Personal Products | "undervalued household personal care beauty products stocks 2026" | 日用品/个护/美妆 |
| **医疗保健** | Health Care Equipment & Services | "undervalued medical device hospital health IT services stocks 2026" | 医疗器械/医院/医疗IT/实验室 |
| | Pharma, Biotech & Life Sciences | "undervalued pharma biotech drug manufacturing life science tools stocks 2026" | 制药/生物/CRO/生命科学工具 |
| **金融** | Banks | "undervalued bank regional bank money center bank stocks 2026" | 大型银行/区域银行/社区银行 |
| | Diversified Financials | "undervalued fintech payment processing asset manager exchange data stocks 2026" | **支付/金融科技/交易所/资管/数据** |
| | Insurance | "undervalued insurance P&C life reinsurance broker stocks 2026" | 财险/寿险/再保/经纪 |
| **信息技术** | Software & Services | "undervalued software SaaS enterprise cloud cybersecurity AI software stocks 2026" | 企业软件/云/SaaS/安全/AI软件 |
| | Technology Hardware & Equipment | "undervalued tech hardware server storage networking equipment stocks 2026" | 服务器/**存储/HBM**/网络设备/消费电子 |
| | Semiconductors & Semiconductor Equipment | "undervalued semiconductor design foundry memory equipment materials stocks 2026" | 芯片设计/代工/**存储(MU)**/设备(AMAT/KLAC)/材料 |
| **公用事业** | Utilities | "undervalued utility electric power gas water nuclear renewable stocks 2026" | 电力/燃气/水务/核电/可再生 |
| **房地产** | Real Estate | "undervalued REIT industrial office residential retail data center healthcare REIT stocks 2026" | 工业REIT/办公/住宅/零售/**数据中心REIT**/医疗REIT |

**执行要求**：
- 以上25个2级行业组**全部搜索，每组至少2次WebSearch：价值型1次 + 成长/事件型1次**（两列搜索词都用），合计≥50次
- **⚠️ 搜索词多样性要求（防止系统性偏差）**：25组**全部**搭配不含"undervalued"的第二视角搜索词（见下表），确保高成长/高估值标的（如NBIS/CoreWeave类）不被系统性排除
- 对返回结果中有潜力的方向，**下钻到3级**（如2级"Semiconductors"→3级"Memory/HBM"单独搜）
- 如果某个2级组返回的候选明显与持仓重复或无投资价值，可快速跳过但必须标注"已扫描，无候选"
- 在报告中输出**25组扫描覆盖矩阵**（✅有候选/⚪无候选/❌跳过+理由），标注每组两列搜索词各自使用的原文

#### GICS各组第二视角搜索词库（成长/事件型，每组必用1条，可自行变化）

| 2级行业组 | 成长/事件型搜索词 |
|-----------|------------------------------------------------|
| Energy | "energy stocks earnings beat guidance raised 2026" / "natural gas pipeline LNG capacity expansion stocks" |
| Materials | "lithium uranium copper miners production growth 2026" / "specialty materials supply shortage stocks" |
| Capital Goods | "defense stocks record backlog order growth 2026" / "electrical equipment grid capex beneficiary stocks" |
| Commercial & Professional Services | "business services stocks high ROIC insider buying 2026" / "staffing payroll stocks hiring recovery" |
| Transportation | "shipping railroad stocks earnings recovery momentum 2026" / "airline stocks capacity discipline margin" |
| Automobiles & Components | "EV stocks deliveries growth 2026" / "auto supplier content per vehicle increase stocks" |
| Consumer Durables & Apparel | "luxury brand pricing power revenue growth 2026" / "appliance housing recovery stocks" |
| Consumer Services | "travel leisure cruise stocks earnings beat 2026" / "restaurant same store sales growth stocks" |
| Retailing | "retail stocks same store sales margin expansion 2026" / "off-price discount retail traffic growth" |
| Telecommunication Services | "telecom stocks FCF dividend growth 5G monetization 2026" / "fiber broadband penetration growth stocks" |
| Media & Entertainment | "streaming gaming stocks subscriber growth profitability 2026" / "advertising stocks digital shift share gains" |
| Staples Distribution & Retail | "grocery drugstore stocks defensive recession stable earnings" / "food distribution volume recovery stocks" |
| Food, Beverage & Tobacco | "food beverage dividend aristocrats pricing power 2026" / "alcohol tobacco volume recovery stocks" |
| Household & Personal Products | "consumer staples quality moat margin stability 2026" / "beauty personal care emerging market growth stocks" |
| Health Care Equipment & Services | "medical device new product cycle FDA approvals 2026" / "hospital health services volume growth stocks" |
| Pharma, Biotech & Life Sciences | "biotech pipeline catalysts FDA approvals 2026" / "life science tools CRO backlog growth stocks" |
| Banks | "bank stocks NIM expansion earnings growth 2026" / "regional bank merger acquisition targets 2026" |
| Diversified Financials | "fintech transaction volume TPV growth 2026" / "exchange market data stocks moat pricing power" |
| Insurance | "insurance hard market combined ratio improvement 2026" / "specialty niche insurer high ROE 2026" |
| Software & Services | "SaaS NRR 120% net revenue retention 2026" / "AI agent software ARR growth triple digit 2026" |
| Technology Hardware & Equipment | "server storage networking AI demand revenue surge 2026" / "hardware margin expansion turnaround stocks" |
| Semiconductors & Semi Equipment | "semiconductor revenue growth 50% AI 2026" / "HBM memory shortage beneficiary stocks" |
| Utilities | "utility data center power demand growth 2026" / "nuclear renewable capacity expansion IPP stocks" |
| Real Estate | "data center REIT FFO growth 2026" / "REIT dividend yield discount to NAV stocks" |

#### 新兴赛道必搜清单·AI侧（GICS无法覆盖的新业态，15个赛道全部搜索）

**GICS分类基于传统行业逻辑，无法捕捉2024年后涌现的新业态。AI产业链远不止"AI软件+AI硬件"两块，以下15个赛道必须独立搜索，每个至少2条不同视角搜索词（视角A=运营商/公司本身，视角B=供应商/瓶颈，视角C=催化剂/事件，任选其二）：**

| # | AI赛道 | 搜索词（多视角，每赛道至少用2条） | 代表标的方向 | 为什么GICS抓不到 |
|---|--------|--------------------------------|-------------|-----------------|
| 1 | **AI Cloud / Neocloud运营商** | A:"AI cloud GPU rental neocloud providers 2026" B:"neocloud contract backlog billion deal wins" C:"coreweave nebius earnings revenue growth" | NBIS, CRWV, Lambda, Crusoe | "买GPU出租算力"新业态，不属传统半导体/软件 |
| 2 | **AI定制芯片ASIC/推理芯片** | A:"custom AI ASIC accelerator design win stocks 2026" B:"broadcom marvell XPU customer pipeline" C:"AI inference chip vs training shift beneficiaries" | AVGO, MRVL, ALAB | 半导体分类不区分通用GPU/定制ASIC |
| 3 | **AI网络/光模块/交换** | A:"800G 1.6T optical module demand growth 2026" B:"AI cluster networking switch CPO stocks" C:"co-packaged optics breakthrough suppliers" | ANET, CIEN, COHR, LITE, CRDO | 光通信横跨硬件+半导体+工业 |
| 4 | **HBM/存储** | A:"HBM4 capacity sold out memory stocks 2026" B:"DRAM NAND supply tightness beneficiary" C:"micron SK hynix HBM revenue growth" | MU, WDC, STX | 存储的周期反转逻辑GICS不反映 |
| 5 | **先进封装/CoWoS链** | A:"advanced packaging CoWoS capacity expansion 2026" B:"OSAT packaging substrate ABF shortage stocks" C:"chiplet hybrid bonding equipment suppliers" | TSM, AMKR, KYEC | 封装是代工子环节，2级行业无此分类 |
| 6 | **半导体设备/材料** | A:"WFE wafer fab equipment spending record 2026" B:"semiconductor materials shortage suppliers" C:"ASML AMAT KLAC backlog book-to-bill" | AMAT, LRCX, KLA, ASML | 设备商的AI驱动资本开支周期 |
| 7 | **AI电力：燃气IPP/核电/铀** | A:"data center power gigawatt pipeline IPP stocks 2026" B:"nuclear SMR fuel uranium enrichment demand" C:"power purchase agreement AI hyperscaler signed" | VST, CEG, TLN, NRG, CCJ, LEU | 跨公用+工业+能源三行业 |
| 8 | **电网设备/变压器** | A:"transformer lead time shortage grid equipment stocks 2026" B:"transmission substation capex beneficiary" C:"electrification switchgear demand surge" | GEV, HIT(日立), ETD, PWR | 电网瓶颈是AI衍生需求，GICS分散 |
| 9 | **AI散热/液冷** | A:"liquid cooling rack power density AI stocks 2026" B:"CDU cold plate immersion cooling suppliers" C:"Vertiv earnings AI backlog growth" | VRT, MODV, SMCI, nVent | 散热分散在工业设备+硬件 |
| 10 | **数据中心REIT/代建/E&C** | A:"data center REIT FFO growth leasing 2026" B:"data center construction E&C backlog stocks" C:"hyperscaler capex guidance data center buildout" | EQIX, DLR, JCI, EME | GICS归地产/工程，本质AI基建 |
| 11 | **AI Agent/应用软件** | A:"AI agent enterprise deployment ARR growth 2026" B:"agentic workflow software adoption metrics" C:"Salesforce ServiceNow Palantir AI revenue disclosure" | CRM, NOW, PLTR, SOUN | AI应用收入是软件子集，GICS无标记 |
| 12 | **AI模型/基础模型生态** | A:"foundation model API token revenue growth 2026" B:"LLM training compute contract suppliers" C:"OpenAI Anthropic valuation revenue multiple" | MSFT, GOOGL, META + 供应商 | 模型层嵌套在大厂内，独立标的在生态链 |
| 13 | **物理AI/人形机器人** | A:"humanoid robot production ramp 2026 stocks" B:"robot actuator reducer sensor suppliers" C:"Tesla Optimus Figure commercial timeline" | TSLA, 供应商群 | GICS无机器人分类，分散在工业+汽车 |
| 14 | **自动驾驶/Robotaxi** | A:"robotaxi commercial fleet expansion 2026" B:"AV lidar compute supplier stocks" C:"autonomous driving regulatory approval milestone" | TSLA, AUR, GOOGL生态 | 跨汽车+软件+硬件 |
| 15 | **加密矿企转AI算力** | A:"bitcoin miner AI pivot HPC hosting 2026" B:"crypto mining data center conversion capacity" C:"Hut 8 Bit Digital AI contract revenue" | BTBT, CLSK, HUT, IREN | GICS归金融但正转型AI基建 |
| 16 | **端侧AI/边缘推理芯片** | A:"AI PC AI phone NPU upgrade cycle stocks 2026" B:"edge AI inference chip smartphone PC silicon suppliers" C:"on-device AI qualcomm mediatek design win" | QCOM, MTK, 端侧传感器链 | 换机潮催化剂密集，GICS半导体组无"端侧推理"视角 |
| 17 | **AI数据/标注/合成数据** | A:"AI data labeling curation public companies 2026" B:"synthetic data training data suppliers stocks" C:"data infrastructure AI governance compliance" | 数据标注、合成数据、数据工具 | 模型层上游新业态，GICS软件组无此分类 |

**AI侧执行要求**：17个赛道**全部搜索**，每个≥2条不同视角词（合计≥34次）。任何赛道"无候选"必须标注扫描词原文。在报告中输出17赛道×视角覆盖矩阵。

#### 新兴赛道必搜清单·非AI侧（GICS正交主题，至少8个各≥1次）

**防止全报告被AI单一叙事绑架：以下非AI主题与AI赛道平行搜索，确保组合候选池两侧均衡（用户历史上多次要求纠正"只看AI"偏差）：**

| # | 非AI主题 | 搜索词示例 | 代表方向 |
|---|---------|-----------|---------|
| 1 | **老龄化/银发经济** | "aging population healthcare demand stocks 2026" / "senior living home healthcare volume growth" | 医疗服务、养老、慢病管理 |
| 2 | **国防现代化** | "defense stocks record backlog NATO rearmament 2026" / "defense electronics ammunition capacity" | LMT/NOC/HWM/欧洲军火 |
| 3 | **能源转型/电网升级** | "grid modernization capex beneficiary stocks 2026" / "energy storage battery demand growth" | 电网、储能、输配电 |
| 4 | **美国制造回岸/自动化** | "reshoring US manufacturing factory automation stocks 2026" / "industrial robot machine tool demand" | 自动化、机床、工业软件 |
| 5 | **利率长期下行受益者** | "rate cut beneficiaries stocks 2026 duration assets" / "REIT utilities relative value falling rates" | REIT、公用、长久期成长 |
| 6 | **GLP-1/减肥药生态** | "GLP-1 supply chain contract manufacturing 2026" / "obesity drug volume growth suppliers" | CDMO、给药装置、原料药 |
| 7 | **水务/基建老化更新** | "water infrastructure replacement cycle stocks 2026" / "pipe valve pump municipal capex" | 水务设备、工程 |
| 8 | **农业科技/粮食安全** | "agriculture technology precision farming stocks 2026" / "fertilizer crop protection supply" | 农化、农机、种子 |
| 9 | **体育博彩/iGaming** | "sports betting iGaming legalization expansion 2026" / "online gambling volume growth stocks" | 博彩运营、平台 |
| 10 | **宠物经济** | "pet economy spending growth stocks 2026" / "veterinary pet food premiumization" | 宠物食品、兽医链 |
| 11 | **奢侈品/品牌护城河** | "luxury brand pricing power heritage moat 2026" / "premium consumer resilience stocks" | LVMH系、高端消费 |
| 12 | **保险硬市场周期** | "insurance hard market pricing cycle 2026" / "P&C reinsurance underwriting margin stocks" | 财险、再保、经纪 |
| 13 | **中国/新兴市场消费复苏** | "China consumer stimulus recovery stocks 2026" / "Chinese ecommerce valuation re-rating catalysts" | 中概电商、消费、本地生活 |
| 14 | **黄金/贵金属（尾部对冲+自身动量）** | "gold miners real rates tail hedge stocks 2026" / "precious metals royalty central bank buying momentum" | 金矿、贵金属权利金公司（FNV/WPM类） |

**非AI侧执行要求**：至少**8个主题各≥1次**搜索（合计≥8次），产生候选不足时如实标注。报告输出主题覆盖矩阵。**主题13/14为优先纳入项**：13催化剂密度高（政策+估值修复），14与5.5的AI泡沫应急规则构成对冲闭环。

#### 多维交叉搜索（必须执行，与GICS行业搜索互补）

**GICS枚举的局限**：任何分类系统都是"按过去的方式组织行业"，无法捕捉跨行业的新兴机会。比如数据中心REIT在GICS是"房地产"，但本质是AI基础设施；BR在GICS是"商业服务"，但本质是金融基建。

**解决方案：用7个正交维度搜索，让不同维度的交集自然浮现枚举会遗漏的标的**：

| 维度 | 逻辑 | 搜索方式（示例） | 为什么GICS枚举抓不到 |
|------|------|----------------|---------------------|
| **D1. 量化筛选** | 用财务指标横切全市场，不分行业 | WebSearch "stocks forward PE under 15 ROE above 20 FCF yield above 8 2026"；用finviz/stockanalysis筛选器 | 量化条件不预设行业，自然跨所有GICS分类 |
| **D2. 主题/趋势** | 按投资主题横切，不分行业 | **直接引用上方两份清单**：AI侧15赛道（每赛道≥2视角词）+ 非AI侧12主题（至少8个）。禁止只搜泛化的"AI infrastructure beneficiaries"这类笼统词 | 一个主题横跨多个GICS行业（AI横跨IT+工业+地产+公用事业）。**NBIS教训：D2只搜了泛化的"AI infrastructure beneficiaries"导致结果全是VRT/GEV等组件商，漏掉了NBIS这类运营商** |
| **D3. 事件驱动** | 按催化剂事件搜索 | "recent spin-off stocks 2026"、"activist investor targets 2026"、"rejected acquisition target stocks"、"earnings beat guidance raised 2026" | Spin-off/activist/M&A等事件与GICS分类无关 |
| **D4. 技术面/资金面** | 按价格行为搜索 | "stocks near 52 week low strong fundamentals 2026"、"oversold stocks institutional buying"、"insider buying cluster 2026" | 技术信号不分行业 |
| **D5. 聪明钱跟踪** | 看顶级投资者在买什么 | "best value investor holdings changes 2026 Q2"、"Berkshire Hathaway portfolio changes"、"top hedge fund new positions 13F" | 顶级投资者的选股不受GICS约束 |
| **D6. 财报催化（必做）** | 搜索最近1周内发布财报且有重大异动的标的 | "stocks earnings beat guidance raise 2026 August"、"biggest earnings movers this week"、"revenue growth over 200% stocks 2026"、"contract backlog billion dollars AI stocks" | **NBIS教训：454%收入增速+$40B合同积压→单日涨34%。财报是最强催化剂，必须有专项搜索**。搜索词不可带"undervalued"——高成长股不会出现在价值筛选器中；另加"analyst estimate revision upgrade momentum stocks 2026"（分析师预期上修=机构资金进场前兆） |
| **D7. 持仓生态链（必做·与来源G互补）** | 对每只持仓搜索其核心供应商/客户 | 对每只持仓WebSearch "{持仓公司} supplier vendor partner"、"who provides AI compute to {持仓公司}" | NBIS是META和MSFT的算力供应商——如果执行了此维度，NBIS必然被发现 |

**执行要求**：
- 以上7个维度**每个至少1次WebSearch**（D6、D7为必做）
- D1量化筛选至少执行**3组不同条件**：价值型（fPE<15）、成长型（收入增速>50%）、收益型（FCF yield>5%）**各一组**——不可全是价值型
- D2主题搜索至少执行**12个不同主题：AI侧≥8个 + 非AI侧≥4个**（从上方两份清单选取，与新兴赛道小节可复用同一搜索但不重复计数）
- **D6财报催化必须搜索"高增长"而非"低估"**——搜索词如"revenue growth over 200%"、"biggest contract backlog"
- **搜索总量硬指标（Stop hook自动校验）**：全程MCP/WebSearch搜索**合计≥80次**（每次调用自动追加记录到 `.claude/.workflow/search-log.txt`）。构成：GICS 25组×2=50 + AI赛道≥30 + 非AI主题≥8 + 7维补充 ≈ 90+，留冗余
- **候选池两侧均衡**：AI相关候选（来源含AI 15赛道/软件/半导体/硬件）**占比不得超过65%**，非AI候选至少35%。candidates.csv 的 source 列必须标注所属清单（AI赛道#n/非AI主题#n/GICS/D1-D7/F-memory/G-生态链），报告末尾输出两侧占比统计
- 各维度的候选汇总后与GICS 25组+新兴赛道候选**去重合并**
- 在报告中标注每个候选的**发现维度**（如"D1量化"或"D6财报催化"或"G-持仓生态链"）

#### 完整筛选流程（不得跳过，不得引用旧结果）
1. **并行执行7路候选来源**（A-G），汇总所有候选名称
2. **去重+分类**：按行业分布缺口优先级排序
3. **从汇总池中提取Top 10-15候选**
4. 对Top候选逐一执行**双重验证**：
   - `/investment-checklist {股票名}` → 巴菲特六关准入测试
   - `/investment-team {股票名}` → 四大师全面评估
   - ⚠️ **两者都通过才能进入终选**（checklist是必要不充分条件）
5. 冒泡排序找Top 2

❌ **绝对禁止**：以"本会话/本轮/之前已执行过漏斗和瓶颈扫描"为由跳过此步骤
❌ **绝对禁止**：引用之前任何会话或轮次的漏斗/瓶颈结果
❌ **绝对禁止**：只搜索2-3个行业就声称"全市场扫描完成"
❌ **绝对禁止**：跳过来源A（portfolio-latest.md待执行项）或来源F（用户历史记忆）或来源G（持仓生态链）
❌ **绝对禁止**：所有搜索词全部带"undervalued"——系统性排斥成长股是设计缺陷

**⚠️ 候选筛选必须考虑行业分布修正需求**：
- 如果第二步半评估发现AI硬件低配>5%，优先筛选AI硬件候选
- 如果非AI价值低配>5%，优先在非AI的**全部子行业**（金融/医疗/消费/工业/能源/公用事业/REITs）中搜索
- 候选的行业类别必须在报告中标注
- **分布缺口是方向提示，不是搜索限制**——即使某行业缺口最大，也必须同时扫描其他行业

### 第四步：冒泡排序终选
对所有候选进行两两比较：
- 护城河：★5 > ★4
- 估值：fPE低者优先
- 下行风险：悲观场景-X%小者优先
- 催化剂：3个月内有财报/新品者优先
- **行业分布契合度：能修正分布偏差者优先**

⚠️ **所有评分必须统一来自/investment-team框架，标注"基于/investment-team"**
❌ 不同框架的分数不可混用、不可直接比较

输出Top 2，说明为何胜出。

### 第五步：输出最终方案
生成 `reports/portfolio-action-{日期}.md`，包含：

#### 5.1 行业分布对比（必须包含）

**当前设计假设**（标注假设是否仍然成立）：
- ✅/❌ AI平台CapEx是短期投入期（2-3年后FCF反弹）
- ✅/❌ 物理瓶颈（CoWoS/HBM/电力）仍是S级瓶颈
- ✅/❌ AI软件定价模式未被根本颠覆
- ✅/❌ 市场未进入AI泡沫破裂阶段

**如果≥2个假设失效，必须在下一轮调仓时触发设计复审。**

| 类别 | 目标 | 硬上限 | 调仓前 | 调仓后 | 修正幅度 | 状态 |
|------|------|--------|--------|--------|---------|------|
| AI平台 | 20-25% | 30% | XX% | XX% | ±X% | ✅/⚠️/🔴 |
| AI软件 | 15-20% | 25% | XX% | XX% | ±X% | ✅/⚠️/🔴 |
| AI硬件 | 25-30% | 35% | XX% | XX% | ±X% | ✅/⚠️/🔴 |
| 非AI价值 | 15-25% | 35% | XX% | XX% | ±X% | ✅/⚠️/🔴 |
| 现金 | 10-20% | 30% | XX% | XX% | ±X% | ✅/⚠️/🔴 |
| **五类合计（校验行）** | — | — | 100.0% | **100.0%** | — | 脚本计算 |
| *AI总暴露（小计·不参与求和）* | 50-65% | 70% | XX% | XX% | ±X% | ✅/⚠️/🔴 |

**非AI价值细分**（如适用）：
| 子类别 | 建议 | 实际 | 状态 |
|--------|------|------|------|
| 防御价值 | 10-15% | XX% | ✅/⚠️ |
| 金融/周期 | 5-15% | XX% | ✅/⚠️ |
| 医疗 | 5-10% | XX% | ✅/⚠️ |

如果调仓后仍有>10%偏差或触及硬上限，必须说明原因和后续修正计划。

**复审提醒**：本次设计基于2026年8月市场状态，下次复审时间：2027年2月。

#### 5.2 执行清单（明确信号）
| 股票 | 股数 | 操作 | 行业类别 | 理由（一句话） |
评分列必须标注框架来源

#### 5.3 执行顺序
1. 先清仓X只 → 回收$Y
2. 再买入Z只 → 投入$W
3. 净效果：M只→N只（≤11只）

#### 5.4 预期回报（1-6个月）
| 标的 | 仓位 | 乐观 | 中性 | 悲观 | 期望 |

#### 5.5 风险管理
- 止损价（-12%触发）；**移动止损**：浮盈>15%后止损上移至成本+5%（或20日均线，取高者）——截断亏损与让利润奔跑并行
- **催化剂兑现退出**：事件驱动仓位在催化剂落地（财报/审批/订单公告）后若无新催化剂接续，兑现离场——"买预期、卖兑现"是1-6个月期限的默认纪律
- **单笔风险预算**：每笔交易 仓位×止损距离 ≤ 总资产1%（如止损-12% → 单笔仓位≤8%）——连错10次总回撤<10%，这是短期重复下注的生存公式
- 催化剂日历
- 执行检查清单
- **AI泡沫破裂应急规则**：
  - 触发条件：纳斯达克100指数从高点回撤>25% 且 AI板块领跌（AI股平均跌幅>市场）
  - 应急措施：将AI总暴露从当前水平降至30%以下，非AI价值提升至40%+，现金提升至20-30%
  - 执行原则：优先减持估值最贵+FCF最弱的AI标的，保留ROIC>30%+FCF稳定的核心持仓

### 第六步：更新portfolio-latest.md
- ⚠️ **执行操作前**：向用户展示操作清单（含行业分布对比），等待确认
- ⚠️ **用户执行后**：逐项确认实际成交（股数/价格/现金），再写文件
- ❌ 绝不在用户确认前覆盖portfolio-latest.md

## 质量标准

### 必须做到
✅ 每只股票明确操作（清/买/持有/加仓/减仓）
✅ **FCF分类处理**：长期持仓（>6个月）FCF为负=清仓红线；短期交易（1-6个月）FCF为负但收入增速>100%+大额合同积压=允许纳入但标注"基建期成长股"，单标的仓位≤8%、此类合计≤12%，且**强制附带-12%止损与催化剂退出计划**（无止损计划=禁止纳入）
✅ 买入前必须通过checklist+investment-team双重验证（成长股可用调整后的checklist，FCF关改为"收入增速+合同积压"评估）
✅ 所有评分标注框架来源（/investment-team或/checklist）
✅ 数据标注来源，关键数据用financial_rigor.py验证
✅ 写文件前逐项确认用户实际持仓
✅ 所有研究必须实时搜索，不复用任何旧文件
✅ **行业分布评估必须执行，偏差>10%必须修正**
✅ **第三步候选扫描必须覆盖全部25个GICS二级行业组** + **至少5个新兴赛道**（不可只搜传统分类），对有潜力的方向下钻到三级行业
✅ **必须执行7维交叉搜索**（量化/主题/事件/技术面/聪明钱/财报催化/持仓生态链），其中D6财报催化和D7持仓生态链为必做
✅ **报告中输出候选发现来源矩阵**：每个候选标注是从哪个维度/行业/来源被发现的
✅ **必须提取portfolio-latest.md中的待执行项作为候选**
✅ **候选来源≥5路**（A-G中至少执行5路，其中A、B、F为必选）
✅ **来源F执行证据**：报告中必须列出"Read了哪些memory文件→提取了哪些ticker"，不可只说"已检索"
✅ **搜索词多样性证据**：报告中必须展示至少10组不含"undervalued"的搜索词，防止价值偏见

### 禁止事项
❌ 模糊建议（"可以考虑""建议关注"）
❌ 未核实持仓就给建议
❌ **复用任何旧评分/旧研究/旧报告——但凡不是本次实时搜索的就是旧的**
❌ 以"本会话已执行过"为由跳过任何步骤
❌ 批量分析多只股票在1个skill调用中
❌ **只搜索与分布缺口"匹配"的行业就声称全市场扫描完成**（必须覆盖25个2级行业组+新兴赛道）
❌ **忽略portfolio-latest.md中已有的"待执行/计划"标的**
❌ 基于假设写portfolio-latest.md
❌ 混用不同框架的分数不标注
❌ 仅用checklist就决定买入（必须同时有investment-team）
❌ **跳过行业分布评估或忽略>10%的偏差**
❌ **所有搜索词全部带"undervalued"**——这是系统性价值偏见，至少10组搜索使用成长/催化/主题型搜索词
❌ **来源F走过场**——只说"已检索memory"但不展示读取了哪些文件、提取了哪些ticker
❌ **忽略持仓生态链**——不搜索当前持仓的核心供应商/客户/合作伙伴

## 输出语言
全部用中文。
