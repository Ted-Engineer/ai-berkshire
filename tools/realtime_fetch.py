#!/usr/bin/env python
"""实时行情批量采集器 - 基于yfinance"""
import sys, json, time
import yfinance as yf

def fetch(tickers):
    results = {}
    for tk in tickers:
        try:
            t = yf.Ticker(tk)
            i = t.info
            results[tk] = {
                'price': i.get('currentPrice'),
                'market_cap': i.get('marketCap'),
                'trailing_pe': i.get('trailingPE'),
                'forward_pe': i.get('forwardPE'),
                'ps': i.get('priceToSalesTrailing12Months'),
                'pb': i.get('priceToBook'),
                'revenue': i.get('totalRevenue'),
                'fcf': i.get('freeCashflow'),
                'op_margin': i.get('operatingMargins'),
                'profit_margin': i.get('profitMargins'),
                'roe': i.get('returnOnEquity'),
                'cash': i.get('totalCash'),
                'debt': i.get('totalDebt'),
                'rev_growth': i.get('revenueGrowth'),
                'eps_growth': i.get('earningsGrowth'),
                '52w_high': i.get('fiftyTwoWeekHigh'),
                '52w_low': i.get('fiftyTwoWeekLow'),
                'dividend_yield': i.get('dividendYield'),
                'shares': i.get('sharesOutstanding'),
                'gross_margin': i.get('grossMargins'),
            }
            print(f"  OK {tk}: ${i.get('currentPrice')} PE={i.get('trailingPE')} fwdPE={i.get('forwardPE')}", file=sys.stderr)
        except Exception as e:
            results[tk] = {'error': str(e)}
            print(f"  ERR {tk}: {e}", file=sys.stderr)
        time.sleep(0.3)
    return results

if __name__ == '__main__':
    tickers = sys.argv[1].split(',')
    r = fetch(tickers)
    print(json.dumps(r, indent=2, default=str))
