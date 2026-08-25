# 瓶颈猎手 — AI算力供应链（电力/光互连/存储）— 2026-08-20

**执行方式**：正式调用 /bottleneck-hunter skill（本轮为 /portfolio-rebalance 全量模式第三步来源D的正式执行）
**数据截止**：2026-08-20 北京时间 ~18:55（美东 8/20 盘前）
**搜索通道**：gnews（Google News RSS）+ tavily MCP（本轮会话实证），逐条见 search-log.txt

## 第一步：超级趋势确认 ✅

趋势：AI基础设施建设。验证事件（本轮搜索实证）：
1. [8/17] Nvidia 为 OpenAI 俄亥俄数据中心提供最高 **$105B 融资担保**（Reuters/CNBC）
2. [8/20] Skanska 签约 **$1.2B** 建设美国东南4座数据中心（Unite.AI，今日）
3. [8/17] Nvidia 向 SB Energy 投资 $1.5B（数据中心电力配套）；Meta El Paso $12.5B 交易
4. 2026 hyperscaler CapEx $610-725B（本轮早前 tavily 验证）

资本开支 >$500B/年 ✅ 物理性 ✅ 加速性 ✅ → **可追踪**

## 瓶颈地图（2026-08-20 增量更新）

### S级瓶颈

**1. 电力设备（变压器/输变电）— 维持S级**
- 6条标准：供给集中🟡 / 扩产周期🔴（**交期已延至4年**，pv magazine USA 8月）/ 替代难度🔴 / 利用率🔴 / 需求增速🔴 / 验证周期🔴 → 5🔴 = S级
- 证据："US power companies scramble to secure equipment"（Yahoo Finance）；"HV Engineer Scarcity Blocks $1T AI Data Center Buildout"（Tech Times——高压工程师短缺成为新瓶颈维度）
- 标的映射：GEV / ETN / PWR / HUBB / POWL / MYR（已入池）
- vs 上次扫描：新增"人力瓶颈"维度（HV工程师），瓶颈未解除、反而加深

**2. 光互连上游——InP衬底/激光器 — 新升级 S级**
- 证据（本轮新增，强）：
  - TrendForce："**InP Shortage Emerges as AI Optical Interconnect Bottleneck**"
  - Nomura：Lumentum 财报确认光芯片持续短缺，中国供应商获得机会
  - Tech Times：**Nvidia $4B 激光器锁单，竞争对手被挤到 2027 之后**
  - LITE R300 光路交换机 backlog >$400M；NVDA 对 LITE $2B 现金投资+多年采购协议（本轮早间搜索）
  - COHR：2026年大部分产能已订满，book-to-bill >4:1
- 6条标准：供给集中🔴（InP晶圆厂极少：Coherent自有+住友电工+JX金属）/ 扩产🔴（>2年）/ 替代🔴（硅光无法替代激光器光源）/ 利用率🔴 / 需求🔴（800G→1.6T）/ 验证🔴 → **6🔴 = 本轮最强S级**
- 标的映射：**AXTI（InP/GaAs衬底纯正标的，本轮H轮发现，Q2财报后+27%）**、LITE、COHR、AAOI、FN（Fabrinet代工）、300308.SZ中际旭创/300502.SZ新易盛（A股，受单一国家敞口约束限制）
- vs 上次扫描（8/18 为A级）：**升级为S级**——InP衬底短缺从传闻变为TrendForce正式确认+Nvidia锁单实证

**3. 存储（DRAM/NAND/HBM挤兑）— 维持S级**
- 证据（本轮新增）：DRAM现货 **$42/条创纪录**（tech-insider）；Apacer CEO：**2027年DRAM对模组厂供给可能骤降>70%**（HBM+服务器挤占产能，Tom's Hardware）；Apple 被迫涨价20%
- 标的映射：MU（HBM 2027年前售罄）、SNDK（$93B backlog论点，24/7 Wall St）、STX/WDC（已入池）
- 风险信号：MU/SK海力士/三星股价近期回调（MarketWise）——市场对"记忆体价格海啸"的持续性存疑

### A级瓶颈
- **液冷/CDU**：维持A级（VRT/NVT 本轮早前4-Agent已评估，均等回调触发价）
- **CoWoS先进封装**：维持A级→趋缓（缺口20%→10%收窄，早前温度判定已验证）

## 瓶颈机会排名表（本轮增量，必填字段标注）

| 排名 | 公司 | 代码 | 市值 | PS估计 | PE | 瓶颈环节 | 评级 | 收入增速 | 信号 | 估值判断 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AXT Inc | AXTI | ~$2-3B(估) | 高(估>15x) | 转正初期 | InP/GaAs衬底 | S | 拐点刚至(Q2 beat+27%) | ★★★ | ⚠️黄灯：亏损转盈初期，需盈利路径验证 |
| 2 | Lumentum | LITE | ~$40B+(估) | 高 | 改善中 | 光芯片/激光器/OCS | S | 加速(路径$2B季收入) | ★★★★ | 黄灯：NVDA $2B投资背书但估值已上修 |
| 3 | Coherent | COHR | 已在watchlist | — | — | InP垂直整合+光模块 | S | book-to-bill>4 | ★★★★ | 待触发价$260-290（沿用watchlist） |
| 4 | Fabrinet | FN | ~$20B+(估) | ~4x(估) | ~25x(估) | 光模块代工产能 | A | 稳健 | ★★★ | 绿灯候选：低PS+盈利，需fetch验证 |
| 5 | Powell Ind. | POWL | ~$5B(估) | — | — | 配电设备(变压器替代链) | S | 高backlog | ★★★ | 早前涨幅大，等回调 |
| 6 | MU/SNDK | — | 已跟踪 | — | — | HBM/NAND | S | 极高 | ★★★ | 记忆体周期顶部风险，观察 |

> ⚠️ 除标注"已验证"外，市值/PS/PE为估计值（本轮未逐一fetch正文验证——按skill 4.2.1，估计值标的信号强度封顶★★★，进入终选前必须补fetch验证）。

## 行动建议

| 标的 | 动作 | 理由 |
|---|---|---|
| AXTI | 加入候选池观察，终选前须4-Agent+checklist | S级瓶颈纯正度最高的小市值标的，但估值黄灯 |
| FN | 加入候选池，低PS绿灯候选 | 瓶颈链中估值最健康 |
| COHR | 维持watchlist触发价纪律 | S级瓶颈但已到高位 |
| 中际旭创/新易盛 | 记录不入池 | 单一非美国家敞口约束（中国A股无法直接纳入当前美股账户框架） |

**候选入池**：AXTI/BAND（H轮）+ SNDK + AAOI + FN + HUBB + POWL 已写入 candidates.csv
