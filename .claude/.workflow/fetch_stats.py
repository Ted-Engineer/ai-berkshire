import re, json, urllib.request, ssl, sys, time
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    return urllib.request.urlopen(req, context=ctx, timeout=30).read().decode('utf-8','ignore')
def grab(html, title):
    m = re.search(r'title:"'+re.escape(title)+r'",value:"([^"]*)"', html)
    return m.group(1) if m else None
def grab_txt(html, prefix, n=140):
    m = re.search(re.escape(prefix)+r'([^"]{10,'+str(n)+r'})', html)
    return m.group(1) if m else None
tickers = sys.argv[1].split(',')
out = {}
for t in tickers:
    try:
        h = get(f'https://stockanalysis.com/stocks/{t.lower()}/statistics/')
        d = {
            'mcap': grab(h,'Market Cap'), 'pe': grab(h,'PE Ratio'), 'fwdPE': grab(h,'Forward PE'),
            'ps': grab(h,'PS Ratio'), 'peg': grab(h,'PEG Ratio'), 'roe': grab(h,'Return on Equity (ROE)'),
            'grossM': grab(h,'Gross Margin'), 'netM': grab(h,'Profit Margin'), 'opM': grab(h,'Operating Margin'),
            'debt': grab(h,'Total Debt'), 'equity': grab(h,'Equity (Book Value)'), 'netcash': grab(h,'Net Cash'),
            'pt': grab(h,'Price Target'), 'rating': grab(h,'Analyst Consensus'),
        }
        inc = grab_txt(h, 'incomeStatement:{text:"')
        bs = grab_txt(h, 'balanceSheet:{text:"')
        cf = grab_txt(h, 'cashFlow:{text:"')
        d['income'] = inc; d['bs'] = bs; d['cf'] = cf
        # overview page for revenue growth
        try:
            h2 = get(f'https://stockanalysis.com/stocks/{t.lower()}/')
            m = re.search(r'Revenue Growth \(YoY\)[^0-9\-+]*([+\-]?[0-9.]+%)', h2)
            d['revGrowth'] = m.group(1) if m else None
        except Exception as e: d['revGrowth']=None
        out[t]=d
        print(t, json.dumps(d, ensure_ascii=False)[:300])
        time.sleep(0.4)
    except Exception as e:
        out[t]={'err':str(e)}; print(t,'ERR',e)
json.dump(out, open('.claude/.workflow/stats_cache.json','w'), ensure_ascii=False, indent=1)
print('SAVED')
