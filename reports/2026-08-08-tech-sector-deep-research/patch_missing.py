#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""对 quotes_us.json 的 missing 列表做慢速单票补抓并合并回写。"""
import json, os, sys, time, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_quotes import single, ok, OUT

NAME = sys.argv[1] if len(sys.argv) > 1 else "quotes_us.json"
p = os.path.join(OUT, NAME)
d = json.load(open(p, encoding="utf-8"))
rows = {r["f12"]: r for r in d["rows"]}
miss = list(d["missing"])
print(f"start: rows={len(rows)} miss={len(miss)}", flush=True)

still = []
for t in miss:
    got = None
    for mk in ("105", "106", "107"):
        for attempt in range(3):
            try:
                r = single(f"{mk}.{t}")
            except Exception:
                traceback.print_exc()
                r = None
            if ok(r):
                r["_mkt"] = "US"
                r["_secid"] = f"{mk}.{t}"
                got = r
                break
            time.sleep(1.2 + attempt)
        if got:
            break
    if got:
        rows[t] = got
        print(f"  + {t} {got.get('f14')} {got.get('f2')}", flush=True)
    else:
        still.append(t)
        print(f"  ! {t} still missing", flush=True)
    time.sleep(0.8)

d["rows"] = list(rows.values())
d["missing"] = still
d["patched_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"DONE rows={len(rows)} still_missing={still}", flush=True)
