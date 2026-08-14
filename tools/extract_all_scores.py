#!/usr/bin/env python
"""
提取所有24只深度研究的详细分数，做真正的n*(n-1)/2轮两两比较
从每个-team-checklist报告提取综合分+4维度分+6关关数
"""
import json, os, re
from glob import glob


def extract_scores_from_report(filepath):
    """从单个深度研究报告中提取详细分数"""
    try:
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
    except:
        return None

    # 提取综合分
    composite_patterns = [
        r'综合[评分估]*\s*\*?\s*([\d.]+)\s*/\s*5',
        r'综合[:：]\s*\**\s*([\d.]+)\s*/\s*5',
        r'★+\s*([\d.]+)\s*/\s*5',
        r'([\d.]+)\s*/\s*5',
    ]

    composite = None
    for p in composite_patterns:
        matches = re.findall(p, content)
        if matches:
            valid = [float(m) for m in matches if 0 <= float(m) <= 5]
            if valid:
                composite = max(valid)
                break

    # 提取四维度评分
    dyp_score = extract_dimension(content, ['段永平', '段永平视角', 'dyp', '生意本质'])
    buffett_score = extract_dimension(content, ['巴菲特', '巴菲特视角', 'buffett', '财务估值'])
    munger_score = extract_dimension(content, ['芒格', '芒格视角', 'munger', '行业'])
    lilu_score = extract_dimension(content, ['李录', '李录视角', 'lilu', '管理层'])

    # 提取6关通过数
    checklist_passed = 6
    m6 = re.search(r'(\d)\s*/\s*6\s*[关过]', content)
    if m6:
        checklist_passed = int(m6.group(1))

    # 提取市值
    mcap_match = re.search(r'市值[：:约]?\s*\$?([\d.]+)\s*B', content)
    mcap = float(mcap_match.group(1)) if mcap_match else None

    return {
        'composite': composite,
        'dyp': dyp_score,
        'buffett': buffett_score,
        'munger': munger_score,
        'lilu': lilu_score,
        'checklist_passed': checklist_passed,
        'mcap_b': mcap,
    }


def extract_dimension(content, keywords):
    """提取特定维度的评分"""
    for kw in keywords:
        # 在关键词后面找分数
        pat = re.compile(rf'{kw}[^★\n]*?★+\s*\*?\s*([\d.]+)\s*/\s*5', re.MULTILINE)
        m = pat.search(content)
        if m:
            try:
                return float(m.group(1))
            except:
                pass
    return None


def collect_all_scores():
    """收集所有深度研究的分数"""
    reports_dir = 'reports'
    all_scores = {}

    for f in os.listdir(reports_dir):
        if f.endswith('-team-checklist-20260809.md'):
            ticker = f.replace('-team-checklist-20260809.md', '')
            filepath = os.path.join(reports_dir, f)
            scores = extract_scores_from_report(filepath)
            if scores and scores['composite']:
                all_scores[ticker] = scores

    return all_scores


def pairwise_compare(scores_dict):
    """真正做n*(n-1)/2轮两两比较"""
    tickers = list(scores_dict.keys())
    n = len(tickers)
    total_comparisons = n * (n - 1) // 2

    print(f"候选池: {n}只")
    print(f"理论两两比较: {total_comparisons}轮")

    comparisons = []
    for i in range(n):
        for j in range(i + 1, n):
            t1, t2 = tickers[i], tickers[j]
            s1, s2 = scores_dict[t1], scores_dict[t2]

            # 多维度对比
            wins_1 = 0
            wins_2 = 0
            dimensions = []

            for dim in ['composite', 'dyp', 'buffett', 'munger', 'lilu', 'checklist_passed']:
                v1 = s1.get(dim)
                v2 = s2.get(dim)
                if v1 is not None and v2 is not None:
                    if v1 > v2:
                        wins_1 += 1
                        dimensions.append(f"{dim}: {t1}胜")
                    elif v2 > v1:
                        wins_2 += 1
                        dimensions.append(f"{dim}: {t2}胜")
                    else:
                        dimensions.append(f"{dim}: 平")

            winner = t1 if wins_1 > wins_2 else (t2 if wins_2 > wins_1 else '平')
            comparisons.append({
                't1': t1,
                't2': t2,
                's1_composite': s1.get('composite'),
                's2_composite': s2.get('composite'),
                'wins_1': wins_1,
                'wins_2': wins_2,
                'winner': winner,
                'dimensions': dimensions,
            })

    print(f"实际完成: {len(comparisons)}轮\n")
    return comparisons


def main():
    print("=" * 60)
    print("  从24只深度研究提取详细分数 + 真正n*(n-1)/2轮两两比较")
    print("=" * 60)

    all_scores = collect_all_scores()
    print(f"\n成功提取: {len(all_scores)}只深度研究的分数")

    # 输出提取的分数
    print("\n=== 详细分数 ===")
    print(f"{'Ticker':6s} {'综合':>5s} {'段永平':>5s} {'巴菲特':>5s} {'芒格':>5s} {'李录':>5s} {'6关':>4s}")
    for tk, sc in sorted(all_scores.items(), key=lambda x: -x[1].get('composite', 0)):
        print(f"{tk:6s} {sc.get('composite',0):5.2f} "
              f"{sc.get('dyp',0) or 0:5.1f} "
              f"{sc.get('buffett',0) or 0:5.1f} "
              f"{sc.get('munger',0) or 0:5.1f} "
              f"{sc.get('lilu',0) or 0:5.1f} "
              f"{sc.get('checklist_passed',0):4d}")

    # 两两比较
    comparisons = pairwise_compare(all_scores)

    # 输出唯二候选的胜率
    win_counts = {}
    for c in comparisons:
        winner = c['winner']
        if winner != '平':
            win_counts[winner] = win_counts.get(winner, 0) + 1

    print("\n=== 两两比较胜率（详细证据） ===")
    sorted_wins = sorted(win_counts.items(), key=lambda x: -x[1])
    for tk, wins in sorted_wins[:10]:
        sc = all_scores[tk]
        print(f"  {tk:6s} 综合{sc.get('composite',0):.2f} 胜{wins}场")

    # 保存
    output = {
        'date': '2026-08-09',
        'candidates_count': len(all_scores),
        'comparisons_count': len(comparisons),
        'all_scores': all_scores,
        'win_counts': win_counts,
        'sorted_wins': sorted_wins,
    }
    with open('reports/pairwise-evidence-20260809.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=1)

    print(f"\n结果已保存: reports/pairwise-evidence-20260809.json")


if __name__ == '__main__':
    main()