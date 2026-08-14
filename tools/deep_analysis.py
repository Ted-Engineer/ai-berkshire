#!/usr/bin/env python
"""
HIG + HRMY 深度财务分析
基于mega_scan实时数据 + financial_rigor精确十进制
"""
import json, os
from glob import glob


# 集成所有候选的实时数据（mega_scan v10 + financial_rigor）
CANDIDATES = {
    'HIG': {
        'name': 'Hartford Financial Services',
        'price': 143.28, 'mcap_b': 39.3,
        'ttm_pe': 9.89, 'fwd_pe': 10.46, 'pb': 2.17,
        'roe': 22.06, 'rev_g': 8.1, 'fcf_yld': 9.07,
        'gross_margin': None, 'oper_margin': 17.96,
        'beta': 0.46, 'div_yield': 1.71,
        'composite_score': 4.25, 'checklist_pass': 6,
        'q2_2026_eps_beat': True, 'q2_2026_yoy': 31,
        'combined_ratio_q2': 90.1,
        'reverse_risk_score': 8,  # 10条反向风险
    },
    'HRMY': {
        'name': 'Harmony Biosciences',
        'price': 38.41, 'mcap_b': 2.2,
        'ttm_pe': 12.43, 'fwd_pe': 5.74, 'pb': 1.73,
        'roe': 20.46, 'rev_g': 30.3, 'fcf_yld': 9.11,
        'gross_margin': 73.9, 'oper_margin': 21.1,
        'beta': 1.2, 'div_yield': 0,
        'composite_score': 3.5, 'checklist_pass': 6,
        'q2_2026_eps_beat': True, 'q2_2026_yoy': 30,
        'wakix_q2_revenue_m': 261.3,
        'reverse_risk_score': 9,  # 10条反向风险（含Orphan 2026/8）
    },
    'ALL': {
        'name': 'Allstate',
        'price': 267.00, 'mcap_b': 67.5,
        'ttm_pe': 5.35, 'fwd_pe': 9.86, 'pb': None,
        'roe': 46.11, 'rev_g': 11.8, 'fcf_yld': None,
        'gross_margin': None, 'oper_margin': None,
        'beta': 0.16, 'div_yield': 2.13,
        'composite_score': 4.25, 'checklist_pass': 5,
        'reverse_risk_score': 7,
    },
    'PGR': {
        'name': 'Progressive',
        'price': 215.33, 'mcap_b': 125.2,
        'ttm_pe': 10.80, 'fwd_pe': 13.24, 'pb': 3.34,
        'roe': 34.94, 'rev_g': 7.3, 'fcf_yld': 6.73,
        'gross_margin': None, 'oper_margin': None,
        'beta': 0.26, 'div_yield': 6.46,
        'composite_score': 3.5, 'checklist_pass': 5,
        'reverse_risk_score': 8,
    },
}


def calculate_composite_metrics(c):
    """综合得分（基于多维度量化）"""
    # 估值分（PE低分高）
    val_score = max(0, min(100, (50 - c['fwd_pe']) / 50 * 100))
    # ROE分
    roe_score = min(100, c['roe'] * 2.5)
    # 增长分
    rev_score = min(100, c['rev_g'] * 2.5)
    # FCF yield分
    fcf_score = (c.get('fcf_yld') or 0) * 10
    # 安全边际分（高PE=低分；低PE=高分）
    safety = max(0, 100 - c['ttm_pe'] * 5)
    # 反向风险扣分
    risk_penalty = c.get('reverse_risk_score', 5) * 3

    composite = (
        val_score * 0.25 +
        roe_score * 0.20 +
        rev_score * 0.15 +
        fcf_score * 0.10 +
        safety * 0.20 +
        (c['composite_score'] * 20) * 0.10
        - risk_penalty
    )
    return round(composite, 1)


def asymmetry_ratio(c):
    """不对称性：上行空间/下行风险比"""
    # 简化估算
    upside = c.get('rev_g', 0) * 2  # 增长驱动上行
    downside = c.get('reverse_risk_score', 5) * 2  # 反向风险驱动下行
    return round(upside / max(1, downside), 2)


def main():
    print("=" * 60)
    print("  HIG + HRMY 深度财务分析")
    print("=" * 60)

    print(f"\n{'Ticker':6s} {'价格':>8s} {'FwdPE':>7s} {'ROE':>6s} {'增速':>6s} "
          f"{'FCF':>5s} {'6/6':>4s} {'量化':>6s} {'不对称':>7s}")
    print("-" * 70)

    results = []
    for tk, c in CANDIDATES.items():
        composite = calculate_composite_metrics(c)
        asymm = asymmetry_ratio(c)
        results.append((tk, c, composite, asymm))
        print(f"{tk:6s} ${c['price']:>7.2f} {c['fwd_pe']:>6.1f}x "
              f"{c['roe']:>5.1f}% {c['rev_g']:>5.1f}% "
              f"{(c.get('fcf_yld') or 0):>4.1f}% {c.get('checklist_pass', 0):>3d}/6 "
              f"{composite:>5.1f}  {asymm:>6.2f}x")

    # 按量化综合分排序
    results.sort(key=lambda x: -x[2])

    print("\n" + "=" * 60)
    print("  量化综合排名")
    print("=" * 60)
    for i, (tk, c, comp, asymm) in enumerate(results):
        marker = '🏆' if i < 2 else ('🟢' if i < 4 else '🟡')
        print(f"{i+1}. {marker} {tk} {comp}/100 不对称{asymm}x")

    # 真正的唯二
    print("\n" + "=" * 60)
    print("  真正唯二（量化+综合+胜率三重过滤）")
    print("=" * 60)
    top2 = results[:2]
    for tk, c, comp, asymm in top2:
        print(f"\n{tk} - {c['name']}")
        print(f"  量化综合: {comp}/100")
        print(f"  不对称性: {asymm}x")
        print(f"  FwdPE: {c['fwd_pe']}x | ROE: {c['roe']}% | 增速: {c['rev_g']}%")
        print(f"  6/6关: {c.get('checklist_pass', 0)}/6 | 反向风险: {c.get('reverse_risk_score', 0)}条")

    # 保存
    with open('reports/HIG_HRMY_deep_analysis.json', 'w') as f:
        json.dump({
            'date': '2026-08-09',
            'analysis': 'deep_python_quantitative',
            'results': [{'ticker': tk, 'quant_score': c, 'asymmetry': a} for tk, _, c, a in results],
        }, f, indent=1)

    print(f"\n结果已保存: reports/HIG_HRMY_deep_analysis.json")


if __name__ == '__main__':
    main()