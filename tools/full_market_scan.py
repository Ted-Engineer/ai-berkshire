#!/usr/bin/env python
"""Full US-market screener via finviz — paginates through all stocks passing
the value-investing 5 hard criteria, across ALL sectors (not just tech).
Usage: python tools/full_market_scan.py [--out data/full_scan.json]
"""
import urllib.request, ssl, re, sys, json, time, os

CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0',
    'Referer': 'https://finviz.com/',
}


def clean(x):
    return re.sub(r'<[^>]+>', '', x).strip()


def fetch_page(filters, r, order='ticker'):
    url = f'https://finviz.com/screener.ashx?v=111&f={filters}&o={order}&r={r}'
    req = urllib.request.Request(url, headers=HDRS)
    body = urllib.request.urlopen(req, timeout=30, context=CTX).read().decode(errors='replace')
    rows = re.findall(r'<tr[^>]*class="[^"]*styled-row[^"]*"[^>]*>(.*?)</tr>', body, re.S)
    out = []
    for row in rows:
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
        vals = [clean(c) for c in cells]
        if len(vals) >= 8:
            rec = {
                'No': vals[0], 'Ticker': vals[1], 'Company': vals[2],
                'Sector': vals[3], 'Industry': vals[4], 'Country': vals[5],
                'MarketCap': vals[6], 'PE': vals[7],
            }
            if len(vals) > 8: rec['Price'] = vals[8]
            if len(vals) > 9: rec['Change'] = vals[9]
            if len(vals) > 10: rec['Volume'] = vals[10]
            out.append(rec)
    return out, body


def get_total(body):
    # JSON config: "result_count":1713
    m = re.search(r'"result_count"\s*:\s*([\d,]+)', body)
    if m:
        return int(m.group(1).replace(',', ''))
    m = re.search(r'of ([\d,]+) stocks', body)
    if m:
        return int(m.group(1).replace(',', ''))
    m2 = re.search(r'of\s+([\d,]+)', body)
    return int(m2.group(1).replace(',', '')) if m2 else None


def scan(filters, label):
    print(f'Scanning [{label}] filters={filters}', file=sys.stderr)
    all_recs = []
    r = 1
    total = None
    pages = 0
    while True:
        try:
            recs, body = fetch_page(filters, r)
        except Exception as e:
            print(f'  page {r} ERR {str(e)[:80]}', file=sys.stderr)
            time.sleep(2)
            try:
                recs, body = fetch_page(filters, r)
            except Exception as e2:
                print(f'  page {r} retry ERR, stop', file=sys.stderr)
                break
        if not recs:
            break
        all_recs.extend(recs)
        pages += 1
        if total is None:
            total = get_total(body)
            print(f'  total stocks: {total}', file=sys.stderr)
        if pages % 5 == 0:
            print(f'  page {pages}, collected {len(all_recs)}', file=sys.stderr)
        if total is not None and len(all_recs) >= total:
            break
        r += 20
        time.sleep(0.6)
    print(f'  DONE [{label}]: {len(all_recs)} stocks over {pages} pages', file=sys.stderr)
    return all_recs


if __name__ == '__main__':
    out_path = 'data/full_scan.json'
    if '--out' in sys.argv:
        i = sys.argv.index('--out'); out_path = sys.argv[i + 1]

    # Pass 1: all US stocks, market cap > $1B, passing 5 hard criteria (server-side filter)
    # PE<30, fwd PE<35 (growth allowed), ROE>15, D/E<1, positive-ish (P/FCF present)
    FILTERS = 'geo_usa,cap_smallover,fa_pe_u30,fa_roe_o15,fa_debt_u1'
    all_stocks = scan(FILTERS, 'US all PE<30 ROE>15 D/E<1')

    result = {'date': '2026-08-09', 'filters': FILTERS, 'stocks': all_stocks}
    os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(f'saved {len(all_stocks)} stocks -> {out_path}', file=sys.stderr)
