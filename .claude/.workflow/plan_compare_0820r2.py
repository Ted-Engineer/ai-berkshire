#!/usr/bin/env python3
# ≤8只方案对比：调仓后分布+约束校验（盘前价口径）
P = {"BABA":(245,121.31,"AI平台"),"MSFT":(60,483.40,"AI软件"),"META":(53,547.29,"AI平台"),
"CRCL":(300,82.73,"加密"),"TSM":(50,410.07,"AI硬件"),"BRK.B":(30,500.25,"非AI对冲"),
"INTU":(40,361.56,"估值修复"),"APLD":(500,27.99,"爆发仓"),"ADBE":(50,273.32,"估值修复"),
"PYPL":(200,61.15,"非AI对冲"),"PGR":(30,217.30,"非AI对冲")}
COST={"BABA":121.69,"MSFT":333.194,"META":604.78,"CRCL":74.515,"TSM":417.08,"BRK.B":508.60,"INTU":319.49,"APLD":27.992,"ADBE":217.267,"PYPL":58.95,"PGR":209.6233}
CASH=83880.0
def eval_plan(name, cuts, baba_shares=245):
    total=0; cash=CASH; cats={}; hold=[]
    for t,(sh,px,cat) in P.items():
        if t in cuts:
            cash += sh*px; continue
        s = baba_shares if t=="BABA" else sh
        if t=="BABA" and baba_shares<245: cash += (245-baba_shares)*px
        mv=s*px; hold.append((t,s,mv,cat)); cats[cat]=cats.get(cat,0)+mv; total+=mv
    total+=cash
    ai=sum(cats.get(c,0) for c in ["AI硬件","AI软件","AI平台","估值修复","爆发仓"])
    hedge=cats.get("非AI对冲",0); crypto=cats.get("加密",0)
    pnl=sum((P[t][1]-COST[t])*P[t][0] for t in cuts)
    if baba_shares<245: pnl += (121.31-COST["BABA"])*(245-baba_shares)
    print(f"\n=== {name} ===")
    print(f"清仓: {', '.join(cuts)}" + (f" + BABA减至{baba_shares}股" if baba_shares<245 else "") + f" | 实现盈亏合计 ${pnl:+,.0f}")
    for t,s,mv,cat in sorted(hold,key=lambda x:-x[2]):
        risk_note=""
        print(f"  {t:6s} {s:5d}股 ${mv:10,.0f} {mv/total*100:5.1f}% {cat}")
    print(f"  现金   ${cash:10,.0f} {cash/total*100:5.1f}%  (🟠带35-45%)")
    print(f"  持仓数 {len(hold)}只 | 总资产 ${total:,.0f} 校验{'✅' if abs(total-292813.72)<1 else '⚠️'}")
    f=lambda v,lo,hi,nm: f"  {nm}: {v/total*100:.1f}% " + ("✅" if lo<=v/total*100<=hi else ("⚠️" if abs(v/total*100-(lo if v/total*100<lo else hi))<=5 else "🔴"))
    print(f(ai,50,75,"AI总暴露(硬50-75)")); print(f(hedge,10,15,"非AI对冲(硬10-15)")); print(f(crypto,0,15,"加密(cap15)")); print(f(cash,35,45,"现金(🟠35-45)"))
eval_plan("方案一·框架纪律：砍PYPL+CRCL+PGR，保META带双闸", ["PYPL","CRCL","PGR"])
eval_plan("方案一b：同上 + BABA减55股至190", ["PYPL","CRCL","PGR"], 190)
eval_plan("方案二·动量优先：砍PYPL+META+PGR，保CRCL带三闸", ["PYPL","META","PGR"])
eval_plan("方案二b：同上 + BABA减55股至190", ["PYPL","META","PGR"], 190)
eval_plan("方案三·纯公式：砍CRCL+BRK.B+META", ["CRCL","BRK.B","META"])
