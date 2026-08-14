import os, json
os.environ['PYTHONHTTPSVERIFY']='0'
import urllib3; urllib3.disable_warnings()
import requests
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
S=requests.Session(); S.headers.update(UA)
S.get('https://fc.yahoo.com',verify=False,timeout=15)
cr=S.get('https://query2.finance.yahoo.com/v1/test/getcrumb',verify=False,timeout=15).text.strip()
out={}
for tk in ['ADBE','CRM','ACN','INTU']:
    u=f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{tk}?modules=insiderTransactions,netSharePurchaseActivity,majorHoldersBreakdown&crumb={cr}'
    r=S.get(u,verify=False,timeout=20)
    if r.status_code!=200:
        out[tk]={'err':r.status_code}; continue
    d=r.json()['quoteSummary']['result'][0]
    ns=d.get('netSharePurchaseActivity',{})
    mh=d.get('majorHoldersBreakdown',{})
    def g(o,k):
        v=o.get(k)
        return v.get('raw') if isinstance(v,dict) else v
    rec={
      'period':ns.get('period'),
      'buyInfoCount':g(ns,'buyInfoCount'),'buyInfoShares':g(ns,'buyInfoShares'),
      'sellInfoCount':g(ns,'sellInfoCount'),'sellInfoShares':g(ns,'sellInfoShares'),
      'netInfoCount':g(ns,'netInfoCount'),'netInfoShares':g(ns,'netInfoShares'),
      'insiderPct':g(mh,'insidersPercentHeld'),'instPct':g(mh,'institutionsPercentHeld'),
    }
    tr=[]
    for t in (d.get('insiderTransactions',{}).get('transactions') or [])[:14]:
        tr.append({'name':t.get('filerName'),'rel':t.get('filerRelation'),'txt':t.get('transactionText'),
                   'sh':g(t,'shares'),'val':g(t,'value'),'date':t.get('startDate',{}).get('fmt') if isinstance(t.get('startDate'),dict) else None})
    rec['recent']=tr
    out[tk]=rec
open('data/insider.json','w').write(json.dumps(out,indent=1))
for tk,v in out.items():
    if 'err' in v: print(tk,'ERR',v['err']); continue
    print(f"\n===== {tk}  insider%={v['insiderPct']}  inst%={v['instPct']}  period={v['period']}")
    print(f"  6mo net: buys={v['buyInfoCount']} ({v['buyInfoShares']} sh) | sells={v['sellInfoCount']} ({v['sellInfoShares']} sh) | net={v['netInfoShares']}")
    for t in v['recent'][:9]:
        print(f"   {t['date']}  {str(t['rel'])[:26]:26s} {str(t['txt'])[:34]:34s} sh={t['sh']} val={t['val']}")
