# 调仓后分布计算（盘前口径2026-08-20）
from decimal import Decimal as D
# 调仓后持仓：ticker, 股数, 现价(盘前), 类别
post = [
    ("MSFT", 60, "483.00", "AI软件"),
    ("META", 53, "546.24", "AI平台"),      # 保留至9/23 Connect决策点
    ("TSM", 50, "410.46", "AI硬件"),
    ("BABA", 190, "120.98", "AI平台"),      # 减仓245→190股
    ("CRCL", 200, "82.05", "加密"),         # 减仓300→200股
    ("INTU", 40, "361.31", "估值修复"),
    ("APLD", 500, "27.92", "爆发仓"),
    ("BRK.B", 30, "500.33", "非AI对冲"),
]
# 回收现金：PGR 30×218 + ADBE 50×273.32 + PYPL 200×61.03 + BABA减55股×120.98 + CRCL减100股×82.05
cash = D("83880.00") + D(30)*D("218.00") + D(50)*D("273.32") + D(200)*D("61.03") + D(55)*D("120.98") + D(100)*D("82.05")
total = cash
for t,sh,px,cat in post:
    total += D(sh)*D(px)
print("== 调仓后持仓（8只，盘前口径） ==")
print(f"{'股票':6s} {'股数':>5s} {'现价':>9s} {'市值$':>10s} {'占比':>6s} 类别")
cats = {}
for t,sh,px,cat in post:
    mv = D(sh)*D(px)
    pct = mv/total*100
    cats[cat] = cats.get(cat,D(0))+mv
    print(f"{t:6s} {sh:5d} {px:>9s} {mv:10.0f} {pct:5.1f}% {cat}")
print(f"{'现金':6s} {'':5s} {'':9s} {cash:10.0f} {cash/total*100:5.1f}%")
print(f"{'总资产':6s} {'':5s} {'':9s} {total:10.0f}")
print()
print("== 调仓后八类分布 ==")
s=D(0)
for cat,mv in cats.items():
    s+=mv/total*100
    print(f"{cat:8s} ${mv:>10.0f} {mv/total*100:5.1f}%")
print(f"现金     ${cash:>10.0f} {cash/total*100:5.1f}%")
print(f"合计校验: {(s+cash/total*100):.1f}%")
ai = sum(mv for c,mv in cats.items() if c in ("AI硬件","AI软件","AI平台","估值修复","爆发仓"))
print(f"\nAI总暴露: {ai/total*100:.1f}%（硬约束50-75%）")
print(f"非AI对冲: {cats.get('非AI对冲',D(0))/total*100:.1f}%（10-15%+挂单$488成交后~10%+）")
print(f"加密: {cats.get('加密',D(0))/total*100:.1f}%（8-12%）")
print(f"现金: {cash/total*100:.1f}%（🟠档35-45%；挂单成交后{(cash-D(15)*D('390')-D(30)*D('488')-D(12)*D('890')-D(10)*D('270'))/total*100:.1f}%）")
print(f"AI硬件: {cats.get('AI硬件',D(0))/total*100:.1f}%（cap35%，MU/TSM触发单成交后~{D(50)*D('410.46')/total*100+D(15)*D('390')/total*100+D(12)*D('890')/total*100:.1f}%）")
print(f"BABA单一非美: {D(190)*D('120.98')/total*100:.1f}%（≤15%）")
# 挂单
print("\n== 挂单/触发价待部署（成交后回补） ==")
orders = [("TSM加仓","$390×15股","~$5,850",f"{D(15)*D('390')/total*100:.1f}%"),
          ("BRK加仓","$488×30股","~$14,640",f"{D(30)*D('488')/total*100:.1f}%"),
          ("MU新建GTC1","$880-900×6股","~$5,340",f"{D(6)*D('890')/total*100:.1f}%"),
          ("MU新建GTC2","$820-850×6股","~$5,010",f"{D(6)*D('835')/total*100:.1f}%"),
          ("ALAB新建GTC","$265-275×10股","~$2,700",f"{D(10)*D('270')/total*100:.1f}%")]
for n,o,v,p in orders:
    print(f"{n:12s} {o:16s} {v:9s} 仓位{p}")
