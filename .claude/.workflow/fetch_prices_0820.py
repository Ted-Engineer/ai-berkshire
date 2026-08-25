#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量获取持仓+指数的 Yahoo v8 chart 数据：收盘价 + 盘前/夜盘最后成交价"""
import json, urllib.request, time, sys

TICKERS = ["BABA","MSFT","META","ADBE","TSM","BRK-B","INTU","APLD","PYPL","CRCL","PGR","^NDX","^VIX","BTC-USD","^GSPC"]

def fetch(t):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1m&range=1d&includePrePost=true"
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)

def analyze(t):
    d = fetch(t)
    res = d["chart"]["result"][0]
    meta = res["meta"]
    ts = res.get("timestamp") or []
    q = res["indicators"]["quote"][0]
    closes = q["close"]
    pairs = [(x,c) for x,c in zip(ts,closes) if c is not None]
    if not pairs:
        return None
    reg_price = meta.get("regularMarketPrice")
    reg_time = meta.get("regularMarketTime")
    prev_close = meta.get("chartPreviousClose") or meta.get("previousClose")
    # 最后一个有效成交
    last_ts, last_px = pairs[-1]
    last_et = time.strftime("%m-%d %H:%M", time.gmtime(last_ts - 4*3600))  # 粗略ET(EDT=UTC-4)
    # 判定时段: regularMarketTime 之后 = 盘后
    session = "盘前/夜盘" if (reg_time and last_ts > reg_time + 60) else "常规时段"
    # 若最后一个点 == regularMarketTime 附近, 则为收盘价
    if reg_time and abs(last_ts - reg_time) <= 90:
        session = "收盘"
    chg_vs_close = None
    if reg_price and session != "收盘" and reg_price:
        chg_vs_close = (last_px - reg_price) / reg_price * 100
    return {
        "ticker": t,
        "currency": meta.get("currency"),
        "prev_close": prev_close,
        "regular_price": reg_price,
        "regular_time_et": time.strftime("%m-%d %H:%M", time.gmtime(reg_time - 4*3600)) if reg_time else None,
        "last_price": round(last_px, 2),
        "last_time_et": last_et,
        "session": session,
        "delayed_vs_close_pct": round(chg_vs_close, 2) if chg_vs_close is not None else None,
        "fifty_two_week_high": meta.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": meta.get("fiftyTwoWeekLow"),
    }

out = []
for t in TICKERS:
    try:
        r = analyze(t)
        if r: out.append(r)
        time.sleep(0.4)
    except Exception as e:
        out.append({"ticker": t, "error": str(e)})

for r in out:
    print(json.dumps(r, ensure_ascii=False))
