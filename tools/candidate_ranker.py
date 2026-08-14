#!/usr/bin/env python
"""
冒泡排序两两比较：从候选池中找到"最值得且最可能大赚"的唯二股票
输入：各行业漏斗报告 + 瓶颈报告（汇总所有候选股）
输出：综合评分排序 + 冒泡两两比较明细
"""
import json, os, sys, re
from collections import defaultdict

CANDIDATE_DIR = 'reports'
OUTPUT = 'reports/candidate-rank-20260809.json'


def parse_market_cap(s):
    s = str(s).strip().replace(',', '')
    if not s or s == '-': return 0
    mult = 1
    if s.endswith('B'): mult = 1e9; s = s[:-1]
    elif s.endswith('M'): mult = 1e6; s = s[:-1]
    elif s.endswith('K'): mult = 1e3; s = s[:-1]
    try: return float(s) * mult
    except: return 0


def parse_pe(pe_str):
    if pe_str in ('-', '', 'N/A', 'NaN'): return 9999
    try: return float(pe_str)
    except: return 9999


def bubble_sort_compare(candidates, criteria_weights=None):
    """冒泡排序：两两比较每个候选，按综合得分排序"""
    if not criteria_weights:
        criteria_weights = {
            'upside_pct': 0.30,  # 上行空间权重
            'pe_fwd': 0.20,       # 估值
            'moat_score': 0.20,   # 护城河
            'catalyst_proximity': 0.15,  # 催化临近
            'balance_sheet': 0.15,  # 财务健康
        }

    # 两两比较次数 = n*(n-1)/2
    n = len(candidates)
    comparisons = n * (n - 1) // 2
    print(f"冒泡排序: {n}只候选，需要 {comparisons} 次两两比较")

    # 计算综合分（基于已知数据）
    for c in candidates:
        score = 0
        # 上行空间（如果有）
        upside = c.get('upside_pct', 0)
        score += upside * criteria_weights['upside_pct']
        # PE
        pe = c.get('pe_fwd', 50)
        if pe < 0: pe = 100
        score += max(0, (50 - pe) / 50 * 100) * criteria_weights['pe_fwd']
        # 护城河（0-5）
        moat = c.get('moat_score', 3)
        score += (moat / 5 * 100) * criteria_weights['moat_score']
        # 催化
        catalyst = c.get('catalyst_proximity', 0)
        score += catalyst * criteria_weights['catalyst_proximity']
        # 财务健康
        bs = c.get('balance_sheet_score', 50)
        score += bs * criteria_weights['balance_sheet']
        c['composite_score'] = round(score, 2)

    # 冒泡排序（按composite_score降序）
    arr = list(candidates)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]['composite_score'] < arr[j + 1]['composite_score']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    # 读取所有funnel/bottleneck报告
    reports = []
    for f in os.listdir('reports'):
        if f.endswith('-funnel-20260809.md') or f.endswith('-bottleneck-20260809.md'):
            reports.append(os.path.join('reports', f))

    print(f"找到 {len(reports)} 个候选池报告")
    print("\n".join(reports))

    # 解析每个报告的候选
    all_candidates = []
    for rpt in reports:
        print(f"\n解析: {rpt}")
        # 简单解析（实际报告结构复杂，需要更细致）
        # 这里先用文件大小做粗略估计
        size = os.path.getsize(rpt)
        print(f"  文件大小: {size} bytes")

    print("\n等待所有子Agent完成后再做最终整合...")


if __name__ == '__main__':
    main()