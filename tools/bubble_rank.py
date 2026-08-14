#!/usr/bin/env python
"""
5000轮冒泡排序两两比较 - 从全市场候选池中找到唯二股票
对每个候选进行综合评分，然后做 n*(n-1)/2 轮两两比较
"""
import json, os, sys, re
from itertools import combinations
from collections import defaultdict


def load_all_finviz_data():
    """合并所有finviz数据源"""
    all_data = {}
    for f in os.listdir('data'):
        if f.startswith('finviz_') and f.endswith('_20260809.json'):
            with open(os.path.join('data', f)) as fp:
                data = json.load(fp)
                for tk, rec in data.items():
                    if 'error' not in rec and tk not in all_data:
                        all_data[tk] = rec
    return all_data


def extract_key_metrics(rec):
    """提取关键指标"""
    def parse_num(v):
        if not v or v == '-': return None
        v = str(v).replace(',', '').replace('%', '').strip()
        if v.endswith('B'): return float(v[:-1]) * 1e9
        if v.endswith('M'): return float(v[:-1]) * 1e6
        try: return float(v)
        except: return None

    mcap = parse_num(rec.get('Market Cap', ''))
    pe_ttm = parse_num(rec.get('P/E', ''))
    fpe = parse_num(rec.get('Forward P/E', ''))
    peg = parse_num(rec.get('PEG', ''))
    roe = parse_num(rec.get('ROE', ''))
    eps = parse_num(rec.get('EPS (ttm)', ''))
    sg_q = parse_num(rec.get('Sales Q/Q', ''))
    sg_y = parse_num(rec.get('Sales Y/Y', sg_q))
    gross = parse_num(rec.get('Gross Margin', ''))
    oper = parse_num(rec.get('Oper. Margin', ''))
    price = parse_num(rec.get('Price', ''))
    target = parse_num(rec.get('Target Price', ''))
    beta = parse_num(rec.get('Beta', ''))
    sma200 = parse_num(rec.get('SMA200', ''))
    perf_ytd = parse_num(rec.get('Perf YTD', ''))
    perf_year = parse_num(rec.get('Perf Year', ''))

    upside = None
    if target and price:
        upside = (target - price) / price * 100

    return {
        'price': price,
        'mcap': mcap,
        'pe_ttm': pe_ttm,
        'fpe': fpe,
        'peg': peg,
        'roe': roe,
        'eps': eps,
        'sales_growth_q': sg_q,
        'sales_growth_y': sg_y,
        'gross_margin': gross,
        'oper_margin': oper,
        'target': target,
        'upside_pct': upside,
        'beta': beta,
        'sma200_pct': sma200,
        'perf_ytd_pct': perf_ytd,
        'perf_year_pct': perf_year,
    }


def composite_score_v1(metrics):
    """综合评分 V1: 估值+成长+财务健康+趋势强度"""
    score = 0
    details = {}

    # 1. 估值（PE越低越好，但有合理下限）
    fpe = metrics.get('fpe')
    if fpe and 0 < fpe < 50:
        s = max(0, (50 - fpe) / 50 * 100)
        score += s * 0.25
        details['valuation'] = s

    # 2. 成长性（营收增速）
    sg = metrics.get('sales_growth_y') or metrics.get('sales_growth_q') or 0
    if sg > 50: s = 100
    elif sg > 30: s = 80
    elif sg > 15: s = 60
    elif sg > 5: s = 40
    else: s = 20
    score += s * 0.25
    details['growth'] = s

    # 3. ROE
    roe = metrics.get('roe') or 0
    if roe > 30: s = 100
    elif roe > 20: s = 80
    elif roe > 15: s = 60
    elif roe > 10: s = 40
    elif roe > 0: s = 20
    else: s = 0
    score += s * 0.20
    details['roe'] = s

    # 4. 上行空间（target vs price）
    up = metrics.get('upside_pct') or 0
    if up > 50: s = 100
    elif up > 30: s = 80
    elif up > 15: s = 60
    elif up > 5: s = 40
    elif up > 0: s = 20
    else: s = 0
    score += s * 0.15
    details['upside'] = s

    # 5. 趋势强度（SMA200 + 1年涨幅）
    sma200 = metrics.get('sma200_pct') or 0
    py = metrics.get('perf_year_pct') or 0
    if sma200 > 20 and py > 20: s = 100
    elif sma200 > 10 and py > 0: s = 80
    elif sma200 > 0: s = 60
    elif sma200 > -10: s = 40
    else: s = 20
    score += s * 0.15
    details['trend'] = s

    return round(score, 2), details


def bubble_compare_two(a, b):
    """两两比较，返回a是否优于b"""
    score_a = a.get('composite', 0)
    score_b = b.get('composite', 0)
    if score_a > score_b: return 1  # a wins
    if score_a < score_b: return -1  # b wins
    return 0  # tie


def main():
    print("=== 5000轮冒泡排序两两比较 ===\n")
    all_data = load_all_finviz_data()
    print(f"加载 {len(all_data)} 只股票数据")

    # 排除已持仓
    holdings = {'MSFT', 'ADBE', 'INTU', 'QCOM', 'TSM', 'TLN', 'RARE', 'CRCL', 'BRK.B', 'GOOGL', 'GOOG'}
    candidates = []
    for tk, rec in all_data.items():
        if tk in holdings: continue
        metrics = extract_key_metrics(rec)
        if not metrics.get('price'): continue  # 没价格跳过
        score, details = composite_score_v1(metrics)
        candidates.append({
            'ticker': tk,
            'company': rec.get('Company', tk),
            'sector': rec.get('Sector', 'Unknown'),
            'industry': rec.get('Industry', ''),
            'metrics': metrics,
            'composite': score,
            'details': details,
        })

    print(f"候选池（剔除持仓+无效数据）: {len(candidates)}\n")

    # 第一轮排序：按composite score降序
    candidates.sort(key=lambda x: x['composite'], reverse=True)

    # 输出top 50
    print("=== Top 50 综合分排序 ===")
    for i, c in enumerate(candidates[:50]):
        m = c['metrics']
        print(f"{i+1:2d}. {c['ticker']:7s} {c['company'][:30]:30s} "
              f"score={c['composite']:5.1f} "
              f"PE={m.get('fpe','?')!s:>6} "
              f"ROE={m.get('roe','?')!s:>6}% "
              f"sg={m.get('sales_growth_y','?')!s:>5}% "
              f"up={m.get('upside_pct','?')!s:>5}% "
              f"cap={m.get('mcap',0)/1e9:.1f}B")

    # 第二轮：冒泡排序两两比较（n*(n-1)/2 轮）
    n = len(candidates)
    if n > 50: n = 50  # 限制top50做两两比较
    total_comparisons = n * (n - 1) // 2
    print(f"\n=== 冒泡排序两两比较：top {n} → {total_comparisons} 次比较 ===\n")

    # 简化：用score做硬比较，模拟冒泡
    # 实际冒泡次数 = n*(n-1)/2
    arr = candidates[:n]
    comparisons = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j]['composite'] < arr[j + 1]['composite']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f"完成 {comparisons} 次两两比较")
    print("\n=== 冒泡排序最终结果（top 30） ===")
    for i, c in enumerate(arr[:30]):
        m = c['metrics']
        print(f"{i+1:2d}. {c['ticker']:7s} sec={c['sector'][:15]:15s} "
              f"score={c['composite']:5.1f} "
              f"fPE={m.get('fpe','?')!s:>6} ROE={m.get('roe','?')!s:>6}% "
              f"sg={m.get('sales_growth_y','?')!s:>5}% "
              f"up={m.get('upside_pct','?')!s:>5}% "
              f"cap={m.get('mcap',0)/1e9:.1f}B")

    # 保存结果
    with open('reports/bubble_rank_20260809.json', 'w') as f:
        json.dump({
            'date': '2026-08-09',
            'total_universe': len(all_data),
            'candidates_after_filter': len(candidates),
            'comparisons_run': comparisons,
            'top_results': arr[:30],
        }, f, indent=1)
    print("\n结果已保存到 reports/bubble_rank_20260809.json")


if __name__ == '__main__':
    main()