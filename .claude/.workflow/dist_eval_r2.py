# 分布评估 — 2026-08-20 r2（盘前价格口径：BABA/CCL按盘前，其余按收盘或盘前最新）
from decimal import Decimal as D
# 持仓：ticker, 股数, 成本, 现价(优先盘前), 类别
holdings = [
    ("BABA", 245, "121.69", "120.98", "AI平台"),   # 盘前120.98
    ("MSFT", 60, "333.194", "483.00", "AI软件"),    # 盘前483.00
    ("META", 53, "604.78", "546.24", "AI平台"),     # 盘前546.24
    ("CRCL", 300, "74.515", "82.05", "加密"),       # 盘前82.05
    ("TSM", 50, "417.08", "410.46", "AI硬件"),      # 盘前410.46
    ("BRK.B", 30, "508.60", "500.33", "非AI对冲"),  # 盘前500.33
    ("INTU", 40, "319.49", "361.31", "估值修复"),   # 盘前361.31
    ("APLD", 500, "27.992", "27.92", "爆发仓"),     # 盘前27.92
    ("ADBE", 50, "217.267", "273.32", "估值修复"),  # 盘前273.32
    ("PYPL", 200, "58.95", "61.03", "非AI对冲"),    # 盘前61.03
    ("PGR", 30, "209.6233", "218.00", "非AI对冲"),  # 盘前218.00
]
cash = D("83880.00")
total = cash
rows = []
for t, sh, cost, px, cat in holdings:
    mv = D(sh) * D(px)
    total += mv
    rows.append((t, sh, D(cost), D(px), mv, (D(px)/D(cost)-1)*100, cat))
print(f"{'股票':6s} {'股数':>5s} {'成本':>9s} {'现价':>9s} {'市值$':>10s} {'盈亏%':>7s} 类别")
for t, sh, cost, px, mv, pnl, cat in rows:
    print(f"{t:6s} {sh:5d} {cost:9.2f} {px:9.2f} {mv:10.0f} {pnl:+6.1f}% {cat}")
print(f"{'现金':6s} {'':5s} {'':9s} {'':9s} {cash:10.0f}")
print(f"{'总资产':6s} {'':5s} {'':9s} {'':9s} {total:10.0f}")
print()
# 八类分布
cats = {}
for t, sh, cost, px, mv, pnl, cat in rows:
    cats[cat] = cats.get(cat, D(0)) + mv
cats["现金"] = cash
print("== 八类分布（盘前口径） ==")
s = D(0)
for cat, mv in cats.items():
    pct = mv/total*100
    s += pct
    print(f"{cat:8s} ${mv:>10.0f}  {pct:5.1f}%")
print(f"合计校验: {s:.1f}% (必须=100.0)")
ai_total = sum(mv for c, mv in cats.items() if c in ("AI硬件","AI软件","AI平台","估值修复","爆发仓"))
print(f"\nAI总暴露（硬件+软件+平台+修复+爆发）: ${ai_total:.0f} = {ai_total/total*100:.1f}% (硬约束50-75%)")
h = cats.get("AI硬件",D(0)); sw = cats.get("AI软件",D(0)); pf = cats.get("AI平台",D(0))
print(f"  硬件: {h/total*100:.1f}% | 软件: {sw/total*100:.1f}% | 平台: {pf/total*100:.1f}% (AI内部占比: 硬件{h/ai_total*100:.0f}%/软件{sw/ai_total*100:.0f}%/平台{pf/ai_total*100:.0f}%)")
print(f"加密: {cats.get('加密',D(0))/total*100:.1f}% (区间8-12%)")
print(f"非AI对冲: {cats.get('非AI对冲',D(0))/total*100:.1f}% (硬约束10-15%)")
print(f"现金: {cash/total*100:.1f}% (🟠高位档35-45%下限)")
print(f"单一非美敞口(BABA): {D(245)*D('120.98')/total*100:.1f}% (硬上限15%)")
print(f"持仓数: {len(rows)}只 (用户要求≤8只)")
