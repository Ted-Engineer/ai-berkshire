#!/usr/bin/env python
"""Batch fetch close + extended-hours prices from CNBC quote API."""
import json, sys, time, urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
TICKERS = sys.argv[1].split(',')

def fetch(tk):
    url = (f"https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol"
           f"?symbols={tk}&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15) as r:
        d = json.load(r)
    q = d['FormattedQuoteResult']['FormattedQuote'][0]
    ext = q.get('ExtendedMktQuote') or {}
    return {
        'close': q.get('last'),
        'close_time': q.get('last_time'),
        'mkt_status': q.get('curmktstatus'),
        'ext_type': ext.get('type'),
        'ext_last': ext.get('last'),
        'ext_change_pct': ext.get('change_pct'),
        'prev_close': q.get('previous_day_closing'),
        'mktcap': q.get('mktcapView'),
        'pe': q.get('pe'),
        '52w_high': q.get('high_52week') or q.get('fiftyTwoWeekHigh'),
        '52w_low': q.get('low_52week') or q.get('fiftyTwoWeekLow'),
    }

out = {}
for tk in TICKERS:
    try:
        out[tk] = fetch(tk)
        print(f"OK {tk}", file=sys.stderr)
    except Exception as e:
        out[tk] = {'error': str(e)[:120]}
        print(f"ERR {tk}: {str(e)[:80]}", file=sys.stderr)
    time.sleep(0.5)

print(json.dumps(out, indent=1))
