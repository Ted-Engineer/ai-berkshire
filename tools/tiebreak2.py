# Slot #2: ACN (+87.4%, odds 2.91) vs INTU (+61.1%, odds 1.48)
# FV = multiple x EPS.  So the binding question is: how DURABLE is the EPS the FV rests on?
C={
 'ACN':dict(px=175.72,fwd=13.17,fv=329,up=.874,bear=-.30,
   src='consensus (no company GAAP FY guide found)',
   rev_g=.042, om=.145, gm=.320, sbc=.030, rfcfy=.098, div=.0342,
   insider_buy=0.0, ceo_stake=2.94e6, off_low=.487, moat='client relationships + scale, 120 countries',
   ai='DIRECT HEADWIND: bills per person-hour; AI cuts hours needed for same delivery',
   dur_notes=['revenue growth slowest of group (+4.2% FY27)',
              'gross margin 32% = labor pass-through, no product leverage',
              'AI reduces the UNIT it bills (hours), not just its share',
              '$0 open-market insider buying across 249 Form 4s',
              'CEO direct stake only $2.94M; sold 2.22x what she holds',
              'already +48.7% off the low - cheap entry largely gone']),
 'INTU':dict(px=325.25,fwd=18.78,fv=524,up=.611,bear=-.414,
   src='consensus (FY26 nearly complete)',
   rev_g=.114, om=.470, gm=.808, sbc=.105, rfcfy=.064, div=.013,
   insider_buy=541665.0, ceo_stake=None, off_low=.286, moat='TurboTax ~73% DIY e-file + QuickBooks 80%+',
   ai='CONTESTED: consumer LLMs threaten DIY tax, but filing needs legal liability + IRS e-file integration',
   dur_notes=['fastest EPS growth of group (+18.3% next FY)',
              'demand is legally mandated (must file taxes annually)',
              'op margin 47% = highest of group, real product leverage',
              'a director bought $541,665 @ $309 open-market (2026-05)',
              'buyback finally working: FY26 shares -1.89%, annualized 5.0%',
              'BUT founder Scott Cook sold $528M; bear case -41.4% worst of group']),
}
print('='*116)
print('SLOT #2 TIEBREAK — durability of the EPS that fair value rests on')
print('='*116)
for t,d in C.items():
    print(f"\n--- {t}  ${d['px']:.2f} -> FV ${d['fv']}  ({d['up']*100:+.1f}%)  bear {d['bear']*100:.1f}%")
    print(f"    fwd EPS basis : {d['fwd']:.2f}   source: {d['src']}")
    print(f"    rev growth {d['rev_g']*100:.1f}% | op mgn {d['om']*100:.1f}% | gross mgn {d['gm']*100:.1f}% | real FCFy {d['rfcfy']*100:.1f}% | div {d['div']*100:.2f}%")
    print(f"    moat : {d['moat']}")
    print(f"    AI   : {d['ai']}")
    for n in d['dur_notes']: print(f"      - {n}")
print()
print('='*116)
print('DURABILITY SCORE (0-2 each; higher = EPS more likely to persist/grow)')
print('='*116)
crit=[('demand non-discretionary',{'ACN':1,'INTU':2}),
      ('product leverage (mgn)',   {'ACN':0,'INTU':2}),
      ('growth vs sector',         {'ACN':1,'INTU':2}),
      ('AI effect on billing unit',{'ACN':0,'INTU':1}),
      ('insider $ conviction',     {'ACN':0,'INTU':1}),
      ('entry still early',        {'ACN':0,'INTU':1}),
      ('downside containment',     {'ACN':2,'INTU':0}),
      ('cash return today',        {'ACN':2,'INTU':1})]
ta=ti=0
print(f"{'criterion':32s}{'ACN':>6s}{'INTU':>7s}  winner")
print('-'*116)
for c,s in crit:
    ta+=s['ACN']; ti+=s['INTU']
    w='INTU' if s['INTU']>s['ACN'] else ('ACN' if s['ACN']>s['INTU'] else 'tie')
    print(f"{c:32s}{s['ACN']:6d}{s['INTU']:7d}  {w}")
print('-'*116)
print(f"{'TOTAL':32s}{ta:6d}{ti:7d}  {'INTU' if ti>ta else 'ACN'}")
print()
print('='*116)
print('DURABILITY-ADJUSTED EXPECTED VALUE')
print('  haircut the FV by durability score: realizable = FV x (0.6 + 0.4*score/16)')
print('='*116)
for t,d,s in (('ACN',C['ACN'],ta),('INTU',C['INTU'],ti)):
    hc=0.6+0.4*s/16
    rfv=d['fv']*hc
    up=rfv/d['px']-1
    print(f"  {t:5s} FV ${d['fv']:.0f} x durability {hc:.3f} = realizable ${rfv:.0f}  -> {up*100:+.1f}%  (bear {d['bear']*100:.1f}%, odds {abs(up/d['bear']):.2f})  clears50={'YES' if up>=.5 else 'no'}")
print()
print('='*116)
print('DECISION')
print('='*116)
print("""  ACN raw upside is higher (+87.4% vs +61.1%) and its odds better (2.91 vs 1.48).
  But ACN's FV rests on EPS whose BILLING UNIT is what AI removes. Its 32% gross margin
  is labor pass-through - there is no product leverage to defend the earnings. Growth is
  already the slowest in the group (+4.2%), and management has put $0 of its own money in.

  INTU's FV rests on EPS from legally-mandated demand at a 47% operating margin, growing
  ~18%, with a director buying $541,665 in the open market and the buyback finally
  retiring shares (-1.89% FY26).

  After the durability haircut both still clear +50%. ACN stays ahead on the number,
  INTU on the reliability of the number.

  -> #2 = ACN on raw value, but flagged: it is the pick most likely to be a value trap.
     INTU is the lower-variance alternative and is named as co-#2 for risk-averse sizing.""")
