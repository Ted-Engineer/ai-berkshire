#!/usr/bin/env python3
"""GENUINELY independent audit: fetch each claim fresh from SEC EDGAR XBRL,
compare to the report's claimed value. No echoing reported_value into fetched_value.

与 report_audit.py 的区别：report_audit 的 fetched_value 由写报告的同一个模型回填，
存在自我验证问题；本工具直接从 SEC companyfacts 拉原始事实，模型只提供报告值。

用法:
    python tools/indep_audit.py --claims claims.json

claims.json 格式（数组，每项）:
    {
      "label": "ADBE FY25 revenue",          # 展示用标签
      "ticker": "ADBE",                       # 美股 ticker
      "tag": "Revenues",                      # us-gaap/dei XBRL 标签
      "value": 23.77,                         # 报告声称值
      "scale": 1e9                            # 单位换算（如 1e9 = 报告值单位为十亿）
    }

常用标签: Revenues / NetIncomeLoss / EarningsPerShareDiluted /
ShareBasedCompensation / PaymentsForRepurchaseOfCommonStock /
NetCashProvidedByUsedInOperatingActivities

退出码: 0 = 无 FAIL；1 = 存在 FAIL（偏差 > 2%）或取数失败。
判定: PASS ≤ 0.6% | WARN ≤ 2% | FAIL > 2%
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

import urllib3
import requests

urllib3.disable_warnings()

S = requests.Session()
S.headers.update({'User-Agent': 'AI-Berkshire Research research@example.com'})

REPO = Path(__file__).resolve().parent.parent
TICKER_CACHE = REPO / 'data' / 'sec_tickers.json'

# 少量常用 CIK 预置，避免每次都拉 company_tickers.json
_KNOWN_CIK = {
    'ADBE': '0000796343', 'INTU': '0000896878', 'ACN': '0001467373',
    'CRM': '0001108524', 'MSFT': '0000789019', 'GOOGL': '0001652044',
    'META': '0001326801', 'AVGO': '0001730168', 'TSM': '0001046179',
    'ORCL': '0001341439', 'DELL': '0001571996', 'MU': '0000723125',
}


def load_cik_map():
    """ticker -> CIK（含 10 位补零）。优先用缓存，缺失时拉 SEC 官方清单。"""
    m = dict(_KNOWN_CIK)
    if TICKER_CACHE.exists():
        try:
            m.update(json.loads(TICKER_CACHE.read_text(encoding='utf-8')))
        except Exception:
            pass
        return m
    try:
        r = S.get('https://www.sec.gov/files/company_tickers.json', timeout=30)
        if r.status_code == 200:
            for _, row in r.json().items():
                m[row['ticker'].upper()] = str(row['cik_str']).zfill(10)
            TICKER_CACHE.parent.mkdir(parents=True, exist_ok=True)
            TICKER_CACHE.write_text(json.dumps(m, ensure_ascii=False), encoding='utf-8')
    except Exception as e:
        print(f'⚠️ 拉取 company_tickers.json 失败: {e}', file=sys.stderr)
    return m


def facts(cik):
    r = S.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',
              timeout=60)
    return r.json() if r.status_code == 200 else None


def units(f, tag):
    for t in ('us-gaap', 'dei'):
        n = f.get('facts', {}).get(t, {}).get(tag, {}).get('units', {})
        for u in ('USD', 'USD/shares', 'shares'):
            if u in n:
                return n[u]
    return []


def days(a, b):
    y1, m1, d1 = map(int, a.split('-'))
    y2, m2, d2 = map(int, b.split('-'))
    return (date(y2, m2, d2) - date(y1, m1, d1)).days


def latest_annual(f, tag):
    """取最近一个完整财年（350-380 天区间）的事实。"""
    best = None
    for e in units(f, tag):
        s, en = e.get('start'), e.get('end')
        if not s or not en:
            continue
        if 350 <= days(s, en) <= 380:
            if best is None or en > best[0]:
                best = (en, e.get('val'))
    return best


def main():
    ap = argparse.ArgumentParser(description='SEC EDGAR 独立复核工具')
    ap.add_argument('--claims', required=True, help='claims JSON 文件路径')
    ap.add_argument('--timeout', type=int, default=60)
    args = ap.parse_args()

    claims = json.loads(Path(args.claims).read_text(encoding='utf-8'))
    if not isinstance(claims, list) or not claims:
        print('❌ claims 文件必须是非空 JSON 数组', file=sys.stderr)
        sys.exit(1)

    cik_map = load_cik_map()
    tickers = sorted({c['ticker'].upper() for c in claims})
    missing = [t for t in tickers if t not in cik_map]
    if missing:
        print(f'❌ 无法解析 CIK: {", ".join(missing)}', file=sys.stderr)
        sys.exit(1)

    print('=' * 100)
    print('INDEPENDENT AUDIT — 每个值直接从 SEC EDGAR 新鲜拉取，与报告声称值比对')
    print('=' * 100)
    print(f'{"claim":28s} {"report":>10s} {"SEC":>12s} {"dev%":>8s}  {"财年止":10s} verdict')
    print('-' * 100)

    F = {t: facts(cik_map[t]) for t in tickers}
    npass = nwarn = nfail = 0
    for c in claims:
        label = c.get('label', '?')
        tk = c['ticker'].upper()
        tag = c['tag']
        rep = float(c['value'])
        scale = float(c.get('scale', 1))
        f = F.get(tk)
        a = latest_annual(f, tag) if f else None
        if not a or a[1] is None:
            print(f'{label:28s} {rep:10.2f} {"NOT FOUND":>12s} {"-":>8s}')
            nfail += 1
            continue
        end, val = a
        got = val / scale
        dev = abs(got - rep) / rep * 100 if rep else 0
        v = 'PASS' if dev <= 0.6 else ('WARN' if dev <= 2 else 'FAIL')
        if v == 'PASS':
            npass += 1
        elif v == 'WARN':
            nwarn += 1
        else:
            nfail += 1
        print(f'{label:28s} {rep:10.2f} {got:12.3f} {dev:7.2f}%  {end:10s} {v}')

    print('-' * 100)
    print(f'PASS {npass}  WARN {nwarn}  FAIL {nfail}   (tolerance: PASS<=0.6%, WARN<=2%)')
    if nfail:
        sys.exit(1)


if __name__ == '__main__':
    main()
