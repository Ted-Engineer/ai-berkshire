#!/usr/bin/env python
"""
2026-08-09 持仓10股冒泡排序 — 6维度两两比较
数据源：Finviz实时(Fri 8/7 close) + financial_rigor精确验算
维度：综合 + 段永平(商业模式) + 巴菲特(财务估值) + 芒格(行业格局) + 李录(管理层) + Checklist(6关)
"""
import json

HOLDINGS = {
    'BABA':  {'composite': 2.25, 'dyp': 2.5, 'buffett': 2.0, 'munger': 2.5, 'lilu': 2.0, 'checklist': 3,
              'price': 128.41, 'fpe': 14.37, 'roe': 10.16, 'mcap': 307.8, 'sector': '中国电商',
              'position_pct': 38.5, 'bull': 32.0, 'base': -10.2, 'bear': -44.2},
    'MSFT':  {'composite': 4.13, 'dyp': 4.5, 'buffett': 3.5, 'munger': 4.5, 'lilu': 4.0, 'checklist': 5,
              'price': 499.99, 'fpe': 21.30, 'roe': 34.04, 'mcap': 3712.7, 'sector': 'AI云软件',
              'position_pct': 21.9, 'bull': 73.7, 'base': 31.0, 'bear': -14.0},
    'ADBE':  {'composite': 3.75, 'dyp': 3.5, 'buffett': 5.0, 'munger': 3.5, 'lilu': 3.0, 'checklist': 5,
              'price': 265.21, 'fpe': 9.64, 'roe': 62.95, 'mcap': 105.4, 'sector': '创意软件',
              'position_pct': 8.1, 'bull': 80.4, 'base': 22.8, 'bear': -23.7},
    'BRK.B': {'composite': 4.25, 'dyp': 4.0, 'buffett': 4.0, 'munger': 4.5, 'lilu': 4.5, 'checklist': 6,
              'price': 521.80, 'fpe': 24.24, 'roe': 10.49, 'mcap': 1011.6, 'sector': '综合保险/控股',
              'position_pct': 5.5, 'bull': 30.0, 'base': 12.0, 'bear': -8.0},
    'INTU':  {'composite': 3.63, 'dyp': 4.0, 'buffett': 4.0, 'munger': 4.0, 'lilu': 2.5, 'checklist': 4,
              'price': 325.25, 'fpe': 11.87, 'roe': 22.50, 'mcap': 89.0, 'sector': '财税软件',
              'position_pct': 4.8, 'bull': 69.8, 'base': 28.4, 'bear': -10.5},
    'QCOM':  {'composite': 3.25, 'dyp': 3.0, 'buffett': 3.5, 'munger': 3.5, 'lilu': 3.0, 'checklist': 4,
              'price': 167.86, 'fpe': 16.31, 'roe': 33.75, 'mcap': 176.3, 'sector': '半导体/通信',
              'position_pct': 2.0, 'bull': 29.7, 'base': -10.0, 'bear': -41.9},
    'TSM':   {'composite': 3.88, 'dyp': 4.0, 'buffett': 4.0, 'munger': 4.5, 'lilu': 3.0, 'checklist': 4,
              'price': 420.04, 'fpe': 19.39, 'roe': 40.06, 'mcap': 2178.5, 'sector': '半导体代工',
              'position_pct': 2.2, 'bull': 103.0, 'base': 25.4, 'bear': -29.7},
    'TLN':   {'composite': 1.88, 'dyp': 2.0, 'buffett': 1.5, 'munger': 2.5, 'lilu': 1.5, 'checklist': 2,
              'price': 347.71, 'fpe': 10.93, 'roe': -12.93, 'mcap': 16.7, 'sector': 'AI电力',
              'position_pct': 1.8, 'bull': 53.1, 'base': 0.0, 'bear': -26.8},
    'RARE':  {'composite': 1.25, 'dyp': 1.0, 'buffett': 1.0, 'munger': 2.0, 'lilu': 1.0, 'checklist': 1,
              'price': 25.91, 'fpe': None, 'roe': -656.5, 'mcap': 2.6, 'sector': '生物科技',
              'position_pct': 1.8, 'bull': 100.0, 'base': 0.0, 'bear': -50.0},
    'CRCL':  {'composite': 1.38, 'dyp': 1.5, 'buffett': 1.0, 'munger': 2.0, 'lilu': 1.0, 'checklist': 2,
              'price': 66.67, 'fpe': 46.69, 'roe': 15.35, 'mcap': 16.9, 'sector': '稳定币/加密',
              'position_pct': 0.4, 'bull': 80.0, 'base': 0.0, 'bear': -40.0},
}


def pairwise_compare(scores):
    tickers = list(scores.keys())
    n = len(tickers)
    total = n * (n - 1) // 2
    print(f"候选池: {n}只  理论比较: {total}轮")
    win_counts = {t: 0 for t in tickers}
    detail = []
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
            detail.append((t1, t2, w1, w2, winner))
    return win_counts, detail


def main():
    print("=" * 75)
    print("  2026-08-09 持仓10股 — 四大师+Checklist 6维度冒泡排序")
    print("  数据基准: Finviz Fri 8/7 close | financial_rigor.py 验算")
    print("=" * 75)
    print(f"\n{'Ticker':7s} {'综合':>5s} {'段':>4s} {'巴':>4s} {'芒':>4s} {'李':>4s} {'关':>4s} "
          f"{'价格':>8s} {'fPE':>6s} {'ROE%':>6s} {'仓位%':>5s} {'乐观':>6s} {'中性':>6s} {'悲观':>6s}")
    print('-' * 90)
    for tk, sc in sorted(HOLDINGS.items(), key=lambda x: -x[1]['composite']):
        fpe_str = f"{sc['fpe']:.1f}" if sc['fpe'] else "—"
        print(f"{tk:7s} {sc['composite']:5.2f} {sc['dyp']:4.1f} {sc['buffett']:4.1f} "
              f"{sc['munger']:4.1f} {sc['lilu']:4.1f} {sc['checklist']:4d} "
              f"${sc['price']:>7.2f} {fpe_str:>5s}x {sc['roe']:6.1f} {sc['position_pct']:5.1f} "
              f"{sc['bull']:>+5.1f}% {sc['base']:>+5.1f}% {sc['bear']:>+5.1f}%")

    win_counts, detail = pairwise_compare(HOLDINGS)
    print(f"\n{'='*50}")
    print("6维度胜率排名（n*(n-1)/2 = 45轮）")
    print(f"{'='*50}")
    for tk, wins in sorted(win_counts.items(), key=lambda x: -x[1]):
        sc = HOLDINGS[tk]
        bar = '█' * wins
        print(f"  {tk:7s} {wins:2d}胜/9场  综合{sc['composite']:.2f}  {bar}")

    print(f"\n{'='*50}")
    print("持仓操作优先级排序")
    print(f"{'='*50}")
    for tk, wins in sorted(win_counts.items(), key=lambda x: -x[1]):
        sc = HOLDINGS[tk]
        if sc['composite'] >= 4.0:
            action = "🟢 持有（核心仓）"
        elif sc['composite'] >= 3.5:
            action = "🟡 持有/条件加仓"
        elif sc['composite'] >= 3.0:
            action = "🔵 持有（观察）"
        elif sc['composite'] >= 2.0:
            action = "🟠 减仓"
        else:
            action = "🔴 事件驱动持有"
        print(f"  {tk:7s} {sc['composite']:.2f}/5  {sc['position_pct']:5.1f}%仓位  {action}")

    with open('reports/portfolio-bubble-0810.json', 'w') as f:
        json.dump({'date': '2026-08-09', 'holdings': len(HOLDINGS),
                   'comparisons': len(HOLDINGS)*(len(HOLDINGS)-1)//2,
                   'scores': HOLDINGS,
                   'win_counts': dict(sorted(win_counts.items(), key=lambda x:-x[1]))},
                  f, indent=1, ensure_ascii=False)
    print("\n结果已保存: reports/portfolio-bubble-0810.json")


if __name__ == '__main__':
    main()
