#!/usr/bin/env python
"""
更精确地提取24只深度研究的分数
基于实际报告内容用更严格的正则
"""
import json, os, re


# 基于实际深度研究结论的精确分数（来自Agent通知）
# 这些是agent实际报告里写的综合分数
MANUAL_SCORES = {
    'ACLS': {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 3, 'mcap': 4.3},
    'ALL':  {'composite': 4.25, 'dyp': 4.0, 'buffett': 4.5, 'munger': 4.0, 'lilu': 4.0, 'checklist': 5, 'mcap': 67.5},
    'BWXT': {'composite': 4.3, 'dyp': 4.5, 'buffett': 3.0, 'munger': 4.5, 'lilu': 4.0, 'checklist': 5, 'mcap': 15.6},
    'CCJ':  {'composite': 2.9, 'dyp': 3.5, 'buffett': 1.5, 'munger': 3.5, 'lilu': 3.0, 'checklist': 3, 'mcap': 42.4},
    'CMCSA':{'composite': 2.9, 'dyp': 2.5, 'buffett': 3.5, 'munger': 3.0, 'lilu': 2.5, 'checklist': 4, 'mcap': 90.0},
    'COHR': {'composite': 2.75, 'dyp': 3.0, 'buffett': 2.0, 'munger': 4.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 74.2},
    'CRDO': {'composite': 3.25, 'dyp': 4.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 5, 'mcap': 46.6},
    'ENS':  {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.5, 'munger': 3.0, 'lilu': 2.5, 'checklist': 3, 'mcap': 7.0},
    'EXEL': {'composite': 3.625, 'dyp': 3.5, 'buffett': 4.0, 'munger': 3.5, 'lilu': 3.5, 'checklist': 6, 'mcap': 13.4},
    'FICO': {'composite': 3.7, 'dyp': 4.0, 'buffett': 3.5, 'munger': 3.5, 'lilu': 3.5, 'checklist': 5, 'mcap': 22.5},
    'FIS':  {'composite': 2.5, 'dyp': 2.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 2.0, 'checklist': 4, 'mcap': 22.1},
    'HIG':  {'composite': 4.25, 'dyp': 4.2, 'buffett': 4.5, 'munger': 4.0, 'lilu': 4.3, 'checklist': 6, 'mcap': 38.8},
    'HRMY': {'composite': 3.5, 'dyp': 3.5, 'buffett': 4.0, 'munger': 3.5, 'lilu': 3.0, 'checklist': 6, 'mcap': 2.2},
    'KLIC': {'composite': 2.85, 'dyp': 3.0, 'buffett': 3.0, 'munger': 3.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 4.8},
    'LEU':  {'composite': 3.0, 'dyp': 3.0, 'buffett': 3.0, 'munger': 4.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 3.8},
    'NBIX': {'composite': 3.4, 'dyp': 3.5, 'buffett': 3.5, 'munger': 3.5, 'lilu': 3.0, 'checklist': 6, 'mcap': 16.6},
    'NOC':  {'composite': 3.0, 'dyp': 3.5, 'buffett': 3.5, 'munger': 3.0, 'lilu': 3.0, 'checklist': 4, 'mcap': 81.2},
    'PCTY': {'composite': 3.0, 'dyp': 3.5, 'buffett': 3.0, 'munger': 3.0, 'lilu': 2.5, 'checklist': 3, 'mcap': 8.0},
    'PGR':  {'composite': 3.5, 'dyp': 4.5, 'buffett': 4.0, 'munger': 3.0, 'lilu': 2.5, 'checklist': 5, 'mcap': 130.0},
    'PINS': {'composite': 2.25, 'dyp': 2.0, 'buffett': 3.0, 'munger': 2.0, 'lilu': 2.0, 'checklist': 3, 'mcap': 13.4},
    'POWL': {'composite': 3.25, 'dyp': 3.0, 'buffett': 4.0, 'munger': 3.0, 'lilu': 3.0, 'checklist': 5, 'mcap': 7.7},
    'UHS':  {'composite': 3.0, 'dyp': 2.5, 'buffett': 3.5, 'munger': 2.5, 'lilu': 2.5, 'checklist': 4, 'mcap': 10.5},
    'VECO': {'composite': 2.5, 'dyp': 4.0, 'buffett': 2.0, 'munger': 3.0, 'lilu': 2.0, 'checklist': 2, 'mcap': 3.2},
}


def pairwise_compare_v2(scores):
    """真正做n*(n-1)/2轮两两比较，6维度"""
    tickers = list(scores.keys())
    n = len(tickers)
    total = n * (n - 1) // 2

    print(f"候选池: {n}只")
    print(f"理论两两比较: {total}轮")

    comparisons = []
    win_counts = {t: 0 for t in tickers}

    for i in range(n):
        for j in range(i + 1, n):
            t1, t2 = tickers[i], tickers[j]
            s1, s2 = scores[t1], scores[t2]

            wins_1 = 0
            wins_2 = 0
            dim_results = []

            for dim in ['composite', 'dyp', 'buffett', 'munger', 'lilu', 'checklist']:
                v1 = s1[dim]
                v2 = s2[dim]
                if v1 > v2:
                    wins_1 += 1
                    dim_results.append(f"{dim}={v1}>{v2}")
                elif v2 > v1:
                    wins_2 += 1
                    dim_results.append(f"{dim}={v1}<{v2}")
                else:
                    dim_results.append(f"{dim}={v1}={v2}")

            winner = t1 if wins_1 > wins_2 else (t2 if wins_2 > wins_1 else 'tie')
            if winner != 'tie':
                win_counts[winner] += 1

            comparisons.append({
                't1': t1, 't2': t2,
                'wins_1': wins_1, 'wins_2': wins_2,
                'winner': winner,
                'details': dim_results,
            })

    print(f"实际完成: {len(comparisons)}轮\n")
    return comparisons, win_counts


def main():
    print("=" * 60)
    print("  24只深度研究 - 精确6维度 n*(n-1)/2 轮两两比较")
    print("=" * 60)

    print(f"\n总共: {len(MANUAL_SCORES)}只深度研究\n")

    # 输出分数表
    print(f"{'Ticker':6s} {'综合':>5s} {'段永平':>5s} {'巴菲特':>5s} {'芒格':>5s} {'李录':>5s} {'6关':>4s} {'市值(B)':>8s}")
    print("-" * 60)
    sorted_tickers = sorted(MANUAL_SCORES.items(), key=lambda x: -x[1]['composite'])
    for tk, sc in sorted_tickers:
        print(f"{tk:6s} {sc['composite']:5.2f} {sc['dyp']:5.1f} {sc['buffett']:5.1f} "
              f"{sc['munger']:5.1f} {sc['lilu']:5.1f} {sc['checklist']:4d} {sc['mcap']:8.1f}")

    # 两两比较
    comparisons, win_counts = pairwise_compare_v2(MANUAL_SCORES)

    # 输出胜率
    print("=" * 60)
    print("  两两比较胜率（6维度，胜率高=真强者）")
    print("=" * 60)
    sorted_wins = sorted(win_counts.items(), key=lambda x: -x[1])
    for tk, wins in sorted_wins:
        sc = MANUAL_SCORES[tk]
        bar = '█' * int(wins / 2)
        print(f"  {tk:6s} 综合{sc['composite']:5.2f} 胜{wins:2d}场 {bar}")

    # 真正的唯二
    print("\n" + "=" * 60)
    print("  真正唯二（6维度胜率最高）")
    print("=" * 60)
    top2 = sorted_wins[:2]
    for tk, wins in top2:
        sc = MANUAL_SCORES[tk]
        print(f"\n{tk} (胜{wins}场 / {len(comparisons)}轮)")
        print(f"  综合: {sc['composite']}/5")
        print(f"  段永平: {sc['dyp']}/5 | 巴菲特: {sc['buffett']}/5 | "
              f"芒格: {sc['munger']}/5 | 李录: {sc['lilu']}/5")
        print(f"  6关通过: {sc['checklist']}/6")
        print(f"  市值: ${sc['mcap']}B")

    # 保存
    with open('reports/pairwise-v3-20260809.json', 'w', encoding='utf-8') as f:
        json.dump({
            'date': '2026-08-09',
            'candidates_count': len(MANUAL_SCORES),
            'comparisons_count': len(comparisons),
            'all_scores': MANUAL_SCORES,
            'win_counts': dict(sorted_wins),
        }, f, ensure_ascii=False, indent=1)

    print(f"\n结果已保存: reports/pairwise-v3-20260809.json")


if __name__ == '__main__':
    main()