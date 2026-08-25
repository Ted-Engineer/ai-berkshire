#!/usr/bin/env python3
"""Fetch latest close + afterhours/premarket last trade via Yahoo v8 chart API."""
import json, sys, urllib.request, datetime

TICKERS = ["BABA","MSFT","META","ADBE","TSM","BRK-B","INTU","APLD","PYPL","CRCL","PGR","^NDX","^VIX","NVDA","BTC-USD"]
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def fetch(sym):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1m&range=1d&includePrePost=true"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.loads(r.read())
    res = d["chart"]["result"][0]
    meta = res["meta"]
    ts = res.get("timestamp") or []
    closes = (res["indicators"]["quote"][0].get("close") or [])
    # last valid trade overall (incl pre/post)
    last_ts = last_px = None
    for t, c in zip(ts, closes):
        if c is not None:
            last_ts, last_px = t, c
    regular = meta.get("regularMarketPrice")
    prev_close = meta.get("chartPreviousClose") or meta.get("previousClose")
    session = ""
    if last_ts:
        dt = datetime.datetime.fromtimestamp(last_ts, datetime.timezone(datetime.timedelta(hours=-4)))
        hm = dt.hour*60 + dt.minute
        session = "post" if hm >= 960 else ("pre" if hm < 570 else "regular")
    return {
        "sym": sym, "regular": regular, "prevClose": prev_close,
        "last": last_px, "lastTs": (datetime.datetime.fromtimestamp(last_ts, datetime.timezone(datetime.timedelta(hours=-4))).strftime("%m-%d %H:%M ET") if last_ts else None),
        "session": session,
        "dayHigh52": meta.get("fiftyTwoWeekHigh"), "dayLow52": meta.get("fiftyTwoWeekLow"),
    }

for s in TICKERS:
    try:
        m = fetch(s)
        chg_ext = (m["last"]/m["regular"]-1)*100 if (m["last"] and m["regular"]) else None
        print(f"{s:8s} reg={m['regular']:<10} last={m['last']:<10.4f} @ {m['lastTs']} ({m['session']}) extChg={chg_ext:+.2f}% 52wH={m['dayHigh52']}" if m["last"] else f"{s:8s} FAIL {m}")
    except Exception as e:
        print(f"{s:8s} ERROR {e}")
