#!/usr/bin/env python
"""
30只深度研究 — 最终6维度n*(n-1)/2轮两两比较
"""
import json, os, re

# 基于实际深度研究报告的综合+4维度评分（从agent通知整合）
SCORES = {
    'ACLS': {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 3, 'mcap': 4.3, 'fpe': 26.6, 'roe': 8.9},
    'ALL':  {'composite': 4.25, 'dyp': 4.0, 'buffett': 4.5, 'munger': 4.0, 'lilu': 4.0, 'checklist': 5, 'mcap': 67.5, 'fpe': 9.9, 'roe': 46.1},
    'APD':  {'composite': 3.0, 'dyp': 4.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 3, 'mcap': 67.6, 'fpe': 21.0, 'roe': 0.0},
    'ARCC': {'composite': 3.1, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.5, 'checklist': 3, 'mcap': 14.4, 'fpe': 10.4, 'roe': 6.9},
    'BWXT': {'composite': 4.3, 'dyp': 4.5, 'buffett': 3.0, 'munger': 4.5, 'lilu': 4.0, 'checklist': 5, 'mcap': 15.6, 'fpe': 32.3, 'roe': 28.3},
    'CCJ':  {'composite': 2.9, 'dyp': 3.5, 'buffett': 1.5, 'munger': 3.5, 'lilu': 3.0, 'checklist': 3, 'mcap': 42.4, 'fpe': 53.0, 'roe': 5.0},
    'CHRW': {'composite': 2.25, 'dyp': 2.0, 'buffett': 2.0, 'munger': 3.0, 'lilu': 2.0, 'checklist': 4, 'mcap': 17.5, 'fpe': 19.9, 'roe': 37.1},
    'CMCSA':{'composite': 2.9, 'dyp': 2.5, 'buffett': 3.5, 'munger': 3.0, 'lilu': 2.5, 'checklist': 4, 'mcap': 90.0, 'fpe': 7.0, 'roe': 12.0},
    'COHR': {'composite': 2.75, 'dyp': 3.0, 'buffett': 2.0, 'munger': 4.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 74.2, 'fpe': 45.3, 'roe': 4.7},
    'COO':  {'composite': 2.5, 'dyp': 2.5, 'buffett': 2.5, 'munger': 2.5, 'lilu': 2.5, 'checklist': 3, 'mcap': 14.5, 'fpe': 14.9, 'roe': 2.9},
    'CRDO': {'composite': 3.25, 'dyp': 4.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 5, 'mcap': 46.6, 'fpe': 27.6, 'roe': 34.0},
    'DKS':  {'composite': 3.5, 'dyp': 3.5, 'buffett': 3.5, 'munger': 3.5, 'lilu': 3.5, 'checklist': 5, 'mcap': 18.7, 'fpe': 12.8, 'roe': 20.9},
    'ENS':  {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.5, 'munger': 3.0, 'lilu': 2.5, 'checklist': 3, 'mcap': 7.0, 'fpe': 14.4, 'roe': 15.3},
    'EXEL': {'composite': 3.625, 'dyp': 3.5, 'buffett': 4.0, 'munger': 3.5, 'lilu': 3.5, 'checklist': 6, 'mcap': 13.4, 'fpe': 13.3, 'roe': 44.4},
    'FICO': {'composite': 3.7, 'dyp': 4.0, 'buffett': 3.5, 'munger': 3.5, 'lilu': 3.5, 'checklist': 5, 'mcap': 22.5, 'fpe': 19.6, 'roe': 0.0},
    'FIS':  {'composite': 2.5, 'dyp': 2.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 2.0, 'checklist': 4, 'mcap': 22.1, 'fpe': 6.4, 'roe': 17.2},
    'GIL':  {'composite': 3.2, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 4.0, 'checklist': 4, 'mcap': 10.6, 'fpe': 10.4, 'roe': 8.7},
    'HIG':  {'composite': 4.25, 'dyp': 4.2, 'buffett': 4.5, 'munger': 4.0, 'lilu': 4.3, 'checklist': 6, 'mcap': 38.8, 'fpe': 10.5, 'roe': 22.1},
    'HRMY': {'composite': 3.5, 'dyp': 3.5, 'buffett': 4.0, 'munger': 3.5, 'lilu': 3.0, 'checklist': 6, 'mcap': 2.2, 'fpe': 5.7, 'roe': 20.5},
    'KLIC': {'composite': 2.85, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 4.8, 'fpe': 16.1, 'roe': 13.2},
    'LEU':  {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.0, 'munger': 4.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 3.8, 'fpe': 53.2, 'roe': 8.1},
    'NBIX': {'composite': 3.4, 'dyp': 3.5, 'buffett': 3.5, 'munger': 3.5, 'lilu': 3.0, 'checklist': 6, 'mcap': 16.6, 'fpe': 13.4, 'roe': 22.1},
    'NOC':  {'composite': 3.0, 'dyp': 3.5, 'buffett': 3.5, 'munger': 3.0, 'lilu': 3.0, 'checklist': 4, 'mcap': 81.2, 'fpe': 18.8, 'roe': 27.0},
    'PCTY': {'composite': 3.0, 'dyp': 3.5, 'buffett': 3.0, 'munger': 3.0, 'lilu': 2.5, 'checklist': 3, 'mcap': 8.0, 'fpe': 17.0, 'roe': 22.0},
    'PGR':  {'composite': 3.5, 'dyp': 4.5, 'buffett': 4.0, 'munger': 3.0, 'lilu': 2.5, 'checklist': 5, 'mcap': 125.2, 'fpe': 13.2, 'roe': 34.9},
    'PINS': {'composite': 2.25, 'dyp': 2.0, 'buffett': 3.0, 'munger': 2.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 13.4, 'fpe': 9.8, 'roe': 6.5},
    'POWL': {'composite': 3.25, 'dyp': 3.0, 'buffett': 4.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 5, 'mcap': 7.7, 'fpe': 31.1, 'roe': 28.3},
    'UHS':  {'composite': 3.0, 'dyp': 2.5, 'buffett': 3.5, 'munger': 2.5, 'lilu': 2.5, 'checklist': 4, 'mcap': 10.5, 'fpe': 7.2, 'roe': 20.9},
    'VICI': {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.5, 'munger': 3.0, 'lilu': 2.5, 'checklist': 4, 'mcap': 29.4, 'fpe': 9.1, 'roe': 9.8},
    'WLK':  {'composite': 2.0, 'dyp': 1.5, 'buffett': 2.0, 'munger': 2.0, 'lilu': 2.5, 'checklist': 2, 'mcap': 9.9, 'fpe': 23.5, 'roe': -11.9},
    'WPC':  {'composite': 2.75, 'dyp': 2.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 4, 'mcap': 16.4, 'fpe': 20.7, 'roe': 7.8},
}


def pairwise_compare(scores):
    tickers = list(scores.keys())
    n = len(tickers)
    total = n * (n - 1) // 2

    print(f"\n候选池: {n}只")
    print(f"理论两两比较: {total}轮")

    win_counts = {t: 0 for t in tickers}
    comparisons = []

    for i in range(n):
        for j in range(i + 1, n):
            t1, t2 = tickers[i], tickers[j]
            s1, s2 = scores[t1], scores[t2]

            wins_1 = 0
            wins_2 = 0
            for dim in ['composite', 'dyp', 'buffett', 'munger', 'lilu', 'checklist']:
                v1, v2 = s1[dim], s2[dim]
                if v1 > v2:
                    wins_1 += 1
                elif v2 > v1:
                    wins_2 += 1

            winner = t1 if wins_1 > wins_2 else (t2 if wins_2 > wins_1 else 'tie')
            if winner != 'tie':
                win_counts[winner] += 1

            comparisons.append((t1, t2, winner, wins_1, wins_2))

    return comparisons, win_counts


def main():
    print("=" * 60)
    print("  30只深度研究 — 6维度 n*(n-1)/2 轮两两比较")
    print("=" * 60)

    print(f"\n总共: {len(SCORES)}只")

    print(f"\n{'Ticker':6s} {'综合':>5s} {'段永平':>5s} {'巴菲特':>5s} {'芒格':>5s} {'李录':>5s} {'6关':>4s} {'市值':>8s}")
    print('-' * 60)
    for tk, sc in sorted(SCORES.items(), key=lambda x: -x[1]['composite']):
        print(f"{tk:6s} {sc['composite']:5.2f} {sc['dyp']:5.1f} {sc['buffett']:5.1f} "
              f"{sc['munger']:5.1f} {sc['lilu']:5.1f} {sc['checklist']:4d} {sc['mcap']:8.1f}")

    comparisons, win_counts = pairwise_compare(SCORES)

    print("\n" + "=" * 60)
    print("  两两比较胜率（30只候选，6维度）")
    print("=" * 60)
    sorted_wins = sorted(win_counts.items(), key=lambda x: -x[1])
    for tk, wins in sorted_wins:
        sc = SCORES[tk]
        print(f"  {tk:6s} 综合{sc['composite']:.2f} 胜{wins:2d}场")

    # 真正的唯二（综合最高）
    print("\n" + "=" * 60)
    print("  真正唯二（综合评分最高）")
    print("=" * 60)
    top2 = sorted(SCORES.items(), key=lambda x: -x[1]['composite'])[:2]
    for tk, sc in top2:
        print(f"\n{tk} (综合{sc['composite']}/5)")
        print(f"  段永平: {sc['dyp']}/5 | 巴菲特: {sc['buffett']}/5 | "
              f"芒格: {sc['munger']}/5 | 李录: {sc['lilu']}/5")
        print(f"  6关: {sc['checklist']}/6 | 市值: ${sc['mcap']}B | FwdPE: {sc['fpe']}x")

    # 保存
    with open('reports/pairwise-v4-20260809.json', 'w') as f:
        json.dump({
            'date': '2026-08-09',
            'candidates_count': len(SCORES),
            'all_scores': SCORES,
            'win_counts': dict(sorted_wins),
        }, f, indent=1)

    print(f"\n结果已保存: reports/pairwise-v4-20260809.json")


if __name__ == '__main__':
    main()