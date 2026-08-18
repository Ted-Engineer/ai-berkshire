# 行业分布计算 — 2026-08-14 22:55 UTC+8 盘中价（fetch_quotes.py 双读验证）
# 数据基准：AVGO $398.04(双读)/TSM $426.27(复验426.44)/其余单读
holdings = [
    # ticker, shares, price, category, subcat
    ("META", 80, 598.55, "AI平台", ""),
    ("BABA", 245, 124.37, "非AI价值", "中国电商"),
    ("MSFT", 60, 498.17, "AI软件", ""),
    ("ADBE", 90, 262.41, "AI软件", ""),
    ("AVGO", 55, 398.04, "AI硬件", ""),
    ("BRK.B", 30, 505.30, "非AI价值", "防御价值"),
    ("INTU", 40, 348.92, "AI软件", ""),
    ("TSM", 30, 426.27, "AI硬件", ""),
    ("PYPL", 200, 59.89, "非AI价值", "金融周期"),
    ("CI", 40, 279.75, "非AI价值", "医疗"),
    ("VST", 50, 148.73, "AI硬件", ""),
]
cash = 82355.60

total = cash + sum(s * p for _, s, p, _, _ in holdings)
cats = {}
subcats = {}
for t, s, p, c, sub in holdings:
    v = s * p
    cats[c] = cats.get(c, 0) + v
    if sub:
        subcats[sub] = subcats.get(sub, 0) + v

print(f"总资产 = ${total:,.2f}")
print()
print("| 标的 | 市值 | 占比 |")
for t, s, p, c, _ in holdings:
    v = s * p
    print(f"| {t} | ${v:,.0f} | {v/total*100:.1f}% | {c}")
print(f"| 现金 | ${cash:,.0f} | {cash/total*100:.1f}% |")

print()
print("=== 五类分布（主类别，合计=100%校验） ===")
checksum = 0
for c in ["AI平台", "AI软件", "AI硬件", "非AI价值", "现金"]:
    v = cats.get(c, 0) if c != "现金" else cash
    pct = v / total * 100
    checksum += pct
    print(f"{c}: ${v:,.0f} = {pct:.2f}%")
print(f"合计校验: {checksum:.2f}% （必须=100.00）")

print()
ai_total = (cats.get("AI平台", 0) + cats.get("AI软件", 0) + cats.get("AI硬件", 0)) / total * 100
print(f"*小计 AI总暴露: {ai_total:.2f}% （不参与求和）")
print(f"*小计 持股合计(不含现金): {(total-cash)/total*100:.2f}%")
print(f"*小计 中国敞口(BABA): {cats.get('非AI价值',0)*0+245*124.37/total*100:.2f}%")

print()
print("=== 非AI价值细分 ===")
for sub, v in subcats.items():
    print(f"{sub}: {v/total*100:.2f}%")

print()
print("=== 全成交情景（挂单TSM+30@~395均价、BRK.B+30@488、VST+50@130） ===")
cash2 = cash - 30*426.27 - 30*488 - 50*130  # 用现价近似TSM成交
total2 = total  # 总资产不变（现金转持仓）
# 重新计算：现金减少，相应类别增加（用现价近似）
adj = {"AI硬件": 30*426.27 + 50*130, "非AI价值": 30*488}
cats2 = dict(cats)
for c, v in adj.items():
    cats2[c] = cats2.get(c, 0) + v
print(f"现金: {cash2:,.0f} = {cash2/total2*100:.2f}%")
for c in ["AI平台", "AI软件", "AI硬件", "非AI价值"]:
    print(f"{c}: {cats2[c]:,.0f} = {cats2[c]/total2*100:.2f}%")
ai2 = (cats2["AI平台"]+cats2["AI软件"]+cats2["AI硬件"])/total2*100
print(f"*AI总暴露: {ai2:.2f}%")
