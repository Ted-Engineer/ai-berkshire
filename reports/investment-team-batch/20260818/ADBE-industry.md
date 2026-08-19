# ADBE（Adobe）行业维度单只重研——芒格视角（v5.4）

**报告属性**：2026-08-18 v5.4 调仓执行 / ADBE 单只重研 / 行业研究员（芒格视角）
**数据截止**：2026-08-18 约 14:40 ET（美股周二盘中，全部为本次实时搜索，未复用旧结论）
**基准价格**（双源）：Yahoo Finance $266.20（盘中 13:32 ET）/ stockanalysis.com $269.72（盘中快照），前收 $263.71；市值约 $107-110B（397.6M 股本 × 现价，python 精算）；P/E（TTM）14.5x、Forward P/E 9.8x（stockanalysis 快照）
**关键闸门**：FQ3 财报 **2026-09-10**（stockanalysis.com 明示 "Earnings Date Sep 10, 2026"，与调仓闸门一致；注意 8/18 网上流传的 "$5.96 EPS beat" 标题为德国聚合站旧闻重发，非本次财报）
**搜索日志**：19 次操作，见 `search-log.txt`（v54-ADBE-industry 段）；方法：Bash curl（Google News RSS / EDGAR / stockanalysis / 出版方正文直抓）

---

## 摘要：芒格一句话

> 2026 年创意软件行业的真相是：**AI 没有吃掉需求，而是重新分配了收入和成本结构**——分发层（ChatGPT/Gemini）拿走入口，模型层烧钱（Canva 增长预期砍三分之一、Sora 阵亡、Figma 盈利倒退），而 Adobe 用"入驻对手入口 + 代理化 + 报表合并"三招守住了 12.7% 的收入加速。市场给整个板块按"永久受损"定价（ADBE P/E 14.5x、CRM 回撤 44%、FIG 距高点 -80%），这更像 2000 年代的"恐慌性板块折价"而非 2010 年代的"平台更替"。但 Adobe 合并报表段落（不再单独披露 Creative/Experience）是管理层自己对护城河边界信心不足的信号——芒格会称之为"连厨师都不肯让你看菜"。

---

## 1. 创意/营销软件 2026 格局：AI 对价值链的重分配（最新证据）

### 1.1 重分配的三层结构（本次搜索到的 2026 年新证据）

| 价值链环节 | 2025 叙事 | 2026 年事实（本次验证） | 谁在收钱 |
|---|---|---|---|
| 入口/分发层（ChatGPT、Gemini） | "Adobe 会被绕过" | **反向**：Adobe 6/19 把 Firefly Creative Agent 装进 ChatGPT 与 Claude（Forbes）；8/6 官宣 "Adobe for ChatGPT"——创建、编辑、交付全在 ChatGPT 内完成（Adobe 官方博客标题，8/6） | OpenAI/Google 收入口租金，Adobe 交租换流量 |
| 模型/生成层 | "生成即成品" | **集体失血**：Sora 社交 App 上线 6 个月即关停（TechCrunch 3/24，正文）；Canva 因"每个 AI 任务的平均服务成本过高"把 2026 增长指引从 30% 砍到 20%（Startup Daily 8/5，正文引自 Perkins 股东信）；Figma Q2 因 Config 投入与 AI 成本 GAAP 运营亏损 $117.3M（EDGAR 8-K） | 无人稳定盈利 |
| 应用/工作流层 | "旧软件被掏空" | **最稳的一层**：Adobe FQ2 收入 $6,618M（+12.68%，连续第四季加速：10.6%→10.7%→10.5%→12.0%→12.7%；EDGAR 10-Q 与 stockanalysis 双源）；Figma 收入 +48%、NDR 136%（EDGAR） | 工作流与文件格式粘性仍在收费 |

### 1.2 芒格式解读："生态学"而非"叙事学"

芒格会问：这个行业的"地形"变了什么？答案：**内容生产的瓶颈从"产能"转移到了"组织与合规"**。三个证据链：
1. **Adobe 自己的产品重心转移**：6/18 创意代理铺进 Photoshop/Premiere/Illustrator/InDesign/Frame.io（公测），功能全部瞄准"苦活"——粗剪、批量重命名、多平台改尺寸、背景替换（The Decoder 6/18，正文）。AI 的卖点从"生成"退到了"编排"。
2. **企业侧买的是供给链而非灵感**：Adobe 4/28 完成收购 Semrush（EDGAR XBRL 日期 2026-04-28），官方口径是"增强 CX Enterprise 的品牌可见度/AI 搜索能力"（Adobe Newsroom 4/28）——即在 AI 搜索时代帮品牌"被引用"，这是全新的需求侧预算。
3. **反向证据同样重要**：Typeface 数据称"AI 让营销活动更慢而不是更快"（PPC Land 6/22，标题级）——生成过剩之后，编排、审校、品牌一致性的工作量反而上升。这对拥有"生产系统"的 Adobe 是净利好。

**结论（行业维度）**：AI 对创意软件的净效应不是"需求消失"而是**"单价通缩 + 产量通胀 + 筛选成本上升"**。收入池向两端（入口、数据/编排）移动，纯生成中间层被压扁。Adobe 的对冲是同时下注两端（入驻入口 + 收购 Semrush 拿品牌数据），方向正确但代价是报表透明度下降（见第 4 节）。

---

## 2. 对手评估（附最新数据）

### 2.1 OpenAI（企业转向后的视频策略）

- **事实链**：3/24 关停 Sora 社交 App（TechCrunch 正文：官方未给原因，推文只说"将公布 App 与 API 的时间表"）；多家报道口径一致——转向企业 AI、开发者工具与 ChatGPT 增长（ITP.net、CyberSecurityNews、PYMNTS"聚焦超级应用"）；HPCwire 直接把此定位为"IPO 前的战略收缩"。
- **视频的后续**：Sora 2 模型本体"令人印象深刻"（TechCrunch 原话），关的是社交壳而非模型；Altman 4/2 称仍在与迪士尼谈判（Hollywood Reporter）。迪士尼 $150M 合作告吹的金额细节仅单一来源（tech-insider/Cryptonomist 转述），**置信度：中**。
- **对 Adobe 的含义**：OpenAI 从"消费品视频平台"退回"企业模型供应商"，等于承认**成品视频的分发与变现做不成**。Premiere/Firefly 视频工作流的最大 To C 威胁解除；剩下的是 API 层竞争（价格战），而 API 价格战伤的是 Canva 这类"重度依赖前沿模型"的玩家——Canva 股东信原话"过度依赖前沿模型"（Startup Daily 正文）。

### 2.2 Google

- Veo 3.1 已进 Flow 与 API（2025-10），2026-01-13 更新：竖屏视频、4K 超分、角色一致性、YouTube 原生集成（blog.google 官方标题 + Storyboard18/Moneycontrol 双源转述）。
- Forbes 5/22 判断行业拐点："AI 视频从片段生成转向制作（production）"——与 Adobe 的"编排"叙事合流。
- 商业模式风险点：Google 用"AI Credits"消费制变现（2025-11 起为外界关注），且 YouTube 集成使其成为**唯一自带分发的视频生成玩家**。这是 10 年维度上比 OpenAI 更结构性的一类对手。
- 注：Google 侧视频收入/用量绝对值本次未获可靠双源数据，**标注缺口**。

### 2.3 Canva

- **最新硬数据**（Startup Daily 8/5 正文 + AFR/The Australian 8/4-8/12 标题，双源）：2026 增长指引 30%→20%（砍三分之一）；6 月季度收入 $921.9M（+25.2% YoY）；估值口径 US$42B（A$60B）；二手市场折价 29%（AFR 8/12），SmartCompany 8/18 称"再蒸发 $11B"；正考虑纳斯达克上市。
- **原因**（Perkins 股东信原话，正文抓取）："服务一个 AI 任务的平均成本过高"、"过度依赖前沿模型"、"定价、消费模型与用量控制没跟上需求"。对策：自研模型、砍 freemium AI 成本、放慢发布节奏。
- **芒格点评**：Canva 是"AI 成本通缩"的第一个上市级伤亡名单成员。它证明了 prosumer 层的价格战没有赢家——这反而减轻了 Adobe 下沉（freemium）的压力：Adobe 被迫做免费层的代价，对手同样付不起。

### 2.4 Figma（EDGAR 8-K 权威数据，2026-08-05）

- Q2 FY26：收入 $370.1M（**+48% YoY，连续第三季加速**）；NDR 136%；GAAP 毛利率 84%；non-GAAP 运营利润率 10%；GAAP 运营亏损 $(117.3)M（Config 营销投入）；FCF $53.2M；现金 $1.7B；**首个完整的 AI credit 货币化季度**；上调全年收入指引（媒体口径至约 $1.47B，+40M）。
- 但股价反应负面：Q3 指引谨慎 + AI 开支担忧引发盘后下挫（qz.com 8/6）；2026 年内距高点回撤 44%-84% 不等（TIKR 7/13、Motley Fool 7/10、TIKR 6/28 三个口径，**区间标注**）。
- Dylan Field 原话（EDGAR 正文）："当代码被商品化、价值向栈上迁移，我们的机会反而变大了"——设计工具层与创意层一样，赢家是"画布+协作"，不是"生成器"。
- **对 Adobe 的含义**：Figma 在 UI/产品设计圈的高粘性没有被动摇（NDR 136% 证明），但资本市场拒绝为"AI 叙事下的设计工具"付钱——板块性折价，非公司性问题。

### 2.5 竞争格局总表（8/18 快照）

| 公司 | 最新核心数据 | 8/18 状态 | 对 ADBE 威胁度 |
|---|---|---|---|
| OpenAI | Sora App 关停（3/24）；转企业+开发者工具 | 视频消费端撤退 | 低（应用层）/ 中（API 价格战） |
| Google | Veo 3.1+YouTube 集成（1/26）；"片段→制作"拐点（5/26） | 唯一自带分发的对手 | 中长期最高 |
| Canva | 指引 30%→20%；Q2 收入 $921.9M +25.2% | AI 成本危机、估值缩水 | 中（prosumer 层相互伤害） |
| Figma | Q2 收入 $370.1M +48%；NDR 136%；GAAP 亏损 | 增长强但市场不给估值 | 中（设计圈，与 PS 受众重叠有限） |
| Salesforce | Agentforce ARR 破 $1B（TIKR 7/23 + Yahoo 6/3 双源）；股 价回撤 44% | 8/26 AWU 计费"审判日" | 见第 4 节 |

---

## 3. AI 代理对创意工具需求的净效应（最新采用数据）

**净效应判断：短期（1-2 年）中性偏正，中期（3-5 年）取决于代理"是否拥有预算"。**

支持证据（本次搜索）：
- 采用面仍早：McKinsey 发现仅约 **10% 的企业职能**在用 AI 代理（Forbes 3/22 标题级）；Gartner 2026 代理式 AI 炒作周期仍在爬坡段（4/15）；a16z 4/8 发布"企业实际在哪里采用 AI"——企业预算尚未系统性流向代理。
- 强制采用在加速：WRITER 调查称 60% 的公司计划"处理"不采用 AI 的员工（Business Wire 4/7）——自上而下的采用压力是真实的。
- **代理增加而非减少软件需求的第一批硬证据**：Figma"首个完整 AI credit 货币化季度"（EDGAR），Adobe ARR $27.10B（+12.5%）中 AEP 与相关应用是点名驱动力（10-Q 原文），Salesforce CX Today 5/28 "AI 代理工作量已超过其人工支持团队"。代理是**新的席位**（credit/API 计费），不是席位的替代。
- 反方证据（必须记录）：Typeface 数据"AI 让活动更慢"（6/22）；SAP 8/3 警告"代理蔓延"已是董事会级治理问题；TNW 5/22 "Agentforce 宣传跑在交付前面"。代理的 ROI 叙事尚未在企业侧完全兑现。

**芒格点评**：代理对 Adobe 是"税"还是"地"？目前证据像"地"——创意代理把 Photoshop/Premiere 的单席位价值从"工具费"升级为"工具费+用量费"（Firefly credits 已验证该模式，Figma 的 136% NDR 部分来自 credit add-ons）。风险在反面：如果代理在 ChatGPT 里调 Firefly 完成全流程，Adobe 沦为"API 供货商"，定价权转移到入口。8/6 的 "Adobe for ChatGPT" 正是这条窄路的入口——**用定价权换分发权，历史上没有几次是好买卖**。

---

## 4. 企业营销侧：Experience Cloud → CX Enterprise vs Salesforce

### 4.1 Adobe 侧的三个结构性动作（按时间）

1. **4/20 Summit**：Experience Cloud 品牌整体更名为 **CX Enterprise**，全押代理式 AI（MarTech 标题；WSJ 独家"在 AI 颠倒威胁下为企业推出代理"；Adobe Newsroom 官宣 CX Enterprise Coworker；同场宣布与 AWS 的代理式 AI 协作、代理机构合作网络扩张——Marketing Dive）。
2. **4/28 完成收购 Semrush**（EDGAR 日期核实）：给 CX Enterprise 补上"品牌可见度/AI 搜索（GEO）"数据能力——AI 搜索时代"品牌被模型引用"是 CMO 的新预算项，这块 Salesforce 目前没有对标资产。
3. **6/15 提交的 FQ2 10-Q：把 Digital Media / Digital Experience / Publishing & Advertising 三段合并为单一可报告分部**（EDGAR 原文："reflecting the Company's shift to unified selling motions"），改按两大客户群披露：**Creative & Marketing Professionals 订阅收入 $4,537M（+12.9%）**、**Business Professionals & Consumers $1,853M（+16.2%）**；"Experience Cloud"一词在 10-Q 中出现次数为 **0**。

> **芒格红旗**：不再单独披露创意 vs 体验云收入，意味着外界从此**无法直接对比 Adobe CX 业务与 Salesforce 的规模与增速**。统一销售口径可以有业务理由，但它同时降低了外部验证能力——这是"信任但要验证"里被砍掉的"验证"。行业研究员立场：将其记为治理侧负分，交给风险研究员跟进。

### 4.2 与 Salesforce 的对位（8/18 快照）

| 维度 | Adobe（CX Enterprise） | Salesforce（Agentforce + Data 360） |
|---|---|---|
| 最新规模口径 | 含在 $27.10B 总 ARR 内，不再单列（10-Q） | Agentforce ARR **破 $1B**（TIKR 7/23、Yahoo 6/3 双源） |
| 增长引擎 | AEP 及相关应用、AEM 被点名驱动 ARR（10-Q 原文） | Q4 FY26 "创纪录"（官方 2/25）；Q1 FY27 beat 但全年指引偏轻（CNBC 5/27） |
| 差异化 | 内容供给+数据+投放编排一体（GenStudio 路线）、Semrush 的 AI 搜索可见度 | 数据云+代理矩阵+$3.6B Informatica 并表（CRN 6/15） |
| 市场态度 | ADBE P/E 14.5x / Fwd 9.8x | 44% 回撤（TIKR 7/23）；8/26 AWU 计费方式"审判日"（Tech Times 8/13） |
| 信任问题 | 分部披露消失 | "宣传快于交付"（TNW 5/22） |

**判断**：企业营销/CX 不是零和市场，但**两家的股价都被"代理货币化慢于叙事"打折**。Adobe 的相对优势是内容供给端（创意→投放闭环）独此一家；相对劣势是客户群更偏营销内容而 Salesforce 钩在 CRM 数据系统记录层。8/26 Salesforce 事件与 9/10 Adobe 财报会把这对"难兄难弟"重新定价一次——注意 **板块共振风险**：CRM 若在 8/26 崩，ADBE 会在 9/10 前被连带压价。

---

## 5. 芒格"生态学"：10 年格局推演

**规则一：产能过剩的行业没有好生意。** 生成模型层正在经历教科书式产能过剩（Sora 关停、Canva 缩量、视频模型价格战），10 年后该层大概率只剩 2-3 家有自有算力/分发的巨头（Google、OpenAI、可能加一家中国系——Alibaba 视频模型 6 月已升至全球第二，VentureBeat 6/22）。

**规则二：价值向"瓶颈"迁移。** 内容链条的新瓶颈是：可信（商业可用版权，Firefly 的差异化仍在）、可组织（ DAM/代理编排）、可被发现（AI 搜索可见度，Semrush 卡位）。Adobe 三项都有座位。

**规则三：入口税不可避免。** "Adobe for ChatGPT"承认了入口在别人手里。10 年尺度上，Adobe 要么把 ChatGPT/Gemini 变成自己的分销渠道（像零售品牌上亚马逊），要么被渠道压毛利。历史上品牌商上亚马逊的结果：活得下去，但利润率永久下台阶。**这是估值从 30x 降到 15x 的核心原因，也是 15x 里已经包含的东西。**

**规则四：人才与惯性。** 专业创意师的技能资产沉淀在 Adobe 工具链里（肌肉记忆+插件+素材库），转换成本在 AI 时代被"生成替代手工"部分抵消，但"成品交付的最后一公里"（印刷色域、广播级时间线、法务合规）仍归 Adobe。10 年内专业层被整体替代的概率低；被持续压价的概率高。

**生态学结论**：10 年后大概率仍是"入口巨头（OpenAI/Google）× 应用寡头（Adobe+一两家垂直新贵）× 数据/编排层（Adobe CX、Salesforce、CRM 系）"的三层结构。Adobe 最可能的终局是**"内容行业的 SAP"**——增速个位数、现金流机器、周期性被叙事殴打。以 Fwd P/E 9.8x 买入"SAP 化的 Adobe"是便宜的吗？芒格：*"以合理价格买优秀公司"的前提是它仍是优秀公司——12.7% 的加速增长和 $10B+ 年化 FCF 说明它还没变成 SAP；14.5x 定价的则是"立刻变成 SAP"。真相在中间，赌注在 9/10。*

---

## 6. 1-6 个月催化剂表（2026-09 → 2027-02）

| 时间 | 事件 | 方向 | 关注点 / 验证指标 |
|---|---|---|---|
| 8/26 | Salesforce AWU 计费"审判日"（Tech Times 8/13） | 板块 β | 代理货币化可信度；CRM 崩则 ADBE 连带承压 |
| 9/10 | **ADBE FQ3 财报（闸门）** | 双向，权重最高 | 收入增速能否续创 13%+；Q4 指引；FY27 早期口径；ARR（剔除 Semrush 后的有机增速 ≥10%？）；AI/credit 货币化披露口径 |
| 9-10 月 | **CEO 继任官宣（随时）** | 双向 | 3/12 宣布 Narayen 卸任至今 5 个月未定（30 天新闻扫描无新进展）；外部空降=战略重置风险，内部提拔=连续性；上任首份战略陈述是重定价触发器 |
| 10 月中下旬 | **Adobe MAX 2026**（历史规律 10 月 LA；官网为 JS 壳，**确切日期未能抓取，标注缺口**） | 偏正 | 创意代理 GA、Firefly 新模型、视频工作流；与 ChatGPT/Gemini 集成深度数据 |
| 11-12 月 | Figma Q3 财报（上次 8/5，Q3 谨慎指引的兑现/证伪） | 行业信号 | AI credit 货币化斜率；设计层竞争读数 |
| 12 月初 | Salesforce Q3 FY27 财报 | 行业信号 | Agentforce ARR 从 $1B 起的斜率；CX 预算风向 |
| 持续 | OpenAI IPO 进程（Sora 收缩被定位为 IPO 前动作，HPCwire 3/26） | 板块事件 | 上市定价将成为"AI 应用层"估值锚，双向波动源 |
| 持续 | Canva 纳斯达克上市决策（股东信确认在考虑） | 行业信号 | 私募创意估值 US$42B 二级折价 29% 的公开化读数 |
| 持续 | 回购执行：4 月新增 $25B 授权，截至 5/29 余 $26.78B（10-Q） | 正 | 9/10 前后的回购节奏是管理层对价格的表态 |

---

## 数据缺口与置信度标注

1. **Adobe MAX 2026 确切日期**：官网为 JS 壳、curl 无法抓取正文——按历史规律推定 10 月，**缺口**。
2. **OpenAI 视频企业化细节（API 时间表、迪士尼 $150M 金额）**：官方未给原因与时间表（TechCrunch 原文确认）；金额单一来源，**置信度中**。
3. **Google Veo/Flow 收入与用量绝对值**：无可靠双源，**缺口**；仅有产品节奏证据。
4. **McKinsey "10% 职能用代理"、Typeface "活动更慢"、WRITER "60% 裁员计划"**：均为标题级单一转述（原始报告正文未抓取），**置信度中**，方向多源一致。
5. **Canva 内部单位成本数字**：股东信未披露绝对值（"平均服务成本过高"为定性原话），**缺口**。
6. Figma FY26 指引 $1.47B 来自财经媒体对财报电话会的口径（biggo），8-K 正文仅确认"上调"，**置信度中高**。
7. ADBE 股本口径：stockanalysis 显示约 397.6M 股（v5.0 报告曾用 413.6M 推算），市值约 $106-110B 区间内，**以 10-Q 封面股本为准的精算留给财务研究员**。

## 主要来源（本次实时抓取）

EDGAR（ADBE 10-Q 2026-06-15 / FIG 8-K 2026-08-05，正文级）；stockanalysis.com（ADBE 概览+季度财务，正文级）；TechCrunch 3/24（Sora，正文级）；The Decoder 6/18（创意代理，正文级）；Startup Daily 8/5（Canva 股东信转述，正文级）；Google News RSS 标题级：Forbes 6/19、Adobe 官方博客 8/6、MarTech 4/20、Adobe Newsroom 4/28、TIKR 7/23、Yahoo Finance 6/3、CNBC 3/12 与 5/27、Hollywood Reporter 4/2、blog.google 1/13、AFR 8/12、SmartCompany 8/18、Tech Times 8/13、VentureBeat 6/22、Forbes 3/22、PPC Land 6/22、qz.com 8/6 等（详见 search-log.txt）。

---

*本报告为学习与研究用途，非投资建议。行业研究员（芒格视角），2026-08-18。*
