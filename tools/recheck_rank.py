import json
# GAAP EPS (TTM, Yahoo v10, cross-checked vs SEC) and consensus EPS CAGR
# shrRed = CURRENT-PACE share reduction, from latest 10-Q diluted WAS YoY (SEC)
D = {
 'ADBE': dict(px=265.21, eps=18.19, cagr=0.126, shrRed=0.062, pe=14.58, bear=-0.189),
 'CRM' : dict(px=192.74, eps=9.80,  cagr=0.098, shrRed=0.102, pe=19.67, bear=-0.379),
 'INTU': dict(px=325.25, eps=16.76, cagr=0.148, shrRed=0.021, pe=19.41, bear=-0.414),
 'ACN' : dict(px=175.72, eps=12.73, cagr=0.059, shrRed=0.024, pe=13.80, bear=-0.30),
}
print('='*84)
print('2-YEAR MATH ON CURRENT-PACE BUYBACK (latest 10-Q YoY diluted WAS)')
print('='*84)
print(f"{'TK':5s} {'2yEPS':>7s} {'@flatPE':>9s} {'upside':>8s} {'PEfor+50%':>10s} {'reRate':>8s} {'bear':>7s} {'odds':>6s}")
rows=[]
for tk,d in D.items():
    # EPS grows by earnings CAGR, then per-share boost from share retirement
    eps2 = d['eps']*(1+d['cagr'])**2 / (1-d['shrRed'])**2
    flat = eps2*d['pe']
    up   = flat/d['px']-1
    need = d['px']*1.5/eps2
    rer  = need/d['pe']-1
    odds = abs(up/d['bear'])
    rows.append((tk,eps2,flat,up,need,rer,d['bear'],odds))
    print(f"{tk:5s} {eps2:7.2f} {flat:9.2f} {up:+7.1%} {need:10.1f}x {rer:+7.1%} {d['bear']:+6.1%} {odds:5.2f}x")

print()
print('='*84)
print('DOES IT CLEAR +50% WITH NO RE-RATING?')
print('='*84)
for tk,eps2,flat,up,need,rer,bear,odds in sorted(rows,key=lambda r:-r[3]):
    verdict = 'YES - self-funded' if up>=0.50 else f'NO - needs +{rer:.0%} re-rate'
    print(f"  {tk:5s} flat-multiple upside {up:+6.1%}   {verdict}")

print()
print('='*84)
print('RANK BY ODDS (upside / downside)')
print('='*84)
for tk,eps2,flat,up,need,rer,bear,odds in sorted(rows,key=lambda r:-r[7]):
    print(f"  {tk:5s} odds {odds:.2f}x   (up {up:+.1%} / bear {bear:+.1%})")
