import os, json, urllib3, requests, datetime
os.environ['PYTHONHTTPSVERIFY']='0'; urllib3.disable_warnings()
UA={'User-Agent':'AI-Berkshire Research research@example.com'}
CIK={'ADBE':'0000796343','CRM':'0001108524','INTU':'0000896878','ACN':'0001467373'}
PX={'ADBE':265.21,'CRM':192.74,'INTU':325.25,'ACN':175.72}

def facts(cik):
    r=requests.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',headers=UA,verify=False,timeout=40)
    return r.json() if r.status_code==200 else None

def qseries(f,tag):
    """quarterly (duration ~90d) values, newest first"""
    out=[]
    for u in f.get('facts',{}).get('us-gaap',{}).get(tag,{}).get('units',{}).values():
        for i in u:
            s,e=i.get('start'),i.get('end')
            if not s or not e: continue
            d=(datetime.date.fromisoformat(e)-datetime.date.fromisoformat(s)).days
            if 80<d<100:
                out.append((e,i['val'],i.get('form')))
    seen={}
    for e,v,fm in out: seen[e]=v
    return sorted(seen.items(), reverse=True)

lines=[]
lines.append('='*100)
lines.append('TTM EPS PERIOD-MATCH CHECK: net income vs WEIGHTED-AVG diluted shares (both TTM)')
lines.append('vs the naive method (TTM NI / CURRENT shares) which overstates EPS for heavy repurchasers')
lines.append('='*100)
res={}
for tk,cik in CIK.items():
    f=facts(cik)
    if not f: lines.append(f'{tk}: FETCH FAIL'); continue
    ni=qseries(f,'NetIncomeLoss')
    was=qseries(f,'WeightedAverageNumberOfDilutedSharesOutstanding')
    if not was: was=qseries(f,'WeightedAverageNumberOfSharesOutstandingBasic')
    ni4=ni[:4]; was4=was[:4]
    if len(ni4)<4 or len(was4)<4:
        lines.append(f'{tk}: insufficient quarterly data ni={len(ni4)} was={len(was4)}'); continue
    ttm_ni=sum(v for _,v in ni4)
    avg_was=sum(v for _,v in was4)/4
    eps_correct=ttm_ni/avg_was
    pe_correct=PX[tk]/eps_correct
    res[tk]=dict(ttm_ni=ttm_ni,avg_was=avg_was,eps=eps_correct,pe=pe_correct,
                 quarters=[e for e,_ in ni4])
    lines.append('')
    lines.append(f'--- {tk}  px=${PX[tk]} ---')
    lines.append(f'  TTM quarters: {", ".join(e for e,_ in ni4)}')
    lines.append(f'  TTM net income      : ${ttm_ni/1e9:.3f}B')
    lines.append(f'  TTM avg diluted WAS : {avg_was/1e6:.1f}M   (per-qtr: {", ".join(f"{v/1e6:.0f}" for _,v in was4)})')
    lines.append(f'  CORRECT TTM EPS     : ${eps_correct:.2f}')
    lines.append(f'  CORRECT GAAP PE     : {pe_correct:.1f}x')
open('data/ttm_fix.txt','w',encoding='utf-8').write('\n'.join(lines))
json.dump(res,open('data/ttm_fix.json','w'),indent=1)
print('\n'.join(lines))
