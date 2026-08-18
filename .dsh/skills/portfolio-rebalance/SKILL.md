---
name: portfolio-rebalance
description: "组合调仓全流程:持仓重研+行业分布体检+全市场候选扫描(300只)+双重准入验证,产出操作信号。当用户想做周期性调仓决策、生成买卖方案时调用(全量/lite/子集三种模式)。"
---

## DSH adapter note

This skill is generated from `skills/portfolio-rebalance.md` so Claude Code, Codex, TRAE, and DSH users share one canonical workflow. DSH discovers it as a project-level skill at `.dsh/skills/portfolio-rebalance/SKILL.md` (rank 100, highest local priority).

- Treat `$ARGUMENTS` as the user's request in the current DSH session.
- Map Claude-only surfaces to the DSH tools available in this session:
  - `Task`(单个后台子代理)→ DSH `subagent`(默认后台运行,可在同一条消息里并行启动多个)。
  - `TaskCreate`(创建多个并行子任务)→ 并行启动多个 `subagent`;当需要大规模 fan-out 编排(几十个 agent、多阶段、结构化结果)时用 `workflow`。
  - `WebSearch` / `WebFetch` → DSH `web_search`(始终可用,无需 `.claude/settings.local.json` 白名单;`WebFetch` 抓全文的能力用 `web_search` 返回的来源 URL + snippet 替代)。
  - `Bash` → DSH `bash`。
  - `Read` / `Write` / `Edit` / `Glob` / `Grep` → DSH 同名工具。
  - `Skill` → DSH `skill`(用于调用其他 ai-berkshire skill)。
  - `TodoWrite` → DSH `todo_write`。
- 配套 Python 工具原地可用:在仓库根目录运行 `python3 tools/financial_rigor.py ...` / `python3 tools/report_audit.py ...` 等(零外部依赖,见 CLAUDE.md 工具表)。DSH skill 为项目级部署,工具路径相对项目根直接生效。
- 引用其他 skill(如 `skills/financial-data.md`)时,优先用 `skill` 工具按名字加载(如 `financial-data`),而非读相对路径文件。
- 研究质量规则保留:开始研究前先 `date` 确认今天日期作为「最新数据」基准并在报告头部标注截止日期;关键财务数据至少 2 个独立来源交叉验证;估值/算术用 `tools/financial_rigor.py`精确计算;诚实标注低置信结论与数据缺口。
- 报告输出沿用既有命名规范:`reports/{公司名}/` 目录 或 `reports/{公司名}-{type}-{YYYYMMDD}.md`。

# 组合调仓：全流程调仓研究与操作信号

对 $ARGUMENTS 执行全流程调仓研究（prompt.md v4 的 skill 化执行入口）。投资期限 1-6 个月，目标是捕捉可兑现的大额收益（催化剂/事件驱动）。

**支持输入格式**：
- （空）：**全量模式**——全部持仓重研 + 全市场候选扫描 + 双重准入 + 操作方案
- `lite`：**周度轻量模式**——持仓体检 + 行业分布评估 + 设计假设核验，跳过第三步全市场扫描
- `META BABA ...`：**子集模式**——只重审指定持仓，其余持仓沿用最近报告（须标注报告路径与日期）

> 与 `/portfolio-review` 的分工：portfolio-review 是轻量组合审视（仓位/集中度/再平衡建议）；本 skill 是全量调仓流水线（含全市场候选发现与双重准入验证），单次执行数小时、成本高，按需调用。

## 运行前必读（磁盘状态与门禁模式）

1. 先运行 `date` 确认今天日期，作为"最新数据"基准并在报告头部标注截止日期。
2. **Read 两个参数文件**（每次执行必须现读，禁止凭记忆——参数可能已调整）：
   - `config/portfolio-targets.md`：目标分布、硬/软约束分级、分类判例表、风险参数、设计假设
   - `config/search-matrix.md`：GICS 25组双视角词、AI 17赛道、非AI 14主题、7维交叉、候选来源A-I
3. **磁盘状态模式**（本流程长，上下文会被压缩——一切中间产物即时落盘，中断后重开会话凭磁盘状态续跑）：
   - 开始时创建 `.claude/.workflow/active` 文件（激活工作流，gate脚本据此生效）
   - 搜索：每次调用后手动追加一行 `UTC时间 | 工具名 | 搜索词` 到 `.claude/.workflow/search-log.txt`，并写对应 `.used` 标记（builtin-websearch.used / mcp-web-search.used / mcp-kepler-search.used）
   - 候选：每发现一只立即追加 `.claude/.workflow/candidates.csv`（表头 `ticker,company,gics_sector,source`，同ticker不重复，下限300只、理想350只）
   - skill执行完成时创建对应 `.done` 标记（如 `investment-team-MSFT-20260815.done`）
   - 每只持仓报告写完即存 `reports/{公司名}/`，不依赖会话记忆
4. **阶段门禁（关键——ZCode下hook不触发的替代方案）**：每完成一个阶段，运行 `bash scripts/workflow-gate-hook.sh`，把JSON输出原文贴入阶段报告。输出含 `decision:block` = 该阶段未达标，禁止进入下一阶段，按 reason 补齐。在 hook 生效的环境（Claude Code）它是 Stop 时的双重保险。
5. 环境适配：Windows下用 `python`（无python3）；持仓研究用 Agent 工具**同一条消息多个调用并发**（subagent_type: general-purpose）；搜索回退链：WebSearch → mcp__kepler__web_search → mcp__web_reader__webReader → **Bash curl直连**（`.claude/.workflow/SEARCH-TOOLKIT.md` 有全套已验证命令：websearch.sh=Brave通用搜索、gnews.sh=Google News、curl Yahoo API=行情/榜单/新闻）。注意：内置WebSearch与webReader MCP是**同一上游配额**（2026-08-17实证同时429），前两层同时失效时直接跳到curl层，勿浪费重试（配额用尽禁止放弃、禁止以工具不可用为由跳过步骤、禁止用训练知识冒充联网结果）。
6. **搜索正文获取铁律（v5.4新增，不可违反）**：使用open-websearch MCP或任何搜索工具时，搜索结果（标题+snippet）**不足以作为分析依据**。必须对关键结果调用 `fetchWebContent`（open-websearch MCP）或 `WebFetch`（内置）获取正文全文，然后才能用作数据点。规则：
   - 每个用于估值/增速/合同等关键数据点的搜索结果，必须fetch正文确认具体数字
   - 仅用于“发现候选ticker”的搜索可以只看标题（发现阶段）
   - 用于“验证/分析/决策”的搜索必须获取正文（验证阶段）
   - 禁止仅凭snippet中的片段数字就写入报告（snippet可能截断/过时/误读）

## 目的与原则

**真实目的**：捕捉1-6个月内可兑现的大额收益，不是长期复利配置。全部框架为之服务：
- **机会优先**：行业分布是风险预算和搜索罗盘，不是收益目标——强催化剂与分布区间冲突时，优先催化剂，用硬上限+止损管理风险
- **生存前提**：流程不承诺盈利；目标是提高每笔胜率与赔率、把单笔亏损锁在可承受范围（单笔风险预算：仓位×止损距离≤总资产1%），靠重复下注积累收益
- **人是唯一执行者**：AI只出信号和证据；写 portfolio-latest.md 前必须逐项向用户确认成交

### 信息推理原则（v5.0新增——最高优先级）

**禁止将任何催化剂标记为"二元事件"然后等待。** 我们的edge不是赌博，是通过信息搜集+深度推理看到别人看不到的底层逻辑：

**每个催化剂/事件前，必须执行“信息推理链”**：
1. **全网搜集**（≥10次搜索，用open-websearch MCP）：
   - 公司近30天产品发布/招聘动向/合作伙伴公告
   - 竞品同期数据反推（如用竞品增速推算目标公司增速）
   - 供应商/客户链信号（如TSM出货数据反推下游需求）
   - 期权隐含波动率/put-call ratio（市场定价了多少波动）
   - 内部人交易/机构持仓变动（13F/insider buy/sell）
   - 管理层近30天公开发言措辞变化（乐观/保守/回避）
   - 行业分析师最新修正（上调/下调目标价）
2. **交叉验证推理**：将多源信息交叉印证，得出概率估计（如"云收入>35%的概率=72%"）
3. **赔率计算**：概率×上行 vs (1-概率)×下行 = 风险回报比
4. **行动映射**：
   - 赔率>3:1 → 重仓（事件前建仓/加仓）
   - 赔率 1.5-3:1 → 标准仓位
   - 赔率<1.5:1 → 不赌（减仓或观望）

**核心信念**：市场定价的是“共识概率”，我们的超额收益来自“比共识更准确的概率估计”。信息搜集越充分、推理链越完整，概率估计越准确，下注越有底气。"别人恐惧时贪婪"不是口号，是信息优势的自然结果。

**执行证据**：每只持仓的催化剂分析必须展示"搜集了哪些信息→推理链→概率估计→赔率→行动"，禁止只写"等待财报"或"二元事件"。

## 三条铁律（最高优先级，不可变通）

### 零复用铁律
- "本次"= 这次执行此skill的过程，不是"当前会话"
- 不得以"本会话早些时候已执行/已研究/已搜索"为由跳过任何步骤
- 不得引用 reports/ 下的旧报告、旧评分、旧结论作为本次结论依据
- 哪怕1小时前刚研究过同一只股票，本次执行也必须重新搜索获取最新数据
- 每一步都必须展示真实执行证据（搜索词、Agent ID、工具输出），不可只说"已完成"
- **执行原则：无法展示这一步在本次执行中真实发生的证据 = 没做**

### Skill执行铁律
- 直接用WebSearch分析股票=未执行，必须通过Skill/Agent工具调用
- 持仓分析必须启动 /investment-team（4个并行Agent），不得用WebSearch替代
- **每只持仓=4个独立Agent×1只股票**：禁止合并多只股票到同一批Agent，禁止将4个视角压缩到1个Agent（详见第二步“四大师并行执行规范”）
- 候选标的必须过 /investment-checklist + /investment-team 双重验证，缺一不可
- /industry-funnel 和 /bottleneck-hunter 必须正式调用skill，不得用“已扫描数据”替代
- 判断标准：✅“调用/investment-checklist BR，Agent ID: xxx，六关全过”=已执行；❌“我用WebSearch搜了BR财务数据”=未执行；❌“WebSearch配额尽所以跳过”=未执行（必须换MCP工具）；❌“1个Agent分析3只股票”=未执行；❌“1个Agent四维度合并分析”=未执行

### 推荐准入铁律
- 最终方案中推荐"买入/新建/换仓"的新标的，必须先通过 /investment-checklist 验证
- 对比研究≠checklist验证（对比是筛选，准入是门槛，两步不可合并）
- 加仓已有持仓不需要新checklist，但换仓/新建必须跑
- **PDD教训（2026-08-13）**：Deep Research对比BABA vs PDD后直接推荐换仓，未跑checklist；用户追问后补跑发现PDD是灰色地带（3/6，净利连续5季下降+Temu模式被de minimis规则拆解），修正为保留BABA。根因：对比研究的结论不能跳过准入验证

---

## 执行流程

### 第零步：异动快速反应协议 + 市场温度判定（最先执行）
- **首先**搜索 "biggest stock movers today" / "stocks surge earnings beat today" 检查当日重大异动
- **延时交易异动（必须）**：用 Yahoo v8 chart API（`includePrePost=true`）获取全部持仓的夜盘/盘前最后成交价，与收盘价对比；延时变动>±1%的标的立即标注为异动信号，纳入优先评估
- 用户关注过的标的（memory有记录）异动>10% → 立即纳入候选并评估
- 持仓的供应商/客户/合作伙伴异动>15% → 评估对持仓的影响
- **市场温度判定（v5.0新增，必须）**：按 `config/portfolio-targets.md` "现金动态规则"执行5个信号搜索（NDX距高点/VIX/市场广度/Fear&Greed/IPO情绪），确认当前温度档位（🔴🟠🟡🟢🔵），输出到报告头部并决定现金下限。禁止凭训练知识判断市场温度，必须实时搜索。
- **AI子行业温度判定（v5.3新增，必须）**：按 `config/portfolio-targets.md` "AI子行业温度动态规则"执行双层判定：
  - 第一层：AI整体水位（搜索"AI capex guidance 2026 hyperscaler"、"AI revenue growth quarterly"、"AI infrastructure bottleneck shortage"）→ 确认AI总暴露区间
  - 第二层：AI硬件水位（搜索"CoWoS HBM supply shortage"、"TSM monthly revenue"、"IPP PPA data center contract"）+ AI软件水位（搜索"AI ARR SaaS growth"、"AI software valuation PE"、"Copilot adoption enterprise"）+ AI平台水位（搜索"META GOOGL FCF capex"、"hyperscaler buyback dilution"）
  - 输出：AI整体水位 + 三子类水位 + 当前应配比例，写入报告头部
- **加密市场温度判定（v5.4新增，必须）**：按 `config/portfolio-targets.md` "加密市场温度动态规则"执行：
  - 搜索 "bitcoin price all time high distance"、"crypto fear greed index"、"bitcoin ETF flows"、"crypto regulation stablecoin" → 确认加密水位（🟢积累/🟡复苏/🟠狂热/🔴崩盘）
  - 输出：加密水位 + 当前应配比例 + 内部路径选择（修复为主/爆发为主），写入报告头部

### 第一步：核实当前持仓（必须逐项确认）
- 必须先 Read `reports/portfolio-latest.md`；若用户提供了持仓清单，以用户数据为准
- 写入任何文件前，必须逐项向用户确认：股数、成本价、现金余额；绝不基于假设写持仓文件
- **提取“待执行/观察/计划买入”项**：持仓文件中所有标记为“待执行”“计划”“观察”但尚未执行的标的，必须在第三步作为候选来源A纳入（不可遗漏）
- **延时价格口径**：组合市值与分布计算必须使用最新可得价格（优先级：盘前 > 夜盘 > 收盘价）；报告持仓表必须同时展示「收盘价」「夜盘/盘前价」「延时vs收盘」三列；延时价格获取方法：`https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?interval=1m&range=1d&includePrePost=true`，取 timestamp+close 序列最后一个有效成交，判断时段（≥16:00 ET=夜盘，<9:30 ET=盘前）

## 第二步：持仓股分析（全部从零研究，禁止复用）
- 每只持仓股都必须在本次执行中重新启动 /investment-team（4并行Agent）实时研究（lite模式降级为：行情+催化剂快查+分布体检）
- 必须展示Agent ID或搜索证据，证明是本次执行新建的研究
- 分析重点（1-6个月视角）：FCF是否为正/增速/ROE；重大催化剂（财报/新品/监管）；下行风险（悲观场景-X%）；仓位是否合理（<3%=机会成本，>25%=集中风险）
- 输出：每只一句话判断 + 明确操作信号（清仓/买入/持有/加仓/减仓，单一动词+触发条件，禁止模糊建议）

#### 四大师并行执行规范（铁律·不可绕过·2026-08-18教训新增）

**执行方式（唯一合法方式）**：
1. **一次只分析一只股票**——按仓位从大到小逐只执行，完成一只再开始下一只
2. **每只股票必须启动4个独立GeneralPurpose subagent**（在同一条消息中并行调用4次Agent工具），分别对应：
   - Agent 1：商业分析师（段永平视角）——商业模式、护城河、定价权
   - Agent 2：财务分析师（巴菲特视角）——财务数据、估值、FCF、安全边际
   - Agent 3：行业研究员（芒格视角）——行业格局、竞争态势、逆向思维
   - Agent 4：风险评估师（李录视角）——风险矩阵、管理层、催化剂、仓位合理性
3. **4个Agent收回后由team-lead（主Agent）综合**，输出四维评分表+一句话判断+操作信号
4. 每只完成后创建 `.done` 标记：`investment-team-{TICKER}-{YYYYMMDD}.done`

**绝对禁止（违规=该股票分析无效，必须重做）**：
- ❌ 将多只股票合并到1个Agent中分析（如"分析ADBE+AVGO+BRK.B"）
- ❌ 将4个视角合并到1个Agent中（如"同时完成四个维度的分析"）
- ❌ 用WebSearch直接分析替代4-Agent并行研究
- ❌ 以"配额不足""效率考虑"为由减少Agent数量
- ❌ 以"本会话已分析过"为由跳过任何一只

**违规判定标准**：
- ✅合法："启动4个Agent分析BABA，Agent ID: xxx/yyy/zzz/www"=已执行
- ❌违规："启动1个Agent分析BABA+MSFT+ADBE"=未执行，必须重做
- ❌违规："启动1个Agent同时完成四维度分析BABA"=未执行，必须重做

**教训存档（2026-08-18）**：META正确使用了4个独立subagent（段永平/巴菲特/芒格/李录各自独立搜索、独立验证、独立结论），暴露了"仓位超风险预算1.34%>1%"这一关键风险；后续BABA/MSFT/ADBE退化为单agent合并分析后，四维张力消失，风险暴露能力严重降级。根因：独立执行产生的视角碰撞是暴露结构性风险的唯一途径，合并执行=自欺欺人。

### 第二步半：行业分布评估（必须执行，不可跳过）
- 按 `config/portfolio-targets.md` 的分类规则归类每只持仓，计算当前分布，输出对比表（目标/当前/偏差/✅⚠️🔴状态）
- **分布表数字生成规则（防错·必读）**：所有百分比必须由脚本计算生成并打印（python/financial_rigor.py），禁止手写或心算；脚本必须输出合计校验行（八个互斥主类别精确合计=100.0%，校验不过禁止写报告）；小计行（AI总暴露）不参与求和，必须视觉区分；用户质疑任何数字时先跑工具再回答
- 按约束分级评估：硬约束（AI总暴露/非AI对冲/现金/单一国家敲口/加密上限）偏差>10%=🔴必须修正；AI三子类别（硬件/软件/平台）只⚠️提示（软约束）
- **集中度检查（v5.4新增）**：每个类别是否超过top 2？超过=标注🔴并在第五步给出减仓建议
- 此评估结果直接影响第三步候选筛选方向（缺口反向映射=来源E）

### 第三步：新候选股筛选（全量模式必做；lite模式跳过）

**候选累积追踪**：维护 `.claude/.workflow/candidates.csv`（ticker,company,gics_sector,source），下限300只、理想350只唯一候选；25个GICS组每组≥4只，7维每维≥5只；候选不足时gate脚本会拦截。

*9路候选来源A-I并行**（缺一不可，详细执行方式见 `config/search-matrix.md` 第五节）：A=持仓文件待执行项、B=全市场多维搜索（GICS 25组×2视角+7维）、C=/industry-funnel、D=/bottleneck-hunter、E=分布缺口反向映射、F=用户历史关注（必选）、G=持仓生态链反向搜索（必选）、**H=爆发股猎手（必选，找"增速被低估"的标的）**、**I=估值修复猎手（必选，找"风险被高估"的标的）**。

#### 来源H：爆发股猎手（2026-08-18新增，全量模式必做）

**目的**：寻找"NBIS@$70""CRCL@$50"级别的早期爆发标的——收入三位数增长、盈利拐点刚至、赛道唯一纯正、华尔街尚未充分覆盖、1-6个月有50-300%上行空间。

*爆发股DNA画像（v5.1修正：5+1概率门，取代旧版6条AND门）**：

> **设计修正理由（2026-08-18教训）**：旧版6条全满足在实证中近乎空转——20+次搜索仅APLD 1只通过。NBIS/CRDO爆发后立刻超标（市值>$50B+覆盖充分），说明旧规则描述的是"爆发前的完美状态"，但现实中无法在爆发前确认爆发。真正的edge是找到"5条满足+第6条正在改善"的标的，在赔率>3:1时下注。

**硬条件（5条，必须全满足）**：
1. **收入增速≥100% YoY**（最近一季，非预测）
2. **盈利拐点**：EBITDA/净利润刚转正或即将转正（≤2个季度）
3. **市值$3B-$80B**（太小=流动性风险；$50-80B为"毕业缓冲区"，见下方规则）
4. **赛道纯正**：主业收入≥70%来自单一高增长主题（AI Cloud/AI网络/HBM/光互连/机器人等）
5. **合同/积压可见性**：backlog≥年收入1.5x 或 大额合同公告（>$1B）

**软条件（1条，灰色可入池但须标注）**：
6. **覆盖错位**（取代旧版"覆盖不足"）：满足以下**任意一条**即算通过：
   - (a) 卖方分析师≤20人覆盖（放宽旧版15人上限）
   - (b) 共识目标价 vs 按当前增速外推的12个月合理估值，存在**>30%低估**（即华尔街还没追上增速）
   - (c) 最近3个月有≥2次目标价上调但股价仍未反映全部增速（"正在被发现"阶段）
   - (d) 机构持股<40%（尚未被基金充分配置）
   - **灰色判定**：若(a)-(d)均不满足但差距<20%（如分析师22人、低估幅度25%），标注"灰色-覆盖错位"仍可入池，但仓位减半（≤4%而非8%）

**扫描工具（强制）**：使用 open-websearch MCP（`CallMcpTool server_name="open-websearch" tool_name="search"`）执行全网覆盖式搜索，默认duckduckgo引擎；每轮搜索≥10组不同关键词，每组返回结果逐条审查。

**必搜关键词矩阵（≥20次搜索，分4轮）**：

| 轮次 | 搜索词（每组独立搜索） | 目的 |
|------|----------------------|------|
| 第1轮·增速发现 | "revenue growth over 100% stocks 2026 earnings"、"triple digit revenue growth AI stocks quarterly"、"fastest growing companies revenue 2026 stock"、"500% revenue growth stock 2026"、"revenue doubled year over year stocks 2026" | 按增速横切全市场 |
| 第2轮·拐点发现 | "EBITDA positive first time 2026 stock AI"、"profitability inflection point stocks 2026"、"breakeven quarter AI company stock 2026"、"backlog billion dollars AI stocks 2026"、"contract wins billion AI infrastructure 2026" | 按盈利拐点+积压筛选 |
| 第3轮·赛道纯正 | "pure play AI cloud stock 2026"、"AI networking only company stock"、"HBM memory pure play stocks"、"optical interconnect AI pure play"、"humanoid robot pure play stock 2026"、"AI inference chip pure play" | 按赛道纯正度筛选 |
| 第4轮·被忽视发现 | "undercovered AI stocks institutional ownership low"、"small cap AI stocks analyst coverage under 10"、"recent IPO AI stocks 2025 2026 revenue growth"、"hidden AI stocks not owned by hedge funds"、"AI stocks Wall Street hasn't discovered yet 2026" | 按覆盖不足/被忽视筛选 |

**筛选流程**：
1. 4轮搜索汇总所有出现的ticker（去重）
2. 对每只候选用Yahoo v8 API获取现价/市值，过滤市值不在$3-80B区间的
3. 对剩余候选逐一验证DNA（搜索"{ticker} revenue growth Q2 2026"确认增速）
4. 5条硬条件全满足 + 软条件通过/灰色 → 写入candidates.csv（source列标注"H-爆发股"或"H-爆发股(灰色)"）
5. 从H来源候选中选Top 3-5 → 进入双重验证（/investment-checklist + /investment-team）

**市值毕业缓冲规则（v5.1新增）**：
- 市值$50-80B = "毕业缓冲区"：已持仓可继续持有（不强制移出），但**新建仓受限**（须用户额外确认"$50B+仍要买入？"）
- 市值>$80B = 强制毕业：移出爆发仓，按主规则重新归类（通常归AI核心）
- 设计理由：NBIS从$15B→$50B仅用2个月，旧规则在爆发主升浪中强制移出=错过最大收益段

**输出要求**：报告末尾输出"爆发股猎手扫描矩阵"——4轮×搜索词×结果数×入池数；标注哪些ticker通过了6条DNA、哪些被哪条拦截。

**绝对禁止**：以"已搜过类似词"为由跳过H轮搜索；只看前2条搜索结果就声称扫描完成；用训练知识列举"已知爆发股"替代实时搜索（NBIS/CRWV/CRDO等已知标的仍须实时验证最新数据）。

#### 来源I：估值修复猎手（v5.2新增，全量模式必做）

**目的**：寻找"好公司被恐惧打折"的标的——生意本身没问题，但市场因可证伪的叙事而给了极端低估值，1-6个月有30-50%修复空间。

**估值修复DNA（4条全满足）**：
1. **好生意确认**：毛利率>40% + 营业利润率>25% + 正FCF（证明不是"便宜该死"）
2. **估值极端**：当前Fwd PE < 自身5年中位数的60%（或EV/Rev < 历史中位50%）
3. **恐惧可归因**：下跌原因是可证伪的叙事（AI颠覆/CEO真空/一次性事件），而非结构性衰退
4. **催化剂可见**：未来1-3个月有明确事件可验证恐惧是否过度（财报/产品发布/管理层更替落地）

**搜索词库**：见 `config/search-matrix.md` 来源I两组（AI修复≥5组 + 加密修复≥15组），合计≥20次搜索。

**筛选流程**：
1. 搜索汇总所有出现的ticker（去重）
2. 对每只候选验证DNA 4条（必须fetch正文确认具体数字，禁止仅凭snippet）
3. 4条全满足 → 写入candidates.csv（source列标注"I-估值修复"或"I-加密修复"）
4. 从I来源候选中选Top 3-5 → 进入双重验证（/investment-checklist + /investment-team）

**与来源H的关系**：H找"增速被低估"（爆发），I找"风险被高估"（修复）。两者互补，覆盖不同的市场错误定价类型。

**输出要求**：报告末尾输出"估值修复猎手扫描矩阵"——搜索词×结果数×入池数；标注哪些ticker通过了4条DNA、哪些被哪条拦截。

**搜索执行**：按 `config/search-matrix.md` 的词库——GICS 25组全部×2视角（≥50次）、AI 17赛道全部×≥2视角（≥34次）、非AI 14主题选≥8（主题13/14优先）、7维各≥1次（D6/D7必做）、**来源H爆发股猎手≥20次（open-websearch MCP）**、**来源I估值修复猎手≥20次（AI修复≥5+加密修复≥15）**；合计≥120次；AI候选≤65%；每次搜索后追加search-log.txt。

**筛选流程**（不得跳过、不得引用旧结果）：
1. 并行执行9路来源（A-I），汇总去重、按分布缺口优先级排序
2. 从汇总池提取Top 10-15候选
3. 对Top候选逐一双重验证：/investment-checklist（六关准入）+ /investment-team（四大师评估）——两者都通过才能进入终选
4. 冒泡排序找Top 2（见第四步）

**绝对禁止**：以"之前已执行过漏斗/瓶颈扫描"为由跳过；只搜2-3个行业就声称全市场扫描完成；跳过来源A/F/G/H；所有搜索词全部带"undervalued"；来源H用内置WebSearch替代open-websearch MCP（必须走MCP以确保覆盖度）。

### 第四步：冒泡排序终选
对所有候选两两比较：护城河★、估值fPE、下行风险（悲观-X%小者优先）、催化剂（3个月内有财报/新品者优先）、行业分布契合度（能修正硬约束偏差者优先）。
**所有评分必须统一来自/investment-team框架并标注"基于/investment-team"**；不同框架的分数不可混用。输出Top 2并说明胜出理由。

### 第五步：输出最终方案
生成 `reports/portfolio-action-{YYYYMMDD}.md`，包含：
1. **5.1 行业分布对比**：设计假设核验（✅/❌，≥2失效触发设计复审）+ 调仓前/后/目标分布对比表（脚本生成+合计校验行）+ 非AI细分表；调仓后仍有>10%硬约束偏差或触及硬上限必须说明原因与修正计划
2. **5.2 执行清单**：每只股票的明确操作（动词+触发条件）+ 行业类别 + 一句话理由；评分标注框架来源
3. **5.3 执行顺序**：先清仓X→回收$Y，再买入Z→投入$W，净效果M只→N只（≤10只）；**集中度检查：每类≤top2，超过则先砍最弱**
4. **5.4 预期回报**（1-6个月）：标的/仓位/乐观/中性/悲观/期望（financial_rigor.py three-scenario生成）
5. **5.5 风险管理**：每笔止损价（-12%）+移动止损（浮盈>15%上移至成本+5%或20日线）+催化剂兑现退出规则+单笔风险预算校验（仓位×止损距离≤1%）+催化剂日历+执行检查清单+AI泡沫破裂应急规则（见config风险参数）
6. **推荐验证矩阵**（最终报告必须包含，任何一行❌=该标的不得进执行清单）：

| 推荐标的 | 推荐类型 | checklist结果 | investment-team评分 | .done标记文件 | 可推荐？ |
|---------|---------|-------------|-------------------|--------------|---------|

7. **推荐清单文件**：最终方案输出前写 `.claude/.workflow/recommended-buys.txt`（每行一个ticker，只列新建/换仓；无新买入写 `# no new buys`；每个ticker必须有对应 `investment-checklist-{TICKER}-*.done`）

### 第六步：更新portfolio-latest.md
- 执行操作前：向用户展示操作清单（含行业分布对比），**等待确认**
- 用户执行后：逐项确认实际成交（股数/价格/现金）再写文件
- 绝不在用户确认前覆盖portfolio-latest.md

## 阶段门禁点（每点必跑 gate 脚本并贴输出）

| 阶段完成点 | 运行 | 必须通过 |
|-----------|------|---------|
| 第二步后（lite模式在此结束） | bash scripts/workflow-gate-hook.sh | investment-team ≥1个.done |
| 第三步后 | bash scripts/workflow-gate-hook.sh | +checklist/funnel/bottleneck .done、candidates≥300、搜索≥110（含H≥20、I≥20）、used标记存在、mcp-open-websearch.used标记存在 |
| 第五步后 | bash scripts/workflow-gate-hook.sh | +recommended-buys全覆盖 |

## 质量标准

**必须做到**：每只股票明确操作信号；FCF分类处理（长期持仓FCF为负=清仓红线；短期"基建期成长股"单标的≤8%、合计≤12%、强制止损）；买入前双重验证；评分标注框架来源；关键数据用financial_rigor.py验证+双源交叉；写文件前逐项确认实际持仓；全部研究实时搜索；报告输出候选发现来源矩阵；来源F/G/H/I执行证据；搜索词多样性证据（≥10组不含"undervalued"）；**来源H爆发股猎手必须输出4轮扫描矩阵+DNA验证表**；**来源I估值修复猎手必须输出4条DNA验证表（好生意/估值极端/恐惧归因/催化剂）**。

**禁止事项**：模糊建议；未核实持仓就给建议；复用旧评分/旧研究；以"本会话已执行"为由跳过步骤；批量分析多只股票在1个skill调用中；只搜与缺口匹配的行业就声称全市场扫描；忽略持仓文件待执行项；混用不同框架分数不标注；仅用checklist就决定买入；跳过行业分布评估或忽略硬约束>10%偏差；来源F走过场；忽略持仓生态链。

## 输出语言
全部用中文。
