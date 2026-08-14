import json
# industry-relative gate: compare each to ITS OWN sector norms, not to software
D={
 'ADBE':dict(px=265.21,ttm=17.47,fy26=17.95,p25=28.9,om=.350,gm=.894,roic=.35,g=.075,sbc=.081,
   ind='software',ind_om=.25,ind_gm=.75,ind_g=.08,off=-.285,pct=3.5,bear=-.189,lev=.606,fcfy=.098,rfcfy=.078,div=0),
 'INTU':dict(px=325.25,ttm=16.36,fy26=18.78,p25=53.2,om=.470,gm=.808,roic=.20,g=.156,sbc=.105,
   ind='software',ind_om=.25,ind_gm=.75,ind_g=.08,off=-.567,pct=1.6,bear=-.414,lev=.467,fcfy=.087,rfcfy=.064,div=.013),
 'ACN':dict(px=175.72,ttm=12.46,fy26=13.17,p25=24.0,om=.145,gm=.320,roic=.22,g=.058,sbc=.030,
   ind='itservices',ind_om=.12,ind_gm=.30,ind_g=.05,off=-.396,pct=3.3,bear=-.300,lev=.523,fcfy=.117,rfcfy=.098,div=.0342),
 'CRM':dict(px=192.74,ttm=8.03,fy26=7.96,p25=41.7,om=.206,gm=.776,roic=.11,g=.021,sbc=.085,
   ind='software',ind_om=.25,ind_gm=.75,ind_g=.08,off=-.284,pct=0.0,bear=-.379,lev=.473,fcfy=.093,rfcfy=.070,div=.010),
}
# peer anchor the market sets TODAY: MSFT 27.9x GAAP w/ 45% om, 18% growth
MSFT=dict(pe=27.9,om=.45,g=.18)
print('='*118); print('INDUSTRY-RELATIVE QUALITY GATE (each vs its OWN sector, not vs software)'); print('='*118)
print(f"{'TK':6s}{'sector':12s}{'om vs ind':>12s}{'gm vs ind':>12s}{'g vs ind':>11s}{'ROIC':>7s}{'flags':>7s}  verdict")
print('-'*118)
for t,d in D.items():
    f=[]
    if d['om']<d['ind_om']*.8: f.append('om below sector')
    if d['gm']<d['ind_gm']*.8: f.append('gm below sector')
    if d['g']<d['ind_g']*.6: f.append('growth below sector')
    if d['roic']<.12: f.append('ROIC<12%')
    if d['sbc']>.12: f.append('SBC>12%')
    d['flags']=f
    v='clean' if not f else ('minor' if len(f)==1 else 'CONCERN')
    print(f"{t:6s}{d['ind']:12s}{d['om']/d['ind_om']:11.2f}x{d['gm']/d['ind_gm']:11.2f}x{d['g']/d['ind_g']:10.2f}x{d['roic']*100:6.0f}%{len(f):7d}  {v}"
          + (('  | '+'; '.join(f)) if f else ''))
print()
print('='*118); print('PEER ANCHOR the market sets TODAY: MSFT 27.9x GAAP (om 45%, g 18%)')
print('  a company with >= MSFT margins and >= half its growth cannot be worth far less than MSFT multiple'); print('='*118)
print(f"{'TK':6s}{'om':>7s}{'g':>7s}{'earns MSFT mult?':>19s}{'@27.9x on ttm':>16s}{'up%':>9s}")
print('-'*118)
for t,d in D.items():
    ok = d['om']>=MSFT['om']*.7 and d['g']>=MSFT['g']*.4
    tgt=27.9*d['ttm']
    print(f"{t:6s}{d['om']*100:6.1f}%{d['g']*100:6.1f}%{('YES' if ok else 'no'):>19s}{tgt:16.2f}{(tgt/d['px']-1)*100:8.1f}%")
print()
print('='*118); print('FINAL FAIR VALUE — median of 3 anchors, on FORWARD (next-FY) earnings')
print('  anchors: (1) own 5yr p25  (2) 25x cap  (3) MSFT peer 27.9x   -- median avoids cherry-picking'); print('='*118)
print(f"{'TK':6s}{'fwdEPS':>8s}{'@p25':>9s}{'@25x':>9s}{'@MSFT':>9s}{'MEDIAN':>9s}{'upside':>9s}{'bear':>8s}{'odds':>7s}  50%?")
print('-'*118)
res=[]
for t,d in D.items():
    a=[d['p25']*d['fy26'],25*d['fy26'],27.9*d['fy26']]
    a.sort(); med=a[1]
    up=med/d['px']-1
    odds=abs(up/d['bear'])
    res.append((t,d,med,up,odds))
    print(f"{t:6s}{d['fy26']:8.2f}{a[0]:9.0f}{a[1]:9.0f}{a[2]:9.0f}{med:9.0f}{up*100:8.1f}%{d['bear']*100:7.1f}%{odds:7.2f}  {'YES' if up>=.5 else 'no'}")
print()
print('='*118); print('SELECTION — must clear +50% AND have <=1 industry-relative flag'); print('='*118)
res.sort(key=lambda x:-x[3])
sel=[]
for t,d,med,up,odds in res:
    ok = up>=.5 and len(d['flags'])<=1
    tag='*** SELECT ***' if ok else 'reject'
    if ok: sel.append((t,d,med,up,odds))
    print(f"  {t:6s} FV ${med:6.0f}  upside {up*100:+6.1f}%  odds {odds:.2f}  flags {len(d['flags'])}  -> {tag}")
print()
print('='*118); print(f'FINAL 2 PICKS'); print('='*118)
for i,(t,d,med,up,odds) in enumerate(sel[:2],1):
    print(f"  #{i}  {t}  @ ${d['px']:.2f} -> FV ${med:.0f}  = {up*100:+.1f}%")
    print(f"      GAAP PE {d['px']/d['ttm']:.1f}x ({d['pct']:.1f} pctile of 5yr) | off high {d['off']*100:.1f}% | op margin {d['om']*100:.1f}%")
    print(f"      real FCF yield {d['rfcfy']*100:.1f}% | div {d['div']*100:.2f}% | bear {d['bear']*100:.1f}% | odds {odds:.2f}")
    print(f"      flags: {'none' if not d['flags'] else '; '.join(d['flags'])}")
json.dump([{'tk':t,'fv':med,'up':up,'odds':o} for t,d,med,up,o in res],open('data/final2.json','w'),indent=1)
