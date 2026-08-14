# 数据质量与局限说明 · 2026-08-08

## 数据源

| 用途 | 来源 | 状态 |
|---|---|---|
| 全量科技股行情 | 东方财富 push2 实时接口（10 主机轮换） | ✅ 2026-08-08 12:47:58 成功取数 |
| 个股基本面/预期 | WebSearch 多源交叉（Yahoo / finviz / Benzinga / moomoo / 官方IR） | ✅ 每个终选标的 ≥2 独立源 |
| 估值验算 | `tools/financial_rigor.py` | ✅ ADBE 市值验算偏差 0.03% |

## 覆盖情况

- 候选池 146 只 → **成功取数 123 只（84.2%）**
- 缺失 23 只：LITE, AAOI, CRDO, MRVL, ALAB, POET, IQE, PSTG, QCOM, TXN, ADI, MCHP, MPWR, SWKS, QRVO, NXPI, GFS, SLAB, JNPR, SQ, CCMP, ONSET, SMIC

## 缺失原因（已诊断）

**不是代码缺陷，也不是代码符号错误，而是 IP 限流。**

诊断过程：
1. `patch_missing.py` 单票补抓在第 3 只后进程异常退出（exit=1，无 stderr）
2. 裸 `urllib` 直连测试：**连已成功取过数的 NVDA 也返回 `RemoteDisconnected`**
3. 10 个备用主机逐一测试：9 个 `RemoteDisconnected`，仅 `push2delay` 存活但返回 `{"f115":"-"}` 空数据

结论：连续大批量请求后，东方财富对本机 IP 触发了连接层限流。**12:47:58 那批 123 只的数据是在限流前取得的，完整有效。**

## 对研究结论的影响

**无实质影响。** 全部终选与对照标的均在已取数的 123 只之内：

INTU / ADBE / CRM / ACN / GOOGL / META / MSFT / MU / AMAT / LRCX / KLAC / TSM / NVDA / AVGO / AXTI / COHR / UCTT / ICHR / ONTO / STX / WDC / SNDK / BABA / ORCL / IBM / NOW / WDAY

缺失的 23 只中，仅 **QCOM**（组合持仓 2.0%）与 **MRVL**（上一轮已评为回避）有参考价值，但均不参与本轮终选决策。

## 复现建议

若需补齐缺失标的，等待数小时限流解除后运行：

```bash
python patch_missing.py quotes_us.json
```

`patch_missing.py` 已实现慢速单票补抓（每票 3 次重试 + 三市场轮询 + 0.8s 间隔）并会自动合并回写 `quotes_us.json`。

## 已知的信源黑名单

| 站点 | 问题 |
|---|---|
| `usabusinesstimes.com` | 称「CRM 年内涨 22%」「摩根士丹利近期升级 CRM」，与官方数据完全相反（实为 -27%、7/21 降级）。疑似 AI 生成内容，**禁止引用** |
