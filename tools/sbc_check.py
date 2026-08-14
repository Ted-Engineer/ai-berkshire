import os, sys, json
os.environ['PYTHONHTTPSVERIFY']='0'
import urllib3; urllib3.disable_warnings()
import requests

UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
S=requests.Session(); S.headers.update(UA)
CRUMB=None
def init():
    global CRUMB
    for h in ('https://fc.yahoo.com','https://finance.yahoo.com'):
        try: S.get(h,verify=False,timeout=15)
        except Exception: pass
    r=S.get('https://query2.finance.yahoo.com/v1/test/getcrumb',verify=False,timeout=15)
    CRUMB=r.text.strip() if r.status_code==200 else None
    return CRUMB

def ts(tk, typ, keys):
    """timeseries fundamentals"""
    ks=','.join(f'annual{k}' for k in keys)
    url=(f'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{tk}'
         f'?symbol={tk}&type={ks}&period1=1500000000&period2=1800000000&merge=false')
    if CRUMB: url+=f'&crumb={CRUMB}'
    try:
        r=S.get(url,verify=False,timeout=25)
        if r.status_code!=200: return {'err':r.status_code}
        out={}
        for blk in r.json().get('timeseries',{}).get('result',[]):
            mt=blk.get('meta',{}).get('type',[None])[0]
            if not mt: continue
            vals=[]
            for it in blk.get(mt,[]) or []:
                if it and it.get('reportedValue'):
                    vals.append((it.get('asOfDate'), it['reportedValue'].get('raw')))
            out[mt.replace('annual','')]=vals
        return out
    except Exception as e:
        return {'err':str(e)[:60]}

init()
KEYS=['StockBasedCompensation','OperatingCashFlow','CapitalExpenditure','FreeCashFlow',
      'NetIncome','TotalRevenue','RepurchaseOfCapitalStock','DilutedEPS','BasicAverageShares','DilutedAverageShares']
for tk in sys.argv[1:]:
    d=ts(tk,'cashflow',KEYS)
    if 'err' in d:
        print(f'{tk}: ERR {d["err"]}'); continue
    print(f'\n===== {tk} =====')
    sbc=dict(d.get('StockBasedCompensation',[]))
    ocf=dict(d.get('OperatingCashFlow',[]))
    ni =dict(d.get('NetIncome',[]))
    rev=dict(d.get('TotalRevenue',[]))
    bb =dict(d.get('RepurchaseOfCapitalStock',[]))
    eps=dict(d.get('DilutedEPS',[]))
    sh =dict(d.get('DilutedAverageShares',[]))
    dates=sorted(set(list(sbc)+list(ni)+list(rev)))[-5:]
    print(f'{"date":12s}{"rev$B":>9}{"NI$B":>9}{"SBC$B":>8}{"SBC/rev":>9}{"SBC/NI":>9}{"OCF$B":>9}{"buyback$B":>11}{"dilEPS":>8}{"shares_M":>10}')
    for dt in dates:
        r_=rev.get(dt); n_=ni.get(dt); s_=sbc.get(dt); o_=ocf.get(dt); b_=bb.get(dt); e_=eps.get(dt); q_=sh.get(dt)
        f=lambda v,sc=1e9: f'{v/sc:>8.2f}' if isinstance(v,(int,float)) else f'{"-":>8}'
        pr=lambda v: f'{v*100:>8.1f}%' if isinstance(v,(int,float)) else f'{"-":>9}'
        print(f'{dt:12s}{f(r_)} {f(n_)} {f(s_)[1:]}'
              f'{pr(s_/r_ if isinstance(s_,(int,float)) and isinstance(r_,(int,float)) and r_ else None)}'
              f'{pr(s_/n_ if isinstance(s_,(int,float)) and isinstance(n_,(int,float)) and n_ else None)}'
              f'{f(o_)} {f(abs(b_) if isinstance(b_,(int,float)) else None)[1:]}  '
              f'{f(e_,1)[3:]} {f(q_,1e6)[1:]}')
