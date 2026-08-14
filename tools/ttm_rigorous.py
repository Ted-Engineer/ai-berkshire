import os, json, urllib3, requests, datetime as dt
os.environ['PYTHONHTTPSVERIFY']='0'; urllib3.disable_warnings()
UA={'User-Agent':'AI-Berkshire Research research@example.com'}
CIK={'ADBE':'0000796343','CRM':'0001108524','INTU':'0000896878','ACN':'0001467373'}
PX={'ADBE':265.21,'CRM':192.74,'INTU':325.25,'ACN':175.72}

def facts(cik):
    r=requests.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',headers=UA,verify=False,timeout=40)
    return r.json() if r.status_code==200 else None

def durs(f,tag):
    """all duration facts: (start,end,days,val)"""
    out=[]
    for u in f.get('facts',{}).get('us-gaap',{}).get(tag,{}).get('units',{}).values():
        for i in u:
            s,e=i.get('start'),i.get('end')
            if not s or not e: continue
            d=(dt.date.fromisoformat(e)-dt.date.fromisoformat(s)).days
            out.append((s,e,d,i['val']))
    return out

def pick(rows, lo, hi):
    """dedupe by (start,end) keeping last; filter by duration window"""
    m={}
    for s,e,d,v in rows:
        if lo<d<hi: m[(s,e)]=v
    return sorted(m.items(), key=lambda x:x[0][1], reverse=True)

L=[]
L.append('='*104)
L.append('RIGOROUS TTM: annual FY + YTD(current) - YTD(prior-year same length)   [SEC XBRL]')
L.append('='*104)
res={}
for tk,cik in CIK.items():
    f=facts(cik)
    if not f: L.append(f'{tk} FETCH FAIL'); continue
    ni_a=pick(durs(f,'NetIncomeLoss'),350,380)      # annual
    ni_q=pick(durs(f,'NetIncomeLoss'),80,100)       # quarterly
    ni_ytd=pick(durs(f,'NetIncomeLoss'),170,290)    # 6mo & 9mo YTD
    was_a=pick(durs(f,'WeightedAverageNumberOfDilutedSharesOutstanding'),350,380)
    was_q=pick(durs(f,'WeightedAverageNumberOfDilutedSharesOutstanding'),80,100)

    (fa_s,fa_e),fy_ni = ni_a[0]
    L.append('')
    L.append(f'--- {tk}   px=${PX[tk]} ---')
    L.append(f'  latest FY : {fa_s} -> {fa_e}   NI=${fy_ni/1e9:.3f}B')

    # newest YTD after FY end
    ytd_cur=[((s,e),v) for (s,e),v in ni_ytd if s>fa_e]
    if ytd_cur:
        (ys,ye),ytd_v = ytd_cur[0]
        ylen=(dt.date.fromisoformat(ye)-dt.date.fromisoformat(ys)).days
        # prior-year YTD of same length
        prior=[((s,e),v) for (s,e),v in ni_ytd if s<=fa_e and abs((dt.date.fromisoformat(e)-dt.date.fromisoformat(s)).days-ylen)<12]
        if prior:
            (ps,pe),pv = prior[0]
            ttm = fy_ni + ytd_v - pv
            L.append(f'  YTD cur   : {ys} -> {ye} ({ylen}d)  ${ytd_v/1e9:.3f}B')
            L.append(f'  YTD prior : {ps} -> {pe}  ${pv/1e9:.3f}B')
            L.append(f'  TTM NI    = {fy_ni/1e9:.3f} + {ytd_v/1e9:.3f} - {pv/1e9:.3f} = ${ttm/1e9:.3f}B')
        else:
            ttm=fy_ni; L.append('  no prior-yr YTD match -> using FY only')
    else:
        # only quarterly available after FY end
        q_after=[((s,e),v) for (s,e),v in ni_q if s>fa_e]
        ytd_v=sum(v for _,v in q_after)
        n=len(q_after)
        q_prior=[((s,e),v) for (s,e),v in ni_q if s<=fa_e][:n]
        pv=sum(v for _,v in q_prior)
        ttm=fy_ni+ytd_v-pv
        L.append(f'  {n} qtr after FY: ${ytd_v/1e9:.3f}B  prior-yr same: ${pv/1e9:.3f}B')
        L.append(f'  TTM NI    = ${ttm/1e9:.3f}B')

    # TTM weighted-avg diluted shares: use newest 4 distinct quarter-ends incl derived Q4
    qs=was_q[:8]
    (wa_s,wa_e),fy_was = was_a[0] if was_a else ((None,None),None)
    # derive Q4 WAS for latest FY = 4*FY_avg - sum(3 quarters of that FY)
    fy_q=[v for (s,e),v in was_q if fa_s<=s and e<=fa_e]
    q4_was=None
    if fy_was and len(fy_q)>=3:
        q4_was=4*fy_was-sum(fy_q[:3])
    after=[v for (s,e),v in was_q if s>fa_e]
    ttm_was_parts=after[:]
    if q4_was and len(ttm_was_parts)<4:
        ttm_was_parts.append(q4_was)
    fyq_sorted=[v for (s,e),v in was_q if fa_s<=s and e<=fa_e]
    i=0
    while len(ttm_was_parts)<4 and i<len(fyq_sorted):
        ttm_was_parts.append(fyq_sorted[i]); i+=1
    ttm_was=sum(ttm_was_parts)/len(ttm_was_parts)
    eps=ttm/ttm_was; pe=PX[tk]/eps
    L.append(f'  TTM WAS   = {ttm_was/1e6:.1f}M  (parts: {", ".join(f"{v/1e6:.0f}" for v in ttm_was_parts)})')
    L.append(f'  >> TTM GAAP EPS = ${eps:.2f}    GAAP PE = {pe:.1f}x')
    res[tk]=dict(ttm_ni=ttm,ttm_was=ttm_was,eps=eps,pe=pe,fy_ni=fy_ni)

json.dump(res,open('data/ttm_rigorous.json','w'),indent=1)
open('data/ttm_rigorous.txt','w',encoding='utf-8').write('\n'.join(L))
print('\n'.join(L))
