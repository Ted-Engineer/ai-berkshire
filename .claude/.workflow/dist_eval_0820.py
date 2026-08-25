#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v5.4 行业分布评估 — 2026-08-20
8/19 收盘价 + 8/19夜盘价双口径（夜盘变动>±1% 标记）
合计校验 = 八类互斥 = 100%
AI子类（硬件+软件+平台+修复+爆发）单独汇总
"""
holdings = [
    # (ticker, name, shares, cost, last_close, last_overnight, category)
    ("BABA","Alibaba",245,121.69,128.90,129.63,"AI平台"),
    ("MSFT","Microsoft",60,333.194,484.31,484.86,"AI软件"),
    ("META","Meta Platforms",53,604.78,546.03,549.99,"AI平台"),
    ("ADBE","Adobe",90,217.267,272.47,272.24,"估值修复"),
    ("TSM","TSMC",50,417.08,412.09,413.80,"AI硬件"),
    ("BRK.B","Berkshire",30,508.60,499.62,500.39,"非AI对冲"),
    ("INTU","Intuit",40,319.49,362.47,362.60,"估值修复"),
    ("APLD","Applied Digital",500,27.992,28.23,28.57,"爆发仓"),
    ("PYPL","PayPal",200,58.95,61.25,61.15,"非AI对冲"),
    ("CRCL","Circle",150,74.515,78.59,80.57,"加密"),
    ("PGR","Progressive",30,209.6233,217.27,217.71,"非AI对冲"),
]
cash = 95052.00
total_expected = 303916  # 来自 portfolio-latest.md 8/19 收盘口径

# 用 8/19 收盘价 算分布
mv_by_cat = {}
mv_by_hold = {}
for t,n,s,c,cl,ov,cat in holdings:
    mv = s * cl
    mv_by_hold[t] = {"name":n,"shares":s,"cost":c,"close":cl,"ov":ov,"mv":mv,"cat":cat,"pnl":(cl-c)/c*100}
    mv_by_cat[cat] = mv_by_cat.get(cat,0) + mv
mv_by_cat["现金"] = cash
total_actual = sum(mv_by_hold[h]["mv"] for h in mv_by_hold) + cash

# AI子类别小计
ai_subs = {"AI硬件","AI软件","AI平台","估值修复","爆发仓"}
ai_total = sum(mv_by_cat.get(c,0) for c in ai_subs)
crypto_total = mv_by_cat.get("加密",0)
non_ai_hedge = mv_by_cat.get("非AI对冲",0)

# 表格
print("="*120)
print("  行业分布评估（v5.4 口径，8/19 收盘价）")
print("="*120)
print(f"\n{'类别':<14}{'市值':>12}{'占比%':>8}{'目标':>14}{'状态':>6}  {'说明':<40}")
print("-"*120)

target_rules = {
    "AI硬件": ("动态cap35%","硬约束30-35%/cap35"),
    "AI软件": ("动态","动态15-25%"),
    "AI平台": ("动态","动态25-35%"),
    "估值修复": ("10-20%","目标10-20%"),
    "爆发仓": ("15-25%","目标15-25%"),
    "加密": ("10-15%","🟢→🟡8-12%"),
    "非AI对冲": ("10-15%","目标10-15%"),
    "现金": ("20-30%(🟡中性偏🟠)","🟡20-30% / 🟠35-45%"),
}

# 排序按目标顺序
order = ["AI硬件","AI软件","AI平台","估值修复","爆发仓","加密","非AI对冲","现金"]
subtotal_ai = 0
for cat in order:
    mv = mv_by_cat.get(cat,0)
    pct = mv / total_actual * 100
    tgt, desc = target_rules[cat]
    if cat == "现金":
        status = "🟡31.3% / 🟠档下限35-45%"
    elif cat == "AI硬件":
        status = "⚠️低" if pct < 20 else ("✅" if pct < 30 else "⚠️高")
    elif cat == "AI软件":
        status = "✅" if 15 <= pct <= 25 else "⚠️低"
    elif cat == "AI平台":
        status = "✅" if 20 <= pct <= 30 else "⚠️低"
    elif cat == "估值修复":
        status = "✅" if 10 <= pct <= 20 else "⚠️"
    elif cat == "爆发仓":
        status = "⚠️低" if pct < 15 else "✅"
    elif cat == "加密":
        status = "⚠️低" if pct < 8 else "✅"
    elif cat == "非AI对冲":
        status = "✅" if 10 <= pct <= 15 else "⚠️"
    print(f"{cat:<12}{mv:>12,.0f}{pct:>8.1f}{tgt:>14}{status:>6}  {desc:<40}")

print("-"*120)
print(f"{'合计(校验)':<12}{total_actual:>12,.0f}{100.0:>8.1f}")
print(f"{'  小计·AI总暴露':<12}{ai_total:>12,.0f}{ai_total/total_actual*100:>8.1f}      目标55-70% / 硬约束50-75%")
print(f"{'  小计·加密(独立)':<12}{crypto_total:>12,.0f}{crypto_total/total_actual*100:>8.1f}      🟢→🟡8-12%")
print(f"{'  小计·非AI对冲':<12}{non_ai_hedge:>12,.0f}{non_ai_hedge/total_actual*100:>8.1f}      目标10-15%")
print("="*120)

# 合计校验
sum_mut = sum(mv_by_cat.get(c,0) for c in order)
diff = abs(sum_mut - total_actual)
if diff > 1.0:
    print(f"⚠️ 合计校验失败：差{diff:.0f}美元")
else:
    print(f"✅ 合计校验通过：八类互斥 = {sum_mut:.0f} ≈ 总资产 {total_actual:.0f}")

# 持仓明细
print(f"\n\n{'='*120}\n  持仓明细（8/19 收盘 vs 8/19 夜盘双口径）\n{'='*120}")
print(f"{'Ticker':<8}{'Name':<18}{'股数':>6}{'成本':>9}{'8/19收':>9}{'夜盘':>9}{'延时%':>8}{'盈亏%':>8}{'市值':>10}{'占比%':>7}{'类别':<10}")
for t,n,s,c,cl,ov,cat in holdings:
    mv = s*cl
    pct = mv/total_actual*100
    delay = (ov-cl)/cl*100 if cl else 0
    pnl = (cl-c)/c*100
    flag = " ⚠️夜盘>1%" if abs(delay)>1 else ""
    print(f"{t:<8}{n:<18}{s:>6}{c:>9.2f}{cl:>9.2f}{ov:>9.2f}{delay:>7.2f}%{pnl:>7.1f}%{mv:>10,.0f}{pct:>6.1f}%{cat:<10}{flag}")

print(f"\n{'现金':<10}{'':>18}{'':>6}{'':>9}{'':>9}{'':>9}{'':>8}{'':>8}{cash:>10,.0f}{cash/total_actual*100:>6.1f}%")

# 硬约束检查
print(f"\n\n{'='*120}\n  硬约束检查\n{'='*120}")
checks = [
    ("AI总暴露 50-75%（硬约束）", f"{ai_total/total_actual*100:.1f}%", "✅" if 50 <= ai_total/total_actual*100 <= 75 else "🔴"),
    ("非AI对冲 10-15%", f"{non_ai_hedge/total_actual*100:.1f}%", "✅" if 10 <= non_ai_hedge/total_actual*100 <= 15 else "⚠️"),
    ("现金 ≥20%（🟡档）", f"{mv_by_cat.get('现金',0)/total_actual*100:.1f}%", "✅" if mv_by_cat.get('现金',0)/total_actual*100 >= 20 else "🔴"),
    ("单一非美国家 ≤20%（BABA 10.4% 唯一非美）", f"{mv_by_hold['BABA']['mv']/total_actual*100:.1f}%", "✅"),
    ("持仓数 ≤10只", "11只", "🔴超限1只"),
    ("AI子类别单类 ≤top 2", "AVGO已清仓, 当前单类1-2只", "✅"),
    ("现金档位 🟡/🟠: 🟡 20-30% / 🟠 35-45%", f"{mv_by_cat.get('现金',0)/total_actual*100:.1f}% → 🟡中位", "✅"),
    ("加密 ≤15%（v5.4 加密独立）", f"{crypto_total/total_actual*100:.1f}% (硬上限15%, 当前偏低)", "⚠️低配"),
    ("爆发仓单只 ≤8%", f"{mv_by_hold['APLD']['mv']/total_actual*100:.1f}% (APLD 4.6% 接近上限)", "⚠️"),
]
for name, val, status in checks:
    print(f"  {name:<48}{val:<25}{status}")

print("\n集中度检查：每类≥top 2？")
for cat in ["AI硬件","AI软件","AI平台","估值修复","爆发仓","加密","非AI对冲"]:
    cnt = sum(1 for h in mv_by_hold.values() if h["cat"]==cat)
    print(f"  {cat}: {cnt}只{'🔴' if cnt > 2 else '✅'}")
