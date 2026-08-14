export const meta = {
  name: 'deep-research-0810',
  description: '全美股下半年潜力扫描：行业漏斗→瓶颈猎手→四大师+checklist→冒泡排序唯二→持仓操作建议',
  phases: [
    { title: 'Funnel', detail: '6个行业漏斗Agent扫描科技+非科技细分' },
    { title: 'Bottleneck', detail: '2个瓶颈猎手Agent扫描供应链' },
    { title: 'Deep', detail: '对涌现标的四大师+checklist深度研究' },
    { title: 'Sort', detail: '冒泡排序唯二 + 持仓操作建议' },
  ],
}

const FUNNEL_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['sector', 'tiers', 'top_candidates'],
  properties: {
    sector: { type: 'string' },
    tiers: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['name', 'level', 'prospect_3_12m', 'rationale'],
        properties: {
          name: { type: 'string', description: '细分领域名' },
          level: { type: 'string', description: '一级/二级/三级/四级细分' },
          prospect_3_12m: { type: 'string', description: '3-12个月上行潜力评级 高/中/低' },
          rationale: { type: 'string' },
        },
      },
    },
    top_candidates: {
      type: 'array',
      description: '该行业3-12个月最可能大赚的标的，6-12只，含实时价格',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['ticker', 'name', 'price', 'catalyst_3_12m', 'why_big_win', 'risk'],
        properties: {
          ticker: { type: 'string' },
          name: { type: 'string' },
          price: { type: 'string', description: '2026-08-10实时价' },
          catalyst_3_12m: { type: 'string' },
          why_big_win: { type: 'string', description: '为什么3-12个月可能大涨50%+' },
          risk: { type: 'string' },
        },
      },
    },
  },
}

const BOTTLENECK_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['bottlenecks'],
  properties: {
    bottlenecks: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['chain', 'tier_level', 'constraint', 'beneficiaries', 'timeline_3_12m'],
        properties: {
          chain: { type: 'string' },
          tier_level: { type: 'string', description: '瓶颈位于几级供应链' },
          constraint: { type: 'string' },
          beneficiaries: { type: 'string', description: '受益标的+实时价格' },
          timeline_3_12m: { type: 'string' },
        },
      },
    },
  },
}

const STOCK_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['ticker', 'research'],
  properties: {
    ticker: { type: 'string' },
    research: {
      type: 'object',
      additionalProperties: false,
      required: ['price_0810', 'business', 'four_masters', 'checklist_6_gates', 'catalysts_3_12m', 'upside', 'verdict', 'confidence'],
      properties: {
        price_0810: { type: 'string' },
        business: { type: 'string', description: '商业模式+数据，必须实时获取' },
        four_masters: { type: 'string', description: '段永平/巴菲特/芒格/李录四视角，每维0-5' },
        checklist_6_gates: { type: 'string', description: '巴菲特六关逐关验证' },
        catalysts_3_12m: { type: 'string' },
        upside: { type: 'string', description: '3-12个月上行空间%' },
        verdict: { type: 'string', enum: ['大赚候选', '值得关注', 'pass'] },
        confidence: { type: 'string', enum: ['高', '中', '低'] },
      },
    },
  },
}

const FINAL_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['top2', 'ranked_pool', 'logic'],
  properties: {
    top2: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['ticker', 'entry_price', 'position_pct', 'upside_3_12m', 'why_win'],
        properties: {
          ticker: { type: 'string' },
          entry_price: { type: 'string' },
          position_pct: { type: 'string' },
          upside_3_12m: { type: 'string' },
          why_win: { type: 'string' },
        },
      },
    },
    ranked_pool: { type: 'string', description: '冒泡排序两两比较全记录：从候选池到唯二的淘汰链' },
    logic: { type: 'string' },
  },
}

const HOLDINGS_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['actions', 'cash_plan'],
  properties: {
    actions: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['ticker', 'action', 'quantity', 'price', 'reason'],
        properties: {
          ticker: { type: 'string' },
          action: { type: 'string', enum: ['清仓', '减仓', '持有', '加仓', '新建'] },
          quantity: { type: 'string' },
          price: { type: 'string' },
          reason: { type: 'string' },
        },
      },
    },
    cash_plan: { type: 'string', description: '卖出回收资金+现金27.6K→买入分配' },
  },
}

const HOLDINGS_CTX = `用户当前持仓(2026-08-10实时收盘价, 总市值~$288K, 现金$27,611占9.6%):
BABA 645股 @$130.71 (29.3%, 超配目标12%, 8/20财报) | MSFT 125.5股 @$509.60 (22.2%) | ADBE 90股 @$269.72 (8.4%, 9/10财报)
CRM 100股 @$195.31 (6.8%, 超5%上限, 8/26财报) | BRK.B 30股 @$533.23 (5.6%) | UBER 200股 @$77.20 (5.4%, 超3%上限)
INTU 40股 @$330.02 (4.6%, 8/25财报) | QCOM 35股 @$163.82 (2.0%) | TSM 15股 @$423.66 (2.2%)
TLN 15股 @$343.70 (1.8%) | RARE 200股 @$26.37 (1.8%, 8/23 PDUFA) | CRCL 20股 @$64.81 (0.5%, 9/16 Arc主网)
投资期限: 3个月-1年。用户要求: 北京时间2026/08/10 23:59的可执行操作方案——卖什么卖多少为什么, 卖了买什么买多少为什么。`

// ===== Wave 1: 行业漏斗 + 瓶颈猎手 (并行8个) =====
phase('Funnel')
const SECTORS = [
  { key: 'ai-software', prompt: '行业漏斗扫描【AI软件/AI Agent/企业SaaS】全美股。覆盖一级细分(AI Agent/企业软件/垂直SaaS)→二级细分(客服/营销/代码/数据/AI安全)→三级细分→四级细分。要求: 必须用WebSearch获取2026年8月实时信息(8月财报季数据/最新催化), 禁止用训练知识当实时数据。3-12个月期限, 找最可能大涨50%+的标的, 给出6-12只候选含实时价格。' },
  { key: 'ai-hardware', prompt: '行业漏斗扫描【AI硬件/半导体/算力】全美股。覆盖一级细分(半导体设备/存储/互连/电力/散热/光模块)→二级细分→三级细分→四级细分。要求: 必须用WebSearch获取2026年8月实时信息(CoWoS产能/HBM供需/电力瓶颈/最新财报), 禁止用训练知识当实时数据。3-12个月期限, 找最可能大涨50%+的标的, 给出6-12只候选含实时价格。' },
  { key: 'cloud-infra', prompt: '行业漏斗扫描【云计算/数据基建/网络/安全】全美股。覆盖一级细分(超大规模云/IDC/网络设备/网络安全/数据存储)→二级细分→三级细分→四级细分。要求: 必须用WebSearch获取2026年8月实时信息, 禁止用训练知识当实时数据。3-12个月期限, 找最可能大涨50%+的标的, 给出6-12只候选含实时价格。' },
  { key: 'healthcare-biotech', prompt: '行业漏斗扫描【医疗/生物科技/器械】全美股。覆盖一级细分(生物科技/器械/诊断/远程医疗)→二级细分(FDA 2026下半年催化/GLP-1/基因治疗)→三级细分→四级细分。要求: 必须用WebSearch获取2026年8月实时信息(FDA审批日历/最新临床数据), 禁止用训练知识当实时数据。3-12个月期限, 找最可能大涨50%+的标的, 给出6-12只候选含实时价格。' },
  { key: 'consumer-fintech', prompt: '行业漏斗扫描【消费/金融科技/支付】全美股。覆盖一级细分(消费品牌/电商/支付/银行/保险)→二级细分(BNPL/跨境支付/数字银行)→三级细分→四级细分。要求: 必须用WebSearch获取2026年8月实时信息, 禁止用训练知识当实时数据。3-12个月期限, 找最可能大涨50%+的标的, 给出6-12只候选含实时价格。' },
  { key: 'industrial-energy', prompt: '行业漏斗扫描【工业/能源/电网/核能/稀土/机器人】全美股。覆盖一级细分(电力/电网设备/核能/铀/稀土/人形机器人/自动化)→二级细分→三级细分→四级细分。要求: 必须用WebSearch获取2026年8月实时信息(核能政策/稀土出口管制/电网投资), 禁止用训练知识当实时数据。3-12个月期限, 找最可能大涨50%+的标的, 给出6-12只候选含实时价格。' },
]

const funnelResults = await parallel(SECTORS.map(s => () =>
  agent(s.prompt, { label: 'funnel:' + s.key, phase: 'Funnel', schema: FUNNEL_SCHEMA })
))

// ===== Wave 2: 瓶颈猎手 (并行2个) =====
phase('Bottleneck')
const bottleneckResults = await parallel([
  () => agent('供应链瓶颈猎手: 扫描【AI算力全产业链】的瓶颈机会, 从一级(芯片/晶圆)→二级(封装/基板/存储)→三级(电力/散热/光模块)→四级(材料/设备零部件)逐级分析, 找出3-12个月内供不应求将持续加剧的瓶颈环节和受益标的。要求: 必须用WebSearch获取2026年8月实时信息(产能/价格/交期/最新财报), 禁止用训练知识当实时数据。', { label: 'bottleneck:ai', phase: 'Bottleneck', schema: BOTTLENECK_SCHEMA }),
  () => agent('供应链瓶颈猎手: 扫描【非AI领域】的供应链瓶颈: 电网设备/变压器/铜/铀/稀土/军工/医疗耗材/航运, 找出3-12个月内供需失衡的瓶颈环节和受益标的。要求: 必须用WebSearch获取2026年8月实时信息, 禁止用训练知识当实时数据。', { label: 'bottleneck:non-ai', phase: 'Bottleneck', schema: BOTTLENECK_SCHEMA }),
])

// ===== 汇总候选池 =====
const pool = new Map()
const valid = [...funnelResults, ...bottleneckResults].filter(Boolean)
for (const r of valid) {
  for (const c of (r.top_candidates || [])) {
    if (!pool.has(c.ticker)) pool.set(c.ticker, { ...c, sector: r.sector || '' })
  }
  for (const b of (r.bottlenecks || [])) {
    for (const t of (b.beneficiaries || '').match(/[A-Z]{2,5}/g) || []) {
      if (!pool.has(t)) pool.set(t, { ticker: t, catalyst_3_12m: b.constraint + '瓶颈受益', sector: b.chain })
    }
  }
}
const tickers = [...pool.keys()]
const meta_info = [...pool.values()].map(c => `${c.ticker}|${c.catalyst_3_12m || ''}|${c.price || ''}`).join('; ')
log(`候选池共 ${tickers.length} 只: ${tickers.join(', ')}`)

// ===== Wave 3: 四大师+checklist 深度研究 (并行8个, 每agent 3-4只) =====
phase('Deep')
const CHUNKS = []
const T = [...tickers]
for (let i = 0; i < Math.min(8, Math.ceil(T.length / 3)); i++) {
  CHUNKS.push(T.slice(i * 3, i * 3 + 3))
}
const deepResults = await parallel(CHUNKS.map((chunk, i) => () =>
  agent(`用investment-team(段永平/巴菲特/芒格/李录四视角)和investment-checklist(巴菲特六关)深度研究以下候选股: ${chunk.join(', ')}。每个ticker产出一条research。要求: 1)必须用WebSearch/WebFetch获取2026年8月实时价格和最新财报数据(本季度), 禁止用训练知识冒充实时数据, 数据日期标注; 2)投资期限3-12个月, 重点评估催化剂和上行空间; 3)六关逐关过; 4)诚实, 数据不足就标注数据不足。候选背景: ${meta_info}`, { label: 'deep:' + chunk.join('-'), phase: 'Deep', schema: STOCK_SCHEMA })
))

// ===== Wave 4: 冒泡排序 + 持仓操作 (并行2个) =====
phase('Sort')
const deepSummary = deepResults.filter(Boolean).map(r =>
  `${r.ticker}: 现价${r.research.price_0810} | 四大师[${r.research.four_masters}] | 六关[${r.research.checklist_6_gates}] | 催化[${r.research.catalysts_3_12m}] | 上行${r.research.upside} | ${r.research.verdict} | 置信${r.research.confidence}`
).join('\n')

const [final, holdings] = await parallel([
  () => agent(`你是投资排序裁判。候选池: ${tickers.join(', ')}。深度研究结果:\n${deepSummary}\n\n任务: 用冒泡排序方法两两比较——对每对(A,B)根据(3-12个月上行空间×确定性×催化剂强度×checklist通过度)判定谁更值得, 逐步淘汰, 最终选出唯二"最值得且最可能大赚"的股票。注意: 1)候选池含用户已持仓(BABA/MSFT/ADBE/CRM/BRK.B/UBER/INTU/QCOM/TSM/TLN/RARE/CRCL), 新买入标的尽量与持仓互补; 2)所有判断基于上面提供的实时数据+你自己的WebSearch补充验证关键数据; 3)3-12个月期限, 大涨50%+为"大赚"标准; 4)ranked_pool字段给出完整淘汰链记录。`, { label: 'final:top2', phase: 'Sort', schema: FINAL_SCHEMA }),
  () => agent(`${HOLDINGS_CTX}\n\n任务: 用investment-team+checklist框架对每只持仓给出北京时间2026/08/10 23:59可执行操作: 清仓/减仓/持有/加仓/新建, 必须给出数量、参考价、理由(基于实时数据+催化+3-12个月前景)。特别处理: BABA 29.3%超配(目标12%, 8/20财报前还是后减?)、CRM 6.8%超5%上限(8/26财报验证Agentforce, 财报前减还是等?)、UBER 5.4%超3%上限(Q3指引弱)。卖出回收的资金+现金$27.6K如何分配买入新标的(结合另一个agent的top2结论, 但独立给出你的资金计划)。必须用WebSearch验证关键事实(如财报日期、最新指引)。`, { label: 'final:holdings', phase: 'Sort', schema: HOLDINGS_SCHEMA }),
])

return { pool_size: tickers.length, tickers, final, holdings }
