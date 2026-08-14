#!/usr/bin/env python
"""Print detailed finalist metrics from a scan JSON."""
import json, sys

path = sys.argv[1] if len(sys.argv) > 1 else 'data/finalist_detail.json'
d = json.load(open(path, encoding='utf-8'))


def n(v):
    try:
        f = float(v)
        if f != f or f in (float('inf'), float('-inf')):
            return None
        return f
    except (TypeError, ValueError):
        return None


rows = []
for tk, r in d.items():
    if 'error' in r:
        continue
    px = n(r.get('price'))
    hi = n(r.get('52w_high'))
    lo = n(r.get('52w_low'))
    tm = n(r.get('target_mean'))
    th = n(r.get('target_high'))
    fcf = n(r.get('fcf'))
    mc = n(r.get('mcap'))
    rows.append({
        'tk': tk,
        'px': px,
        'pe': n(r.get('pe_ttm')),
        'fpe': n(r.get('pe_fwd')),
        'peg': n(r.get('peg')),
        'ps': n(r.get('ps')),
        'pb': n(r.get('pb')),
        'roe': n(r.get('roe')),
        'gm': n(r.get('gross_margin')),
        'om': n(r.get('oper_margin')),
        'pm': n(r.get('profit_margin')),
        'de': n(r.get('debt_to_equity')),
        'cr': n(r.get('current_ratio')),
        'fcfy': (fcf / mc * 100) if (fcf and mc) else None,
        'ocfni': n(r.get('ocf_ni')),
        'revg': n(r.get('rev_growth')),
        'earng': n(r.get('earn_growth')),
        'tgt': tm,
        'tgt_up': ((tm / px - 1) * 100) if (tm and px) else None,
        'tgt_hi_up': ((th / px - 1) * 100) if (th and px) else None,
        'hi_rec': ((hi / px - 1) * 100) if (hi and px) else None,
        'lo_dn': ((lo / px - 1) * 100) if (lo and px) else None,
        'nan': n(r.get('num_analysts')),
        'rec': n(r.get('rec_mean')),
        'short': n(r.get('short_pct_float')),
        'inst': n(r.get('held_inst')),
        'ed': r.get('earnings_date'),
        'mcb': (mc / 1e9) if mc else None,
        'mcdiff': n(r.get('mcap_diff_pct')),
    })

rows.sort(key=lambda x: x['fpe'] if x['fpe'] else 999)


def f(v, d=1, suf=''):
    return f'{v:.{d}f}{suf}' if v is not None else '-'


print('=== VALUATION & QUALITY (price as of 2026-08-07 close) ===')
print(f'{"TK":6s}{"price":>9s}{"mcap$B":>8s}{"PE":>7s}{"fPE":>7s}{"PEG":>6s}{"PS":>7s}{"PB":>7s}{"ROE%":>8s}{"GM%":>7s}{"OM%":>7s}{"NM%":>7s}')
for r in rows:
    print(f'{r["tk"]:6s}{f(r["px"],2):>9s}{f(r["mcb"],1):>8s}{f(r["pe"]):>7s}{f(r["fpe"]):>7s}{f(r["peg"],2):>6s}'
          f'{f(r["ps"]):>7s}{f(r["pb"]):>7s}{f(r["roe"]*100 if r["roe"] else None):>8s}'
          f'{f(r["gm"]*100 if r["gm"] else None):>7s}{f(r["om"]*100 if r["om"] else None):>7s}{f(r["pm"]*100 if r["pm"] else None):>7s}')

print()
print('=== CASHFLOW / BALANCE / GROWTH ===')
print(f'{"TK":6s}{"FCFyld%":>9s}{"OCF/NI":>8s}{"D/E":>7s}{"CurRat":>8s}{"revG%":>8s}{"earnG%":>8s}{"mcapChk%":>9s}')
for r in rows:
    print(f'{r["tk"]:6s}{f(r["fcfy"],2):>9s}{f(r["ocfni"],2):>8s}{f(r["de"],0):>7s}{f(r["cr"],2):>8s}'
          f'{f(r["revg"]*100 if r["revg"] is not None else None):>8s}{f(r["earng"]*100 if r["earng"] is not None else None):>8s}'
          f'{f(r["mcdiff"],2):>9s}')

print()
print('=== UPSIDE / SENTIMENT ===')
print(f'{"TK":6s}{"tgtMean":>9s}{"tgtUp%":>8s}{"tgtHiUp%":>10s}{"to52wHi%":>10s}{"to52wLo%":>10s}{"nAnl":>6s}{"recMean":>9s}{"short%":>8s}{"inst%":>7s}{"nextER":>12s}')
for r in rows:
    print(f'{r["tk"]:6s}{f(r["tgt"],2):>9s}{f(r["tgt_up"]):>8s}{f(r["tgt_hi_up"]):>10s}{f(r["hi_rec"]):>10s}'
          f'{f(r["lo_dn"]):>10s}{f(r["nan"],0):>6s}{f(r["rec"],2):>9s}'
          f'{f(r["short"]*100 if r["short"] else None):>8s}{f(r["inst"]*100 if r["inst"] else None):>7s}{str(r["ed"] or "-"):>12s}')
