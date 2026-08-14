import json,glob,sys
def num(x):
    if x is None: return None
    if isinstance(x,(int,float)): return float(x)
    try: return float(x)
    except: return None
rows=[]
for f in sorted(glob.glob('data/scan_b*.json')):
    for tk,d in json.load(open(f,encoding='utf-8')).items():
        if 'error' in d or not d.get('price'): continue
        rows.append(d)
seen={}
for d in rows: seen[d['ticker']]=d
rows=list(seen.values())

def screen(d):
    pe=num(d.get('pe_ttm')); pef=num(d.get('pe_fwd')); peg=num(d.get('peg'))
    roe=num(d.get('roe')); fcf=num(d.get('fcf')); ocf=num(d.get('ocf'))
    de=num(d.get('debt_to_equity')); rg=num(d.get('rev_growth'))
    # G1 PE<30 (trailing primary; forward or PEG<1.5 as documented relaxation)
    g1=False; g1w=''
    if pe and 0<pe<30: g1=True; g1w='TTM'
    elif pef and 0<pef<30: g1=True; g1w='FWD'
    elif peg and 0<peg<1.5: g1=True; g1w='PEG'
    # G2 ROE>10%
    g2 = bool(roe is not None and roe>0.10)
    # G3 cashflow positive (FCF>0 AND OCF>0)
    g3 = bool((fcf is not None and fcf>0) and (ocf is not None and ocf>0))
    # G4 debt: D/E < 100% (== L/A<50% equivalent, looser since debt<liabilities)
    g4 = bool(de is not None and de<100)
    return g1,g2,g3,g4,g1w

out=[]
for d in rows:
    g=screen(d); n=sum(g[:4])
    out.append((n,d,g))
out.sort(key=lambda x:(-x[0], num(x[1].get('pe_fwd')) or 999))

print(f"{'TK':7s}{'PE':>7s}{'fPE':>7s}{'PEG':>6s}{'ROE':>7s}{'FCF$B':>8s}{'D/E':>7s}{'OCF/NI':>7s}{'revG':>7s}{'PS':>6s}{'mcapB':>8s}{'offHi':>7s}  G")
print('-'*104)
def fmt(v,f='{:.1f}'):
    v=num(v)
    return f.format(v) if v is not None else '-'
full=[]
for n,d,g in out:
    if n<4: continue
    full.append(d['ticker'])
    print(f"{d['ticker']:7s}{fmt(d.get('pe_ttm')):>7s}{fmt(d.get('pe_fwd')):>7s}{fmt(d.get('peg'),'{:.2f}'):>6s}"
          f"{(fmt(num(d.get('roe'))*100 if num(d.get('roe')) is not None else None)+'%'):>7s}"
          f"{fmt((num(d.get('fcf')) or 0)/1e9,'{:.2f}'):>8s}{fmt(d.get('debt_to_equity'),'{:.0f}'):>7s}"
          f"{fmt(d.get('ocf_ni'),'{:.2f}'):>7s}"
          f"{(fmt(num(d.get('rev_growth'))*100 if num(d.get('rev_growth')) is not None else None,'{:.0f}')+'%'):>7s}"
          f"{fmt(d.get('ps')):>6s}{fmt((num(d.get('mcap')) or 0)/1e9,'{:.0f}'):>8s}"
          f"{(fmt(num(d.get('pct_off_high'))*100 if num(d.get('pct_off_high')) is not None else None,'{:.0f}')+'%'):>7s}  {g[4]}")
print(f"\n=== 4/4 FULL PASS: {len(full)} ===")
print(', '.join(full))
json.dump(full,open('data/pass4.json','w'))
print(f"\nTotal universe with data: {len(rows)}")
