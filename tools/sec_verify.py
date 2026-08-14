#!/usr/bin/env python
"""Cross-verify GAAP fundamentals against SEC EDGAR XBRL companyfacts.
This is source-of-truth: the actual filed 10-K/10-Q data.
Usage: python tools/sec_verify.py ADBE CRM ACN INTU
"""
import os, sys, json, time
os.environ['PYTHONHTTPSVERIFY'] = '0'
import urllib3
urllib3.disable_warnings()
import requests

UA = {'User-Agent': 'ai-berkshire-research contact@example.com'}

CIK = {
    'ADBE': '0000796343',
    'CRM': '0001108524',
    'ACN': '0001467373',
    'INTU': '0000896878',
    'TTD': '0001671933',
    'MU': '0000723125',
    'WDC': '0000106040',
    'QCOM': '0000804328',
    'DOCS': '0001516513',
    'PYPL': '0001633917',
}

TAGS = {
    'Revenues': ['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues',
                 'RevenueFromContractWithCustomerIncludingAssessedTax'],
    'NetIncome': ['NetIncomeLoss'],
    'EPSDiluted': ['EarningsPerShareDiluted'],
    'OpIncome': ['OperatingIncomeLoss'],
    'GrossProfit': ['GrossProfit'],
    'OCF': ['NetCashProvidedByUsedInOperatingActivities'],
    'Capex': ['PaymentsToAcquirePropertyPlantAndEquipment'],
    'SBC': ['ShareBasedCompensation'],
    'Buyback': ['PaymentsForRepurchaseOfCommonStock'],
    'Equity': ['StockholdersEquity'],
    'Assets': ['Assets'],
    'Liabilities': ['Liabilities'],
    'SharesDiluted': ['WeightedAverageNumberOfDilutedSharesOutstanding'],
    'Cash': ['CashAndCashEquivalentsAtCarryingValue'],
}


def facts(cik):
    url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'
    r = requests.get(url, headers=UA, verify=False, timeout=40)
    if r.status_code != 200:
        return None, f'HTTP {r.status_code}'
    return r.json(), None


def annual(d, tags):
    """Return list of (fy, fp, end, val) for annual (FY) periods, most recent first."""
    us = d.get('facts', {}).get('us-gaap', {})
    for t in tags:
        if t not in us:
            continue
        for unit, arr in us[t].get('units', {}).items():
            rows = []
            for it in arr:
                if it.get('form') in ('10-K', '10-K/A') and it.get('fp') == 'FY':
                    st, en = it.get('start'), it.get('end')
                    # full-year duration only (or instant for balance items)
                    if st and en:
                        try:
                            from datetime import date
                            y1 = date.fromisoformat(st)
                            y2 = date.fromisoformat(en)
                            if not (330 <= (y2 - y1).days <= 400):
                                continue
                        except Exception:
                            pass
                    rows.append((it.get('fy'), it.get('end'), it.get('val'), t, unit))
            if rows:
                seen = {}
                for fy, en, val, tag, unit in rows:
                    seen[en] = (fy, en, val, tag, unit)
                return sorted(seen.values(), key=lambda x: x[1], reverse=True)[:5]
    return []


for tk in sys.argv[1:]:
    cik = CIK.get(tk.upper())
    if not cik:
        print(f'{tk}: no CIK mapped')
        continue
    d, err = facts(cik)
    if err:
        print(f'{tk}: {err}')
        continue
    print(f'\n{"="*88}\n{tk}  (CIK {cik})  — SEC EDGAR XBRL filed data\n{"="*88}')
    for label, tags in TAGS.items():
        rows = annual(d, tags)
        if not rows:
            continue
        cells = []
        for fy, en, val, tag, unit in rows:
            if unit == 'USD':
                s = f'{val/1e9:,.2f}B' if abs(val) > 1e8 else f'{val/1e6:,.1f}M'
            elif unit == 'USD/shares':
                s = f'{val:,.2f}'
            elif unit == 'shares':
                s = f'{val/1e6:,.1f}M'
            else:
                s = str(val)
            cells.append(f'{en}:{s}')
        print(f'  {label:14s} ' + '  '.join(cells))
    time.sleep(0.4)
