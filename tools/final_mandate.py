#!/usr/bin/env python
"""Final mandate test on COMPANY GAAP GUIDANCE (apples-to-apples).
All three finalists tested on the same standard used to disqualify CRM."""
from decimal import Decimal as D

def pct(x): return f'{x*100:+.1f}%'

# ---- verified primary-source inputs ----
# ADBE: 8-K 2026-06-11 exh99.1  FY26 GAAP EPS guide 17.90-18.00, shares 399M
#       FY25 actual GAAP EPS 16.70 (SEC XBRL)
#       FY26 GAAP op margin guide 35.0% vs FY25 actual 36.6%
# CRM : 8-K 2026-05-27 exh99.1  FY27 GAAP EPS guide 7.93-7.99
#       FY26 actual GAAP EPS 7.80 (SEC XBRL)
# INTU: FY25 actual GAAP EPS 13.67 (SEC XBRL); TTM GAAP EPS 16.36 (period-matched)
#       consensus rev growth +13.5% next FY

NAMES = {
 'ADBE': dict(px=265.21, fy_guide_eps=17.95, fy_prior_eps=16.70,
              ttm_eps=17.47, shr_yoy=-0.062, revg=0.116,
              pe_pctile=3.5, off_hi=-0.285, bear=-0.189,
              guide_src='8-K 2026-06-11 FY26 GAAP $17.90-18.00'),
 'INTU': dict(px=325.25, fy_guide_eps=None, fy_prior_eps=13.67,
              ttm_eps=16.36, shr_yoy=-0.021, revg=0.135,
              pe_pctile=1.6, off_hi=-0.567, bear=-0.414,
              guide_src='no GAAP FY guide located; using TTM + consensus rev'),
 'CRM':  dict(px=192.74, fy_guide_eps=7.96, fy_prior_eps=7.80,
              ttm_eps=8.03, shr_yoy=-0.102, revg=0.110,
              pe_pctile=0.0, off_hi=-0.284, bear=-0.379,
              guide_src='8-K 2026-05-27 FY27 GAAP $7.93-7.99'),
 'ACN':  dict(px=175.72, fy_guide_eps=None, fy_prior_eps=12.15,
              ttm_eps=12.46, shr_yoy=-0.024, revg=0.056,
              pe_pctile=3.3, off_hi=-0.396, bear=-0.300,
              guide_src='no GAAP FY guide located; consensus rev +5.6%'),
}

print('='*118)
print('FINAL MANDATE TEST — COMPANY GAAP GUIDANCE BASIS (same standard for all four)')
print('='*118)
print(f'{"TK":6s}{"px":>9s}{"ttmEPS":>8s}{"PE":>6s}{"guideG":>8s}'
      f'{"implG":>7s}{"2yEPS_g":>9s}{"up@flat":>9s}{"PE50":>7s}{"reRate":>8s}{"bear":>8s}{"odds":>7s}')
print('-'*118)

rows=[]
for tk,d in NAMES.items():
    px=d['px']; ttm=d['ttm_eps']; pe=px/ttm
    # growth on company guidance where available
    if d['fy_guide_eps']:
        gg=d['fy_guide_eps']/d['fy_prior_eps']-1
    else:
        gg=None
    # implied sustainable GAAP EPS growth = revenue growth + buyback shrink (margin flat)
    implg = d['revg'] + (-d['shr_yoy'])
    # conservative: use guidance growth if we have it, else implied
    use_g = gg if gg is not None else implg
    eps2 = ttm*(1+use_g)**2
    tgt  = eps2*pe
    up   = tgt/px-1
    need = px*1.5/eps2
    rr   = need/pe-1
    odds = (up/abs(d['bear'])) if d['bear'] else None
    rows.append((tk,px,ttm,pe,gg,implg,eps2,up,need,rr,d['bear'],odds,d))
    print(f'{tk:6s}{px:9.2f}{ttm:8.2f}{pe:6.1f}'
          f'{(pct(gg) if gg is not None else "n/a"):>8s}'
          f'{pct(implg):>7s}{eps2:9.2f}{pct(up):>9s}{need:7.1f}x{pct(rr):>8s}'
          f'{pct(d["bear"]):>8s}{odds:7.2f}x')

print()
print('='*118)
print('SENSITIVITY: if margins hold and EPS grows at revenue+buyback pace instead of guidance pace')
print('='*118)
for tk,px,ttm,pe,gg,implg,_,_,_,_,bear,_,d in rows:
    eps2b = ttm*(1+implg)**2
    upb   = eps2b*pe/px-1
    needb = px*1.5/eps2b
    rrb   = needb/pe-1
    print(f'  {tk:6s} implied g {pct(implg):>7s}  2yEPS {eps2b:6.2f}  '
          f'up@flat {pct(upb):>8s}  PE for +50% {needb:5.1f}x ({pct(rrb)} re-rate)  odds {upb/abs(bear):4.2f}x')

print()
print('='*118)
print('VERDICT — who can reach +50% and how')
print('='*118)
for tk,px,ttm,pe,gg,implg,_,_,_,_,bear,_,d in rows:
    eps2g = ttm*(1+(gg if gg is not None else implg))**2
    eps2i = ttm*(1+implg)**2
    rr_g  = (px*1.5/eps2g)/pe-1
    rr_i  = (px*1.5/eps2i)/pe-1
    lo,hi = sorted([rr_g,rr_i])
    verdict = 'PLAUSIBLE' if lo<=0.20 else ('STRETCH' if lo<=0.35 else 'FAIL')
    print(f'  {tk:6s} needs {pct(lo)} to {pct(hi)} re-rate   PE now {pe:5.1f}x '
          f'at {d["pe_pctile"]:4.1f} pctile of 5yr   off high {pct(d["off_hi"])}   -> {verdict}')

print()
print('='*118)
print('NOTE ON METHOD')
print('='*118)
print('  Guidance basis is the honest test: company GAAP guidance already embeds buyback,')
print('  so layering buyback on top of consensus non-GAAP growth double-counts it.')
print('  That double-count is exactly what inflated my earlier CRM +49.5% figure.')
for tk,d in NAMES.items():
    print(f'    {tk:6s} {d["guide_src"]}')
