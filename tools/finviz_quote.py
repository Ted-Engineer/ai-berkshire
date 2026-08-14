#!/usr/bin/env python
"""Finviz quote fetcher — full snapshot for US stocks. Works from CN network.
Data source: finviz.com/quote.ashx?t=TICKER (real-time / last close).
Usage: python tools/finviz_quote.py MSFT,CRM,ADBE [--out data/finviz.json]
"""
import urllib.request, ssl, re, sys, json, time, os

CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36',
    'Referer': 'https://finviz.com/',
    'Accept': 'text/html,application/xhtml+xml',
}


def clean(x):
    return re.sub(r'<[^>]+>', '', x).strip()


def fetch_one(ticker):
    url = f'https://finviz.com/quote.ashx?t={ticker}'
    req = urllib.request.Request(url, headers=HDRS)
    body = urllib.request.urlopen(req, timeout=25, context=CTX).read().decode(errors='replace')
    out = {'ticker': ticker}
    # --- price / change ---
    m = re.search(r'class="[^"]*quote-price_wrapper[^"]*"[^>]*>.*?([\d.,]+)', body, re.S)
    if m:
        out['Price'] = m.group(1)
    m = re.search(r'id="quotepage-change"[^>]*>\s*([+\-][\d.,]+%?)', body)
    if m:
        out['Change'] = m.group(1)
    # --- snapshot pairs: label -> value ---
    # each field row: <div class="snapshot-td-label">LABEL</div> ... <div class="snapshot-td-content">VALUE</div>
    pat = re.compile(
        r'<div class="snapshot-td-label">(.*?)</div>.*?'
        r'<div class="snapshot-td-content">(.*?)</div>', re.S)
    for label_html, val_html in pat.findall(body):
        label = clean(label_html).strip()
        val = clean(val_html)
        val = re.sub(r'\s+', ' ', val)
        if label:
            out[label] = val
    return out


def fetch(tickers, sleep=0.4):
    results = {}
    for tk in tickers:
        try:
            r = fetch_one(tk)
            results[tk] = r
            print(f"OK {tk} ${r.get('Price','?')} cap={r.get('Market Cap','?')} PE={r.get('P/E','?')}", file=sys.stderr)
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
        print(f"saved -> {out_path}", file=sys.stderr)
    print(json.dumps(r, ensure_ascii=False, indent=1))
