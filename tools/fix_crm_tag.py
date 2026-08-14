import os,json
os.environ['PYTHONHTTPSVERIFY']='0'
import urllib3; urllib3.disable_warnings()
import requests
S=requests.Session(); S.headers.update({'User-Agent':'AI-Berkshire Research research@example.com'})
def facts(c):
    r=S.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json',verify=False,timeout=60)
    return r.json() if r.status_code==200 else None
def days(a,b):
    from datetime import date
    y1,m1,d1=map(int,a.split('-')); y2,m2,d2=map(int,b.split('-'))
    return (date(y2,m2,d2)-date(y1,m1,d1)).days

f=facts('0001108524')
print('='*90)
print('CRM revenue — ALL candidate XBRL tags, latest annual each')
print('='*90)
for tag in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax',
            'RevenueFromContractWithCustomerIncludingAssessedTax']:
    n=f['facts'].get('us-gaap',{}).get(tag,{}).get('units',{}).get('USD',[])
    best=None
    for e in n:
        s,en=e.get('start'),e.get('end')
        if not s or not en: continue
        if 350<=days(s,en)<=380:
            if best is None or en>best[0]: best=(en,e.get('val'))
    if best:
        print(f'  {tag:52s} {best[0]}  ${best[1]/1e9:7.3f}B')
    else:
        print(f'  {tag:52s} not present')

print()
print('='*90)
print('ADBE liabilities/assets — FY-end vs latest quarter (both are true, dates differ)')
print('='*90)
fa=facts('0000796343')
def instants(ff,tag):
    out=[]
    for e in ff['facts']['us-gaap'][tag]['units']['USD']:
        if e.get('start') or not e.get('end'): continue
        out.append((e['end'],e['val']))
    return sorted(set(out),reverse=True)
L=dict(instants(fa,'Liabilities')); A=dict(instants(fa,'Assets'))
for d in sorted(set(L)&set(A),reverse=True)[:4]:
    print(f'  {d}   L ${L[d]/1e9:7.2f}B / A ${A[d]/1e9:7.2f}B = {L[d]/A[d]*100:5.1f}%')
