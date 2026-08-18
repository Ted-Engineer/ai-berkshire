import re, json, urllib.request, ssl, sys, time
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    return urllib.request.urlopen(req, context=ctx, timeout=30).read().decode('utf-8','ignore')
tickers = sys.argv[1].split(',')
cache = json.load(open('.claude/.workflow/stats_cache.json'))
for t in tickers:
    try:
        h = get(f'https://stockanalysis.com/stocks/{t.lower()}/financials/?p=quarterly')
        d = re.search(r'datekey:\[([^\]]+)\]', h)
        r = re.search(r'revenue:\[([0-9.,null]+)\]', h)
        if d and r:
            dates = [x.strip('"') for x in d.group(1).split(',')]
            vals = [None if x=='null' else float(x) for x in r.group(1).split(',')]
            q = dict(zip(dates, vals))
            last4 = vals[:4]; prev4 = vals[4:8]
            if all(v is not None for v in last4+prev4):
                g = (sum(last4)/sum(prev4)-1)*100
                cache.setdefault(t,{})['ttmGrowth'] = round(g,1)
                cache[t]['quarters'] = q
                print(t, 'TTM growth:', round(g,1), '% | quarters:', {k[:7]:v for k,v in list(q.items())[:6]})
        time.sleep(0.3)
    except Exception as e: print(t,'ERR',e)
json.dump(cache, open('.claude/.workflow/stats_cache.json','w'), ensure_ascii=False, indent=1)
print('SAVED')
