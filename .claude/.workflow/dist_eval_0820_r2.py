#!/usr/bin/env python3
# ≤8只调仓续作：盘前价口径分布计算（2026-08-20 20:55 CST盘前，CNBC API）
POS = [  # ticker, shares, cost, premkt_price, category
 ("BABA",245,121.69,121.31,"AI平台"),
 ("MSFT",60,333.194,483.40,"AI软件"),
 ("META",53,604.78,547.29,"AI平台"),
 ("CRCL",300,74.515,82.73,"加密"),
 ("TSM",50,417.08,410.07,"AI硬件"),
 ("BRK.B",30,508.60,500.25,"非AI对冲"),
 ("INTU",40,319.49,361.56,"估值修复"),
 ("APLD",500,27.992,27.99,"爆发仓"),
 ("ADBE",50,217.267,273.32,"估值修复"),
 ("PYPL",200,58.95,61.15,"非AI对冲"),
 ("PGR",30,209.6233,217.30,"非AI对冲"),
]
CASH=83880.00
mv={t:s*p for t,s,c,p,cat in POS}
total=sum(mv.values())+CASH
print(f"{'股票':6s} {'股数':>5s} {'成本':>9s} {'盘前价':>9s} {'市值':>11s} {'盈亏%':>7s} {'占比%':>6s} 类别")
for t,s,c,p,cat in sorted(POS,key=lambda x:-mv[x[0]]):
    print(f"{t:6s} {s:5d} {c:9.2f} {p:9.2f} {mv[t]:11,.0f} {(p/c-1)*100:+6.1f}% {mv[t]/total*100:5.1f}% {cat}")
print(f"{'现金':6s} {'':5s} {'':9s} {'':9s} {CASH:11,.0f} {'':7s} {CASH/total*100:5.1f}%")
print(f"总资产 = {total:,.2f}")
print()
cats={}
for t,s,c,p,cat in POS: cats[cat]=cats.get(cat,0)+mv[t]
cats["现金"]=CASH
order=["AI硬件","AI软件","AI平台","估值修复","爆发仓","加密","非AI对冲","现金"]
target={"AI硬件":"动态cap35","AI软件":"动态15-25","AI平台":"动态25-35(占AI)","估值修复":"10-20","爆发仓":"15-25","加密":"8-12(🟢→🟡)","非AI对冲":"10-15","现金":"25-35(🟠边缘)"}
ssum=0
print("八类分布（v5.4口径，盘前价）")
for c in order:
    v=cats.get(c,0); ssum+=v
    print(f"{c:8s} {v:11,.0f} {v/total*100:5.1f}%  目标{target[c]}")
print(f"合计校验: {ssum:,.2f} vs 总资产 {total:,.2f} -> {'✅ 100.0%' if abs(ssum-total)<0.01 else '❌'}")
ai=sum(cats.get(c,0) for c in ["AI硬件","AI软件","AI平台","估值修复","爆发仓"])
print(f"AI总暴露(硬+软+平台+修复+爆发) = {ai:,.0f} = {ai/total*100:.1f}% (硬约束50-75%)")
print(f"持仓数 = {len(POS)}只 (用户新约束 ≤8只 → 需砍{len(POS)-8}只)")
# 类别集中度检查 top2
from collections import Counter
cnt=Counter(cat for _,_,_,_,cat in POS)
for c,n in cnt.items():
    flag="🔴超top2" if n>2 else ("⚠️达top2" if n==2 else "✅")
    print(f"  {c}: {n}只 {flag}")
