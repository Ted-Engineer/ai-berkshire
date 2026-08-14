# Agent-E 数据包：美股软件股 H2 扫描 —— 深价值 vs AI颠覆之辩

> 数据截止：2026-08-07（周五，美股最近收盘日）｜报告生成：2026-08-08（北京时间）
> 采集人：Agent-E（软件板块：深价值与AI颠覆之辩）
> 方法：web_search 英文查询；来源以 stockanalysis.com / macrotrends / gurufocus / investing.com / Yahoo Finance / MarketWatch / barchart / 公司IR 为主。
> 规则：所有数字注明来源与口径；搜索不到一律 N/A；推算值明确标注"推算"并降低置信度。严禁编造。

## 0. 一句话结论（数据层）

软件板块 2 月暴跌后极度分化："工作流入口型"软件（INTU/ADBE/HUBS/FICO/CRM/NOW/WDAY/ORCL）YTD 仍跌 20~60%，forward PE 压到 9~25x 历史低位；而"AI基建/受益型"软件（PANW +95%、DDOG 约+120%、CRWD +79%、SNOW +45%、NET、PLTR）已创新高。**营收并未崩塌**（16 家最近一季营收 YoY 在 +10%~+93% 之间），崩塌的是估值倍数——"黄金坑还是价值陷阱"取决于 agents 吞噬 seats/工作流是否成为长期事实。

## 一、2026年2月 "SaaSpocalypse" 事件回顾（必查项#1）

| 日期 | 事件 | 影响 / 来源 |
|---|---|---|
| 2026-02-03 | Anthropic 发布 Claude Cowork 行业插件（含法律插件） | 触发单日约 $285B 软件股抛售（"SaaSpocalypse"；前轮检索，Reuters/Bloomberg 报道） |
| 2026-02-03~24 | 法律软件受冲击最重 | Thomson Reuters -16%、RELX -14%、Wolters Kluwer -13%（Bloomberg；前轮检索） |
| 2月上旬 | Anthropic "Claude Code Security" 相关发布 | 单日抹去安全股约 $15B 市值（但安全板块其后完全收复并领涨：PANW YTD +95%） |
| 2026-02-06 | Claude Opus 4.6 发布 | 情绪面持续施压（前轮检索） |
| 2026-02-24 | 软件股反弹日 | Anthropic 新版本发布被解读为利好，CRM 当日 +4%（前轮检索） |
| 截至 2026-02-24 | 软件/服务板块累计蒸发约 $1 万亿市值 | Reuters 2/24（前轮检索） |
| 4~5月 | 反弹波段 | NOW 曾录"历史性月份"（5/29；前轮检索）；Fortune 2/10："agents 不会杀死 SaaS，但也不能高枕无忧" |
| 2026-05-20/21 | INTU 下调 TurboTax 全年指引 | 5/21 单日 -20%（Reuters），并引发证券集体诉讼（定价问题；class period 2025/8/22~2026/5/20） |
| 2026-06-02 | 高盛下调 INTU 至 Sell，目标价 $519→$276 | 空头叙事顶峰（前轮检索） |
| 2026年6月 | CRM 连续 14 个交易日下跌，最低 $146（YTD 一度 -42%）；2025年9月以来第三轮裁员 | 前轮检索 |
| 2026-07-22 | OpenAI 发布 Presence；OpenAI Frontier 产品线推进 | AI 巨头继续向企业软件腹地进攻（前轮检索） |
| 2026-08-03~06 | 财报季极端分化 | PLTR +30%、TEAM +35%、NET +8~15%；HUBS -19%、DDOG -19%（本轮核实） |

**板块基准 IGV（iShares 软件 ETF）**：
- YTD ≈ **-6.0%**（marketbeat，截至 8/6）；etfrc（截至 7/31）为 -10.5%；NAV $99.46（MarketWatch 8/6）。
- 1年 ≈ **-11.1%**（marketbeat 8/6）。同期 Yahoo 显示科技类基金 1年均值 +55%、YTD +13.5%（8/6）→ 软件相对整个科技的跑输幅度极端。
- 口径说明：任务简报中"IGV YTD -27%"对应 **2~3月谷底**水平（推算），目前已从谷底显著反弹；现价相对年初约 -6~-10%。


## 二、16 股核心数据总表

> 价格口径说明：美股 8/7 为周五收盘日，但多数来源快照停留在 8/6 收盘；凡 8/7 收盘价已核实者标 ✓，其余注明 8/7 盘中/盘前数据。所有 PE/市值/涨幅均为来源原始值或标注推算。

| 代码 | 最新价（口径） | 市值 | TTM PE | Forward PE | 最近一季营收 YoY | YTD | 1年涨幅 | 下一次财报 |
|---|---|---|---|---|---|---|---|---|
| INTU | $321.91（8/6收盘 macrotrends；8/7 约持平，stockanalysis 8/7 市值 $88.05B 反推吻合；Yahoo 曾显示 $326.35，矛盾未采信） | $88.05B（stockanalysis 8/7 ✓） | ~18.4（macrotrends 8/7；SA 20.1） | 11.6~12.3（前轮检索） | +10%（FQ3'26 $8.6B，investing 5/20） | **约-49%**（simplywall.st）；较2025高点$808 约-60%（任务简报口径） | 约-59%（stockanalysis 市值口径 8/7；tradingeconomics 7月快照 -61.7%） | **8/25 盘后**（IR 官方 ✓）+ 9/17 投资者日 |
| ADBE | **$267.54（8/7收盘 ✓，investing.com）** | ~$107~112B（推算：financecharts 8/5 $103.7B 按 8/7 价换算） | 14.3~14.7（Yahoo key-stats/SA 8/5） | 9.5~10.3（gurufocus 9.49、SA 9.93、Yahoo 10.27） | +13%（FQ2'26 创纪录 $6.62B，Yahoo） | 约-30%（推算，前轮） | -41%（barchart 7/7，前轮检索） | **约9/10**（预期，前轮核实） |
| CRM | $186.77（8/6收盘，Salesforce IR/macrotrends ✓；8/7 盘中 $190~194，MarketWatch/gurufocus） | ~$180B（capital.com 8/7；tradingeconomics $184.9B） | 20.98（stockanalysis；macrotrends GAAP 17.82） | 12.97~13.71（SA/Yahoo/gurufocus 8/7） | +13.3%（FY27Q1 $11.13B，前轮检索） | **-27.5%**（macrotrends，前轮；6月低点$146时-42%） | -22.34%（investing.com） | **8/26**（预期，前轮核实） |
| NOW | $117.35（8/6收盘 macrotrends/investing ✓；8/7 盘中 $124.61 +6.2%，MarketWatch） | ~$121B（前轮检索） | ~73（GAAP，前轮检索） | N/A | +24%（Q2'26；订阅收入 +24.5%，前轮检索） | -22.9%（macrotrends，前轮） | N/A（2025-12-18 完成 1拆5，现价 $117≈拆前 $585；52周区间 $81.24~$1057.39 含拆前口径，ADVFN） | ~10/28（预期，未确认） |
| FICO | $1,031.89（8/6收盘 macrotrends/tradingeconomics ✓，当日-5.47%；8/7 盘中约 $1,052 Robinhood，低置信） | ~$22.3B（前轮检索） | ~30（前轮检索） | ~24.3（推算：8/6 收盘 ÷ FY26 指引 EPS $42.43，Yahoo） | +26%（FQ3'26 $674M，beat 但低于买方预期；scores +41%、platform +66%，前轮检索） | 约-37%（推算，前轮） | 约-48%（推算，前轮） | ~11月初（未确认） |
| TEAM | $110.17（8/6收盘 Yahoo ✓；8/6盘后 FY26Q4 超预期 → **+35.5% 至 $149.25**，investing transcript；8/7 收盘约 $140~149，推算） | ~$36.6B（8/6口径，前轮；8/7大涨口径推算 ~$39B） | N/A（GAAP 亏损） | ~15.5~20.3（前轮检索） | +28%（FY26Q4 约$1.8B，EPS $1.87 超预期，前轮检索） | 约-7%（推算：年初约$155；2月低点$70 曾-55%） | 约-49%（推算；2025全年-74%，前轮） | 8/6 已报；下次 ~10/29（预期） |
| WDAY | $170.24（8/6收盘 tradingeconomics/MarketWatch prev close；8/7 盘中 $179.37 +5.4%，MarketWatch） | ~$43.6~45.9B（tradingeconomics $43.57B/capital.com $45.92B，8/5-8/6） | ~50（Yahoo 7/31 49.95，低置信） | ~15.1（前轮检索） | +13.5%（FY27Q1 $2.542B，前轮检索） | 约-20%（macrotrends 8/4 -20.25%，低置信；Yahoo +16.5% 字段冲突，未采信） | -23.34%（investing.com） | **8/27 盘后**（官方 ✓，Yahoo） |
| HUBS | **$212.49（8/7收盘 ✓，Yahoo history）** | ~$11.2B（推算：约52.7M股×$212.49） | 78.7（macrotrends，前轮；Robinhood 125.81 口径不同） | ~18.5（前轮检索） | +19.8%（Q2'26 $912M 超预期，但下调指引，8/5 盘后，bizjournals） | 约-45%（推算：年初约$384） | 约-55%（推算；52周高 $525.51） | ~11月初（未确认） |
| PLTR | $155.92（8/6收盘 MarketWatch prev close ✓；8/7 盘中 $158.5~160.3） | ~$374B（推算：public.com 7/31 $295B÷$123.06≈2.40B股 × $155.92） | ~135（推算，低置信） | N/A | **+93%**（Q2'26 $1.935B，GAAP 净利 $1.07B/EPS 41c，marketbeat 8/4） | 约-13%（推算：年初约$177） | 约+35%（推算） | 8/3 已报；下次 ~11月初（未确认） |
| MSFT | $499.86（8/6收盘 MarketWatch prev close ✓；8/7 盘中 $502.80 +0.59%） | ~$3.71T（前轮检索） | ~27.9（前轮检索） | ~25.4（前轮检索） | +18%（FY26Q4 $90.01B；Azure +43%、FY26 Azure 突破 $100B，前轮检索） | +2.2%（前轮检索） | -5.8%（marketbeat，前轮检索） | ~10/28（未确认） |
| ORCL | $143.47（8/6收盘 Oracle IR ✓；8/7 盘前 $144.84，CNN） | ~$400B（前轮检索） | ~24.6（前轮检索） | N/A | +21%（FY26Q4；云 +47%，但软件/许可证 -1%，前轮检索） | 约-22%（推算：年初约$185） | 约-35%（推算；52周高 $345.72，CNBC，现价较高点约-58%） | ~9/8（预期，部分来源 9/13-14） |
| SNOW | $318.00（8/6收盘 macrotrends/investing ✓；8/7 盘中 $327.20 +2.9%，MarketWatch） | ~$110B（前轮检索） | N/A（GAAP 亏损） | 141~147（前轮检索） | +33%（FY27Q1；产品营收 +34%，前轮检索） | **+45%**（前轮检索） | +54%（financecharts，前轮检索） | **8/26**（预期） |
| DDOG | $235.40（8/7 Yahoo 行情 +2.66%；8/6 收盘 $229.29 ✓ macrotrends/investing） | ~$84B（推算：public.com 8/5 $100.8B÷$283.17≈356M股 × $235.40；macrotrends 8/7 仍显示 $100.8B，疑未更新） | ~462（stockanalysis） | 87.3（stockanalysis；Yahoo 111） | **+36%**（Q2'26 $1.12B，EPS $0.65 超预期并上调指引，但 8/6 单日-19%，investing） | 约+120%（推算：年初约$107；8/4 历史高 $288.15） | +75.31%（tradingeconomics ✓） | 8/6 已报（盘前）；下次 ~11月初 |
| PANW | $359.49（8/6收盘 Yahoo history ✓；8/6盘后 $363.99，MarketWatch） | ~$293B（前轮检索） | ~290（前轮检索） | ~80.7（前轮检索） | +31%（FY26Q3 $3.0B，前轮检索） | **+95%**（Yahoo，前轮） | 约+90%（推算） | **9/1**（已核实，前轮 ✓） |
| CRWD | $207.45（8/6收盘 macrotrends ✓；CNN $207.39；8/7 盘前 $212.68 +2.55%，CNN） | ~$210B（前轮检索） | N/A（GAAP 亏损） | N/A | +26%（FY27Q1；ARR $5.51B +24%，前轮检索） | **+79%**（macrotrends，前轮） | +67.8%（前轮检索） | **8/26**（Yahoo 核实 ✓） |
| NET | $284.43（8/6收盘 Yahoo history ✓；8/7 盘中 +8~15% 至约 $307~325 区间，MarketWatch 盘前 +15.6%、Yahoo 10:48 +8.1%；8/7 收盘约 $307~310，推算，低置信） | $103.55B（macrotrends 8/6 ✓；8/7 大涨后推算 ~$110B） | N/A（GAAP 亏损） | ~232（前轮检索） | **+36%**（Q2'26 $696M 超预期；FY 指引上调至 $2.86~2.87B，EPS $1.25~1.26，前轮检索） | N/A（推算 +40~50%，低置信；屡创新高） | +35%（investing，前轮检索） | 8/6 已报（盘后）；下次 ~10/29（预期） |

**YTD 跌幅榜（由深到浅）**：INTU 约-49%（较高点-60%）＞ HUBS 约-45% ＞ FICO 约-37% ＞ ADBE 约-30% ＞ CRM -27.5% ＞ NOW -22.9% ＞ ORCL 约-22% ＞ WDAY 约-20% ＞ PLTR 约-13% ＞ TEAM 约-7%（财报后基本收复）＜ MSFT +2.2% ＜ SNOW +45% ＜ CRWD +79% ＜ PANW +95% ＜ DDOG 约+120%（NET 推算 +40~50%）。


## 三、AI颠覆之辩专节

### 3.1 多头证据（"颠覆是真的"）

1. **Anthropic 插件化进攻**：2/3 Claude Cowork 行业插件（法律、金融等）直接对标垂直 SaaS 工作流；法律信息/研究软件单日重挫（TR -16%、RELX -14%），Bloomberg 认定法律软件受冲击最重。
2. **累计杀伤力**：至 2/24 软件+服务板块累计蒸发约 $1 万亿市值（Reuters）。
3. **OpenAI 持续进攻**：7/22 发布 Presence、推进 Frontier 等企业级 agent 产品（前轮检索）。Anthropic 估值 $380B、Claude Code 年收入 >$2.5B（前轮检索）——AI 原生工具的商业化速度在加快。
4. **管理层亲口承认**：HUBS CEO Yamini Rangan 在 8/5 Q2 电话会上明确把"AI 竞争 + 销售周期拉长"作为下调 2026 指引的理由 → 8/6 单日 -19%（bizjournals/MarketBeat）。这是中型 SaaS 首个"管理层自认被 AI 冲击"的案例。
5. **INTU 的税季验证偏空**：5/20 下调 TurboTax 全年指引至 $5.277~5.282B（原 $5.305B），5/21 股价 -20%（Reuters）；叠加"定价问题"集体诉讼（class period 2025/8/22~2026/5/20）。高盛 6/2 降级 Sell、目标价砍至 $276。
6. **空头理论**：Storm Ventures："系统记录（systems of record）正在沦为哑数据库"——若 agents 直接操作数据层，按 seat 收费的界面层软件失去定价权。

### 3.2 空头证据（"颠覆被夸大/已被定价"）

1. **营收没有崩塌**：16 家全部为正增长，TEAM +28%、PLTR +93%、NET/DDOG/SNOW/PANW +31~36%、CRM +13.3%、INTU 也有 +10%。被"判死刑"的公司收入端仍双位数增长。
2. **财报即反转**：TEAM 8/6 财报 +35.5%、PLTR 8/4 +30%、NET 8/7 +8~15%、CRM 自 6 月低点 $146 反弹约 +27%（至 8/7 ~$190-194）；2/24 Anthropic 新版本发布当天软件股就反弹（CRM +4%）。
3. **AI 货币化是软件公司的期权**：CRM Agentforce ARR $1.2B（+205% YoY，FY27Q1；AI+Data 合计 ARR $3.4B）；ADBE Firefly AI-first ARR 三倍至 >$500M（FY26Q2，6/11）；MSFT Azure FY26 >$100B（+43%）；PANW/CRWD/DDOG 直接受益于 AI 带来的新攻击面与新可观测负载。
4. **政策利好**：IRS Direct File 已于 2025年11月废除 → TurboTax 最大政策威胁消失；TurboTax FQ2 营收仍 +12%（$581M，协助报税驱动）。
5. **Fortune 2/10 中间派观点**："agents 不会杀死 SaaS，但软件公司不能高枕无忧"——更可能的是行业洗牌而非行业消亡。
6. **估值极端压缩**：ADBE fwd PE 9.5~10x、INTU 11.6~12.3x、CRM ~13x、WDAY ~15x、FICO ~24x——即使增长中枢下移 3~5 个百分点，当前定价也已包含大量悲观预期（价值投资视角的安全边际论据）。

### 3.3 受冲击程度分类（本轮数据支持）

| 类别 | 代表 | 证据 | 判断 |
|---|---|---|---|
| 消费者工作流入口（agents 替代弹性最高） | INTU（报税）、ADBE（创意消费端）、HUBS（SMB营销） | INTU -49%、HUBS -45% 且管理层自认AI冲击 | 冲击最实，需逐季验证 DIY 流失 |
| 法律/专业信息服务 | TR、RELX（非本清单） | 2/3 单日 -14~-16% | 首个被点名的受害行业 |
| 企业 seat 型 SaaS | CRM、NOW、WDAY、TEAM | YTD -7~-28%，但营收仍 +13~28%，CRM/NOW 靠 agent 产品对冲 | 冲击中等，货币化能力决定分化 |
| 有数据/合规护城的垄断者 | FICO、ORCL、MSFT | FICO -37% 但 scores +41%、指引上调；ORCL 云 +47% | 情绪杀为主，基本面未破 |
| AI 的直接受益者 | PANW、CRWD、DDOG、NET、SNOW、PLTR | YTD +45~+120%，营收 +26~93% | AI 越多，安全/可观测/数据/推理需求越大 |

### 3.4 必查专题结果

**① TurboTax 2026 报税季实际表现（必查#2）**：
- FQ2（覆盖报税季前半段）：TurboTax 营收 $581M，+12% YoY，由 assisted tax（协助报税）驱动。
- FQ3（5/20 公布）：全年 TurboTax 指引从 $5.305B 微降至 $5.277~5.282B；公司总指引反而上调（FY26 营收 $21.34~21.37B）→ 市场聚焦税业务放缓，5/21 股价 -20%（Reuters）。
- 结论：**DIY 未崩塌（仍双位数增长），但增速放缓 + 定价受质疑（集体诉讼）**；IRS Direct File 废除消除了政策尾部风险；公司同步裁员 17%（约3,000人）、重组费用 $300~340M 以对冲。8/25 财报是 H2 第一个关键验证点。

**② Adobe Firefly（必查#3）**：AI-first ARR 同比三倍至 **>$500M**（FY26Q2，6/11 公布）；FY26 ARR 增速指引 10.2%；FY26 总营收指引 $26.5~26.6B。→ AI 货币化真实存在，但股价仍 YTD 约-30%，市场担心创意工具消费端（Canva/生成式模型）侵蚀核心。9/10 财报验证。

**③ Salesforce Agentforce（必查#4）**：ARR **$1.2B**（FY27Q1，+205% YoY；上季 $800M/+169%；交易数 29K→38K+）；AI+Data 合计 ARR $3.4B。→ agent 产品货币化是全行业最快之一，但未能抵消市场对 seat 压缩的担忧（YTD -27.5%）。8/26 财报验证。

## 四、个股简评（每条约80字）

1. **INTU（$322，YTD -49%）**：税季指引下调+集体诉讼+高盛砍目标价至$276，三重打击后 fwd PE 仅 ~12x。DIY 未崩但增速放缓已证实；8/25 财报+9/17 投资者日是"价值陷阱还是黄金坑"的第一判决点。
2. **ADBE（$267.54，YTD -30%）**：fwd PE 9.5~10x 为上市以来最低区间，Firefly ARR 三倍至 $500M+ 证明 AI 货币化，但市场担心创意工具消费端被生成式模型侵蚀。9/10 财报看 ARR 增速能否守住 10%+。
3. **CRM（$186.77→8/7约$190-194，YTD -27.5%）**：6月14连阴后已反弹 +27%；Agentforce ARR $1.2B（+205%）是行业最强 agent 货币化证据，fwd PE ~13x。8/26 财报验证 seat 流失 vs agent 增量的赛跑。
4. **NOW（$117.35，YTD -22.9%）**：拆股后价格失真需注意；Q2 营收 +24% 稳健，4~5月曾"历史性反弹"。企业工作流+合规护城河较深，但估值仍 ~73x GAAP PE，AI 对 IT 工单自动化的替代是中期疑问。
5. **FICO（$1,031.89，YTD 约-37%）**：FQ3 +26% 但低于预期引发大跌；scores +41% 显示按揭定价垄断仍在，FY26 指引上调（EPS $42.43）。fwd ~24x，风险在 FHFA 政策干预而非 AI。
6. **TEAM（$110.17→8/7约$140-149）**：8/6 财报 +35.5% 是本轮最强反转信号——营收 +28% 证明协作软件未死；2025 年 -74% 的极端悲观定价正在修复。关注 FY27 指引质量。
7. **WDAY（$170.24，YTD 约-20%）**：营收 +13.5% 稳健但 HR SaaS 是 agents 替代的高危区（招聘/绩效流程自动化）；fwd PE ~15x 已便宜。8/27 财报与 AI 产品 ARR 披露是关键。
8. **HUBS（$212.49，YTD 约-45%）**：本轮"AI 受害者"最实锤——CEO 亲口以 AI 竞争下调指引，单日 -19%。但营收仍 +19.8%、fwd ~18.5x；赌的是 SMB 营销预算回流 vs agents 自建营销。
9. **PLTR（$155.92，YTD 约-13%）**：营收 +93%、Rule-of-40=155、美国商业 +149%，是 AI 时代的平台赢家而非受害者；但估值 ~135x TTM PE，风险在定价而非商业模式。
10. **MSFT（$499.86，YTD +2.2%）**：Azure FY26 >$100B（+43%），AI 基建收入直接对冲 M365 seat 风险；~28x PE 是软件辩论中的"中立参照系"。关注 Copilot 货币化与 OpenAI 关系。
11. **ORCL（$143.47，YTD 约-22%）**：云 +47% 但传统软件许可证 -1%——教科书式的 AI 时代新旧业务剪刀差；52周高 $345.72 回撤 -58%。9/8 财报看 RPO 与云增速持续性。
12. **SNOW（$318，YTD +45%）**：数据平台是 agents 的弹药库，营收 +33%/产品 +34%；但 fwd PE 141~147x 已完全定价乐观。8/26 财报与 CRM 同日，验证数据层景气度。
13. **DDOG（$235.40，YTD 约+120%）**：营收 +36%+上调指引仍单日 -19%——说明受益型软件的拥挤度与预期已极高；可观测性是 AI 负载的刚需，风险在估值消化而非需求。
14. **PANW（$359.49，YTD +95%）**：2月"Claude Code Security"曾砸出 $15B 坑，随后证明 AI 扩大攻击面 → 安全预算增加。营收 +31%，9/1 财报；风险同 DDOG：好公司贵价格。
15. **CRWD（$207.45，YTD +79%）**：ARR $5.51B +24%，平台化（Falcon）对冲单点替代风险；8/26 财报是"财报压力测试"（home.saxo 6/1 语）。拆股后流动性改善。
16. **NET（$284.43→8/7约$307-310）**：Q2 +36%+上调指引，AI 推理/边缘网络是核心叙事（Morningstar 8/7）；8/7 财报后大涨 +8~15%。YTD 未找到精确值（推算 +40~50%）。


## 五、H2 催化剂日历（财报与事件）

| 日期 | 事件 | 状态 |
|---|---|---|
| 2026-08-25 | INTU FY26Q4 财报（盘后 4:30pm ET） | 官方确认（investor.intuit.com ✓） |
| 2026-08-26 | CRM FY27Q2 财报 | 预期（前轮核实） |
| 2026-08-26 | CRWD FY27Q2 财报 | Yahoo 确认 ✓ |
| 2026-08-26 | SNOW FY27Q2 财报 | 预期 |
| 2026-08-27 | WDAY FY27Q2 财报（盘后 4:05pm ET） | 官方确认（Yahoo ✓） |
| 2026-09-01 | PANW FY26Q4 财报 | 前轮核实 ✓ |
| ~2026-09-08 | ORCL FY26Q1 财报 | 预期（部分来源称 9/13-14） |
| ~2026-09-10 | ADBE FY26Q3 财报 | 预期（前轮核实） |
| 2026-09-17 | INTU 投资者日 | 官方确认（Investing.com 8/4 ✓） |
| ~2026-10-22~24 | Atlassian Team '26 大会 | 前轮检索 |
| ~2026-10-28 | MSFT FY26Q1 财报 | 未确认 |
| ~2026-10-28 | NOW FY26Q3 财报 | 未确认 |
| ~2026-10-29 | TEAM FY27Q1 财报 | 预期 |
| ~2026-10-29 | NET Q3'26 财报 | 预期 |
| ~2026-11月初 | FICO FY26Q4、HUBS Q3、PLTR Q3、DDOG FY26Q3 | 均未确认 |

关键观察点：8/25~8/27 三天（INTU/CRM/CRWD/SNOW/WDAY）是软件板块 H2 最密集的验证窗口——深价值组（INTU/CRM/WDAY）与受益组（CRWD/SNOW）同台对质。

## 六、数据源与置信度说明

- 8/7 收盘价已核实：ADBE $267.54（investing.com history）、HUBS $212.49（Yahoo Finance history）、DDOG $235.40（Yahoo 行情，+2.66%）。
- 其余 13 只：8/6 收盘价已核实（macrotrends/IR/Yahoo history/MarketWatch prev close），8/7 仅有盘中/盘前/盘后快照（已在表内注明）。
- 已知来源冲突：① INTU 8/6 收盘 Yahoo 显示 $326.35 vs macrotrends/indmoney $321.91~322.01（采信后者，与 stockanalysis 8/7 市值 $88.05B 反推一致）；② WDAY/HUBS 的 Yahoo YTD 字段（+16.5%/+46.8%）与价格事实明显矛盾，未采信；③ IGV YTD：marketbeat -5.97%（8/6）vs Yahoo +5.92%，采信 marketbeat（与 etfrc 7/31 -10.5% 方向一致）；④ DDOG 财报时间为 8/6 盘前（stockanalysis），此前记录的 8/6 盘后系误，已更正。
- 所有"推算"值仅用于排序与定性判断，不作为投资依据；N/A 表示未找到可信来源。

## 七、JSON 数据

```json
[
  {"ticker":"INTU","price":321.91,"mcap_b":88.05,"ttm_pe":18.4,"fwd_pe":12.0,"rev_growth_yoy":10,"ytd_pct":-49,"one_year_pct":-59,"earnings_date":"2026-08-25","notes":"价格为8/6收盘(macrotrends;8/7约持平,stockanalysis 8/7市值$88.05B反推吻合)。fwd PE区间11.6-12.3。FQ3营收$8.6B+10%;5/20下调TurboTax指引($5.305B->5.277-5.282B)->5/21单日-20%(Reuters)+定价集体诉讼;裁员17%。YTD-49%(simplywall.st);较2025高点$808约-60%。9/17投资者日。"},
  {"ticker":"ADBE","price":267.54,"mcap_b":110,"ttm_pe":14.5,"fwd_pe":9.9,"rev_growth_yoy":13,"ytd_pct":-30,"one_year_pct":-41,"earnings_date":"2026-09-10(预期)","notes":"价格为8/7收盘(investing.com✓)。市值为推算(financecharts 8/5 $103.7B按8/7价换算,$107-112B)。FQ2创纪录$6.62B+13%;Firefly AI-first ARR三倍至>$500M(6/11);FY26指引$26.5-26.6B。TTM PE 14.3-14.7;fwd PE区间9.5-10.3。YTD约-30%为推算;1年-41%(barchart 7/7)。"},
  {"ticker":"CRM","price":186.77,"mcap_b":180,"ttm_pe":21.0,"fwd_pe":13.5,"rev_growth_yoy":13.3,"ytd_pct":-27.5,"one_year_pct":-22.3,"earnings_date":"2026-08-26(预期)","notes":"价格为8/6收盘(Salesforce IR/macrotrends);8/7盘中约$190-194(MarketWatch/gurufocus $193.57)。市值~$180B(capital.com 8/7)。FY27Q1 $11.13B+13.3%;Agentforce ARR $1.2B(+205%);AI+Data合计ARR $3.4B;第三轮裁员。6月14连阴最低$146(YTD-42%),其后反弹约+27%。"},
  {"ticker":"NOW","price":117.35,"mcap_b":121,"ttm_pe":73.3,"fwd_pe":"N/A","rev_growth_yoy":24,"ytd_pct":-22.9,"one_year_pct":"N/A","earnings_date":"~2026-10-28(预期,未确认)","notes":"价格为8/6收盘(macrotrends/investing✓);8/7盘中$124.61+6.2%(MarketWatch)。2025-12-18完成1拆5(newsroom),现价$117约等于拆前$585;52周区间$81.24-$1057.39(ADVFN,含拆前口径)。Q2营收+24%/订阅+24.5%。YTD-22.9%(macrotrends)。"},
  {"ticker":"FICO","price":1031.89,"mcap_b":22.3,"ttm_pe":30.2,"fwd_pe":24.3,"rev_growth_yoy":26,"ytd_pct":-37,"one_year_pct":-48,"earnings_date":"~2026-11月初(未确认)","notes":"价格为8/6收盘(macrotrends/tradingeconomics,当日-5.47%);8/7盘中约$1052(Robinhood,低置信)。FQ3 $674M+26%但低于买方预期;scores+41%/platform+66%。8/5上调FY26指引至营收$2.53B、EPS $42.43(Yahoo),fwd PE按此推算≈24.3。YTD/1年为推算。"},
  {"ticker":"TEAM","price":110.17,"mcap_b":36.6,"ttm_pe":"N/A","fwd_pe":18.0,"rev_growth_yoy":28,"ytd_pct":-7,"one_year_pct":-49,"earnings_date":"2026-08-06已报;下次~2026-10-29(预期)","notes":"价格为8/6收盘(Yahoo history✓);8/6盘后FY26Q4超预期+35.5%至$149.25(investing transcript);8/7收盘约$140-149(推算)。FY26Q4营收约$1.8B+28%,EPS $1.87超预期。市值为8/6口径~$36.6B(前轮),8/7大涨口径推算~$39B。2025全年-74%;2月低点$70。GAAP亏损故TTM PE为N/A。"},
  {"ticker":"WDAY","price":170.24,"mcap_b":45.0,"ttm_pe":50,"fwd_pe":15.1,"rev_growth_yoy":13.5,"ytd_pct":-20,"one_year_pct":-23.3,"earnings_date":"2026-08-27盘后(官方✓)","notes":"价格为8/6收盘(tradingeconomics/MarketWatch prev close);8/7盘中$179.37+5.4%。市值$43.6-45.9B(tradingeconomics/capital.com)。FY27Q1 $2.542B+13.5%。YTD为macrotrends 8/4 -20.25%(低置信);Yahoo +16.5%字段冲突未采信。1年-23.34%(investing);52周区间110.36-249.85。TTM PE 49.95(Yahoo 7/31,低置信)。"},
  {"ticker":"HUBS","price":212.49,"mcap_b":11.2,"ttm_pe":78.7,"fwd_pe":18.5,"rev_growth_yoy":19.8,"ytd_pct":-45,"one_year_pct":-55,"earnings_date":"~2026-11月初(未确认);2026-08-05已报","notes":"价格为8/7收盘(Yahoo history✓)。8/5 Q2 beat($912M+19.8%)但因AI竞争+销售周期拉长下调指引(CEO Rangan,bizjournals 8/6)->8/6单日-19.2%至$202.24(MarketBeat),8/7反弹+5.1%。市值为推算(约52.7M股×$212.49)。52周高$525.51。YTD/1年为推算。本轮AI冲击最实锤标的。"},
  {"ticker":"PLTR","price":155.92,"mcap_b":374,"ttm_pe":135,"fwd_pe":"N/A","rev_growth_yoy":93,"ytd_pct":-13,"one_year_pct":35,"earnings_date":"2026-08-03已报;下次~2026-11月初(未确认)","notes":"价格为8/6收盘(MarketWatch prev close);8/7盘中$158.5-160.3。Q2 $1.935B+93%,GAAP净利$1.07B(EPS 41c),Rule-of-40=155,美国商业+149%,FY26指引上调至$8.15-8.158B(+82%)->8/4单日+30%(marketbeat)。市值为推算(public.com 7/31 $295B/$123.06口径约2.40B股×$155.92);TTM PE约135为推算,低置信。"},
  {"ticker":"MSFT","price":499.86,"mcap_b":3710,"ttm_pe":27.9,"fwd_pe":25.4,"rev_growth_yoy":18,"ytd_pct":2.2,"one_year_pct":-5.8,"earnings_date":"~2026-10-28(未确认)","notes":"价格为8/6收盘(MarketWatch prev close✓);8/7盘中$502.80+0.59%。FY26Q4(7/30)营收$90.01B+18%,Azure+43%,FY26 Azure>$100B。AI基建直接受益者,软件辩论中的中性参照。"},
  {"ticker":"ORCL","price":143.47,"mcap_b":400,"ttm_pe":24.6,"fwd_pe":"N/A","rev_growth_yoy":21,"ytd_pct":-22,"one_year_pct":-35,"earnings_date":"~2026-09-08(预期,部分来源9/13-14)","notes":"价格为8/6收盘(Oracle IR✓);8/7盘前$144.84(CNN)。FY26Q4总营收+21%,云+47%,但软件/许可证-1%(新旧业务剪刀差)。52周区间114.50-345.72(CNBC),现价较高点约-58%。YTD/1年为推算(年初约$185)。"},
  {"ticker":"SNOW","price":318.0,"mcap_b":110,"ttm_pe":"N/A","fwd_pe":144,"rev_growth_yoy":33,"ytd_pct":45,"one_year_pct":54,"earnings_date":"2026-08-26(预期)","notes":"价格为8/6收盘(macrotrends/investing✓);8/7盘中$327.20+2.9%(MarketWatch)。FY27Q1总营收+33%/产品营收+34%。GAAP亏损故TTM PE为N/A;fwd PE区间141-147(前轮检索)。YTD+45%为AI受益组。"},
  {"ticker":"DDOG","price":235.4,"mcap_b":84,"ttm_pe":462,"fwd_pe":87.3,"rev_growth_yoy":36,"ytd_pct":120,"one_year_pct":75.3,"earnings_date":"2026-08-06已报(盘前);下次~2026-11月初(未确认)","notes":"价格为8/7(Yahoo行情+2.66%,中置信);8/6收盘$229.29✓(macrotrends/investing)。8/6盘前FY26Q2 beat(营收$1.12B+36%,EPS $0.65,上调指引)但单日-19%(获利了结+指引未达买方高预期);8/7 Baird目标价$210->$300。历史高$288.15(8/4)。市值为推算(public.com 8/5 $100.8B/$283.17口径约356M股×$235.40);macrotrends 8/7仍显示$100.8B疑未更新。1年+75.31%(tradingeconomics✓)。YTD约+120%为推算(年初约$107)。"},
  {"ticker":"PANW","price":359.49,"mcap_b":293,"ttm_pe":290,"fwd_pe":80.7,"rev_growth_yoy":31,"ytd_pct":95,"one_year_pct":90,"earnings_date":"2026-09-01(前轮核实✓)","notes":"价格为8/6收盘(Yahoo history✓);8/6盘后$363.99(MarketWatch)。FY26Q3 $3.0B+31%。YTD+95%(Yahoo,前轮)=软件板块最大赢家:2月Claude Code Security冲击后,实际安全支出因AI扩大攻击面而加速。6/18-7/17三十日+24.6%(tickeron)。1年约+90%为推算。"},
  {"ticker":"CRWD","price":207.45,"mcap_b":210,"ttm_pe":"N/A","fwd_pe":"N/A","rev_growth_yoy":26,"ytd_pct":79,"one_year_pct":67.8,"earnings_date":"2026-08-26(Yahoo核实✓)","notes":"价格为8/6收盘(macrotrends✓;CNN $207.39);8/7盘前$212.68+2.55%(CNN)。FY27Q1营收+26%,ARR $5.51B+24%。约2026-07完成1拆4。YTD+79%(macrotrends,前轮)。8/26为财报压力测试(home.saxo 6/1)。GAAP亏损故TTM PE为N/A。"},
  {"ticker":"NET","price":284.43,"mcap_b":103.6,"ttm_pe":"N/A","fwd_pe":232,"rev_growth_yoy":36,"ytd_pct":"N/A","one_year_pct":35,"earnings_date":"2026-08-06已报(盘后);下次~2026-10-29(预期)","notes":"价格为8/6收盘(Yahoo history✓);8/7盘中+8~15%(MarketWatch盘前+15.6%,Yahoo 10:48 +8.1%,区间$306.95-$324.73),收盘约$307-310(推算,低置信)。Q2 $696M+36%超预期,FY指引上调至$2.86-2.87B、EPS $1.25-1.26;AI推理需求为核心叙事(Morningstar 8/7)。YTD未找到精确值(推算+40~50%,低置信)。市值$103.55B(macrotrends 8/6),8/7大涨后推算~$110B。"}
]
```

—— 文件完 ——
