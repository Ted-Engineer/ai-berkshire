import json

# Corrected period-matched TTM GAAP EPS (SEC XBRL, rigorous method)
D = {
 'ADBE': dict(px=265.21, eps=17.47, pe=15.2, shrYoY=-0.062, epsG=0.126, bear=-0.189),
 'CRM' : dict(px=192.74, eps=8.03,  pe=24.0, shrYoY=-0.102, epsG=0.098, bear=-0.379),
 'INTU': dict(px=325.25, eps=16.36, pe=19.9, shrYoY=-0.021, epsG=0.148, bear=-0.414),
 'ACN' : dict(px=175.72, eps=12.46, pe=14.1, shrYoY=-0.024, epsG=0.059, bear=-0.300),
}

print("="*100)
print("CORRECTED +50% MANDATE TEST  (period-matched TTM GAAP EPS, current-pace buyback)")
print("="*100)
print(f"{'TK':6s}{'px':>9s}{'ttmEPS':>8s}{'PE':>7s}{'2yEPS':>8s}{'@flatPE':>10s}{'upside':>9s}{'PEfor50':>9s}{'reRate':>9s}{'bear':>8s}{'odds':>7s}")
print("-"*100)
rows=[]
for tk,v in D.items():
    # 2yr EPS: earnings growth compounds, share count shrinks at current pace
    ni_g = (1+v['epsG'])**2          # net income proxy growth over 2yr
    shr  = (1+v['shrYoY'])**2        # share count after 2yr
    eps2 = v['eps'] * ni_g / shr
    flat = eps2 * v['pe']
    up   = flat/v['px']-1
    pe50 = v['px']*1.5/eps2
    rer  = pe50/v['pe']-1
    odds = (up if up>0 else 0)/abs(v['bear'])
    rows.append((tk,eps2,flat,up,pe50,rer,odds,v))
    print(f"{tk:6s}{v['px']:>9.2f}{v['eps']:>8.2f}{v['pe']:>7.1f}{eps2:>8.2f}{flat:>10.2f}{up*100:>8.1f}%{pe50:>9.1f}x{rer*100:>8.1f}%{v['bear']*100:>7.1f}%{odds:>7.2f}x")

print()
print("="*100)
print("CLEARS +50% AT UNCHANGED MULTIPLE?")
print("="*100)
for tk,eps2,flat,up,pe50,rer,odds,v in rows:
    verdict = "YES" if up>=0.50 else f"NO - needs +{rer*100:.0f}% re-rate"
    print(f"  {tk:5s} flat-multiple 2yr upside {up*100:+6.1f}%   {verdict}")

print()
print("="*100)
print("RANK BY ODDS (upside / bear downside)")
print("="*100)
for tk,eps2,flat,up,pe50,rer,odds,v in sorted(rows,key=lambda r:-r[6]):
    print(f"  {tk:5s} odds {odds:4.2f}x   up {up*100:+6.1f}%  bear {v['bear']*100:+6.1f}%  PE {v['pe']:.1f}x")
