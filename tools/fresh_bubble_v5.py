#!/usr/bin/env python
"""
FRESH 2026-08-09 最终冒泡排序 — 12只候选 × n*(n-1)/2轮两两比较
数据源：FRESH Agent报告 + teammate四视角交叉验证 + financial_rigor验算
"""
import json

# 基于2026-08-09全新实时数据的综合评分（6维度）
CANDIDATES = {
    'HIG':  {'composite': 4.2, 'dyp': 4.2, 'buffett': 4.4, 'munger': 3.9, 'lilu': 4.2, 'checklist': 6, 'price': 143.28, 'fpe': 10.45, 'roe': 22.1, 'mcap': 38.8, 'sector': '综合保险'},
    'TMUS': {'composite': 3.5, 'dyp': 4.0, 'buffett': 4.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 5, 'price': 177.19, 'fpe': 12.75, 'roe': 18.0, 'mcap': 190.1, 'sector': '电信'},
    'ALL':  {'composite': 3.75,'dyp': 4.0, 'buffett': 3.5, 'munger': 4.0, 'lilu': 4.0, 'checklist': 5, 'price': 267.00, 'fpe': 9.93, 'roe': 46.1, 'mcap': 67.5, 'sector': 'P&C保险'},
    'PGR':  {'composite': 3.25,'dyp': 4.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 5, 'price': 215.33, 'fpe': 13.30, 'roe': 34.9, 'mcap': 125.2, 'sector': 'P&C保险'},
    'ADBE': {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 5, 'price': 265.21, 'fpe': 9.64, 'roe': 62.95,'mcap': 105.4, 'sector': '软件'},
    'EXEL': {'composite': 3.25,'dyp': 3.5, 'buffett': 3.5, 'munger': 3.0, 'lilu': 3.0, 'checklist': 4, 'price': 54.07,  'fpe': 13.50, 'roe': 44.4, 'mcap': 13.4, 'sector': '医药'},
    'NBIX': {'composite': 3.5, 'dyp': 3.0, 'buffett': 3.5, 'munger': 4.0, 'lilu': 3.5, 'checklist': 6, 'price': 163.41, 'fpe': 16.68, 'roe': 22.1, 'mcap': 16.6, 'sector': '医药'},
    'HRMY': {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 2.5, 'checklist': 5, 'price': 38.41,  'fpe': 9.20, 'roe': 17.9, 'mcap': 2.2, 'sector': '医药'},
    'BWXT': {'composite': 3.4, 'dyp': 4.0, 'buffett': 2.5, 'munger': 4.0, 'lilu': 3.0, 'checklist': 5, 'price': 169.90, 'fpe': 32.17, 'roe': 28.2, 'mcap': 15.6, 'sector': '核燃料'},
    'CRDO': {'composite': 2.5, 'dyp': 3.0, 'buffett': 2.0, 'munger': 3.0, 'lilu': 2.0, 'checklist': 3, 'price': 249.89, 'fpe': 27.64, 'roe': 34.4, 'mcap': 46.6, 'sector': '半导体'},
    'FIS':  {'composite': 2.5, 'dyp': 2.5, 'buffett': 3.0, 'munger': 2.0, 'lilu': 2.5, 'checklist': 3, 'price': 42.77,  'fpe': 6.36, 'roe': 17.2, 'mcap': 22.1, 'sector': '支付'},
    'ANF':  {'composite': 2.0, 'dyp': 2.5, 'buffett': 2.0, 'munger': 2.0, 'lilu': 2.0, 'checklist': 3, 'price': 112.62, 'fpe': 9.61, 'roe': 39.0, 'mcap': 5.0, 'sector': '服装零售'},
}


def pairwise_compare(scores):
    tickers = list(scores.keys())
    n = len(tickers)
    total = n * (n - 1) // 2
    print(f"候选池: {n}只  理论比较: {total}轮")
    win_counts = {t: 0 for t in tickers}
    for i in range(n):
        for j in range(i + 1, n):
            t1, t2 = tickers[i], tickers[j]
            s1, s2 = scores[t1], scores[t2]
            w1, w2 = 0, 0
            for dim in ['composite', 'dyp', 'buffett', 'munger', 'lilu', 'checklist']:
                if s1[dim] > s2[dim]: w1 += 1
                elif s2[dim] > s1[dim]: w2 += 1
            winner = t1 if w1 > w2 else (t2 if w2 > w1 else 'tie')
            if winner != 'tie': win_counts[winner] += 1
    return win_counts


def main():
    print("=" * 65)
    print("  2026-08-09 FRESH 全新研究 — 12只候选6维度冒泡排序")
    print("=" * 65)
    print(f"\n{'Ticker':6s} {'综合':>5s} {'段永平':>5s} {'巴菲特':>5s} {'芒格':>5s} {'李录':>5s} {'6关':>4s} {'价格':>8s} {'fPE':>6s} {'市值(B)':>8s}")
    print('-' * 70)
    for tk, sc in sorted(CANDIDATES.items(), key=lambda x: -x[1]['composite']):
        print(f"{tk:6s} {sc['composite']:5.2f} {sc['dyp']:5.1f} {sc['buffett']:5.1f} "
              f"{sc['munger']:5.1f} {sc['lilu']:5.1f} {sc['checklist']:4d} "
              f"${sc['price']:>7.2f} {sc['fpe']:5.1f}x {sc['mcap']:8.1f}")

    win_counts = pairwise_compare(CANDIDATES)
    print("\n=== 6维度胜率 ===")
    for tk, wins in sorted(win_counts.items(), key=lambda x: -x[1]):
        sc = CANDIDATES[tk]
        bar = '█' * wins
        print(f"  {tk:6s} 综合{sc['composite']:.2f} 胜{wins:2d}场 {bar}")

    print("\n=== 唯二候选 ===")
    top2 = sorted(CANDIDATES.items(), key=lambda x: -x[1]['composite'])[:2]
    for tk, sc in top2:
        print(f"\n{tk} — {sc['sector']} (综合{sc['composite']}/5)")
        print(f"  现价 ${sc['price']} | FwdPE {sc['fpe']}x | ROE {sc['roe']}% | 市值 ${sc['mcap']}B")
        print(f"  段永平{sc['dyp']}/巴菲特{sc['buffett']}/芒格{sc['munger']}/李录{sc['lilu']} | 6关{sc['checklist']}/6")

    with open('reports/fresh-bubble-v5-20260809.json', 'w') as f:
        json.dump({'date': '2026-08-09', 'candidates': len(CANDIDATES),
                   'comparisons': len(CANDIDATES)*(len(CANDIDATES)-1)//2,
                   'scores': CANDIDATES, 'win_counts': dict(sorted(win_counts.items(), key=lambda x:-x[1]))},
                  f, indent=1)
    print("\n结果已保存: reports/fresh-bubble-v5-20260809.json")


if __name__ == '__main__':
    main()