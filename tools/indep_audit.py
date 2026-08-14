#!/usr/bin/env python
"""GENUINELY independent audit: fetch each claim from SEC fresh, compare to report text.
No echoing reported_value into fetched_value."""
import os,io,json,re,sys
os.environ['PYTHONHTTPSVERIFY']='0'
import urllib3; urllib3.disable_warnings()
import requests
S=requests.Session(); S.headers.update({'User-Agent':'AI-Berkshire Research research@example.com'})

CIK={'ADBE':'0000796343','INTU':'0000896878','ACN':'0001467373','CRM':'0001108524'}
def facts(c):
    r=S.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json',verify=False,timeout=60)
    return r.json() if r.status_code==200 else None
def units(f,tag):
    for t in ('us-gaap','dei'):
        n=f.get('facts',{}).get(t,{}).get(tag,{}).get('units',{})
        for u in ('USD','USD/shares','shares'):
            if u in n: return n[u]
    return []
def days(a,b):
    from datetime import date
    y1,m1,d1=map(int,a.split('-')); y2,m2,d2=map(int,b.split('-'))
    return (date(y2,m2,d2)-date(y1,m1,d1)).days
def latest_annual(f,tag):
    best=None
    for e in units(f,tag):
        s,en=e.get('start'),e.get('end')
        if not s or not en: continue
        if 350<=days(s,en)<=380:
            if best is None or en>best[0]: best=(en,e.get('val'))
    return best

F={k:facts(v) for k,v in CIK.items()}

# claims to verify INDEPENDENTLY from SEC
CLAIMS=[
 ('ADBE FY25 revenue',    'ADBE','Revenues',                 23.77, 1e9),
 ('ADBE FY25 net income', 'ADBE','NetIncomeLoss',             7.13, 1e9),
 ('ADBE FY25 diluted EPS','ADBE','EarningsPerShareDiluted',  16.70, 1),
 ('ADBE FY25 SBC',        'ADBE','ShareBasedCompensation',    1.94, 1e9),
 ('ADBE FY25 buyback',    'ADBE','PaymentsForRepurchaseOfCommonStock', 11.28, 1e9),
 ('ADBE FY25 OCF',        'ADBE','NetCashProvidedByUsedInOperatingActivities', 10.03, 1e9),
 ('INTU FY25 revenue',    'INTU','Revenues',                 18.83, 1e9),
 ('INTU FY25 net income', 'INTU','NetIncomeLoss',             3.87, 1e9),
 ('INTU FY25 diluted EPS','INTU','EarningsPerShareDiluted',  13.67, 1),
 ('INTU FY25 SBC',        'INTU','ShareBasedCompensation',    1.97, 1e9),
 ('INTU FY25 buyback',    'INTU','PaymentsForRepurchaseOfCommonStock', 2.77, 1e9),
 ('ACN FY25 revenue',     'ACN','Revenues',                  69.67, 1e9),
 ('ACN FY25 net income',  'ACN','NetIncomeLoss',              7.68, 1e9),
 ('ACN FY25 SBC',         'ACN','ShareBasedCompensation',     2.09, 1e9),
 ('CRM FY26 revenue',     'CRM','Revenues',                  41.52, 1e9),
 ('CRM FY26 net income',  'CRM','NetIncomeLoss',              7.46, 1e9),
 ('CRM FY26 diluted EPS', 'CRM','EarningsPerShareDiluted',    7.80, 1),
 ('CRM FY26 buyback',     'CRM','PaymentsForRepurchaseOfCommonStock', 12.60, 1e9),
]
print('='*100)
print('INDEPENDENT AUDIT — each value fetched fresh from SEC EDGAR, compared to report claim')
print('='*100)
print(f'{"claim":28s} {"report":>10s} {"SEC":>12s} {"dev%":>8s}  {"date":10s} verdict')
print('-'*100)
npass=nwarn=nfail=0
for label,tk,tag,rep,scale in CLAIMS:
    f=F.get(tk)
    a=latest_annual(f,tag) if f else None
    if not a or a[1] is None:
        print(f'{label:28s} {rep:10.2f} {"NOT FOUND":>12s} {"-":>8s}')
        nwarn+=1; continue
    end,val=a
    got=val/scale
    dev=abs(got-rep)/rep*100 if rep else 0
    v='PASS' if dev<=0.6 else ('WARN' if dev<=2 else 'FAIL')
    if v=='PASS': npass+=1
    elif v=='WARN': nwarn+=1
    else: nfail+=1
    print(f'{label:28s} {rep:10.2f} {got:12.3f} {dev:7.2f}%  {end:10s} {v}')
print('-'*100)
print(f'PASS {npass}  WARN {nwarn}  FAIL {nfail}   (tolerance: PASS<=0.6%, WARN<=2%)')
print()
print('='*100)
print('DERIVED-METRIC RECHECK (recomputed from the SEC values above, not from report)')
print('='*100)
px={'ADBE':265.21,'INTU':325.25,'ACN':175.72,'CRM':192.74}
for tk in ['ADBE','INTU','ACN','CRM']:
    f=F[tk]
    li=latest_annual(f,'Liabilities'); asx=latest_annual(f,'Assets')
    # point-in-time balance sheet: use instant facts
    def instant(tag):
        best=None
        for e in units(f,tag):
            if e.get('start') or not e.get('end'): continue
            if best is None or e['end']>best[0]: best=(e['end'],e.get('val'))
        return best
    L=instant('Liabilities'); A=instant('Assets')
    if L and A and L[1] and A[1]:
        print(f'  {tk:5s} L/A = {L[1]/A[1]*100:5.1f}%  (as of {A[0]})   {"PASS <50%" if L[1]/A[1]<0.5 else "FAIL >=50%"}')
    else:
        eq=instant('StockholdersEquity')
        if A and eq and A[1] and eq[1]:
            print(f'  {tk:5s} L/A = {(A[1]-eq[1])/A[1]*100:5.1f}%  (derived A-E, as of {A[0]})   {"PASS" if (A[1]-eq[1])/A[1]<0.5 else "FAIL"}')
