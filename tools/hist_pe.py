import os, json, sys
os.environ['PYTHONHTTPSVERIFY']='0'
import urllib3; urllib3.disable_warnings()
import requests
from datetime import datetime, timezone

UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
S=requests.Session(); S.headers.update(UA)

# GAAP diluted EPS by fiscal year end (from SEC EDGAR, verified)
EPS={
 'ADBE':{'2021-12-03':10.02,'2022-12-02':10.10,'2023-12-01':11.82,'2024-11-29':12.36,'2025-11-28':16.70},
 'CRM' :{'2022-01-31':1.48,'2023-01-31':0.21,'2024-01-31':4.20,'2025-01-31':6.36,'2026-01-31':7.80},
 'ACN' :{'2021-08-31':9.16,'2022-08-31':10.71,'2023-08-31':10.77,'2024-08-31':11.44,'2025-08-31':12.15},
 'INTU':{'2021-07-31':7.56,'2022-07-31':7.28,'2023-07-31':8.42,'2024-07-31':10.43,'2025-07-31':13.67},
}
CUR={'ADBE':(265.21,18.19),'CRM':(192.74,9.80),'ACN':(175.72,12.73),'INTU':(325.25,16.76)}

out=[]
for tk,eps_map in EPS.items():
    url=f'https://query1.finance.yahoo.com/v8/finance/chart/{tk}?interval=1mo&range=6y'
    try:
        r=S.get(url,verify=False,timeout=20)
        d=r.json()['chart']['result'][0]
        ts=d['timestamp']; close=d['indicators']['quote'][0]['close']
    except Exception as e:
        out.append(f'{tk}: fetch err {e}'); continue
    # for each month, find the most recent fiscal-year EPS available
    fy=sorted(eps_map.items())
    pes=[]
    for t,c in zip(ts,close):
        if c is None: continue
        dt=datetime.fromtimestamp(t,timezone.utc).strftime('%Y-%m-%d')
        eps=None
        for fend,e in fy:
            if fend<=dt: eps=e
        if eps and eps>0:
            pes.append((dt,c/eps))
    if not pes: continue
    vals=[p for _,p in pes]
    vals_s=sorted(vals)
    n=len(vals_s)
    def pct(q): return vals_s[min(n-1,int(q*n))]
    cp,ce=CUR[tk]
    cur_pe=cp/ce
    # percentile rank of current
    rank=sum(1 for v in vals_s if v<cur_pe)/n
    out.append(f'{tk:5s} 5yGAAP-PE  min={min(vals):5.1f}  p25={pct(.25):5.1f}  median={pct(.5):5.1f}  p75={pct(.75):5.1f}  max={max(vals):6.1f}  |  NOW={cur_pe:5.1f}  pctile={rank*100:4.1f}%')
    # what price at median / p25
    out.append(f'      -> at median PE {pct(.5):.1f}: ${pct(.5)*ce:7.2f} ({(pct(.5)*ce/cp-1)*100:+6.1f}%)   at p25 PE {pct(.25):.1f}: ${pct(.25)*ce:7.2f} ({(pct(.25)*ce/cp-1)*100:+6.1f}%)')
open('data/hist_pe.txt','w').write('\n'.join(out))
