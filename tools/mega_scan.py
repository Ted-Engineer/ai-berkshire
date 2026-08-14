#!/usr/bin/env python
"""Mega fundamentals scanner - Yahoo Finance v8/v10 (SSL verify off).
Usage: python tools/mega_scan.py TICKER1 TICKER2 ... [--out FILE]
"""
import os, sys, json, time
os.environ['PYTHONHTTPSVERIFY'] = '0'
import urllib3
urllib3.disable_warnings()
import requests

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
MODULES = 'price,summaryDetail,defaultKeyStatistics,financialData,incomeStatementHistory,balanceSheetHistory,cashflowStatementHistory,calendarEvents'

S = requests.Session()
S.headers.update(UA)

CRUMB = None

def init_crumb():
    """Yahoo now requires cookie+crumb for v10 quoteSummary."""
    global CRUMB
    if CRUMB:
        return CRUMB
    for host in ('https://fc.yahoo.com', 'https://finance.yahoo.com'):
        try:
            S.get(host, verify=False, timeout=15, allow_redirects=True)
        except Exception:
            pass
    try:
        r = S.get('https://query2.finance.yahoo.com/v1/test/getcrumb', verify=False, timeout=15)
        if r.status_code == 200 and r.text and len(r.text) < 40:
            CRUMB = r.text.strip()
            print('CRUMB ok:', CRUMB[:12])
            return CRUMB
    except Exception as e:
        print('crumb err', e)
    print('CRUMB FAILED')
    return None


def g(d, *keys, default=None):
    cur = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
        if cur is None:
            return default
    if isinstance(cur, dict):
        return cur.get('raw', default)
    return cur


def fetch_one(tk, retries=3):
    out = {'ticker': tk}
    url = f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{tk}?modules={MODULES}'
    if CRUMB:
        url += f'&crumb={CRUMB}'
    for a in range(retries):
        try:
            r = S.get(url, verify=False, timeout=20)
            if r.status_code == 200:
                res = r.json().get('quoteSummary', {}).get('result')
                if not res:
                    out['error'] = 'empty result'
                    return out
                d = res[0]
                pr, sd, ks, fd = d.get('price', {}), d.get('summaryDetail', {}), d.get('defaultKeyStatistics', {}), d.get('financialData', {})
                out['name'] = pr.get('shortName')
                out['price'] = g(pr, 'regularMarketPrice')
                out['mcap'] = g(pr, 'marketCap')
                out['currency'] = pr.get('currency')
                out['pe_ttm'] = g(sd, 'trailingPE')
                out['pe_fwd'] = g(sd, 'forwardPE')
                out['peg'] = g(ks, 'pegRatio')
                out['ps'] = g(sd, 'priceToSalesTrailing12Months')
                out['pb'] = g(ks, 'priceToBook')
                out['eps_ttm'] = g(ks, 'trailingEps')
                out['eps_fwd'] = g(ks, 'forwardEps')
                out['shares'] = g(ks, 'sharesOutstanding') or g(pr, 'sharesOutstanding')
                out['float_shares'] = g(ks, 'floatShares')
                out['roe'] = g(fd, 'returnOnEquity')
                out['roa'] = g(fd, 'returnOnAssets')
                out['gross_margin'] = g(fd, 'grossMargins')
                out['oper_margin'] = g(fd, 'operatingMargins')
                out['profit_margin'] = g(fd, 'profitMargins')
                out['ebitda_margin'] = g(fd, 'ebitdaMargins')
                out['revenue'] = g(fd, 'totalRevenue')
                out['rev_growth'] = g(fd, 'revenueGrowth')
                out['earn_growth'] = g(fd, 'earningsGrowth')
                out['gross_profit'] = g(fd, 'grossProfits')
                out['ebitda'] = g(fd, 'ebitda')
                out['net_income'] = g(ks, 'netIncomeToCommon')
                out['ocf'] = g(fd, 'operatingCashflow')
                out['fcf'] = g(fd, 'freeCashflow')
                out['cash'] = g(fd, 'totalCash')
                out['debt'] = g(fd, 'totalDebt')
                out['debt_to_equity'] = g(fd, 'debtToEquity')
                out['current_ratio'] = g(fd, 'currentRatio')
                out['quick_ratio'] = g(fd, 'quickRatio')
                out['ev'] = g(ks, 'enterpriseValue')
                out['ev_rev'] = g(ks, 'enterpriseToRevenue')
                out['ev_ebitda'] = g(ks, 'enterpriseToEbitda')
                out['bvps'] = g(ks, 'bookValue')
                out['beta'] = g(ks, 'beta') or g(sd, 'beta')
                out['52w_high'] = g(sd, 'fiftyTwoWeekHigh') or g(pr, 'regularMarketDayHigh')
                out['52w_low'] = g(sd, 'fiftyTwoWeekLow')
                out['div_yield'] = g(sd, 'dividendYield')
                out['payout'] = g(sd, 'payoutRatio')
                out['target_mean'] = g(fd, 'targetMeanPrice')
                out['target_high'] = g(fd, 'targetHighPrice')
                out['target_low'] = g(fd, 'targetLowPrice')
                out['rec_mean'] = g(fd, 'recommendationMean')
                out['num_analysts'] = g(fd, 'numberOfAnalystOpinions')
                out['held_insiders'] = g(ks, 'heldPercentInsiders')
                out['held_inst'] = g(ks, 'heldPercentInstitutions')
                out['short_pct_float'] = g(ks, 'shortPercentOfFloat')
                out['52w_change'] = g(ks, 'fiftyTwoWeekChange')
                out['earnings_date'] = None
                ce = d.get('calendarEvents', {}).get('earnings', {})
                eds = ce.get('earningsDate') or []
                if eds:
                    out['earnings_date'] = eds[0].get('fmt')
                # Balance sheet history for equity / total assets
                bs = d.get('balanceSheetHistory', {}).get('balanceSheetStatements') or []
                if bs:
                    b0 = bs[0]
                    out['total_assets'] = g(b0, 'totalAssets')
                    out['total_liab'] = g(b0, 'totalLiab')
                    out['equity'] = g(b0, 'totalStockholderEquity')
                    out['bs_date'] = b0.get('endDate', {}).get('fmt') if isinstance(b0.get('endDate'), dict) else None
                # Income statement history (annual revenue/NI trend)
                inc = d.get('incomeStatementHistory', {}).get('incomeStatementHistory') or []
                out['inc_hist'] = [{'d': (x.get('endDate') or {}).get('fmt'), 'rev': g(x, 'totalRevenue'),
                                    'op': g(x, 'operatingIncome'), 'ni': g(x, 'netIncome')} for x in inc[:4]]
                # Cashflow history
                cfh = d.get('cashflowStatementHistory', {}).get('cashflowStatements') or []
                out['cf_hist'] = [{'d': (x.get('endDate') or {}).get('fmt'), 'ocf': g(x, 'totalCashFromOperatingActivities'),
                                   'capex': g(x, 'capitalExpenditures'), 'buyback': g(x, 'repurchaseOfStock')} for x in cfh[:4]]
                # derived
                if out.get('total_liab') and out.get('total_assets'):
                    out['debt_ratio'] = round(out['total_liab'] / out['total_assets'], 4)
                if out.get('fcf') and out.get('mcap'):
                    out['fcf_yield'] = round(out['fcf'] / out['mcap'], 4)
                if out.get('ocf') and out.get('net_income') and out['net_income'] > 0:
                    out['ocf_ni'] = round(out['ocf'] / out['net_income'], 3)
                if out.get('price') and out.get('52w_high') and out['52w_high']:
                    out['pct_off_high'] = round(out['price'] / out['52w_high'] - 1, 4)
                if out.get('price') and out.get('shares'):
                    out['mcap_calc'] = round(out['price'] * out['shares'])
                    if out.get('mcap'):
                        out['mcap_diff_pct'] = round(out['mcap_calc'] / out['mcap'] - 1, 4)
                return out
            elif r.status_code in (429, 502, 503):
                time.sleep(1.5 * (a + 1))
                continue
            else:
                out['error'] = f'HTTP {r.status_code}'
                return out
        except Exception as e:
            if a == retries - 1:
                out['error'] = str(e)[:120]
            else:
                time.sleep(1.0)
    return out


def main():
    args = [a for a in sys.argv[1:]]
    outfile = None
    if '--out' in args:
        i = args.index('--out')
        outfile = args[i + 1]
        args = args[:i] + args[i + 2:]
    tickers = args
    init_crumb()
    results = {}
    for i, tk in enumerate(tickers):
        r = fetch_one(tk)
        results[tk] = r
        if 'error' in r:
            print(f'[{i+1}/{len(tickers)}] ERR {tk}: {r["error"]}', flush=True)
        else:
            pe = r.get('pe_ttm')
            pef = r.get('pe_fwd')
            roe = r.get('roe')
            mc = r.get('mcap')
            def f2(v, pct=False, suf=''):
                if v is None: return '-'
                try:
                    return f'{v*100:.1f}%' if pct else f'{v:.1f}{suf}'
                except Exception: return '-'
            print(f'[{i+1}/{len(tickers)}] {tk:6s} ${r.get("price")} mcap={f2(mc/1e9 if mc else None,suf="B")} PE={f2(pe)} fPE={f2(pef)} ROE={f2(roe,pct=True)} rev_g={f2(r.get("rev_growth"),pct=True)}', flush=True)
        time.sleep(0.25)
    if outfile:
        with open(outfile, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=1)
        print(f'\nSaved {len(results)} -> {outfile}')


if __name__ == '__main__':
    main()
