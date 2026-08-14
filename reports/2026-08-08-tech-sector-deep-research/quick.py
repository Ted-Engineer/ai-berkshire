#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""终选名单快速实时取数（单票接口，最稳）"""
import json, time, sys, random, urllib.request, os

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36",
      "Referer": "https://quote.eastmoney.com/"}
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "data")
os.makedirs(OUT, exist_ok=True)
HOSTS = ["push2", "1.push2", "7.push2", "23.push2", "push2delay", "12.push2",
         "33.push2", "44.push2", "56.push2", "60.push2"]
F2 = "f1,f2,f3,f5,f6,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,f23,f24,f25,f26,f100,f115,f184"

LIST = [
    ("105", ["ADBE", "MU", "INTU", "AXTI", "FN", "COHR", "LITE", "AMAT", "LRCX", "KLAC",
             "UCTT", "ICHR", "ONTO", "ENTG", "MRVL", "AVGO", "NVDA", "CRDO", "WDAY",
             "PANW", "GOOGL", "META", "MSFT", "QCOM", "AMD", "AMKR", "TER", "CIEN",
             "AAOI", "ALAB", "SNDK", "WDC", "STX", "PLTR", "ARM", "GFS", "NXPI", "SMCI"]),
    ("106", ["CRM", "ANET", "TSM", "GLW", "ORCL", "NOW", "IBM", "ACN", "VRT", "BABA",
             "ETN", "PWR", "TLN", "DELL", "HPE", "NET", "S", "TWLO", "SQ"]),
]


def get(path, retry=5):
    for i in range(retry):
        h = HOSTS[(i + random.randrange(len(HOSTS))) % len(HOSTS)]
        try:
            req = urllib.request.Request(f"https://{h}.eastmoney.com{path}", headers=UA)
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            time.sleep(0.6 + 0.8 * i)
    return None


rows = []
miss = []
for mk, ts in LIST:
    for t in ts:
        d = get(f"/api/qt/stock/get?secid={mk}.{t}&fltt=2&invt=2&fields={F2}")
        r = (d or {}).get("data")
        if r and r.get("f2") not in (None, "-", 0):
            r["_secid"] = f"{mk}.{t}"
            rows.append(r)
            print(f"{t:6s} {r.get('f2'):>10} {str(r.get('f3')):>8}%  PE={r.get('f115')} "
                  f"PB={r.get('f23')} MC={r.get('f20')} 60d={r.get('f24')} ytd={r.get('f25')}",
                  flush=True)
        else:
            miss.append(t)
        time.sleep(0.25)

json.dump({"fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"), "rows": rows, "missing": miss},
          open(os.path.join(OUT, "quick.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"\nOK {len(rows)}, miss={miss}")
