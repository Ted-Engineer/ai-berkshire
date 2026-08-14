#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fix stale body claims in the final report, leaving the correction-record section intact."""
import io

P = 'reports/50pct-upside-final-20260808.md'
s = io.open(P, encoding='utf-8').read()

# marker: everything after this heading is the correction record and must NOT be touched
MARK = '## 十一、重大更正记录'
if MARK in s:
    body, tail = s.split(MARK, 1)
    tail = MARK + tail
else:
    body, tail = s, ''

reps = [
# 162 - fPE vs GAAP PE table
('| CRM | 12.4x | **19.7x** | +58% |',
 '| CRM | 12.4x | **24.0x** | +94% |'),

# 223/226/230 - bubble sort ADBE vs INTU table (guidance basis)
('| **PE 不变的目标价** | **$382.17 = +44.1%** | $447.32 = +37.5% |',
 '| **PE 不变的目标价（GAAP 指引口径）** | **$306.4 = +15.5%**（指引 +7.5%/年）<br>**$368.2 = +38.8%**（利润率企稳口径） | $434.6 = +33.6% |'),

('| **上行/下行赔率** | **2.33x** | **0.91x** |',
 '| **上行/下行赔率** | **0.82x**（指引口径）～ **2.05x**（利润率企稳口径） | **0.81x** |'),

('**裁决：ADBE 胜。** INTU 生意更好、增速更快、跌得更深，但 ADBE 的上行绝大部分（+44.1% / 目标 +50%，即 88%）由回购与增长的算术自动产生，只需 +4.1% 的轻度重估补足；INTU 需 +9.1%。且 ADBE 赔率 2.33x 是 INTU（0.91x）的 2.6 倍——INTU 赔率已低于 1，即赔率上不划算。',
 '**裁决：ADBE 胜，但胜得比初版窄得多，且胜负取决于一个未定事实。**\n\n'
 'ADBE 的优势只在「利润率企稳」口径下成立：那时赔率 2.05x vs INTU 0.81x，且只需 +8.1% 重估。\n'
 '但按公司 FY26 GAAP 指引（EPS +7.5%、GAAP 经营利润率 36.6%→35.0%）原样外推，ADBE 需 +29.8% 重估、赔率仅 0.82x，'
 '**反而略低于 INTU 的 0.81x 同级**——即两者在指引口径下都不划算。\n\n'
 '**因此真正的分歧点是：ADBE FY26 的利润率压缩是一次性的还是结构性的。** 支持一次性的证据：'
 '$0.18/股商誉减值（Publishing & Advertising 报告单元，非核心业务）属非经常项；收入 TTM 仍 +12.7% 在加速。'
 '支持结构性的证据：FY26 SBC 指引 $5.53/股，占 non-GAAP EPS 的 22.7%，且逐年上升；公司本季**主动推迟一次提价**'
 '（管理层原话 deferring it, but not closing it），这是定价权的自我让步。**我无法确定哪一个成立，这是本轮最大未解项。**\n\n'
 'INTU 的劣势则是确定的：悲观下行 -41.4% 四家最差，赔率 0.81x。'),

# 239 - slot 2 table
('| PE 不变目标 | +37.5% | **+49.5%** |',
 '| PE 不变目标（GAAP 指引口径） | **+33.6%** | **+4.1%**（公司 FY27 GAAP 指引仅 +2.1%） |'),

# 309
('5. 悲观情景下行仅 -18.9%，四家最小，赔率 2.33x 最优',
 '5. 悲观情景下行仅 -18.9%，四家最小；赔率 0.82x（指引口径）～2.05x（利润率企稳口径），后者为四家最优'),

# 335 - CRM header stats
('现价 $192.74｜市值 $157.85B（手算校验 **0.00%**）｜GAAP PE **19.7x（5年 0.0 分位＝绝对最低）**｜TTM 收入增速 **+13.3%**',
 '> ### ⛔ 本节结论已被推翻 —— CRM 已从终选剔除\n'
 '> 详见第十一节《重大更正记录》。三处硬错误：\n'
 '> ① GAAP PE 实为 **24.0x**（非 19.7x）——原算法用 TTM 净利 ÷ **当期**股数，而 CRM 期中回购了 14% 股份，分子分母期间不匹配；\n'
 '> ② 收入增速 **+13.3% 是 Q1 FY27 单季**数字，FY26 全年实为 **+9.58%**；\n'
 '> ③ 公司 8-K（2026-05-27）FY27 **GAAP** EPS 指引 **$7.93–7.99** vs FY26 实际 $7.80 = **仅 +2.1%**，'
 '且指引股数已内含 ASR 的 1.03 亿股缩减。按此，CRM 两年空间仅 **+4.1%**，达标需 **+44% 重估**。\n'
 '> 以下原文保留仅为留痕，不作为结论依据。\n\n'
 '现价 $192.74｜市值 $157.85B（手算校验 **0.00%**）｜GAAP PE **24.0x（已更正）**｜FY26 收入增速 **+9.58%（已更正）**'),

# 372 - holdings table
('| **ADBE** | 8.4% | ✅ 4/4 通过 | **留 + 加仓** | 本轮 **#1**，+44.1% 靠算术、仅需 +4% 重估 |',
 '| **ADBE** | 8.4% | ✅ 4/4 通过 | **留 + 加仓** | 本轮 **#1**，赔率 0.82–2.05x，需 +8.1%～+29.8% 重估 |'),

# 417 - action table
('| **1** | **ADBE 加至 12%**（+38 股 → 128 股） | ~$10,152 | #1 标的，赔率 2.33x |',
 '| **1** | **ADBE 加至 12%**（+38 股 → 128 股） | ~$10,152 | #1 标的，5年 PE 3.5 分位 |'),

# 453 - three-scenario caveat
('**⚠️ 重要限定**：上表用 non-GAAP fwdEPS 且为 5 年期，数值偏乐观。**本报告采用的正式目标是第五节的 GAAP 口径 2 年模型（ADBE +44.1%、CRM +49.5%，均为 PE 不变口径）**，那才是结论依据。三情景表仅用于展示区间形状。',
 '**⚠️ 重要限定**：上表用 non-GAAP fwdEPS 且为 5 年期，数值**严重偏乐观**，因 non-GAAP 剔除了 SBC。'
 '**本报告的正式结论口径是第一节与第十一节的「公司 GAAP 指引 / 利润率企稳」双口径 2 年模型**（ADBE +15.5%～+38.8%、INTU +33.6%）。'
 '三情景表仅用于展示区间形状，其绝对数值不可作为目标价。'),
]

n = 0
for a, b in reps:
    if a in body:
        body = body.replace(a, b, 1)
        n += 1
    else:
        print('NOT FOUND:', a[:70])

# also swap the #2 slot label from CRM to INTU in the slot-2 section heading if present
body = body.replace('#2 槽位对决：INTU vs CRM', '#2 槽位对决：INTU vs CRM（最终裁定 INTU 入选，CRM 剔除）')

out = body + tail
io.open(P, 'w', encoding='utf-8').write(out)
print('applied', n, 'of', len(reps))
print('new len', len(out))
