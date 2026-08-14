# Portfolio recompute with REAL 2026-08-07 closes (from this session's scan)
px = {'BABA':128.41,'MSFT':499.99,'ADBE':265.21,'BRK-B':521.80,'INTU':325.25,
      'QCOM':167.86,'TSM':420.04,'TLN':347.71,'RARE':25.91,'CRCL':66.67}
hold = {'BABA':845,'MSFT':125.5,'ADBE':90,'BRK-B':30,'INTU':40,
        'QCOM':35,'TSM':15,'TLN':15,'RARE':200,'CRCL':20}
stated = {'BABA':107315,'MSFT':60868,'ADBE':22500,'BRK-B':15450,'INTU':13440,
          'QCOM':5600,'TSM':6240,'TLN':5025,'RARE':5000,'CRCL':1220}
CASH = 35811

print("="*84)
print("PORTFOLIO RECOMPUTED AT REAL 2026-08-07 CLOSES (vs file's 8/6 estimates)")
print("="*84)
print(f"{'TK':8s}{'sh':>8s}{'realPx':>10s}{'realVal':>12s}{'statedVal':>12s}{'diff$':>10s}{'diff%':>8s}")
tot=0
for t,s in hold.items():
    v = px[t]*s; tot += v
    d = v - stated[t]; dp = d/stated[t]*100
    print(f"{t:8s}{s:>8.1f}{px[t]:>10.2f}{v:>12,.0f}{stated[t]:>12,.0f}{d:>+10,.0f}{dp:>+7.1f}%")
TOT = tot + CASH
print(f"{'CASH':8s}{'':>8s}{'':>10s}{CASH:>12,.0f}{CASH:>12,.0f}")
print(f"{'TOTAL':8s}{'':>8s}{'':>10s}{TOT:>12,.0f}{278468:>12,.0f}{TOT-278468:>+10,.0f}{(TOT-278468)/278468*100:>+7.1f}%")

print("\n" + "="*84)
print("ACTUAL WEIGHTS")
print("="*84)
rows=[(t,px[t]*hold[t]) for t in hold]
rows.sort(key=lambda x:-x[1])
for t,v in rows:
    print(f"  {t:8s} {v:>10,.0f}  {v/TOT*100:>5.1f}%")
print(f"  {'CASH':8s} {CASH:>10,.0f}  {CASH/TOT*100:>5.1f}%")

# Sector buckets
print("\n" + "="*84)
print("CONCENTRATION / DIVERSIFICATION")
print("="*84)
buckets = {
 'China tech (BABA)':['BABA'],
 'US enterprise software (MSFT/ADBE/INTU)':['MSFT','ADBE','INTU'],
 'Semis+hardware (TSM/QCOM)':['TSM','QCOM'],
 'Power (TLN)':['TLN'],
 'Defensive (BRK-B)':['BRK-B'],
 'Speculative (RARE/CRCL)':['RARE','CRCL'],
}
for k,ts in buckets.items():
    v=sum(px[t]*hold[t] for t in ts)
    print(f"  {k:44s} {v:>10,.0f}  {v/TOT*100:>5.1f}%")
print(f"  {'Cash':44s} {CASH:>10,.0f}  {CASH/TOT*100:>5.1f}%")

print("\n" + "="*84)
print("PROPOSED ADDITIONS: ADBE (add) + CRM (new)")
print("="*84)
adbe_now = px['ADBE']*hold['ADBE']
print(f"ADBE currently {adbe_now:,.0f} = {adbe_now/TOT*100:.1f}%")
for tgt in (0.10,0.12,0.15):
    want = TOT*tgt; add = want-adbe_now; sh = add/px['ADBE']
    print(f"  -> to {tgt*100:.0f}%: add ${add:>8,.0f} = {sh:>5.0f} sh  (total {hold['ADBE']+sh:.0f} sh)")
print(f"\nCRM new position @ ${192.74}")
for tgt in (0.03,0.04,0.05):
    want = TOT*tgt; sh = want/192.74
    print(f"  -> {tgt*100:.0f}%: ${want:>8,.0f} = {sh:>5.0f} sh")

print("\n" + "="*84)
print("SOFTWARE CONCENTRATION AFTER ADDS")
print("="*84)
sw_now = sum(px[t]*hold[t] for t in ['MSFT','ADBE','INTU'])
print(f"  now (MSFT+ADBE+INTU)                     {sw_now:>10,.0f}  {sw_now/TOT*100:>5.1f}%")
add_adbe = TOT*0.12 - adbe_now
add_crm  = TOT*0.04
sw_after = sw_now + add_adbe + add_crm
print(f"  after ADBE->12% + CRM 4%                 {sw_after:>10,.0f}  {sw_after/TOT*100:>5.1f}%")
print(f"  cash after both adds                     {CASH-add_adbe-add_crm:>10,.0f}  {(CASH-add_adbe-add_crm)/TOT*100:>5.1f}%")
print(f"\n  NOTE: funding both from cash alone leaves {(CASH-add_adbe-add_crm)/TOT*100:.1f}% cash.")
print(f"  BABA at {px['BABA']*hold['BABA']/TOT*100:.1f}% remains the dominant risk, unrelated to these adds.")
