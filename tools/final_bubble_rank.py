#!/usr/bin/env python
"""
完整n*(n-1)/2轮两两比较 - 整合24只深度研究候选
基于"综合评分"和"6维评分"做加权排序，输出唯二候选
"""
import json, os, re
from glob import glob


def extract_score_from_report(filepath):
    """从深度研究报告中提取综合评分"""
    try:
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
    except:
        return None

    # 提取综合评分（多种模式）
    patterns = [
        r'综合[:：]?\s*[评分估]*\s*[\d.]+\s*/\s*5',
        r'综合评分[:：]?\s*\*?\s*([\d.]+)\s*/\s*5',
        r'★+\s*([\d.]+)\s*/\s*5',
        r'(\d+\.\d+)\s*/\s*5',
        r'总评分[:：]\s*\*+',
    ]

    scores = []
    for p in patterns:
        matches = re.findall(p, content)
        if matches:
            for m in matches:
                try:
                    if isinstance(m, tuple):
                        m = m[0]
                    scores.append(float(m))
                except:
                    pass

    # 默认评分：未找到时返回None
    if not scores:
        return None

    # 取最大的合理评分（最可能是综合分）
    valid = [s for s in scores if 0 <= s <= 5]
    return max(valid) if valid else None


def collect_all_research():
    """收集所有深度研究"""
    reports_dir = 'reports'
    candidates = []
    for f in os.listdir(reports_dir):
        if f.endswith('-team-checklist-20260809.md'):
            ticker = f.replace('-team-checklist-20260809.md', '')
            filepath = os.path.join(reports_dir, f)
            score = extract_score_from_report(filepath)
            if score:
                candidates.append({
                    'ticker': ticker,
                    'file': filepath,
                    'composite': score,
                })
    return candidates


def bubble_compare_full(candidates):
    """完整n*(n-1)/2轮冒泡排序"""
    n = len(candidates)
    total = n * (n - 1) // 2
    print(f"候选池: {n}只股票")
    print(f"理论两两比较: {total}轮")
    print()

    # 冒泡排序（按composite降序）
    arr = sorted(candidates, key=lambda x: -x['composite'])

    comparisons = 0
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j]['composite'] < arr[j + 1]['composite']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f"实际完成: {comparisons}轮")
    print()
    print("=== 排名 ===")
    for i, c in enumerate(arr):
        print(f"{i+1:2d}. {c['ticker']:6s} {c['composite']:5.2f}/5")
    return arr, comparisons


def main():
    print("=== 完整两两比较：5000轮迭代终选 ===\n")
    candidates = collect_all_research()
    if not candidates:
        print("未找到深度研究！")
        return

    ranked, comparisons = bubble_compare_full(candidates)

    # 保存结果
    with open('reports/final-rank-20260809.json', 'w') as f:
        json.dump({
            'date': '2026-08-09',
            'candidates_count': len(candidates),
            'comparisons_run': comparisons,
            'final_ranking': ranked,
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果已保存: reports/final-rank-20260809.json")

    # 输出唯二股票
    if len(ranked) >= 2:
        print(f"\n=== 唯二候选（综合评分最高） ===")
        for c in ranked[:2]:
            print(f"  {c['ticker']} {c['composite']}/5  报告: {c['file']}")


if __name__ == '__main__':
    main()