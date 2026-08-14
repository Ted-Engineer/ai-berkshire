#!/usr/bin/env python
"""Rigorous GAAP screen: period-matched TTM EPS + real FCF yield + current-pace buyback.
Fixes the non-GAAP fPE contamination that biased the original funnel."""
import os,sys,json,time
os.environ['PYTHONHTTPSVERIFY']='0'
import urllib3; urllib3.disable_warnings()
import requests

UA={'User-Agent':'AI-Berkshire Research research@example.com'}
S=requests.Session(); S.headers.update(UA)

def cik_map():
    r=S.get('https://www.sec.gov/files/company_tickers.json',verify=False,timeout=30)
    d=r.json(); m={}
    for v in d.values(): m[v['ticker'].upper()]=str(v['cik_str']).zfill(10)
    return m

def facts(cik):
    r=S.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',verify=False,timeout=60)
    return r.json() if r.status_code==200 else None

def units(f,tag):
    for t in ('us-gaap','ifrs-full','dei'):
        n=f.get('facts',{}).get(t,{}).get(tag,{}).get('units',{})
        for u in ('USD','USD/shares','shares'):
            if u in n: return n[u]
    return []

def days(a,b):
    from datetime import date
    y1,m1,d1=map(int,a.split('-')); y2,m2,d2=map(int,b.split('-'))
    return (date(y2,m2,d2)-date(y1,m1,d1)).days

def annual(f,tag):
    """latest annual (350-380d) value"""
    best=None
    for e in units(f,tag):
        s,en=e.get('start'),e.get('end')
        if not s or not en: continue
        dd=days(s,en)
        if 350<=dd<=380:
            if best is None or en>best[1]: best=(s,en,e.get('val'))
    return best

def ytd_at(f,tag,start,end_max):
    """YTD value with given start, longest duration ending <= end_max"""
    best=None
    for e in units(f,tag):
        s,en=e.get('start'),e.get('end')
        if s!=start or not en or en>end_max: continue
        dd=days(s,en)
        if best is None or dd>best[0]: best=(dd,en,e.get('val'))
    return best

def ttm(f,tag):
    """rigorous TTM = latest FY + YTD(cur) - YTD(prior same length)"""
    a=annual(f,tag)
    if not a: return None,None
    fys,fye,fyv=a
    if fyv is None: return None,None
    # find YTD after fye
    cur=None
    for e in units(f,tag):
        s,en=e.get('start'),e.get('end')
        if not s or not en or en<=fye: continue
        dd=days(s,en)
        if 60<=dd<=300:
            if cur is None or dd>cur[0]: cur=(dd,s,en,e.get('val'))
    if not cur: return fyv,fye  # no stub, use FY
    cd,cs,ce,cv=cur
    if cv is None: return fyv,fye
    # prior-year same-length YTD starting at fys
    pri=None
    for e in units(f,tag):
        s,en=e.get('start'),e.get('end')
        if s!=fys or not en: continue
        dd=days(s,en)
        if abs(dd-cd)<=20:
            if pri is None or abs(dd-cd)<abs(pri[0]-cd): pri=(dd,en,e.get('val'))
    if not pri or pri[2] is None: return fyv,fye
    return fyv+cv-pri[2], ce

def latest_q_was(f):
    """most recent ~quarterly diluted weighted-avg shares, and yoy same qtr"""
    got=[]
    for e in units(f,'WeightedAverageNumberOfDilutedSharesOutstanding'):
        s,en=e.get('start'),e.get('end')
        if not s or not en: continue
        dd=days(s,en)
        if 80<=dd<=100 and e.get('val'): got.append((en,s,e['val']))
    if not got: return None,None
    got.sort(key=lambda x:x[0],reverse=True)
    latest=got[0]
    ly=None
    for en,s,v in got[1:]:
        if 350<=days(en,latest[0])<=380: ly=v; break
    return latest[2], ly

def yahoo(tks):
    out={}
    try:
        S2=requests.Session(); S2.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        for h in ('https://fc.yahoo.com','https://finance.yahoo.com'):
            try: S2.get(h,verify=False,timeout=12)
            except Exception: pass
        cr=S2.get('https://query2.finance.yahoo.com/v1/test/getcrumb',verify=False,timeout=12).text.strip()
        for tk in tks:
            u=f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{tk}?modules=price,summaryDetail,defaultKeyStatistics,financialData&crumb={cr}'
            try:
                r=S2.get(u,verify=False,timeout=20)
                if r.status_code!=200: continue
                d=r.json()['quoteSummary']['result'][0]
                g=lambda m,k: (d.get(m,{}).get(k) or {}).get('raw') if isinstance(d.get(m,{}).get(k),dict) else d.get(m,{}).get(k)
                out[tk]={'px':g('price','regularMarketPrice'),'mcap':g('price','marketCap'),
                         'hi':g('summaryDetail','fiftyTwoWeekHigh'),'lo':g('summaryDetail','fiftyTwoWeekLow'),
                         'roe':g('financialData','returnOnEquity'),'de':g('financialData','debtToEquity'),
                         'fcf':g('financialData','freeCashflow'),'ocf':g('financialData','operatingCashflow'),
                         'revg':g('financialData','revenueGrowth'),'earng':g('financialData','earningsGrowth'),
                         'div':g('summaryDetail','dividendYield'),'gm':g('financialData','grossMargins'),
                         'om':g('financialData','operatingMargins')}
            except Exception: pass
            time.sleep(0.12)
    except Exception as e: print('yahoo err',e)
    return out

TK=sys.argv[1:]
print('mapping CIKs...',flush=True)
cm=cik_map()
yh=yahoo(TK)
rows=[]
for tk in TK:
    cik=cm.get(tk.upper().replace('-','.')) or cm.get(tk.upper())
    if not cik:
        print(f'{tk}: no CIK'); continue
    f=facts(cik)
    if not f:
        print(f'{tk}: no facts'); continue
    ni,nid=ttm(f,'NetIncomeLoss')
    rev,_=ttm(f,'Revenues')
    if rev is None: rev,_=ttm(f,'RevenueFromContractWithCustomerExcludingAssessedTax')
    ocf,_=ttm(f,'NetCashProvidedByUsedInOperatingActivities')
    capex,_=ttm(f,'PaymentsToAcquirePropertyPlantAndEquipment')
    sbc,_=ttm(f,'ShareBasedCompensation')
    bb,_=ttm(f,'PaymentsForRepurchaseOfCommonStock')
    wl,wy=latest_q_was(f)
    # TTM weighted avg diluted shares: approximate from annual tag TTM
    was,_=ttm(f,'WeightedAverageNumberOfDilutedSharesOutstanding')
    y=yh.get(tk,{})
    px=y.get('px'); mcap=y.get('mcap')
    if not px or not ni or not was: 
        print(f'{tk}: missing px/ni/was  ni={ni} was={was}')
        continue
    eps=ni/was
    pe=px/eps if eps>0 else None
    fcf=(ocf-capex) if (ocf is not None and capex is not None) else y.get('fcf')
    realfcf=(fcf-sbc) if (fcf is not None and sbc is not None) else None
    rows.append(dict(tk=tk,px=px,mcap=mcap,ni=ni,rev=rev,eps=eps,pe=pe,was=was,
        ocf=ocf,capex=capex,sbc=sbc,bb=bb,fcf=fcf,realfcf=realfcf,wl=wl,wy=wy,
        shr_yoy=((wl/wy-1) if (wl and wy) else None),
        hi=y.get('hi'),lo=y.get('lo'),roe=y.get('roe'),de=y.get('de'),
        revg=y.get('revg'),earng=y.get('earng'),div=y.get('div'),gm=y.get('gm'),om=y.get('om'),nid=nid))
    print(f'{tk:6s} EPS={eps:7.2f} PE={pe if pe else 0:6.1f} SBC/rev={(sbc/rev*100 if sbc and rev else 0):5.1f}% shrYoY={(rows[-1]["shr_yoy"]*100 if rows[-1]["shr_yoy"] is not None else 0):6.2f}%',flush=True)

json.dump(rows,open('data/rigorous.json','w',encoding='utf-8'),indent=1)
print()
print('saved',len(rows),'-> data/rigorous.json')
