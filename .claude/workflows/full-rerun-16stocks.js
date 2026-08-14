export const meta = {
  name: 'full-rerun-16stocks-4skills',
  description: '16只股票从零重跑 investment-team/checklist/bottleneck-hunter/funnel，综合持仓给出逐股操作建议',
  phases: [
    { title: '公司研究', detail: '16个Agent各执行investment-team+checklist' },
    { title: '瓶颈扫描', detail: '6个行业瓶颈猎手' },
    { title: '行业漏斗', detail: '7个行业漏斗筛选' },
    { title: '综合研判', detail: '交叉验证+持仓操作建议' },
  ],
}

const PRE = [
  '## 全局要求（最高优先级）',
  '- 今天是2026-08-08（北京时间）。这是完全从零的重跑：reports/ 下已有报告是旧结论，一律忽略、禁止抄用旧数据，一切以本次联网搜索为准。',
  '- 用 WebSearch/WebFetch 获取实时数据：当前股价、市值、最新季度财报、近30天重大新闻。工具不可用时先用 ToolSearch 加载。若联网失败，必须在报告中醒目标注「联网失败、置信度降级」，严禁用训练知识伪装成联网结果。',
  '- 美股财务数据至少两个独立来源交叉验证（macrotrends + stockanalysis 为基础，辅以 Yahoo Finance/公司财报原文），两源误差>1%必须标注。货币单位明确为美元。',
  '- 市值=股价×总股本必须用 Bash 调 python tools/financial_rigor.py verify-market-cap 校验；PE/三情景估值用 verify-valuation / three-scenario 子命令精确计算，禁止心算。工具报错时手写公式计算并注明过程。',
  '- 严格遵守 CLAUDE.md 客观性原则：不预设看多看空，先数据后结论，每个核心判断附反面论据，数据标来源，估计值标「估计」，不用「我认为/显然」。',
  '- 报告全部用中文，风格直接犀利，评分用★1-5（无半星），穿插巴菲特/芒格/段永平/李录语录点评。',
  '- 【文件复用规则】写报告前先 Glob 检查是否已有同主题报告文件：有→直接覆盖更新原文件（保留原文件名，正文顶部更新"最后更新：2026-08-08"），不要另建带新日期的重复文件；没有→才新建。旧报告内容是旧结论，覆盖即可，不需要保留旧内容。',
  '- 【准出审计必须执行】每份报告写完后执行数据抽检：Bash 运行 python tools/report_audit.py extract --report <报告路径>（Windows 下 python3 不可用就用 python）→ 对抽检清单每项从可靠信源取数填 fetched_value（可复用本次已交叉验证的数据）→ python tools/report_audit.py verdict --results \'[...]\' --report <报告文件名>。注意三个已知坑：(1) verdict 的 results JSON 每项必须带 reported_value，否则偏差全报 inf% 假警告；(2) 括号负数如 (2.7) 会被工具误读为正数，此类偏差在 note 说明即可，不算数据错误；(3) 口径不一致的异类指标不要当 source2 硬比对，移到 note。【准出】→通过；【打回】→修正报告后重审，最多2轮，仍不通过就在报告中如实注明审计局限。',
  '- 你的最终输出是结构化返回值（StructuredOutput），不是给人看的对话，不写客套话。',
].join('\n')

const STOCKS = [
  { t: 'VRT',   n: 'Vertiv',             s: 'AI数据中心电力与散热',    hold: false },
  { t: 'MRVL',  n: 'Marvell',            s: '半导体-定制ASIC',         hold: false },
  { t: 'MU',    n: 'Micron美光',         s: '半导体-存储/HBM',         hold: false },
  { t: 'ADBE',  n: 'Adobe',              s: '企业软件-创意/营销',      hold: true },
  { t: 'LRCX',  n: 'Lam Research',       s: '半导体设备-刻蚀沉积',     hold: false },
  { t: 'CRWD',  n: 'CrowdStrike',        s: '网络安全',                hold: false },
  { t: 'INTU',  n: 'Intuit',             s: '企业软件-财税',           hold: true },
  { t: 'CRM',   n: 'Salesforce',         s: '企业软件-CRM/Agentforce', hold: false },
  { t: 'MSFT',  n: 'Microsoft',          s: '企业软件-云/AI平台',      hold: true },
  { t: 'BRK.B', n: 'Berkshire Hathaway', s: '综合控股/保险',           hold: true },
  { t: 'BABA',  n: '阿里巴巴(ADR)',       s: '中国互联网平台',          hold: true },
  { t: 'QCOM',  n: 'Qualcomm',           s: '半导体-移动/边缘AI',      hold: true },
  { t: 'TSM',   n: '台积电(ADR)',         s: '半导体-晶圆代工',         hold: true },
  { t: 'TLN',   n: 'Talen Energy',       s: '电力-独立发电',           hold: true },
  { t: 'RARE',  n: 'Ultragenyx',         s: '生物科技-罕见病',         hold: true },
  { t: 'CRCL',  n: 'Circle',             s: '稳定币/数字资产',         hold: true },
]

const COMPANY_SCHEMA = {
  type: 'object',
  required: ['ticker','price','data_quality','team_score','dimension_scores','checklist_result','action','buy_range','bull_case','bear_case','key_risks','confidence','report_files'],
  properties: {
    ticker: { type: 'string' },
    price: { type: 'string', description: '现价（美元）+数据时间' },
    market_cap: { type: 'string' },
    data_quality: { type: 'string', enum: ['A','B','C'] },
    team_score: { type: 'string', description: '四大师综合评分，如 3.5/5' },
    dimension_scores: { type: 'string', description: '段永平★/巴菲特★/芒格★/李录★ 各维度评分一句话' },
    checklist_result: { type: 'string', description: '通过X/6关 / 未通过（触发红线） / 灰色地带' },
    checklist_stars: { type: 'string', description: '能力圈/好生意/护城河/管理层/安全边际各几星' },
    forward_pe: { type: 'string' },
    fcf_yield: { type: 'string' },
    bull_case: { type: 'string', description: '看多核心逻辑3-5条浓缩' },
    bear_case: { type: 'string', description: '看空核心逻辑3-5条浓缩' },
    key_risks: { type: 'string' },
    buy_range: { type: 'string', description: '合理买入区间' },
    target_12m: { type: 'string', description: '12个月目标价/区间（中性）' },
    action: { type: 'string', description: '买入/加仓/持有/减仓/卖出/等回调/回避 之一' },
    confidence: { type: 'string', enum: ['high','medium','low'] },
    report_files: { type: 'array', items: { type: 'string' } },
    audit_status: { type: 'string', description: '准出审计结果：准出/打回已修正/审计局限说明' },
  },
}

const SECTOR_SCHEMA = {
  type: 'object',
  required: ['sector','bottleneck_map','focus_ticker_assessment','new_candidates','report_file'],
  properties: {
    sector: { type: 'string' },
    bottleneck_map: { type: 'string', description: 'S/A/B级瓶颈清单浓缩，每条一句话' },
    focus_ticker_assessment: { type: 'string', description: '每个重点股票一条：瓶颈层级/评级+估值判断' },
    new_candidates: { type: 'string', description: '新发现的Layer2-3标的+信号强度★；无则写无' },
    valuation_flags: { type: 'string', description: '估值红灯/黄灯的标的及原因' },
    report_file: { type: 'string' },
    audit_status: { type: 'string', description: '准出审计结果' },
  },
}

const FUNNEL_SCHEMA = {
  type: 'object',
  required: ['industry','universe_count','layers_summary','top3','focus_ticker_verdicts','report_file'],
  properties: {
    industry: { type: 'string' },
    universe_count: { type: 'number' },
    layers_summary: { type: 'string', description: '各层数量与关键淘汰理由浓缩' },
    top3: { type: 'string', description: '终选3家：代码+推荐度★+买入区间+仓位类型' },
    focus_ticker_verdicts: { type: 'string', description: '每个重点股票一条：终选/观察/淘汰+理由' },
    report_file: { type: 'string' },
    audit_status: { type: 'string', description: '准出审计结果' },
  },
}

function companyPrompt(s) {
  const role = s.hold ? '用户已持仓该股（分析保持客观，不因持仓预设立场）' : '该股在用户观察名单中、未持仓'
  return PRE + '\n\n' + [
    `## 任务：对 ${s.n}（${s.t}）从零完整执行两个skill。所属板块：${s.sector}。${role}。`,
    '1. 先 Read skills/investment-team.md、skills/investment-checklist.md、skills/financial-data.md 了解框架要求。',
    `2. 【investment-team】按四大师视角研究：段永平（商业模式/护城河/好生意标准）、巴菲特（财务/估值/安全边际，必做financial_rigor验算）、芒格（行业格局/竞争/失败模式）、李录（风险/管理层/文明级趋势）。合并写成一份报告：先 Glob reports/${s.t}/ 查找已有的 investment-team/四大师/研究类报告，有→覆盖更新原文件；没有→新建 reports/${s.t}/${s.t}-investment-team-20260808.md。必含：信息丰富度评级(A/B/C)、四维评分表+综合评分X/5、核心数据速览（近2年对比）、Bull vs Bear各5条、三情景估值（工具输出）、分层操作建议+价格区间。`,
    `3. 【investment-checklist】执行六关（能力圈/好生意/护城河/管理层/安全边际/仓位纪律）+镜子测试+快速否决清单：先 Glob reports/${s.t}/ 查找已有 checklist 报告，有→覆盖更新原文件；没有→新建 reports/${s.t}/${s.t}-checklist-20260808.md。结论明确：通过X/6关 / 未通过（哪条红线） / 灰色地带。`,
    '4. 两个报告各自独立完整，但可共享你本次搜集的数据。所有价格/财务必须是本次搜索的最新数据。',
    '5. 完成后返回结构化结果。action 字段给出你基于数据得出的明确操作倾向（买入/加仓/持有/减仓/卖出/等回调/回避之一）。',
  ].join('\n')
}

const BOTTLENECKS = [
  { name: '半导体与AI算力供应链', focus: 'TSM(代工)、MU(存储/HBM)、LRCX(设备)、MRVL(定制ASIC)、QCOM(边缘芯片)', file: '半导体产业链', trend: 'AI基础设施建设+半导体再工业化' },
  { name: 'AI数据中心电力与散热', focus: 'VRT(电源/热管理/液冷)、TLN(独立核电+天然气发电)', file: 'AI数据中心电力', trend: 'AI基础设施建设-电力层' },
  { name: '企业软件与AI Agent', focus: 'MSFT、ADBE、INTU、CRM', file: '企业软件AI-Agent', trend: '企业AI软件渗透' },
  { name: '网络安全', focus: 'CRWD(端点/XDR)', file: '网络安全', trend: 'AI驱动的攻防对抗升级' },
  { name: '生物医药与创新药', focus: 'RARE(罕见病基因疗法)', file: '生物医药', trend: '罕见病疗法/基因疗法产业化' },
  { name: '数字资产与中国互联网', focus: 'CRCL(稳定币/USDC)、BABA(中国互联网平台)', file: '数字资产与中国互联网', trend: '稳定币支付基础设施+中国互联网估值重构' },
]

function bnPrompt(b) {
  return PRE + '\n\n' + [
    `## 任务：对「${b.name}」从零执行 bottleneck-hunter 扫描。关联趋势：${b.trend}。重点公司：${b.focus}。`,
    '1. 先 Read skills/bottleneck-hunter.md 了解框架。',
    '2. 供应链物理拆解（Layer0-4），按6条标准识别S/A/B级瓶颈，重点扫描Layer2-3（alpha集中区），不停留在龙头概念层。',
    '3. 对每个重点公司评估：所处瓶颈层级、瓶颈受益度、估值检查（PS/PE/TAM红黄绿灯规则，瓶颈真实≠投资机会，估值是硬门槛）。',
    '4. 同时扫描该链条上新出现的Layer2-3标的（优先美股，小市值不等于好机会，必须过财务质量关），给出信号强度★1-5。',
    `5. 报告写入：先 Glob reports/bottleneck-map/ 查找是否已有「${b.file}」相关的 bottleneck 扫描报告，有→覆盖更新原文件；没有→新建 reports/bottleneck-map/${b.file}-bottleneck-20260808.md。写完执行准出审计。`,
    '6. 完成后返回结构化结果。',
  ].join('\n')
}

const FUNNELS = [
  { name: '半导体与AI算力', focus: 'TSM、MU、LRCX、MRVL、QCOM', file: '半导体AI算力' },
  { name: '企业软件', focus: 'MSFT、ADBE、INTU、CRM', file: '企业软件' },
  { name: '网络安全', focus: 'CRWD', file: '网络安全' },
  { name: '电力与能源基建', focus: 'TLN、VRT', file: '电力能源基建' },
  { name: '中国互联网(美股ADR)', focus: 'BABA', file: '中国互联网ADR' },
  { name: '生物科技与罕见病', focus: 'RARE', file: '生物科技罕见病' },
  { name: '稳定币与数字金融', focus: 'CRCL', file: '稳定币数字金融' },
]

function funnelPrompt(f) {
  return PRE + '\n\n' + [
    `## 任务：对「${f.name}」行业从零执行 industry-funnel 漏斗筛选。重点公司：${f.focus}。`,
    '1. 先 Read skills/industry-funnel.md 了解框架。用户只做美股（含ADR）：扫描池可含全球公司以了解格局，但粗筛后保留与终选仅限美股可交易标的。',
    '2. 执行四层漏斗：全市场扫描(30-60家)→5条硬指标粗筛(≤10家)→精细分析→终选3家（含推荐度★/仓位类型/买入区间/关键监测指标）。每层留淘汰记录，不许黑箱。',
    `3. 关键任务：对重点公司 ${f.focus} 逐一给出明确漏斗判定（终选/观察/淘汰+理由），不得回避。`,
    `4. 报告写入：先 Glob reports/ 查找是否已有 ${f.file}-funnel* 报告，有→覆盖更新原文件；没有→新建 reports/${f.file}-funnel-20260808.md（根目录）。写完执行准出审计。`,
    '5. 完成后返回结构化结果。',
  ].join('\n')
}

const SYNTH_SCHEMA = {
  type: 'object',
  required: ['per_stock','portfolio_actions','key_conflicts','report_file'],
  properties: {
    per_stock: {
      type: 'array',
      items: {
        type: 'object',
        required: ['ticker','status','action','position_advice','price_trigger','one_line_rationale'],
        properties: {
          ticker: { type: 'string' },
          status: { type: 'string', description: '持仓/观察名单' },
          action: { type: 'string', description: '加仓/持有/减仓/卖出/买入/等回调/回避' },
          position_advice: { type: 'string', description: '建议仓位或调整幅度' },
          price_trigger: { type: 'string', description: '触发价格/条件' },
          one_line_rationale: { type: 'string' },
        },
      },
    },
    portfolio_actions: { type: 'string', description: '组合级操作：P0/P1/P2执行顺序、资金来源、集中度问题' },
    key_conflicts: { type: 'string', description: '三类研究结果间的关键分歧及取舍判断' },
    catalysts_calendar: { type: 'string', description: '关键日期日历（北京时间）' },
    report_file: { type: 'string' },
  },
}

log('启动30个研究Agent：16公司级(team+checklist) + 6瓶颈猎手 + 7行业漏斗')

const batch = [
  ...STOCKS.map(s => () => agent(companyPrompt(s), { label: 'team+checklist:' + s.t, phase: '公司研究', schema: COMPANY_SCHEMA })),
  ...BOTTLENECKS.map(b => () => agent(bnPrompt(b), { label: '瓶颈:' + b.file, phase: '瓶颈扫描', schema: SECTOR_SCHEMA })),
  ...FUNNELS.map(f => () => agent(funnelPrompt(f), { label: '漏斗:' + f.file, phase: '行业漏斗', schema: FUNNEL_SCHEMA })),
]

const raw = await parallel(batch)
const company = raw.slice(0, STOCKS.length).filter(Boolean)
const bn = raw.slice(STOCKS.length, STOCKS.length + BOTTLENECKS.length).filter(Boolean)
const fn = raw.slice(STOCKS.length + BOTTLENECKS.length).filter(Boolean)
log(`研究完成：公司级 ${company.length}/16，瓶颈 ${bn.length}/6，漏斗 ${fn.length}/7。进入综合研判`)

phase('综合研判')

const synthPrompt = PRE + '\n\n' + [
  '## 任务：综合研判——对16只股票逐一给出明确操作建议（你是最终裁决者）',
  '',
  '### 输入1：16份公司级研究（investment-team + investment-checklist）',
  JSON.stringify(company),
  '',
  '### 输入2：6份瓶颈猎手行业扫描',
  JSON.stringify(bn),
  '',
  '### 输入3：7份行业漏斗筛选',
  JSON.stringify(fn),
  '',
  '### 输入4：用户真实持仓（2026-08-08，组合约$278K，现金$35,811≈12.9%）',
  'BABA 845股 成本$127.10 占38.5%（严重过度集中，此前已在分批减仓通道中）；MSFT 125.5股 成本$394.50 占21.9%；ADBE 90股 成本$217.27 占8.1%；BRK.B 30股 成本$508.60 占5.5%；INTU 40股 成本$319.49 占4.8%；QCOM 35股 成本$156.45 占2.0%；TSM 15股 成本$407.81 占2.2%；TLN 15股 成本$334.12 占1.8%；RARE 200股 成本$25.04 占1.8%；CRCL 20股 成本$0 占0.4%。',
  '观察名单（未持仓）：VRT、MRVL、MU、LRCX、CRWD、CRM。',
  '关键日历：8/23 RARE DTX401 PDUFA；8/25 INTU财报；8月底 CRM财报；8/28 BABA财报；9/10 ADBE财报；9/16 CRCL Arc主网；9/19 RARE UX111 PDUFA。',
  '',
  '### 要求',
  '1. 交叉验证三类结果：公司级研究与行业级（瓶颈/漏斗）结论冲突时，明确记录分歧并给出取舍判断（说明理由）；不同Agent报价冲突时以最新来源为准并标注。BRK.B无行业级skill覆盖（综合控股不适用行业瓶颈/漏斗框架），仅用公司级研究判断，报告中说明。',
  '2. 对16只股票逐一给出操作建议：持仓股=加仓/持有/减仓/卖出+触发条件+建议仓位；观察股=买入区间+建议仓位%或回避。建议必须从数据推出，不得预设。',
  '3. 组合级：BABA集中度如何处理（结合8/28财报）、现金$35,811+BABA减仓资金的部署优先级、给出P0/P1/P2执行顺序表。',
  '4. 保持客观：呈现正反两面，不确定就说不确定。',
  '5. 写完整综合报告：先 Glob reports/ 查找是否已有综合研判/综合操作建议类报告（文件名含「综合」或覆盖本次16股主题的旧报告），有→覆盖更新原文件；没有→新建 reports/16股-四skill综合操作建议-20260808.md（reports根目录）。必含：16股总评分表（四大师/checklist/瓶颈评级/漏斗排名四列）、逐股操作建议详述、关键分歧记录、P0-P2执行顺序、关键日期日历、数据声明（哪些数据是估计、需券商APP核实）。综合报告以判断为主、数据点少，准出审计可只对其中财务数据表执行一次。',
  '6. 完成后返回结构化结果。',
].join('\n')

const synth = await agent(synthPrompt, { label: '综合研判', phase: '综合研判', schema: SYNTH_SCHEMA, effort: 'high' })

return {
  summary: synth ? synth.per_stock : [],
  portfolio_actions: synth ? synth.portfolio_actions : null,
  key_conflicts: synth ? synth.key_conflicts : null,
  report_file: synth ? synth.report_file : null,
  coverage: { company: company.length, bottleneck: bn.length, funnel: fn.length },
}
