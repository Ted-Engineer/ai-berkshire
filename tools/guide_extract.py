#!/usr/bin/env python
"""Pull GAAP EPS guidance from latest earnings 8-K exhibits (SEC EDGAR).
Same standard applied to CRM, applied to every finalist."""
import os, sys, json, re, time
os.environ['PYTHONHTTPSVERIFY'] = '0'
import urllib3; urllib3.disable_warnings()
import requests

S = requests.Session()
S.headers.update({'User-Agent': 'AI-Berkshire Research research@example.com'})


def cik_of(tk):
    r = S.get('https://www.sec.gov/files/company_tickers.json', verify=False, timeout=30)
    for v in r.json().values():
        if v['ticker'].upper() == tk.upper():
            return str(v['cik_str']).zfill(10)
    return None


def recent_8k(cik, n=4):
    r = S.get(f'https://data.sec.gov/submissions/CIK{cik}.json', verify=False, timeout=40)
    d = r.json().get('filings', {}).get('recent', {})
    out = []
    for form, acc, date, doc in zip(d.get('form', []), d.get('accessionNumber', []),
                                    d.get('filingDate', []), d.get('primaryDocument', [])):
        if form == '8-K':
            out.append((date, acc.replace('-', '')))
        if len(out) >= n:
            break
    return out


def exhibits(cik, accn):
    """list files in the filing via index.json"""
    u = f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/index.json'
    try:
        r = S.get(u, verify=False, timeout=30)
        if r.status_code != 200:
            return []
        return [i['name'] for i in r.json().get('directory', {}).get('item', [])]
    except Exception:
        return []


def text_of(cik, accn, fname):
    u = f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/{fname}'
    try:
        r = S.get(u, verify=False, timeout=40)
        if r.status_code != 200:
            return ''
        t = re.sub(r'<[^>]+>', ' ', r.text)
        t = t.replace('&nbsp;', ' ').replace('&#8226;', '|').replace('&#58;', ':').replace('&amp;', '&')
        return re.sub(r'\s+', ' ', t)
    except Exception:
        return ''


def find_guidance(txt):
    """capture generous windows around GAAP EPS guidance phrases"""
    hits = []
    pats = [
        r'GAAP\s+diluted\s+(?:net\s+income|earnings)\s+per\s+share[^|]{0,220}',
        r'diluted\s+(?:net\s+income|earnings)\s+per\s+share[^|]{0,220}',
        r'targets?[^|]{0,300}per\s+share[^|]{0,160}',
    ]
    for p in pats:
        for m in re.finditer(p, txt, re.I):
            s = m.group(0).strip()
            if re.search(r'\d', s):
                hits.append(s)
    seen, out = set(), []
    for h in hits:
        k = h[:90]
        if k not in seen:
            seen.add(k); out.append(h)
    return out[:8]


for tk in sys.argv[1:]:
    print('=' * 104)
    print(tk)
    print('=' * 104)
    cik = cik_of(tk)
    if not cik:
        print('  no CIK'); continue
    for date, accn in recent_8k(cik, 4):
        files = exhibits(cik, accn)
        cands = [f for f in files if f.lower().endswith(('.htm', '.html'))
                 and ('ex' in f.lower() or '99' in f.lower())]
        if not cands:
            cands = [f for f in files if f.lower().endswith(('.htm', '.html'))]
        for f in cands[:3]:
            t = text_of(cik, accn, f)
            if not t or len(t) < 2000:
                continue
            g = find_guidance(t)
            if g:
                print(f'  --- {date}  {f}  (len {len(t)})')
                for x in g:
                    print(f'      {x[:230]}')
                break
        time.sleep(0.2)
    print()
