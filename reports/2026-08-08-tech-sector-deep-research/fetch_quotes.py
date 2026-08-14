#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""定向候选池实时取数 v2（小批次 + 重试 + 单票兜底；自动解析 105/106/107）"""
import json, time, sys, random, urllib.request, urllib.parse, os

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36",
      "Referer": "https://quote.eastmoney.com/"}
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "data")
os.makedirs(OUT, exist_ok=True)
HOSTS = ["push2", "1.push2", "7.push2", "23.push2", "push2delay", "12.push2",
         "33.push2", "44.push2", "56.push2", "60.push2"]
FIELDS = ("f1,f2,f3,f5,f6,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,"
          "f23,f24,f25,f26,f100,f115,f184")


def get(path, retry=6):
    for i in range(retry):
        h = HOSTS[(i + random.randrange(len(HOSTS))) % len(HOSTS)]
        try:
            req = urllib.request.Request(f"https://{h}.eastmoney.com{path}", headers=UA)
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            time.sleep(0.8 + 1.2 * i)
    return None


def ulist(secids):
    path = (f"/api/qt/ulist.np/get?secids={','.join(secids)}"
            f"&fltt=2&invt=2&fields={FIELDS}")
    d = get(path)
    if not d or not d.get("data"):
        return []
    diff = d["data"].get("diff") or []
    if isinstance(diff, dict):
        diff = list(diff.values())
    return diff


def single(secid):
    d = get(f"/api/qt/stock/get?secid={secid}&fltt=2&invt=2&fields={FIELDS}")
    if not d or not d.get("data"):
        return None
    return d["data"]


def ok(r):
    return r and r.get("f12") and r.get("f2") not in (None, "-", 0)


def resolve(tickers, markets=("105", "106", "107"), chunk=10):
    found = {}
    for mk in markets:
        todo = [t for t in tickers if t not in found]
        if not todo:
            break
        for i in range(0, len(todo), chunk):
            batch = todo[i:i + chunk]
            for attempt in range(3):
                rows = ulist([f"{mk}.{t}" for t in batch])
                hit = 0
                for r in rows:
                    c = r.get("f12")
                    if ok(r) and c not in found:
                        r["_mkt"] = "US"
                        r["_secid"] = f"{mk}.{c}"
                        found[c] = r
                        hit += 1
                if rows:
                    break
                time.sleep(1.5 + attempt)
            time.sleep(0.9)
        print(f"  m:{mk} -> {len(found)}/{len(tickers)}", file=sys.stderr, flush=True)

    # 单票兜底
    miss = [t for t in tickers if t not in found]
    if miss:
        print(f"  fallback singles for {len(miss)}", file=sys.stderr, flush=True)
        for t in miss:
            for mk in markets:
                r = single(f"{mk}.{t}")
                if ok(r):
                    r["_mkt"] = "US"
                    r["_secid"] = f"{mk}.{t}"
                    found[t] = r
                    break
                time.sleep(0.35)
            time.sleep(0.35)
    return found


if __name__ == "__main__":
    tickers = [t.strip().upper() for t in open(sys.argv[1], encoding="utf-8").read().split() if t.strip()]
    tickers = list(dict.fromkeys(tickers))
    print(f"resolving {len(tickers)} tickers", file=sys.stderr, flush=True)
    found = resolve(tickers)
    miss = [t for t in tickers if t not in found]
    name = sys.argv[2] if len(sys.argv) > 2 else "quotes.json"
    json.dump({"fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"),
               "rows": list(found.values()), "missing": miss},
              open(os.path.join(OUT, name), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"OK {len(found)}/{len(tickers)}, missing={miss}")
