# 瓶颈猎手 — AI全链路瓶颈扫描 2026-08-14（晚间重跑版）

**执行方式**：本次为 prompt.md 调仓任务内嵌执行，数据来自当日30次AI赛道MCP搜索（搜索词见 .claude/.workflow/search-log.txt）+ 29只短名单实时报价（fetch_quotes.py 22:4x UTC+8）
**与早间版（AI硬件缺口-bottleneck-20260814.md）关系**：独立重跑，零复用

---

## 瓶颈地图（六大环节评级）

| 环节 | 评级 | 核心证据（当日来源） | 标的及估值检查 |
|------|------|---------------------|---------------|
| **CoWoS/先进封装** | **S级**（维持） | 2026全球产能1.3M wafers +48%（DIGITIMES）；TSMC "sold out through 2026"（魏哲家股东会）；月产能120-140K创纪录（TrendForce 6/15） | TSM $428（持仓，挂单$390/400在挂）✅绿灯 |
| **HBM/存储** | **S级**（维持） | MU HBM4 2026全部售罄且为binding contracts（Reddit/官方）；三大厂同时sold out；DRAM 2026价格+125-180%预测（Gartner/GS）；存储收入2026占半导体>50%（Omdia） | MU $969 ⚠️透支（H1已暴涨，周期顶盈利陷阱，LRN-012）★★ |
| **AI电力(IPP)** | **S级**（维持） | 2026 hyperscaler capex $860B +80%（Yahoo/MS）；<1/3计划产能实际开工，卡在电力（IBD）；VST-Meta 3.8GW×20年PPA；TeraWulf-Anthropic $19B 20年租约 | VST $149（持仓，$130挂单）✅；NRG $124 ❌净利率2.6%；CEG/TLN已涨价 |
| **电网设备/变压器** | **S级**（维持） | 变压器交期2-4年（LinkedIn行业）；GEV报价排到2028-2030；2026需求比2024高21%（AWS白皮书） | GEV $1061 ⚠️fPE 41x透支★★；HUBB $487 🟡（Q2 EPS $5.52 beat+电气订单+25%，观察）；PWR $626 🟡 |
| **光模块/CPO** | **A→S升级中** | "CPO或成下一瓶颈"（Semianalysis）；NVDA $4B光学战略+$2B投资两家光学公司（Kindig）；CPO市场CAGR 35.7% | COHR/LITE未报价；CRDO $261 ❌纪律区$130-150上方2倍 |
| **Neocloud GPU云** | **S→A降级 ⚠️** | **META 7/1宣布自建AI云市场**，NBIS/CRWV/IREN当日跳水（Yahoo/TechTimes）；Meta合同集中：CRWV $35.2B + NBIS $27B = $62.2B → 客户集中成结构性风险 | NBIS/CRWV/IREN ❌（此前否决维持：套现/流动性/二元） |
| **ABF基板** | S级（维持，8-6结论延续） | 需求+40%/供给+12% | ONTO/CAMT ❌估值；AMKR ❌FCF负 |
| **硅片** | B级 | Sumco产能2026售罄（SemiWiki） | 标的在日股，用户限定美股 |

## 关键判断

1. **S级瓶颈 × 可买价格 = 空集（除已持仓）**：TSM/AVGO/VST是仅有的同时满足"S级瓶颈正上方+估值可过"的标的——全部已在持仓内，挂单（TSM@$390/400、VST@$130）即瓶颈执行方案。GEV/MU/CRDO/VRT/ANET全部卡在估值红灯。
2. **Neocloud降级是本轮最重要变化**：META自建AI云+客户集中（单客户>60%）动摇"GPU即瓶颈"叙事——验证了不追高neocloud的纪律。
3. **Layer 1错杀股复查**：QCOM $166（8-6结论"Layer 1被错杀"仍成立，但已高于纪律区$120-130）→ 等回调，★标黄。
4. **HUBB为唯一新观察**：电网S级瓶颈+Q2 beat+电气+25%，~25x PE非透支——加入watchlist，等回调至$430-450评估。

## 行动建议
- 挂单（TSM/VST/BRK.B）继续持有等待成交 = AI硬件缺口修正主路径
- 不新增瓶颈标的（估值全红灯）
- 观察名单新增：HUBB（触发$430-45）、QCOM（触发$120-135）
- CRDO/LEU纪律区不变（$130-150/$110-130）

**数据截止**：2026-08-14 22:45 UTC+8（美股盘中）
**信息充分度自评**：估值A（fetch_quotes实时）｜行业格局A（30次搜索多源）｜财务细节B（未逐家验证，终选标的将过checklist）
