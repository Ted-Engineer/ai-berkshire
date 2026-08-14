#!/usr/bin/env python
"""Fetch real-time quotes for the whole 512-candidate pool via fetch_quotes.py.
Writes data/candidates/quotes_20260810.json + a markdown table.
"""
import subprocess, json, os, time, re

tickers = [t.strip() for t in open('data/candidates/pool.txt') if t.strip()]
os.makedirs('data/candidates', exist_ok=True)

fetched = {}
errors = []
start = time.time()
for i in range(0, len(tickers), 6):
    batch = tickers[i:i+6]
    try:
        r = subprocess.run(['python', 'tools/fetch_quotes.py'] + batch,
                           capture_output=True, text=True, timeout=90)
        for line in r.stdout.split('\n'):
            m = re.match(r'^OK (\S+): (\S+)', line)
            if m:
                fetched[m.group(1)] = m.group(2)
        for line in r.stdout.split('\n'):
            m = re.match(r'^ERR (\S+)', line)
            if m:
                errors.append(m.group(1))
    except Exception as e:
        pass
    time.sleep(0.15)

json.dump({'date': '2026-08-10', 'fetched': fetched, 'errors': errors,
           'elapsed_sec': round(time.time()-start, 1)},
          open('data/candidates/quotes_20260810.json', 'w'), indent=1)

print(f'fetched {len(fetched)}/{len(tickers)} errors={len(errors)} elapsed={round(time.time()-start,1)}s')

# Merge with prior manually-fetched prices for holdings
manual = {'BABA':131.38,'MSFT':506.77,'ADBE':271.99,'CRM':196.24,'UBER':77.58,
          'INTU':331.31,'TSM':421.38,'QCOM':164.04,'TLN':344.34,'RARE':25.89,
          'CRCL':65.94,'BRK.B':529.41,'META':594.75,'GOOGL':354.79,'AXP':337.28,
          'NOC':579.22,'JPM':357.37,'FICO':1062.08,'LRCX':307.88,'GEV':995.13,
          'NVDA':217.27,'AMD':475.18,'AVGO':423.55,'MU':879.17,'MRVL':213.93,
          'CRDO':248.30,'LEU':191.56,'DOCS':25.89,'VST':143.77,'CEG':273.61,
          'VRT':273.46,'SMCI':31.92,'DELL':465.17,'ANET':190.78,'ORCL':149.68}
for t, p in manual.items():
    if t not in fetched:
        fetched[t] = str(p)

json.dump({'date': '2026-08-10', 'fetched': fetched, 'errors': errors},
          open('data/candidates/quotes_merged.json', 'w'), indent=1)
print('merged total:', len(fetched))