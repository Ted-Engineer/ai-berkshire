#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""全市场科技股实时扫描器 — 东方财富行情源（多主机轮换 + 断点续传）
industry-funnel 第一层：A(成交活跃) ∪ B(60日涨幅) ∪ C(市值锚定)
"""
import json, time, sys, random, urllib.request, urllib.parse, os

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36",
      "Referer": "https://quote.eastmoney.com/"}
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "data")
os.makedirs(OUT, exist_ok=True)
CKPT = os.path.join(OUT, "universe_raw.json")

HOSTS = ["push2", "1.push2", "7.push2", "23.push2", "push2delay",
         "12.push2", "33.push2", "44.push2", "56.push2", "60.push2"]
FIELDS = "f1,f2,f3,f5,f6,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,f23,f24,f25,f26,f100,f115,f184"

MARKETS = {
    "US": "m:105,m:106,m:107",
    "HK": "m:128+t:3,m:128+t:4,m:128+t:1,m:128+t:2",
    "A":  "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23",
}
SORTS = {"C": "f20", "A": "f6", "B": "f24"}
DEPTH = {"US": {"C": 12, "A": 5, "B": 5}, "HK": {"C": 6, "A": 3, "B": 3}, "A": {"C": 8, "A": 4, "B": 4}}

store = {}
if os.path.exists(CKPT):
    try:
        old = json.load(open(CKPT, encoding="utf-8"))
        for r in old.get("rows", []):
            store[f"{r['_mkt']}|{r['f12']}"] = r
        print(f"resume {len(store)} rows", file=sys.stderr)
    except Exception:
        pass

done_pages = set()
DONE = os.path.join(OUT, "_pages_done.json")
if os.path.exists(DONE):
    done_pages = set(json.load(open(DONE)))


def save():
    json.dump({"fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"), "rows": list(store.values())},
              open(CKPT, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(sorted(done_pages), open(DONE, "w"))


def get(path, retry=8):
    for i in range(retry):
        h = HOSTS[(i + random.randrange(len(HOSTS))) % len(HOSTS)]
        try:
            req = urllib.request.Request(f"https://{h}.eastmoney.com{path}", headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            time.sleep(1.2 + 1.8 * i)
    return None


def scan(mkt, fs, tag, fid, pages):
    got = 0
    for pn in range(1, pages + 1):
        pk = f"{mkt}|{tag}|{pn}"
        if pk in done_pages:
            continue
        path = (f"/api/qt/clist/get?pn={pn}&pz=100&po=1&np=1&fltt=2&invt=2&fid={fid}"
                f"&fs={urllib.parse.quote(fs)}&fields={FIELDS}")
        d = get(path)
        if not d or not d.get("data"):
            print(f"  [{mkt}/{tag}] p{pn} EMPTY", file=sys.stderr)
            time.sleep(4)
            continue
        diff = d["data"].get("diff") or []
        if isinstance(diff, dict):
            diff = list(diff.values())
        if not diff:
            done_pages.add(pk)
            break
        for it in diff:
            k = f"{mkt}|{it.get('f12')}"
            it["_mkt"] = mkt
            if k in store:
                store[k]["_cls"] = "".join(sorted(set(store[k].get("_cls", "") + tag)))
            else:
                it["_cls"] = tag
                store[k] = it
        got += len(diff)
        done_pages.add(pk)
        if pn % 3 == 0:
            save()
        time.sleep(1.6 + random.random())
    print(f"  [{mkt}/{tag}] +{got} (store={len(store)})", file=sys.stderr)


if __name__ == "__main__":
    for mkt, fs in MARKETS.items():
        print(f"=== {mkt} ===", file=sys.stderr)
        for tag, fid in SORTS.items():
            scan(mkt, fs, tag, fid, DEPTH[mkt][tag])
            save()
            time.sleep(2)
    save()
    bym = {}
    for r in store.values():
        bym[r["_mkt"]] = bym.get(r["_mkt"], 0) + 1
    print(json.dumps(bym, ensure_ascii=False, indent=2))
    print(f"TOTAL {len(store)} rows")
