#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""industry-funnel 机械化四级漏斗筛选（Level 1 -> Level 3）"""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(BASE, "data", "quotes_us.json"), encoding="utf-8"))


def n(v):
    try:
        return float(v)
    except Exception:
        return None


R = []
for r in d["rows"]:
    pe = n(r.get("f115")) or n(r.get("f9"))
    R.append({"t": r.get("f12"), "name": (r.get("f14") or "")[:22],
              "px": n(r.get("f2")), "mc": (n(r.get("f20")) or 0) / 1e9,
              "pe": pe, "pb": n(r.get("f23")),
              "d60": n(r.get("f24")), "ytd": n(r.get("f25")),
              "amt": (n(r.get("f6")) or 0) / 1e6})
R = [x for x in R if x["px"]]

print(f"## Level 1 · 全市场科技股扫描\n\n候选池 **{len(R)}** 只（美股科技/半导体/AI基建/软件/中概科技）\n")

# ---- Level 2: 五条硬指标 ----
gates = []
L2 = []
for x in R:
    fail = []
    if x["mc"] < 5:
        fail.append("市值<$5B")
    if x["pe"] is None or x["pe"] <= 0:
        fail.append("不盈利")
    elif x["pe"] > 35:
        fail.append(f"PE>{35}")
    if x["amt"] < 50:
        fail.append("成交额<$50M")
    if x["ytd"] is not None and x["ytd"] > 120:
        fail.append("YTD>120%(过热)")
    if x["pb"] is not None and x["pb"] > 25:
        fail.append("PB>25")
    if not fail:
        L2.append(x)
    else:
        gates.append((x["t"], fail))

print(f"\n## Level 2 · 五条硬指标粗筛\n")
print("硬指标：① 市值≥$5B ② TTM盈利为正 ③ PE≤35 ④ 日成交额≥$50M ⑤ YTD≤+120% 且 PB≤25\n")
print(f"通过 **{len(L2)}** 只 / 淘汰 {len(gates)} 只\n")
print("| 代码 | 名称 | 收盘$ | 市值$B | PE | PB | 60日% | YTD% |")
print("|---|---|--:|--:|--:|--:|--:|--:|")
for x in sorted(L2, key=lambda y: y["pe"]):
    f = lambda v, k=1: ("-" if v is None else f"{v:,.{k}f}")
    print(f"| {x['t']} | {x['name']} | {f(x['px'],2)} | {f(x['mc'])} | {f(x['pe'])} | "
          f"{f(x['pb'],2)} | {f(x['d60'])} | {f(x['ytd'])} |")

# ---- Level 3: 逆向度 + 质量 ----
print(f"\n## Level 3 · 逆向度排序（被市场抛弃且仍盈利）\n")
print("排序逻辑：YTD 跌幅越大 + PE 越低 = 潜在错杀越深。剔除中概政策风险与非科技主业。\n")
EXCL = {"TCOM", "FUTU", "BILI", "JD", "PDD", "BIDU", "NTES", "BABA",
        "VST", "NRG", "CEG", "FSLR", "ENPH", "HPQ", "PYPL", "HOOD", "COIN", "CRCL"}
L3 = [x for x in L2 if x["t"] not in EXCL and x["ytd"] is not None]
L3.sort(key=lambda y: (y["ytd"]))
print("| 排名 | 代码 | 名称 | 收盘$ | 市值$B | PE | YTD% | 逆向分* |")
print("|--:|---|---|--:|--:|--:|--:|--:|")
for i, x in enumerate(L3[:18], 1):
    score = (-(x["ytd"]) / 10) + max(0, (30 - x["pe"]) / 5)
    print(f"| {i} | {x['t']} | {x['name']} | {x['px']:,.2f} | {x['mc']:,.1f} | "
          f"{x['pe']:,.1f} | {x['ytd']:,.1f} | {score:,.2f} |")
print("\n\\* 逆向分 = (-YTD%/10) + max(0,(30-PE)/5)，越高代表「跌得越狠且越便宜」")

print(f"\n## 被淘汰的代表性标的与原因\n")
key = ["AXTI", "COHR", "MU", "AMAT", "LRCX", "KLAC", "NVDA", "AVGO", "AMD", "PLTR",
       "UCTT", "ICHR", "ONTO", "STX", "WDC", "SNDK", "ARM", "INTC", "TSM", "ANET", "FN"]
print("| 代码 | 未通过原因 |")
print("|---|---|")
for t, f in gates:
    if t in key:
        print(f"| {t} | {'、'.join(f)} |")
