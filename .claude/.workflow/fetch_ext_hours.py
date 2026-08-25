#!/usr/bin/env python
"""Fetch extended-hours prices via Yahoo v10 quoteSummary price module (requests, SSL verify off)."""
import os, sys, json, time, datetime
os.environ['PYTHONHTTPSVERIFY'] = '0'
import urllib3
urllib3.disable_warnings()
import requests

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'}
TICKERS = sys.argv[1].split(',')

def et(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone(datetime.timedelta(hours=-4))).strftime('%m-%d %H:%M ET')

out = {}
for tk in TICKERS:
    try:
        url = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{tk}?modules=price'
        r = requests.get(url, verify=False, timeout=12, headers=UA)
        if r.status_code != 200:
            out[tk] = {'error': f'HTTP {r.status_code}'}
            print(f'ERR {tk} HTTP {r.status_code}', file=sys.stderr)
            continue
        p = r.json()['quoteSummary']['result'][0]['price']
        rec = {}
        for k in ['regularMarketPrice','regularMarketTime','regularMarketChangePercent',
                  'preMarketPrice','preMarketTime','preMarketChangePercent',
                  'postMarketPrice','postMarketTime','postMarketChangePercent',
                  'marketState','fiftyTwoWeekHigh','fiftyTwoWeekLow','marketCap']:
            v = p.get(k)
            rec[k] = v.get('raw') if isinstance(v, dict) else v
        out[tk] = rec
        print(f'OK {tk}', file=sys.stderr)
    except Exception as e:
        out[tk] = {'error': str(e)[:120]}
        print(f'ERR {tk}: {str(e)[:80]}', file=sys.stderr)
    time.sleep(0.4)

print(json.dumps(out, indent=1))
