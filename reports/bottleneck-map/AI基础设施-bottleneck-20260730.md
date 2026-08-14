# AI 基础设施供应链瓶颈扫描 — 2026-07-30

> **趋势**：AI 基础设施建设（全球 capex $700-725B/年，2026-2031 累计 $7.6 万亿）
> **执行模式**：team-lead 单干 + WebSearch 多源验证
> **核心理念**：不问"AI 推荐什么股票"，问"如果 capex 继续扩张，哪一环会先不够用？"
> **范围**：Layer 2-3 为主（Layer 1 已被充分定价），美股+ADR 为主

---

## 第一步：趋势确认

```
趋势名称：AI 基础设施建设
核心驱动力：四大 hyperscaler 2026 年 capex $700-725B（+77% YoY），2026-2031 累计 $7.6 万亿
已发生的验证事件：
  1. [2026-07-22] Alphabet Q2 FCF 历史首次转负 -$5.9B（capex $44.9B），全年指引 $195-205B
  2. [2026-07-29] Microsoft FY26Q4 财报：capex ~$190B，Azure AI +40%
  3. [2026-07-27] CXMT A 股首日 +466%，市值 ~$500B——AI 芯片短缺仍极严重
  4. [2026-07] Amazon 维持 $200B capex 指引；Meta $115-135B
资本开支规模：全球约 $700-725B/2026，增速 +77% YoY
供需缺口判断：需求增速 (+77%) >>> 供给扩产速度（CoWoS +30%、HBM +40%、InP 激光 +20%）
趋势确认：✅ 可追踪——这是 2020s 年代最大的物理供应链扩张
```

**关键背景**：上周 Mag 7 因 Google FCF 转负单日蒸发 $8000 亿，市场开始区分"烧钱买未来"和"已经赚到 AI 钱"的公司。**但无论 hyperscaler 股价怎么跌，物理供应链的 capex 已经签约/在建——瓶颈不会因为股价下跌而消失。**

---

## 第二步：供应链物理拆解（聚焦 Layer 2-3）

```
Layer 0：AI 模型训练/推理服务
Layer 1（已被充分定价）：GPU/加速器（NVDA）、HBM（SK Hynix/Samsung/Micron）、CoWoS（TSMC）
─── alpha 集中区 ───
Layer 2（重点扫描）：
  ├─ 🔴 光通信核心：InP 衬底、EML/CW 激光器、光探测器
  ├─ 🔴 先进封装载板：ABF 基板、IC 载板
  ├─ 🔴 电力基础设施：高压变压器、开关柜、母线槽
  ├─ 🟡 晶圆级测试：Probe Card、老化测试、ATE
  ├─ 🟡 散热：液冷系统、CDU、浸没式冷却液
  └─ 🟡 PCB/载板：高频高速 PCB、特殊玻纤布
Layer 3：
  ├─ 外延设备：MOCVD、MBE
  ├─ 光刻/刻蚀：特殊波长光刻、InP 刻蚀
  └─ 原材料：高纯金属（铟、镓、锗）、特气、靶材
Layer 4：
  ├─ 电力：核电、天然气发电、输变电
  ├─ 冷却水/散热基础设施
  └─ 数据中心土地/许可
```

---

## 第三步：瓶颈地图

### 🔴 S 级瓶颈（单点故障级）

| # | 瓶颈环节 | 供给集中度 | 扩产周期 | 替代难度 | 利用率 | 需求增速 | 客户验证 | 评级 |
|---|---------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | **InP 衬底 + EML/CW 激光器** | ≤3家 | >2年 | 不可替代 | >90% | >50%/年 | >1年 | **S** |
| 2 | **高压电力变压器** | ≤4家 | **2-5年** | 不可替代 | >95% | >30%/年 | >2年 | **S** |
| 3 | **CoWoS 先进封装** | **TSMC 独家** | >2年 | 不可替代 | >95% | >50%/年 | >1年 | **S**（已知） |

### 🟡 A 级瓶颈（严重受限）

| # | 瓶颈环节 | 供给集中度 | 扩产周期 | 替代难度 | 利用率 | 需求增速 | 评级 |
|---|---------|:--:|:--:|:--:|:--:|:--:|:--:|
| 4 | **ABF 基板（IC 载板核心材料）** | 4家寡头 | 1.5-2年 | 部分可替代 | >90% | 40%/年（2027） | **A** |
| 5 | **HBM 用 Probe Card** | 3家主导 | 1-2年 | 部分可替代 | >90% | >40%/年 | **A** |
| 6 | **液冷散热基础设施** | 5-8家 | 1年 | 部分可替代 | >85% | >50%/年 | **A** |

### 🟢 B 级瓶颈（有压力但可控）

| # | 瓶颈环节 | 评级 | 说明 |
|---|---------|:--:|------|
| 7 | 高频高速 PCB + 特殊玻纤布 | B | 供给分散，但低损耗等级紧张 |
| 8 | MOCVD 外延设备 | B | Veeco/LPE/Aixtron，供给集中但需求增速适中 |
| 9 | 高纯铟/镓/锗原材料 | B | 地缘集中（中国主导），但战略储备可缓冲 |

---

## 第四步：公司筛选 + 估值检查

### 重点标的（美股上市，按瓶颈纯正度+估值合理性排序）


### 瓶颈机会排名表

| 排名 | 公司 | 代码 | 市值 | 年收入 | PS | PE | 瓶颈环节 | 瓶颈评级 | 收入增速 | 信号强度 | 估值判断 |
|:--:|------|------|------|--------|-----|-----|---------|:--:|:--:|:--:|:--:|
| 1 | **Fabrinet** | FN | $17B | $4.24B | **4.0x** | 40.5x | 光收发器代工 | S | +30% | ★★★★ | **合理偏低** |
| 2 | **FormFactor** | FORM | $6.5B | $1.03B | 6.3x | ~25x(Fwd) | HBM Probe Card | A | +32% | ★★★★ | **合理** |
| 3 | **Lumentum** | LITE | $55B | $2.49B | **22x** | N/A(亏损转盈) | EML/CW 激光器 | S | +69% | ★★★ | ⚠️ **偏高** |
| 4 | **GE Vernova** | GEV | ~$130B | ~$36B | 3.6x | ~30x | 电力变压器/电网 | S | +15% | ★★★ | 合理 |
| 5 | **Coherent** | COHR | $50B | $2.1B | **24x** | 50x | 激光器+InP | S | +58% | ★★★ | ⚠️ **偏高** |
| 6 | **Aehr Test** | AEHR | ~$1.5B | ~$80M | 19x | N/A(亏损) | 晶圆级老化测试 | A | +50% | ★★ | ⚠️ 黄灯 |
| 7 | **POET Technologies** | POET | $1.1B | $1.1M | **1000x** | N/A | 硅光 InP 引擎 | S | N/A | ★ | 🚫 **透支** |

### 逐家分析

#### 🥇 Fabrinet（FN）— S 级光通信瓶颈的"卖铲人"

**瓶颈定位**：Layer 2，光收发器代工（EMS），NVIDIA 第一大客户
- 全球光收发器代工龙头，市占率 ~30%+
- 客户：NVIDIA（第一大）、Lumentum、Coherent、Cisco
- 不制造激光器/芯片，但**组装测试最终收发器**——所有光通信瓶颈最终都要流过它

**为什么现在值得关注**：
- InP 激光器短缺 → 收发器涨价 → 代工毛利改善
- NVIDIA $2B Coherent 订单 → Fabrinet 是组装方
- FY2026 Q3 营收创纪录，AI 相关收入占比持续提升

**财务快照**（已有报告 7-12 底座）：
- 市值 $17B / TTM 营收 $4.24B / **PS 仅 4.0x**（五家中最低）
- PE 40.5x / Forward PE 28.75x / ROE 19.1% / 净现金 +$956M
- PS 4x + 收入增速 30% + 盈利 = **估值绿灯**

**估值安全边际检验**：
- 10 年后 25x PE 退出，需净利润 $6.75B
- 按净利率 10%（当前水平），需收入 $67.5B（是今天 $4.24B 的 16x）
- 对应 10 年 CAGR 32%——**与当前 30% 增速一致，年化回报 ~12-15%**
- ✅ **有安全边际**

**风险检查**：
- [x] 替代技术：CPO（共封装光学）可能绕过独立收发器代工——**5-8 年后风险**
- [x] 客户集中：NVIDIA 占比 >30%（最大单点风险）
- [x] 毛利率天花板：代工模式净利率 ~10%，难以大幅提升
- [x] 地缘：泰国工厂集中（洪水/政变风险）

**结论**：✅ **值得深入研究**（已有 7-12 报告）。五家中估值最合理、护城河最清晰、现金流最真实。**Layer 2 瓶颈的首选标的。**

---

#### 🥈 FormFactor（FORM）— HBM 测试瓶颈

**瓶颈定位**：Layer 2，HBM Probe Card（探针卡）
- 全球 Probe Card 市占率 #1（~25-30%）
- HBM 测试是"AI 芯片出厂前的最后关卡"——每片 HBM 需要 10,000-50,000 接触点测试
- 客户：SK Hynix、Samsung、Micron（三大 HBM 厂）、TSMC、NVIDIA

**为什么现在值得关注**：
- Q2 2026 营收 $258M 创纪录（+32% YoY），$1B+ 年化 run rate
- HBM probe card 占收入 ~25%，随 HBM 产能扩张同步增长
- Farmers Branch 新设施 Q4 投产，扩产瓶颈解除

**财务快照**：
- 市值 $6.5B / 年化营收 $1.03B / PS 6.3x / 增速 +32%
- 盈利（Q3 EPS 指引 $0.86）→ PE ~25x（Forward）
- ⚠️ GuruFocus GF Value 标"高估 59.8%"——但 GF Value 对高速增长股常滞后

**估值检查**：
- PS 6.3x + 32% 增速 + 盈利 = **估值黄灯偏绿**
- 市值 $6.5B / TAM（Probe Card 市场 ~$25-30B）= 22-26%——接近 TAM 20% 红线但不超
- 10 年 25x PE 退出需净利 $2.6B，按净利率 20% 需收入 $13B（是今天 $1B 的 13x）
- 对应 10 年 CAGR 29%——**与当前增速一致，年化回报 ~10-12%**
- ✅ **勉强有安全边际**

**结论**：✅ **加入观察名单**。HBM 测试是"每片 HBM 都要过"的关卡，纯正度高。**等回调至 PS 5x 以下（~$130）加仓。**

---

#### 🥉 Lumentum（LITE）+ Coherent（COHR）— 激光器双雄

**瓶颈定位**：Layer 2，EML/CW 激光器设计+制造（S 级瓶颈最纯正）
- LITE：全球激光器 #2，InP 激光器是 800G/1.6T 收发器核心
- COHR：全球激光器 #1（含 II-VI 合并），**NVIDIA $2B 订单**
- 2026 年 InP 激光器需求 2.2 亿颗，结构性短缺至 2027

**估值检查**：⚠️ **双双偏高**
- LITE：PS 22x，市值 $55B > 激光器 TAM $26B（200%+）
- COHR：PS 24x，PE 50x，市值 $50B 同样 > TAM
- **触发红灯#1**：市值 > TAM 的 20%（这里超过 TAM 本身）
- 10 年 25x PE 退出需净利 $22B（LITE）/ $20B（COHR）
- 对应 10 年 CAGR 45%——**远超可持续水平**

**结论**：⚠️ **暂不追踪（估值透支）**。瓶颈逻辑最纯正（S 级 + 增速最快 69%），但 PS 22-24x 已 price in 未来 5 年增长。**等回调至 PS 12-15x 再评估。** 已有 LITE 7-10 报告可复用。

> 这是"瓶颈真实 ≠ 投资机会"的典型案例——skill 第 8 条原则的教科书式验证。

---

#### GE Vernova（GEV）— 电力变压器瓶颈

**瓶颈定位**：Layer 4 → Layer 2，电网设备+变压器
- 高压变压器交期 2-5 年，12-16 GW 数据中心产能仅 5 GW 在建
- GE Vernova = GE 可再生能源+电网设备分拆（2024）
- 燃气轮机+高压直流+变压器——"电力瓶颈的全面受益者"
- 订单积压 $120B+

**估值检查**：合理
- PS 3.6x（最低之一） / PE ~30x / 收入增速 ~15%
- 电力瓶颈"最慢但最确定"——订单已签到 2029-2031

**结论**：⚠️ **加入观察名单**。适合作为"防守型 AI 基建"配置，不适合追求高增速。

---

#### 🚫 POET Technologies（POET）— 硅光投机

**估值检查**：🚫 **透支**
- PS **1000x**（市值 $1.1B / 收入 $1.1M）
- 触发所有红灯——纯投机，无安全边际

**结论**：🚫 **暂不追踪**。


---

## 第五步：交叉验证

### 正向验证汇总

| 验证项 | FN | FORM | LITE | GEV | 状态 |
|--------|:--:|:--:|:--:|:--:|------|
| 客户验证 | ✅ NVIDIA | ✅ SK Hynix | ✅ NVIDIA 链 | ✅ 公用事业 | 全部通过 |
| 收入验证 | ✅ Q3 创纪录 | ✅ Q2 创纪录 | ✅ +69% YoY | ✅ 订单 $120B+ | 全部通过 |
| 价格验证 | ✅ 收发器涨价 | ✅ ASP 提升 | ✅ 激光器分配制 | ✅ 变压器涨价 | 全部通过 |
| 产能验证 | ✅ 泰国扩产 | ✅ Farmers Branch | ⚠️ InP 紧张 | ✅ 但交期 2-5y | 4/5 通过 |

### 反向验证（芒格式否定）

| 反向问题 | 最危险标的 | 解答 |
|---------|----------|------|
| 瓶颈能被绕过吗？ | FN（CPO 共封装）| 5-8 年后风险，短期不会 |
| 中国能复制产能吗？ | FORM（中国探针卡）| 中低端可以，HBM 级别不能 |
| 终端需求腰斩会怎样？ | LITE/COHR | 收入跌 40%+，但 PS 已透支 |
| 估值隐含什么假设？ | LITE/COHR | 隐含 45% CAGR 10 年——不可持续 |

---

## 第六步：行动建议

| 标的 | 建议动作 | 理由 | 触发价格 |
|------|---------|------|---------|
| **Fabrinet (FN)** | **🥇 首选标的** | PS 4x + 盈利 + S 级瓶颈 + 净现金 | 当前 $470 可建仓；$400 以下加满 |
| **FormFactor (FORM)** | **🥈 加入观察** | HBM 测试纯度高，估值不算便宜 | 等 $130（PS 5x）以下 |
| **GE Vernova (GEV)** | **🥉 防守配置** | 电力瓶颈最纯正，订单可见性极高 | 当前可小仓位（防守型） |
| Lumentum (LITE) | 暂不追踪 | 瓶颈纯正但 PS 22x 透支 | 等 $300-400（PS 12-15x） |
| Coherent (COHR) | 暂不追踪 | 同 LITE，市值 > TAM 200% | 等 PS 12x 以下 |
| Aehr (AEHR) | 加入观察 | 逻辑成立但小市值亏损 | 等盈利后评估 |
| POET (POET) | 不追踪 | PS 1000x 纯投机 | — |

### 跨公司核心洞察

1. **Fabrinet 是 Layer 2 瓶颈的"最优解"**——PS 4x 是七家中最低，盈利能力最强（净利率 10%），且处于"所有光通信瓶颈最终都要流过它"的咽喉位置。无论 InP 短缺还是 CoWoS 扩产，Fabrinet 都受益。

2. **激光器双雄（LITE/COHR）瓶颈最纯但估值最贵**——"瓶颈真实 ≠ 投资机会"的典型案例。S 级瓶颈 + 69% 增速被 PS 22-24x 充分定价。**等回调 40-50% 才有安全边际。**

3. **电力瓶颈（GEV）是"最慢但最确定"的**——变压器交期 2-5 年意味着订单已签到 2029+，但收入增速仅 15%。

4. **HBM 测试（FORM）是被忽视的"每片 HBM 都要过"关卡**——HBM 产能扩张 40%/年，Probe Card 同步受益。

---

## 第七步：与 MSFT/GOOG 对比的启示

回到本对话的原始问题（"最值得买的 AI 公司"）：

| 维度 | 买 MSFT/GOOG | 买瓶颈股（FN/FORM） |
|------|-------------|-------------------|
| 定价层 | Layer 0（终端服务）| Layer 2（物理瓶颈）|
| 估值 | PE 20-32x | PS 4-6x |
| 风险 | capex ROI 不确定 | 客户集中+技术替代 |
| 收益来源 | AI 变现 | AI capex 物理瓶颈涨价 |
| 时间窗口 | 长期（5-10 年）| 中期（2-3 年，瓶颈解除前）|

**段永平式总结**："MSFT 是已经赚到 AI 钱的公司，FN 是卖铲给挖金子的人的公司。两者不冲突——MSFT 买确定性，FN 买弹性和低估。但如果只能选一个，MSFT 的护城河+管理层+资产负债表更让人放心。**FN 更适合作为 MSFT 的对冲+增强配置——如果 AI capex 兑现，FN 涨更多；如果 MSFT capex ROI 不及预期，FN 已经物理交付赚到钱了。**"

---

## 附录：数据来源

**capex/趋势**：
- [Yahoo Finance — Big Tech $7.6T capex 2026-2031](https://finance.yahoo.com/sectors/technology/article/meta-microsoft-amazon-and-alphabet-are-about-to-spend-a-shocking-amount-of-money-to-dominate-the-ai-era-115359575.html)
- [CNBC — Mag 7 $700B AI spending](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html)

**InP/激光器瓶颈**：
- [Wukong — InP substrate shortage 220M chips](https://wukong123.substack.com/p/inp-substrate-supply-demand-price)
- [ChipStrat — Lumentum laser bottleneck](https://www.chipstrat.com/p/lumentum-and-the-laser-bottleneck)
- [Photon Capital — EML/CW shortage trajectory](https://photoncap.net/p/everyone-saw-a-laser-shortage-the)

**ABF 基板瓶颈**：
- [LinkedIn — ABF 40% YoY growth 2027](https://www.linkedin.com/posts/fuyuanliu_abf-ajinomoto-build-up-film-substrates-activity-7446620317017513984-gAz0)
- [TechTimes — ABF gap 10% H2 2026, 21% 2027](https://www.techtimes.com/articles/321754/20260728/ai-supply-crisis-moves-upstream-advanced-packaging-becomes-binding-constraint.htm)

**电力瓶颈**：
- [EnkiAI — Data center power crisis 2026](https://enkiai.com/data-center/data-center-power-crisis-2026-the-grid-bottleneck/)
- [Emergage — 12-16 GW capacity, only 5 GW under construction](https://emergedge.com/blog/ai-datacenter-power-bottleneck-2026)

**HBM 测试**：
- [FormFactor Blog — AI+HBM redefining test](https://www.formfactor.com/blog/2026/how-ai-and-hbm-are-redefining-semiconductor-test/)
- [FormFactor Q2 2026 — $258M record revenue](https://finance.yahoo.com/markets/stocks/articles/formfactor-inc-form-q2-2026-050432973.html)

**已有报告底座**：
- [Fabrinet (FN) 投研报告 7-12](../Fabrinet-FN-investment-research-20260712.md)
- [Lumentum (LITE) 投研报告 7-10](../Lumentum-LITE-investment-research-20260710.md)

---

*报告日期：2026-07-30 | 执行：team-lead 单干 + WebSearch 多源验证 | 免责声明：AI 驱动，不构成投资建议。瓶颈有时效性，每个瓶颈都会被解除，关键是判断时间窗口。*
