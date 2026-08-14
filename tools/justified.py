import json
# justified PE from fundamentals (no reliance on bubble-era history)
# Gordon: P/E = payout_equiv / (r - g), payout_equiv = 1 - g/ROIC
# use r = 9% equity cost, g = sustainable growth (conservative), ROIC proxy
D = {
 'ADBE': dict(px=265.21, ttm=17.47, guide=17.95, om=.350, gm=.894, roe=.630, roic=.35,
              g_near=.075, g_sust=.045, p25=28.9, med=36.7, sbc=.081, off=-.285, fcfy=.078),
 'INTU': dict(px=325.25, ttm=16.36, guide=None, om=.470, gm=.808, roe=.225, roic=.20,
              g_near=.156, g_sust=.045, p25=53.2, med=60.2, sbc=.105, off=-.567, fcfy=.064),
 'ACN' : dict(px=175.72, ttm=12.46, guide=None, om=.145, gm=.320, roe=.244, roic=.22,
              g_near=.058, g_sust=.035, p25=24.0, med=28.2, sbc=.030, off=-.396, fcfy=.098),
 'CRM' : dict(px=192.74, ttm=8.03,  guide=7.96, om=.206, gm=.776, roe=.169, roic=.11,
              g_near=.021, g_sust=.045, p25=41.7, med=73.5, sbc=.085, off=-.284, fcfy=.070),
}
r=0.09
print('='*118)
print('JUSTIFIED PE FROM FUNDAMENTALS (Gordon growth, r=9%) — no bubble-era history used')
print('  justified PE = (1 - g/ROIC) / (r - g),  g capped at 4.5% (long-run GDP+inflation)')
print('='*118)
print(f"{'TK':6s}{'g_sust':>8s}{'ROIC':>7s}{'reinvest':>10s}{'justPE':>8s}{'curPE':>7s}{'FV@just':>10s}{'up%':>9s}{'own p25':>9s}")
print('-'*118)
res={}
for tk,d in D.items():
    g=d['g_sust']; roic=d['roic']
    reinv=g/roic
    just=(1-reinv)/(r-g)
    cur=d['px']/d['ttm']
    fv=just*d['ttm']
    up=fv/d['px']-1
    res[tk]=dict(just=just,fv=fv,up=up,cur=cur)
    print(f"{tk:6s}{g*100:7.1f}%{roic*100:6.0f}%{reinv*100:9.0f}%{just:8.1f}{cur:7.1f}{fv:10.2f}{up*100:8.1f}%{d['p25']:9.1f}")

print()
print('='*118)
print('STRICT TEST — 50%+ upside on TODAY earnings (no forward growth credit)')
print('  three independent fair-value anchors, take the MEDIAN to avoid cherry-picking')
print('='*118)
print(f"{'TK':6s}{'@justified':>12s}{'@own p25':>11s}{'@25x cap':>10s}{'MEDIAN FV':>11s}{'upside':>9s}{'clears 50%':>12s}")
print('-'*118)
rank=[]
for tk,d in D.items():
    a=res[tk]['fv']
    b=min(d['p25'],40)*d['ttm']
    c=25*d['ttm']
    vals=sorted([a,b,c]); med=vals[1]
    up=med/d['px']-1
    rank.append((up,tk,med,a,b,c))
    print(f"{tk:6s}{a:12.0f}{b:11.0f}{c:10.0f}{med:11.0f}{up*100:8.1f}%{('YES' if up>=.50 else 'no'):>12s}")

print()
print('='*118)
print('QUALITY GATE — is the low multiple JUSTIFIED (value trap) or NOT (mispricing)?')
print('='*118)
for tk,d in D.items():
    # a low multiple is justified if margins are thin AND growth is low AND the model is threatened
    flags=[]
    if d['om']<.20: flags.append('thin op margin')
    if d['g_near']<.06: flags.append('growth <6%')
    if d['gm']<.50: flags.append('low gross margin (labor model)')
    if d['sbc']>.10: flags.append('SBC >10% of rev')
    verdict='TRAP RISK HIGH' if len(flags)>=2 else ('clean' if not flags else 'minor')
    print(f"  {tk:6s} om={d['om']*100:4.1f}%  gm={d['gm']*100:4.1f}%  g={d['g_near']*100:4.1f}%  SBC={d['sbc']*100:4.1f}%  -> {verdict}")
    if flags: print(f"         flags: {', '.join(flags)}")

print()
print('='*118)
print('FINAL 2 — clears 50% on today earnings AND passes quality gate')
print('='*118)
rank.sort(reverse=True)
for up,tk,med,a,b,c in rank:
    d=D[tk]
    flags=sum([d['om']<.20, d['g_near']<.06, d['gm']<.50, d['sbc']>.10])
    ok = up>=.50 and flags<2
    print(f"  {tk:6s} median FV ${med:,.0f}  upside {up*100:+.1f}%  qualityflags={flags}  -> {'*** SELECT ***' if ok else 'reject'}")
