#!/usr/bin/env python
"""Bulk fetch stockanalysis.com stats/financials/cashflow for funnel screening."""
import re, html, json, time
import urllib3
import requests
urllib3.disable_warnings()

TICKERS = "CEG TLN NRG CCJ LEU GEV VRT ETN PWR HUBB POWL BELFB ENLT NRGV BE PLUG ET OKE ENB VST CAT AIT MYRG ROK ECL MMM".split()
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0'}

def txt(url):
    try:
        r = requests.get(url, verify=False, timeout=15, headers=H)
        t = re.sub(r'<script.*?</script>|<style.*?</style>', '', r.text, flags=re.S)
        t = re.sub(r'<[^>]+>', ' ', t)
        return html.unescape(re.sub(r'\s+', ' ', t))
    except Exception as e:
        return ''

def grab(t, kw, n=60):
    i = t.find(kw)
    if i < 0: return None
    return t[i:i+n].strip()

def num(s, idx=0):
    """extract idx-th float from string"""
    if not s: return None
    m = re.findall(r'-?\$?[\d,]+\.?\d*k?M?B?%?', s)
    vals = []
    for x in m:
        x = x.replace('$', '').replace(',', '')
        mult = 1
        if x.endswith('%'): x = x[:-1]
        try:
            vals.append(float(x))
        except: pass
    return vals[idx] if len(vals) > idx else None

out = {}
for tk in TICKERS:
    d = {}
    s = txt(f'https://stockanalysis.com/stocks/{tk.lower()}/statistics/')
    for key, kw in [('mcap','has a market cap or net worth of'),('pe','PE Ratio'),('fpe','Forward PE'),
                    ('ps','PS Ratio'),('roe','Return on Equity (ROE)'),('gm','Gross Margin'),
                    ('pm','Profit Margin'),('debt','Total Debt'),('equity','Equity (Book Value)'),
                    ('rev_fc','Revenue Growth Forecast (3Y)'),('ebitda_m','EBITDA Margin')]:
        seg = grab(s, kw, 80)
        if seg is None: d[key] = None; continue
        # for mcap use number right after phrase
        if key == 'mcap':
            m = re.search(r'net worth of \$([\d,.]+)\s*(trillion|billion|million)', seg)
            d[key] = m.group(0).replace('has a market cap or net worth of ','') if m else None
        elif key in ('pe','fpe','ps'):
            m = re.search(re.escape(kw)+r'\s+([\d.-]+)', seg)
            d[key] = m.group(1) if m else None
        elif key in ('roe','gm','pm','ebitda_m','rev_fc'):
            m = re.search(re.escape(kw)+r'\s*(-?[\d.]+)%', seg)
            d[key] = m.group(1)+'%' if m else None
        elif key == 'debt':
            m = re.search(r'Total Debt \$?([\d,.]+)([KMB]?)\s', seg)
            d[key] = m.group(0) if m else None
        elif key == 'equity':
            m = re.search(r'Equity \(Book Value\) \$?([\d,.]+)([KMB]?)', seg)
            d[key] = m.group(0) if m else None
    f = txt(f'https://stockanalysis.com/stocks/{tk.lower()}/financials/')
    seg = grab(f, 'Revenue Growth', 80)
    d['rev_ttm'] = num(seg, 0) if seg else None   # first num after "Revenue Growth" is TTM revenue
    d['rev_growth'] = num(seg, 6) if seg else None  # growth % is 6th number (rev x6 then growth x1)
    seg2 = grab(f, 'Net Income Net Income Growth', 60)
    d['ni_ttm'] = num(seg2, 0) if seg2 else None
    c = txt(f'https://stockanalysis.com/stocks/{tk.lower()}/financials/cash-flow-statement/')
    seg3 = grab(c, 'Operating Cash Flow', 40)
    d['ocf_ttm'] = num(seg3, 0) if seg3 else None
    out[tk] = d
    print(tk, json.dumps(d, ensure_ascii=False), flush=True)
    time.sleep(0.25)

with open('.claude/.workflow/tmpfin/bulk_fin.json', 'w') as fp:
    json.dump(out, fp, indent=1)
print('DONE')
