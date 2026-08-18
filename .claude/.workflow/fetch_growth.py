import re, json, urllib.request, ssl, sys, time
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    return urllib.request.urlopen(req, context=ctx, timeout=30).read().decode('utf-8','ignore')
tickers = sys.argv[1].split(',')
cache = json.load(open('.claude/.workflow/stats_cache.json'))
for t in tickers:
    try:
        h = get(f'https://stockanalysis.com/stocks/{t.lower()}/financials/')
        # extract revenue array
        m = re.search(r'data:\{datekey:\[([^\]]+)\].{0,400}?revenue:\[([^\]]+)\]', h)
        if not m:
            m2 = re.search(r'revenue:\[([0-9.,null]+)\]', h)
            dates = re.search(r'datekey:\[([^\]]+)\]', h)
            revs = [float(x) for x in m2.group(1).split(',') if x!='null'] if m2 else []
        else:
            dates, revs = m.group(1), None
        d = re.search(r'datekey:\[([^\]]+)\]', h)
        r = re.search(r'revenue:\[([0-9.,null]+)\]', h)
        if d and r:
            years = [x.strip('"') for x in d.group(1).split(',')]
            vals = [float(x) for x in r.group(1).split(',') if x.strip() and x!='null']
            cache.setdefault(t, {})['rev_hist'] = dict(zip(years, vals))
            if len(vals) >= 2:
                g = (vals[0]/vals[1]-1)*100
                cache[t]['revGrowth'] = f"{g:.1f}% (FY{years[0][:4]} vs FY{years[1][:4]})"
        print(t, cache.get(t,{}).get('revGrowth'))
        time.sleep(0.3)
    except Exception as e:
        print(t, 'ERR', e)
json.dump(cache, open('.claude/.workflow/stats_cache.json','w'), ensure_ascii=False, indent=1)
print('SAVED')
