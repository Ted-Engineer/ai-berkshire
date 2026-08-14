#!/usr/bin/env python
"""Stock quote fetcher using Yahoo Finance v8 API (SSL verify off)."""
import os, sys, json, time
os.environ['PYTHONHTTPSVERIFY'] = '0'
import urllib3
urllib3.disable_warnings()
import requests

def fetch_quotes(tickers):
    results = {}
    for tk in tickers:
        try:
            url = f'https://query1.finance.yahoo.com/v8/finance/chart/{tk}?interval=1d&range=5d'
            r = requests.get(url, verify=False, timeout=10,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'})
            if r.status_code == 200:
                data = r.json()
                meta = data['chart']['result'][0]['meta']
                results[tk] = {
                    'price': meta.get('regularMarketPrice'),
                    'prev_close': meta.get('previousClose'),
                    '52w_high': meta.get('fiftyTwoWeekHigh'),
                    '52w_low': meta.get('fiftyTwoWeekLow'),
                    'volume': meta.get('regularMarketVolume'),
                    'currency': meta.get('currency'),
                    'exchange': meta.get('exchangeName'),
                }
                print(f'OK {tk}: ${meta.get("regularMarketPrice")}')
            else:
                results[tk] = {'error': f'HTTP {r.status_code}'}
                print(f'ERR {tk} HTTP {r.status_code}')
        except Exception as e:
            results[tk] = {'error': str(e)[:100]}
            print(f'ERR {tk}: {str(e)[:80]}')
    return results

def fetch_stats(ticker):
    """Fetch key statistics."""
    try:
        url = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=defaultKeyStatistics,financialData,summaryDetail'
        r = requests.get(url, verify=False, timeout=10,
            headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            data = r.json()
            res = data['quoteSummary']['result'][0]
            fk = res.get('financialData', {})
            sk = res.get('defaultKeyStatistics', {})
            sd = res.get('summaryDetail', {})
            return {
                'forward_pe': (sd.get('forwardPE') or {}).get('raw'),
                'trailing_pe': (sd.get('trailingPE') or {}).get('raw'),
                'pb': (sk.get('priceToBook') or {}).get('raw'),
                'ps': (sk.get('priceToSalesTrailing12Months') or {}).get('raw'),
                'roe': (fk.get('returnOnEquity') or {}).get('raw'),
                'op_margin': (fk.get('operatingMargins') or {}).get('raw'),
                'profit_margin': (fk.get('profitMargins') or {}).get('raw'),
                'rev_growth': (fk.get('revenueGrowth') or {}).get('raw'),
                'eps_growth': (fk.get('earningsGrowth') or {}).get('raw'),
                'fcf': (fk.get('freeCashflow') or {}).get('raw'),
                'cash': (fk.get('totalCash') or {}).get('raw'),
                'debt': (fk.get('totalDebt') or {}).get('raw'),
                'gross_margin': (fk.get('grossMargins') or {}).get('raw'),
                'current_ratio': (fk.get('currentRatio') or {}).get('raw'),
                'target_mean': (fk.get('targetMeanPrice') or {}).get('raw'),
                '52w_high': (sd.get('fiftyTwoWeekHigh') or {}).get('raw'),
                '52w_low': (sd.get('fiftyTwoWeekLow') or {}).get('raw'),
            }
    except Exception as e:
        return {'error': str(e)[:200]}
    return {}

if __name__ == '__main__':
    tickers = sys.argv[1].split(',')
    quotes = fetch_quotes(tickers)
    stats = {}
    for tk in tickers:
        time.sleep(0.5)
        stats[tk] = fetch_stats(tk)
        print(f'  stats {tk} ok', file=sys.stderr)
    out = {'quotes': quotes, 'stats': stats}
    print(json.dumps(out, indent=2, default=str))
