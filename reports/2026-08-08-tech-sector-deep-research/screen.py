#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""候选池结构化筛选表：估值 / 涨幅 / 市值，输出 markdown + 分组。"""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "data", sys.argv[1] if len(sys.argv) > 1 else "quotes_us.json")
d = json.load(open(p, encoding="utf-8"))
rows = d["rows"]


def num(v):
    try:
        f = float(v)
        return f
    except Exception:
        return None


recs = []
for r in rows:
    recs.append({
        "t": r.get("f12"),
        "name": (r.get("f14") or "")[:28],
        "px": num(r.get("f2")),
        "chg": num(r.get("f3")),
        "mc": (num(r.get("f20")) or 0) / 1e9,
        "pe": num(r.get("f115")) if num(r.get("f115")) else num(r.get("f9")),
        "pb": num(r.get("f23")),
        "d60": num(r.get("f24")),
        "ytd": num(r.get("f25")),
        "ind": r.get("f100") or "",
    })

recs = [x for x in recs if x["px"]]
print(f"# 候选池实时快照  ({d.get('fetched_at')}  patched:{d.get('patched_at','-')})")
print(f"共 {len(recs)} 只 | 数据源: 东方财富 push2 (美股 2026-08-07 收盘)\n")

def table(title, sel, key, rev=False, n=100):
    s = sorted([x for x in recs if sel(x)], key=key, reverse=rev)[:n]
    print(f"\n## {title}  ({len(s)})\n")
    print("| 代码 | 名称 | 收盘$ | 涨跌% | 市值$B | PE | PB | 60日% | YTD% |")
    print("|---|---|--:|--:|--:|--:|--:|--:|--:|")
    for x in s:
        f = lambda v, d=1: ("-" if v is None else f"{v:,.{d}f}")
        print(f"| {x['t']} | {x['name']} | {f(x['px'],2)} | {f(x['chg'])} | {f(x['mc'])} | "
              f"{f(x['pe'])} | {f(x['pb'],2)} | {f(x['d60'])} | {f(x['ytd'])} |")


# A. 估值合理 + 盈利 (PE 0~30)
table("A. 盈利且 PE<30（估值可接受区）", lambda x: x["pe"] and 0 < x["pe"] < 30, lambda x: x["pe"])
# B. PE 30~60
table("B. PE 30-60（偏贵但可讨论）", lambda x: x["pe"] and 30 <= x["pe"] < 60, lambda x: x["pe"])
# C. 过热 PE>60 或亏损
table("C. PE>60 / 亏损（估值红灯）", lambda x: (x["pe"] is None) or x["pe"] >= 60 or x["pe"] < 0,
      lambda x: -(x["ytd"] or -999), True)
# D. YTD 落后（被错杀候选）
table("D. YTD 落后榜（<+15%，含下跌）", lambda x: x["ytd"] is not None and x["ytd"] < 15,
      lambda x: x["ytd"])
