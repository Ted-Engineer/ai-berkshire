#!/usr/bin/env python
"""Intrinsic value vs price. The mandate question: is price >=50% below defensible FV?
Method: (a) normalized-multiple on GAAP owner earnings, (b) reverse-DCF hurdle,
(c) FCF-yield-to-fair-yield. All GAAP, period-matched."""
from decimal import Decimal as D, getcontext
getcontext().prec=28

# session-verified, SEC XBRL period-matched TTM GAAP + company 8-K guidance
S={
 'ADBE':dict(px=265.21, ttm=17.47, fy_guide=17.95, g=.075, g_hi=.126,
    gm=.894, om=.350, roe=.630, shr=-.062, sbc_rev=.081,
    p25=28.9, med=36.7, lo5=12.3, pct=3.5, offhi=-.285),
 'INTU':dict(px=325.25, ttm=16.36, fy_guide=None, g=.148, g_hi=.183,
    gm=.808, om=.470, roe=.225, shr=-.021, sbc_rev=.105,
    p25=53.2, med=60.2, lo5=19.1, pct=1.6, offhi=-.567),
 'ACN':dict(px=175.72, ttm=12.46, fy_guide=None, g=.059, g_hi=.073,
    gm=.320, om=.145, roe=.244, shr=-.024, sbc_rev=.029,
    p25=24.0, med=28.2, lo5=10.2, pct=3.3, offhi=-.396),
 'CRM':dict(px=192.74, ttm=8.03, fy_guide=7.96, g=.021, g_hi=.098,
    gm=.776, om=.206, roe=.169, shr=-.102, sbc_rev=.085,
    p25=41.7, med=73.5, lo5=20.1, pct=0.0, offhi=-.284),
}

# market anchor: S&P500 forward PE ~20.1-21.5x (FactSet, 8-7). Use 20.1 as the
# multiple the AVERAGE US business commands. A franchise with >30% op margin and
# >20% ROE should not trade BELOW the market multiple absent impairment.
SPX_FWD=20.1

print('='*118)
print('QUESTION: is current price >=50% below a DEFENSIBLE fair value?')
print(f'Market anchor: S&P500 forward PE {SPX_FWD}x (FactSet 2026-08-07)')
print('='*118)
print(f"{'TK':6s}{'px':>9s}{'ttmEPS':>8s}{'PE':>6s}{'opMgn':>7s}{'ROE':>7s}  {'vs SPX':>8s} {'@SPX':>9s}{'up%':>8s}")
print('-'*118)
for tk,d in S.items():
    pe=D(str(d['px']))/D(str(d['ttm']))
    at_spx=D(str(SPX_FWD))*D(str(d['ttm']))
    up=(at_spx/D(str(d['px']))-1)*100
    disc=(pe/D(str(SPX_FWD))-1)*100
    print(f"{tk:6s}{d['px']:9.2f}{d['ttm']:8.2f}{float(pe):6.1f}{d['om']*100:6.1f}%{d['roe']*100:6.1f}%  {float(disc):+7.1f}% {float(at_spx):9.2f}{float(up):+8.1f}%")

print()
print('='*118)
print('FAIR-VALUE LADDER — what price does each multiple imply, and upside from today')
print('='*118)
print(f"{'TK':6s}{'basis EPS':>10s} | {'@SPX 20.1x':>22s} | {'@5yr p25':>22s} | {'@25x':>22s}")
print('-'*118)
for tk,d in S.items():
    e=D(str(d['fy_guide'] if d['fy_guide'] else d['ttm']))
    px=D(str(d['px']))
    def f(m):
        t=D(str(m))*e; return f"{float(t):8.2f} ({float((t/px-1)*100):+6.1f}%)"
    print(f"{tk:6s}{float(e):10.2f} | {f(SPX_FWD):>22s} | {f(d['p25']):>22s} | {f(25):>22s}")

print()
print('='*118)
print('2-YEAR TOTAL RETURN AT A *NORMALIZED* (not flat, not bubble) MULTIPLE')
print('  normalized = min(5yr p25, 25x) -- deliberately conservative: below own p25 AND capped at 25x')
print('='*118)
print(f"{'TK':6s}{'norm PE':>8s}{'2yEPS(g)':>10s}{'2yEPS(hi)':>10s} | {'target(g)':>18s} | {'target(hi)':>18s} | {'>=50%?':>8s}")
print('-'*118)
res={}
for tk,d in S.items():
    e=D(str(d['fy_guide'] if d['fy_guide'] else d['ttm']))
    px=D(str(d['px']))
    norm=min(D(str(d['p25'])),D('25'))
    sh=D('1')+D(str(d['shr']))
    e2=e*(D('1')+D(str(d['g'])))**2/sh**2
    e2h=e*(D('1')+D(str(d['g_hi'])))**2/sh**2
    t=norm*e2; th=norm*e2h
    u=(t/px-1)*100; uh=(th/px-1)*100
    ok='YES' if uh>=50 else 'no'
    res[tk]=(float(u),float(uh),float(norm),float(t),float(th))
    print(f"{tk:6s}{float(norm):8.1f}{float(e2):10.2f}{float(e2h):10.2f} | {float(t):9.2f} ({float(u):+6.1f}%) | {float(th):9.2f} ({float(uh):+6.1f}%) | {ok:>8s}")

print()
print('='*118)
print('REVERSE-DCF: what perpetual growth does TODAY\'S price already assume?')
print('  owner earnings = GAAP net income (SBC already expensed). discount 9%.')
print('='*118)
r=D('0.09')
for tk,d in S.items():
    e=D(str(d['ttm'])); px=D(str(d['px']))
    # px = e*(1+g)/(r-g)  ->  g = (px*r - e)/(px + e)
    g=(px*r-e)/(px+e)
    print(f"  {tk:6s} price implies perpetual growth of {float(g)*100:+6.2f}%   vs consensus near-term {d['g_hi']*100:+5.1f}%")
    if float(g)<0:
        print(f"         -> market is pricing PERMANENT DECLINE. any growth at all = upside.")

print()
print('='*118)
print('VERDICT')
print('='*118)
for tk,(u,uh,norm,t,th) in sorted(res.items(),key=lambda x:-x[1][1]):
    d=S[tk]
    print(f"  {tk:6s} FV ${t:.0f}-${th:.0f} at {norm:.0f}x  ->  upside {u:+.1f}% to {uh:+.1f}%   (PE now {d['px']/d['ttm']:.1f}x, {d['pct']} pctile, {d['offhi']*100:+.1f}% off high)")
