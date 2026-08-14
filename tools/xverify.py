#!/usr/bin/env python
"""Cross-verify key metrics from a 2nd source (stockanalysis.com)."""
import os,sys,json,re,time
os.environ['PYTHONHTTPSVERIFY']='0'
import urllib3; urllib3.disable_warnings()
import requests
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0 Safari/537.36'}
def get(tk):
    out={'ticker':tk}
    url=f'https://stockanalysis.com/stocks/{tk.lower()}/'
    try:
        r=requests.get(url,headers=UA,verify=False,timeout=25)
        if r.status_code!=200:
            out['err']=f'HTTP {r.status_code}'; return out
        h=r.text
        # stockanalysis embeds a JSON blob; fall back to regex on rendered table
        pats={
          'price':r'"price":\s*([\d.]+)',
          'marketCap':r'"marketCap":\s*(\d+)',
          'peRatio':r'"peRatio":\s*([\d.\-]+)',
          'forwardPE':r'"forwardPE":\s*([\d.\-]+)',
          'eps':r'"eps":\s*([\d.\-]+)',
          'revenue':r'"revenue":\s*(\d+)',
          'netIncome':r'"netIncome":\s*(-?\d+)',
          'sharesOut':r'"sharesOut":\s*(\d+)',
          'fcf':r'"fcf":\s*(-?\d+)',
          'roe':r'"roe":\s*([\d.\-]+)',
          'debt':r'"totalDebt":\s*(-?\d+)',
          'psRatio':r'"psRatio":\s*([\d.\-]+)',
          'pbRatio':r'"pbRatio":\s*([\d.\-]+)',
        }
        for k,p in pats.items():
            m=re.search(p,h)
            if m:
                try: out[k]=float(m.group(1))
                except: pass
    except Exception as e:
        out['err']=str(e)[:80]
    return out
res={}
for tk in sys.argv[1:]:
    r=get(tk); res[tk]=r
    if 'err' in r: print(f'{tk:6s} ERR {r["err"]}')
    else:
        mc=r.get('marketCap'); ni=r.get('netIncome'); sh=r.get('sharesOut'); eps=r.get('eps')
        print(f'{tk:6s} px={r.get("price")} mcap={mc/1e9 if mc else None} PE={r.get("peRatio")} '
              f'fPE={r.get("forwardPE")} eps={eps} NI={ni/1e9 if ni else None} sh={sh/1e6 if sh else None}M '
              f'ROE={r.get("roe")} FCF={r.get("fcf")/1e9 if r.get("fcf") else None}')
    time.sleep(0.8)
json.dump(res,open('data/xverify.json','w'),indent=1)
