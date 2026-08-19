# INTU（Intuit）行业维度单只重研——芒格视角（v5.4）

**报告属性**：2026-08-18 v5.4 调仓执行 / INTU 单只重研 / 行业研究员（芒格视角）
**数据截止**：2026-08-18 约 14:10 ET（美股周二盘中，全部为本次实时搜索，未复用旧结论）
**基准价格**（双源）：Yahoo Finance chart API 盘中 **$353.51**（前收 $336.44，日内 +5.1%；52 周区间 $252.84–$719.10）；stockanalysis.com 同日快照（页面 JS 化，仅部分字段可读，未采信冲突值）。**市值约 $96.7B**（python 精算：273.537M 股 × $353.51；股本来自 EDGAR 10-Q 封面，2026-05-14 为准）
**回撤校验**（Yahoo 数据 python 复核）：8/17 收盘 $335.60 = 较 52 周高点 **-53.3%**（与任务书"-53%"一致）；较 6 月末低点 $252.84 已反弹 **+39.8%**（低点 × 1.31 = $331.2 ≈ 8 月初水平，与任务书"+31%"一致）；当前 $353.51 距高点仍 **-50.8%**，年内约 -45%（TIKR 8/15 标题口径）
**关键闸门**：FQ4+FY26 财报 **2026-08-25**（官方 PR 7/30："Intuit to Announce Fourth-Quarter and Full-Year Fiscal 2026 Results on Aug. 25; Investor Day Set for Sep. 17"，Yahoo Finance 转载；Barchart 8/12、MarketBeat 8/18 双源佐证）；**Investor Day 2026-09-17**（Intuit IR 站日历 URL slug `20260917-intuits-annual-investor-day` 官方确认）
**搜索日志**：约 40 次独立操作（55 行），见 `search-log.txt` v54-INTU-industry 段（含时区更正注记：该段时间戳实为 UTC，真实 ET = 标注 -4h）。方法：Bash curl（Google News RSS / EDGAR / TechCrunch / Futurum / IT Jungle / JOC / BVP / Kalkine 正文直抓）。失败源已标注：Finviz/DDG/Bing/Google-HTML/StockTitan/TheStreet/CIO/PYMNTS/TIKR 等被 JS 墙或付费墙挡住，均未采信其数据。

---

## 摘要：芒格一句话

> 把"AI 代理会替代财务软件"这句话放到行业层面检验，2026 年 8 月的证据是：**恐慌把"入口"当成了"生意"**。OpenAI 确实拿到了入口（2 亿人每月问 ChatGPT 金融问题），但报税是全美国最深的"监管+责任+数据"三重护城河生态位——连 OpenAI 自己都说"计划很快支持 Intuit"（TechCrunch 5/15 正文），而 Intuit 7/21 官宣与 OpenAI/Anthropic 战略合作：**鲨鱼没有进攻珊瑚礁，鲨鱼搬进了珊瑚礁**。与此同时，政府竞争者（IRS Direct File）2025 年 11 月被特朗普政府亲手击毙（Bessent："私营部门能做得更好"），2026 税季是死后第一个完整税季，2027 税季是第二个。市场按"永久受损"给 INTU 定价（-53%），私募却在 8/13 用 Silver Lake 洽购 Workday 给整个软件板块**托底**——芒格会说：当买方调查最深入的一群人（PE）和最恐慌的一群人（公募）对同一批资产得出相反结论时，钱通常站在少数那一边。但我必须诚实：记账（bookkeeping）这个生态位确实在被代理层重定价，Xero 今天（8/18）刚上线自然语言 AI 代理构建器——**税务是堡垒，记账是战场**。

---

## 1. "AI 代理替代财务软件"恐慌的行业检验（含 8 月软件股反弹驱动）

### 1.1 恐慌的完整证据链（本次逐环验证）

| 环节 | 时间 | 事实（本次抓取正文级证据） | 对 INTU 的实际伤害 |
|---|---|---|---|
| ① SaaSpocalypse | 2026 年初 | 企业用 Claude Cowork 等工具"氛围编程"（vibe coding）自建软件的幽灵引发 SaaS 抛售，Salesforce/Workday/ServiceNow/Adobe/**Intuit**/Atlassian/Elastic/MongoDB 合计蒸发数千亿美元市值（IT Jungle 7/27 正文，引述明确点名 Intuit）。Reuters 后续定性为"low-key threat"（低调威胁，标题级） | 板块性估值压缩，非基本面事件 |
| ② 点产品最脆弱论 | 2026 上半年 | IT Jungle 总结教训："point products（如**报税=Intuit**、照片增强=Adobe）有被 AI 复制的风险，但 AI 尚无法复制 ERP 级的数据与流程精确协同" | 这正是市场把 INTU 打成"-53%"的理论依据 |
| ③ OpenAI 入场金融 | 2026-04→05 | 4 月收购个人金融创业公司 Hiro 团队（Ribbit/GC/Restive 投）；**5/15 上线 ChatGPT 个人金融工具（Pro 订阅者预览）**：经 Plaid 接入 1.2 万家金融机构（Schwab/Fidelity/Chase/Robinhood/Amex/Capital One），提供支出分析、订阅管理、购房规划；**月活 2 亿+用户已每月向 ChatGPT 提问金融问题**；GPT-5.5 强化上下文推理并建金融基准（TechCrunch 5/15 全文） | 情绪杀伤极大：Credit Karma 式仪表盘被 ChatGPT 原生复刻 |
| ④ 同期友军失守 | 2026-05 | Perplexity 基于 Computer agent 推出金融研究产品（TechCrunch 5/15 文中提及） | 入口层三面受敌 |
| ⑤ Intuit 自我收缩 | 2026-05-20 | 裁员 17%（约 3,000 人，总员工 18,200），CEO Goodarzi 内部备忘录称"简化结构、聚焦 AI"（TechCrunch 5/20 引 Reuters）；Goodarzi FY25 薪酬 $36.8M 被点名对照 | 市场读作"确认受损" |
| ⑥ 股价兑现 | 6 月末→8 月 | 52 周低点 $252.84（6 月末，IBT 6/30"在多年低点附近企稳"）；8/17 收 $335.60 = 距高点 **-53.3%** | — |

**关键反证（本次抓到的最强一条）**：OpenAI 在 5/15 发布中明确表示"**plans to support Intuit soon**"——即 ChatGPT Finances 将接入 Intuit 数据（如股票出售的税务影响分析）（TechCrunch 正文原话）。7/21 Intuit 官方博客标题《Intuit AI Principles: Strategic Partnerships with OpenAI & Anthropic》确认合作落地（Intuit 官网博客，标题级，正文 404 未取到，**置信度：中高，双源标题互证**）。芒格点评：**如果掠夺者选择与你共建而非绕过你，生态位大概率比恐慌者以为的更牢固。**

### 1.2 8 月软件股反弹的驱动（INTU +31%→+40% 的板块背景）

四层驱动，全部有正文级证据：

1. **私募并购托底（最硬的一条）**：8/13 Reuters 独家——Silver Lake 洽购 Workday，WDAY 单日 +18%（10 年最佳，盘中一度 +30% 触发临停），市值站上 $51B；Breakingviews 模拟 $227/股、30% 溢价、约 $53.8B、5x 2027E 收入；同期 Thoma Bravo 宣布以约 $16B 收购 Dayforce。当日 SAP/Salesforce/Adobe/ServiceNow 联动 +1.9%~4.5%（Futurum 8/18 全文，即今日发布）。
2. **板块数据**：S&P 500 软件与服务指数本季度至今（QTD）已涨约 **+25%**（Futurum 8/18 正文）；TradingView 8/3 标题直接点名"WDAY、ADBE、**INTU**、ADSK、CRM 软件股 7 月齐反弹"。
3. **聪明钱表态**：Michael Burry 4 月起建仓 CRM/PYPL，称"软件抛售不是 TACO 交易"（Stocktwits 4/16 标题）；6/21"AI 将分化出软件赢家与输家"（Benzinga 标题）；6/23 Times of India："Burry 回应'软件已死'论：LLM 无论……"（标题级）。
4. **企业买家行为证伪恐慌**（Futurum 引用调研）：42.6% 的企业决策者**不打算**减少/整合应用数量，另 22% 仍在评估；37.6% 表示"只有在市场条件允许时才可能换供应商"。75.4% 把生成式 AI 列为最高优先级技术——**想用 AI 与抛弃现有系统是两回事**。
5. **今日盘面**：INTU 盘中 +5.1%（Yahoo），MarketWatch 今日标题"Intuit 股票在强劲交易日跑赢同行"。

**检验结论（行业维度）**：恐慌的"需求消失"假设被三组事实削弱（企业不换系统、PE 用真金白银托底、OpenAI 选择接入而非绕过 Intuit）；但"单价通缩+入口被拿走"的假设部分成立——这才是 Credit Karma（导流生意）与 TurboTax（责任生意）必须分开估值的原因。

---

## 2. 税务赛道：Direct File 死后的空白 + H&R Block 反抢跑后状态

### 2.1 IRS Direct File 之死（结构性利好，时间线全部双源）

- **2025-11-05/06 关停**：财长 Bessent（兼任代理 IRS 局长）在白宫对记者说"**我们有更好的替代方案……它用得不多，私营部门能做得更好**"（Journal of Accountancy 11/6 正文，多台转述）。ITEP 11/5、Nextgov 11/6、Marketplace 11/12 多源一致。
- **使用量与成本（Treasury 报告国会版，JOC 正文转述）**：TY2023 试点 140,803 份（12 州）；TY2024 296,531 份（25 州），仅占约 1.46 亿份申报的 **0.20%**（python 复核）；TY2024 成本至少 $4,100 万且被指低估。
- **2026-03-24 FedScoop**：IRS 去年被曝**高估 Direct File 成本 $4,500 万**（超过全部真实成本）——政府自废武功的行政注脚。
- **复活尝试未果**：参议员 Warren 3/13 推动复活（Spectrum News 标题）；新泽西州 2/19 提出州级免费申报方案（NJ Spotlight 标题）。截至本次检索，无联邦级复活进展。
- **IRS 自身衰弱**：JOC 8/12（一周前）报道"IRS 裁员导致纸质申报和退税延迟"——收税方变慢，私营软件+专业 preparer 的价值上升。
- **Free File 补位有限**：AGI ≤ $84,000 者可用合作商免费产品（JOC 正文），IRS 转向"Free Filing Modernization Summit"+向软件商收取更多使用数据——即**政府把免费申报的执行权交回私营部门**。

### 2.2 H&R Block 反抢跑后状态（FY26 全年，EDGAR 8-K 正文，6/30 止财年）

- **总量**：营收 **$3.95B，+4.9%**（+ $184.4M）；净利（持续经营）+20.8% 至 $736.3M（含一次性 IRS 审查和解税务收益 $84.1M ≈ $0.65 EPS）；经调整 EPS **$5.31，+13.9%**；经营现金流 **+23%**；股东回报 $714M；季度股息 +10% 至 $0.46（8-K Exhibit 99.1 全文，8/11 发布）。
- **分部拆解（python 复核增长率）**：Assisted（门店人工+AI）**$2,560.9M，+6.1%**；DIY **$384.6M，+0.2%**（几乎零增长）；特许 Royalties -3.9%；美国税务相关合计 +4.7%；Emerald Card/Spruce -5.6%。
- **AI 叙事**：2/9 官方 PR《H&R Block Combines AI Power with Digital Enhancements and Unmatched Tax Pro Expertise to Win Tax Season》；3/17 StockTitan 标题"AI 税务助手数秒内处理**数百万**提问"（标题级，**正文被墙，具体用量数字缺口**）；3/17 获行业"Best Overall Tax Service"认可。

**芒格解读**：HRB 的"反抢跑"不是从 TurboTax 手里抢 DIY 份额（DIY 仅 +0.2%），而是**用 AI 降本提价把人工税季做成了更赚钱的生意**（NAC 提升 + 门店量增长）。这印证税务赛道的真实格局：**AI 在税务上是提价工具，不是替代工具**——因为报税的本质是"责任承担+审计追溯"，客户为"错了有人负责"付费。Direct File 死后，这一生态位两头（INTU 的 DIY + HRB 的人工）同时受益，而**2026 税季是死后第一个完整税季，2027 税季（明年 1-4 月）是第二个**——递延的份额回收还在路上。

---

## 3. 中小企业财务软件格局

| 玩家 | 本次抓到的最新事实 | 对格局的含义 |
|---|---|---|
| **Intuit QuickBooks** | 7/22 PYMNTS 报道"Intuit 把 QuickBooks 变成小企业**信贷中心**"（标题级，正文 404）；7/21 推 Intuit Enterprise Suite 瞄准中端市场（官方博客标题）；8/17 TradingView"INTU 瞄准庞大的中端市场机会"（标题）；8/11 Avalara 为 QuickBooks 自动化销售税合规（PRN）；**8/18（今日）Mashable：QuickBooks 套餐 3 个月 1 折促销** | 从"记账工具"转向"资金+信贷+中端 ERP"平台；但 1 折促销暗示获客成本上升/需求疲软（单源标题，**置信度：中**） |
| **Intuit 资本配置** | 7/27 官宣投资 DOSS（TechCrunch 3/24：DOSS 融 $55M 做"即插 ERP 的 AI 库存管理"） | 用 CVC 换赛道情报，防"氛围编程"式绕后 |
| **H&R Block（Wave）** | FY26 财报正文：**Wave 订阅收入与支付交易量增长**是集团增长动力之一（EDGAR 8-K） | 二线 SMB 记账活着且在长，但量级（计入"国际+其他"）远不足以撼动 QBO |
| **Xero（ASX:XRO）** | FY26（3 月止财年）5/15 发布：营收双位数增长+利润率扩张，支付（Melio 并购整合）与国际扩张驱动（Yahoo AU/简单墙报 5/15 标题级）；**8/18（今日）Kalkine 全文：Xero 上线自然语言 AI 代理构建器**，让小企业和会计"零代码"自动化财务/合规工作流，限量内测；股价 A$82.75 | 记账层竞争者把"代理化"做成产品化能力——记账生态位的战争已经打响 |
| **OpenAI** | 7/26 Forbes："ChatGPT 面向小企业的新培训"（标题级） | 入口方向 SMB 渗透，但尚无记账系统级产品 |

**格局结论**：SMB 财务软件正在**分层**——(a) 记账/对账/合规执行层：被 AI 代理商品化（Xero 代理构建器、Mashable 1 折促销都是症状）；(b) 资金层（信贷/支付/资金停靠）：QuickBooks 转型方向，粘性最高；(c) 中端 ERP 层：Intuit Enterprise Suite 上攻，对手是 NetSuite/Microsoft。INTU 在 (b)(c) 的卡位是它对冲 (a) 通缩的方式。

---

## 4. AI 代理层对企业软件计价模式的影响

**行业级证据（本次正文级两篇+标题级五篇）**：

1. **Bessemer《AI 定价与变现手册》（2/9，全文）**：AI 与传统软件的根本区别是**交付不再免费**——推理算力+人工兜底构成真实 COGS，"每一次查询都有不低的成本"；结论章节标题即"**AI 产品负责人将按结果变现（monetize outcomes）**"。
2. **CIO.com 6/16**："IT 行业正冲向'企业计价大重置'（Great Enterprise Pricing Reset）"（标题级，正文 404）。
3. **CNBC 7/14**：Sierra 联合创始人（Bret Taylor）谈"AI 代理可能改变软件公司的收钱方式"（标题级）。
4. **RSM 3/25**："代理化 AI 改造行业，SaaS 厂商必须调整计价模式"（标题级）。
5. **Futurum 5/20**：Zendesk 押注自主代理+**按结果计价**颠覆客服模式（标题级）。
6. **WSJ 4/30、CRN 2/18、Built In 3/24**：同一主题的媒体/渠道侧确认（标题级）。
7. **McKinsey 5 月（经 IT Jungle 7/27 全文转述）**：对 $100B 全球 ERP 市场给出五种情景——从"彻底解体（SaaSpocalypse 极端版：代理即时创建流程、应用逻辑商品化）"到"代理加速 ERP 实施"；其**基准情景**是"ERP 继续存在但 AI 化：应用逻辑仍执行商业规则、数据结构保证一致性、系统记录提供可审计性——只是**用户不再直接与系统交互**，由代理执行、人类设定意图/校验结果/处理例外"。

**芒格点评**：计价从"按席位"到"按结果"的迁移，短期对 INTU 是**保护而非破坏**——Intuit 本来就按"一次申报/一笔账/一笔贷款"结果收费（TurboTax 按次、QuickBooks 按月但锚定账目规模、Credit Karma 按转化），它比任何按席位的 SaaS（CRM/HCM）都更接近结果计价。真正的风险在 10 年维度：当结果本身（"报完税"）可被代理以近零边际成本交付时，收费锚点必须从"结果"进一步上移到"责任与资金"（审计、担保、信贷分发）——这恰好是 Intuit 正在搬迁的方向（见第 3 节 QuickBooks 信贷中心化）。

---

## 5. 芒格"生态学"：10 年税务/记账格局推演

芒格的 ecology 方法：先看地形（谁靠谁活着），再看物种（谁适应地形），最后才看天气（季度股价）。

**地形的三根支柱（10 年维度）**：
1. **税法的复杂度只会上升**：2025-11 ITEP《特朗普提高了申报成本》+ 2026-04-09 CBPP《纳税人三重打击：IRS 削减、无 Direct File、扭曲的税法修改》（双标题级）——新税法增加条款复杂性 = 付费辅助需求上升。**复杂度是 TurboTax 的食物链底层**。
2. **政府退出捕食**：Direct File 已死、IRS 在裁员（JOC 8/12：纸质退税延迟）、Warren 复活努力停留在标题。10 年内免费政府申报卷土重来的概率：低（两党口径罕见一致——私营部门更好）。
3. **责任不可代理**：AI 代理可以算税，但**不能坐牢、不能被审计、不能赔罚款**。"签字责任"的供给者（Intuit 的 Maximize/审计保障、HRB 的人工）在 10 年内仍是稀缺资源。

**物种演化的两种命运**：
- **税务（TurboTax + 专业 preparer）**：堡垒生态位。入口（ChatGPT 问税）会分流低价 DIY，但 OpenAI 选择接入 Intuit（"plans to support Intuit"+Intuit 7/21 官宣合作）说明入口层也想要这块的数据与责任联盟。10 年格局大概率仍是 INTU 占 DIY 高价值段、HRB 占人工段、二者合计份额上升（Direct File 死者份额的再分配）。
- **记账（QuickBooks/记账员）**：战场生态位。Xero 代理构建器、氛围编程、Mashable 1 折促销共同指向：**纯执行层（对账、分类、合规表格）10 年内会被代理压缩到近零毛利**。幸存者的形态是"资金层平台"（信贷+支付+存款停靠）与"中端 ERP"——这正是 Intuit 2026 年的战略搬迁方向。搬迁能否成功是 10 年问题的核心，本次行业维度证据**不足以定论**（见缺口）。

**反向清单（什么会推翻以上推演）**：(a) OpenAI 从"接入 Intuit"翻脸为"自营报税+承担审计责任"（需牌照与责任结构，10 年内门槛高）；(b) 联邦复活 Direct File 并强制预填（当前无迹象）；(c) 会计职业界监管剧变允许 AI 签字（无迹象）。

---

## 6. 1-6 个月催化剂表

| 日期 | 事件 | 性质 | 行业维度看点 | 来源 |
|---|---|---|---|---|
| **2026-08-25（周二，盘后）** | INTU FQ4+FY26 财报 | ★★★ 直接 | FY27 指引：QuickBooks 记账层是否被代理通缩（ARPS vs 订户数）、TurboTax 税季后份额回收、Direct File 死后首季留存 | 官方 PR 7/30（Yahoo 转载）+ Barchart 8/12 + MarketBeat 8/18 |
| **2026-09-08** | 证券集体诉讼首席原告截止 | ★ 风险 | 四家律所（Levi & Korsinsky/Faruqi/Gross 等）PR 齐发；诉讼聚焦期间内披露问题——和解金与 FY27 管理层注意力成本 | GlobeNewswire/PRN/TMX/Newsfile 四源标题 |
| **2026-09-17** | Intuit 年度 Investor Day | ★★★ 直接 | 新财年战略：Intuit Intelligence 代理平台定价（按结果？）、OpenAI/Anthropic 合作细节、中端市场（Enterprise Suite）目标 | IR 站 URL slug `20260917-intuits-annual-investor-day` + 官方 PR 标题 |
| **2026-10~12** | 软件板块并购延续性观察 | ★★ 板块 | Silver Lake-Workday 谈判是否落地（8/13 起）；若落地，SaaS 估值地板确认，INTU 修复行情延续；破裂则回吐 | Reuters 8/13 独家（Futurum 8/18 转述细节） |
| **2027-01~04** | 2027 税季（Direct File 死后第二个税季） | ★★★ 直接 | OBBBA 税法修改首个完整生效税季（CBPP"三重打击"），复杂度红利兑现；TurboTax 定价权与 HRB NAC 双升验证 | CBPP 4/9 + ITEP 11/25 + HRB FY26 8-K 分部数据 |
| 持续 | 分析师目标价重置 | ★ 情绪 | Mizuho 8/17 前后：维持跑赢大盘，PT $500→**$430**（隐含 +21.6%，python 复核）——"FY27 展望重置"基调；Truist 8/4 已先降级至 Hold | Investing.com/Moomoo/MarketBeat/MarketScreener 四源标题 |

---

## 7. 行业评分与缺口

### 7.1 行业维度评分（芒格视角）：**7.0 / 10**（较恐慌时点上调，非看多一切软件）

- **+2.0 税务生态位**：Direct File 死亡 + IRS 衰弱 + 税法复杂度上升，三重顺风，10 年内可见度极高
- **+1.5 估值保护**：PE（Silver Lake/Thoma Bravo）用 ~5x 2027E 收入的价格抢购"被 AI 恐慌错杀"的软件资产；企业买家调研证明迁移惰性
- **+1.0 计价模式免疫**：INTU 天生按结果计价，比按席位 SaaS 更抗压；且正主动搬迁到资金/责任层
- **+1.0 入口威胁缓和**：OpenAI"计划支持 Intuit"+Intuit 官宣 OpenAI/Anthropic 合作（双源）
- **+0.5 竞争者验证**：HRB FY26 证明 AI 在税务上是提价工具（Assisted +6.1%、EPS +13.9%）
- **-1.5 记账层通缩**：Xero 代理构建器（今日）+ QBO 1 折促销（今日）+ 氛围编程幽灵——QuickBooks 的执行层 10 年内毛利承压是真实的
- **-1.0 入口租金**：2 亿月金融提问在 ChatGPT 手里，Credit Karma 类导流生意的长期分成结构未定
- **-1.0 自证嫌疑**：Intuit 裁员 17% 聚焦 AI + Mizuho"FY27 展望重置"——管理层比任何人更早知道增长在哪不在哪

### 7.2 缺口清单（如实标注，未补齐即低置信）

1. **INTU FQ4 共识 EPS/收入**：Zacks 预览（Yahoo 8/18 载）被重定向墙挡住，**未取得具体一致预期数字**——财报前的锚缺失
2. **HRB AI Tax Assist 用量**："数百万提问"仅标题级（StockTitan 被墙），无正文数字
3. **Intuit-OpenAI/Anthropic 合作条款**：Intuit 官方博客 7/21 正文 404，仅有标题+OpenAI 侧 5/15 正文间接互证
4. **Xero FY26 具体营收/订户数**：定性"双位数增长+利润率扩张"（多源标题），未取得绝对值（其官网被墙）
5. **QuickBooks 订户数/ARPS 趋势**：需 8/25 财报原文，本次仅行业侧证据（促销+信贷中心化）
6. **Silver Lake-Workday 谈判条款**：仅为报道阶段（Reuters 独家），未签约， Breakingviews $227/股为模拟值
7. **OBBBA 税法条款对 2027 税季的具体影响面**：CBPP/ITEP 标题级，未取正文逐条

### 7.3 双源对照表（关键数据）

| 数据 | 源 1 | 源 2 | 状态 |
|---|---|---|---|
| INTU 盘中价 $353.51 / 52 周区间 | Yahoo chart API | stockanalysis（页面可读部分无冲突）+ TIKR YTD -45% 口径互洽 | ✅ |
| 市值 $96.7B | 10-Q 股本 273.537M（EDGAR） | × Yahoo 现价（python 精算） | ✅ |
| 8/25 财报 + 9/17 Investor Day | Intuit 官方 PR 7/30 | IR 站日历 slug + Barchart/MarketBeat | ✅ |
| Direct File 死亡与 0.20% 份额 | JOC 11/6 正文（Treasury 报告数据） | Marketplace/Nextgov/ITEP/CBPP 多源 | ✅ |
| HRB FY26 分部数字 | EDGAR 8-K Ex99.1 正文 | GlobeNewswire 同文（8-K 引用） | ✅（同一 PR 的两个载体，实质单源，已标注） |
| OpenAI→接入 Intuit | TechCrunch 5/15 正文原话 | Intuit 7/21 博客标题（OpenAI/Anthropic 合作） | ✅（标题级互证） |
| 软件指数 QTD +25% / WDAY +18% | Futurum 8/18 正文 | Reuters 8/13 / CNBC 8/13（标题） | ✅ |
| SaaSpocalypse 定义与受损名单 | IT Jungle 7/27 正文 | ChosunBiz 8 月标题（SaaSpocalypse 措辞） | ✅ |
| Mizuho PT $430（原 $500） | Investing.com 标题 | Moomoo/MarketBeat/MarketScreener 三源标题 | ✅ |
| Xero AI 代理构建器（8/18） | Kalkine 全文 | —（单源正文） | ⚠️ 单源，已标注 |
| McKinsey 五情景 | IT Jungle 转述 | McKinsey 原文未直取 | ⚠️ 二手转述，已标注 |

---

**芒格最后一问**：如果这个行业十年后什么都没变只是更贵了，你会难过吗？——税务端不会（堡垒只会更深）；记账端会（那是一场必须打赢的搬迁）。8/25 财报和 9/17 Investor Day 就是看这场搬迁路线图的窗口。

*本报告为学习与研究用途，不构成投资建议。*
