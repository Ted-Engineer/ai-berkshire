#!/usr/bin/env python
"""Print multi-year revenue/NI trend + analyst targets from scan json."""
import json, sys
f = sys.argv[1]
tks = sys.argv[2:]
d = json.load(open(f, encoding='utf-8'))
for tk in (tks or d.keys()):
    r = d.get(tk)
    if not r or 'error' in r:
        print(f'{tk}: no data'); continue
    print(f'\n=== {tk} {r.get("name")} ${r.get("price")} mcap=${(r.get("mcap") or 0)/1e9:.1f}B ===')
    print(f'  PE {r.get("pe_ttm")} fPE {r.get("pe_fwd")} PEG {r.get("peg")} PS {r.get("ps")} PB {r.get("pb")}')
    print(f'  EPS ttm {r.get("eps_ttm")} fwd {r.get("eps_fwd")} | shares {(r.get("shares") or 0)/1e6:.1f}M')
    print(f'  ROE {r.get("roe")} GM {r.get("gross_margin")} OM {r.get("oper_margin")} NM {r.get("profit_margin")}')
    print(f'  OCF ${(r.get("ocf") or 0)/1e9:.2f}B FCF ${(r.get("fcf") or 0)/1e9:.2f}B FCFyield {r.get("fcf_yield")}')
    print(f'  cash ${(r.get("cash") or 0)/1e9:.2f}B debt ${(r.get("debt") or 0)/1e9:.2f}B D/E {r.get("debt_to_equity")} curr {r.get("current_ratio")}')
    print(f'  52wH {r.get("52w_high")} 52wL {r.get("52w_low")} offHigh {r.get("pct_off_high")}')
    print(f'  target mean {r.get("target_mean")} high {r.get("target_high")} low {r.get("target_low")} recMean {r.get("rec_mean")} n={r.get("num_analysts")}')
    print(f'  earnings {r.get("earnings_date")} | inst {r.get("held_inst")} insider {r.get("held_insiders")} shortFloat {r.get("short_pct_float")}')
    ih = r.get('inc_hist') or []
    for row in ih:
        rev = row.get('rev'); ni = row.get('ni')
        print(f'   {row.get("d")}: rev ${rev/1e9:.2f}B  NI ${ni/1e9:.2f}B  margin {ni/rev*100:.1f}%' if rev and ni else f'   {row.get("d")}: partial')
