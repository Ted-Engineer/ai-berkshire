#!/usr/bin/env python
"""StockAnalysis quote fetcher — 第二数据源（与 finviz 交叉验证）。
Usage: python tools/sa_quote.py MU,INTU,CRM [--out data/sa.json]
"""
import urllib.request, ssl, re, sys, json, time, os

CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
HDRS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0'}

# 需要的字段（stockanalysis 统计表格）
FIELDS = ['Market Cap', 'Revenue (ttm)', 'Net Income', 'EPS', 'Shares Out',
          'PE Ratio', 'Forward PE', 'PEG', 'Price/Sales', 'Price/Book',
          'EV/EBITDA', 'Gross Margin', 'Operating Margin', 'Profit Margin',
          'Free Cash Flow', 'FCF Margin', 'Operating Cash Flow', 'Capital Expenditures',
          'Debt/Equity', 'ROE', 'ROIC', 'Current Ratio', 'Quick Ratio',
          'Revenue Growth', 'Profit Growth', 'EPS Growth', '52-Week Range',
          'Price Target', 'Dividend', 'Forward Dividend']


def clean(x):
    return re.sub(r'<[^>]+>', '', x).strip()


def fetch_one(ticker):
    url = f'https://stockanalysis.com/stocks/{ticker.lower()}/'
    req = urllib.request.Request(url, headers=HDRS)
    body = urllib.request.urlopen(req, timeout=25, context=CTX).read().decode(errors='replace')
    out = {'ticker': ticker}
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', body, re.S)
    for row in rows:
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
        vals = [clean(c) for c in cells]
        if len(vals) >= 2 and vals[0] in FIELDS:
            out[vals[0]] = vals[1]
    # 价格
    m = re.search(r'data-price="([\d.]+)"', body) or re.search(r'"currentPrice":\s*([\d.]+)', body)
    if m:
        out['Price'] = m.group(1)
    return out


def fetch(tickers, sleep=0.4):
    results = {}
    for tk in tickers:
        try:
            results[tk] = fetch_one(tk)
            print(f"OK {tk}", file=sys.stderr)
        except Exception as e:
            results[tk] = {'ticker': tk, 'error': str(e)[:120]}
            print(f"ERR {tk}: {str(e)[:80]}", file=sys.stderr)
        time.sleep(sleep)
    return results


if __name__ == '__main__':
    tickers = [t.strip().upper() for t in sys.argv[1].split(',') if t.strip()]
    r = fetch(tickers)
    out_path = None
    if '--out' in sys.argv:
        i = sys.argv.index('--out')
        out_path = sys.argv[i + 1]
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(r, f, ensure_ascii=False, indent=1)
    print(json.dumps(r, ensure_ascii=False, indent=1))
