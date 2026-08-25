#!/usr/bin/env python3
# v5.0三刀公式：减仓优先级得分 = 0.5/期望收益排名 + 0.3/赔率排名 + 0.2/不确定性排名（排名1=该维度最差，得分最高最先砍）
# 期望/悲观值来源：reports/portfolio-action-20260820.md §5.4（今日同执行日四大师框架）；BABA为财报后4-Agent更新
# BABA财报后修正：乐观+22%(云重估)/中性+6%/悲观-12% 概率30/45/25 → 期望+5.5%
H = [ # ticker, 期望%, 悲观%, 不确定性排名(1=最不确定), 4Agent评分, 备注
 ("CRCL", -1.0, -45, 1, 2.25, "9/16Arc二元+USDC证伪线;盘前+5.3%动量;风险预算1.80%🔴"),
 ("PYPL",  9.1, -18.4, 2, 3.13, "9/15要约二元+CEO更换;checklist 3/6⚠️"),
 ("APLD", 28.3, -22, 3, 2.75, "爆发仓DNA 5.5/6保护;10/8右侧加仓"),
 ("BABA",  5.5, -12, 4, 3.63, "财报后4Agent更新:云+45%✅ FCF-¥447亿❌;風險1.24%🔴"),
 ("META",  3.2, -15, 5, 3.10, "FCF-91%+折旧潮;$560卖单在场;风险预算1.49%🔴"),
 ("ADBE",  9.0, -10, 6, 3.60, "9/10 Q3+CEO落定;浮盈+25.8%趋势保护"),
 ("INTU", 12.2, -15, 7, 4.00, "8/25财报5天;浮盈+13.2%"),
 ("TSM",  11.1, -22, 8, 4.55, "最高分;$390买单;浮亏-1.7%"),
 ("MSFT",  4.4, -12.9, 9, 3.70, "浮盈+45%趋势保护+$436移动止损"),
 ("PGR",   5.4, -10, 10, 4.40, "9/16月报<1月;赔率0.54>0.5→绝对不砍保护"),
 ("BRK.B", 2.4, -8.9, 11, 4.13, "最稳但期望最低带;$488买单在场"),
]
odds = {t: (e/abs(p) if e>0 else 0.0) for t,e,p,u,s,n in H}
rank_exp = {t:i+1 for i,(t,*_) in enumerate(sorted(H,key=lambda x:x[1]))}
rank_odds= {t:i+1 for i,t in enumerate(sorted(odds,key=lambda k:odds[k]))}
rows=[]
for t,e,p,u,s,n in H:
    score = 0.5/rank_exp[t] + 0.3/rank_odds[t] + 0.2/u
    rows.append((score,t,e,odds[t],u,s,n))
rows.sort(reverse=True)
print(f"{'砍序':4s} {'标的':6s} {'得分':>6s} {'期望%':>6s} {'赔率':>5s} {'不确定#':>7s} {'4A分':>5s}  保护/备注")
for i,(sc,t,e,o,u,s,n) in enumerate(rows,1):
    print(f"#{i:<3d} {t:6s} {sc:6.3f} {e:+6.1f} {o:5.2f} {u:7d} {s:5.2f}  {n}")
