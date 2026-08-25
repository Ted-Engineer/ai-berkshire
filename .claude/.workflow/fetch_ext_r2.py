import json, urllib.request, datetime
TICKERS = ["BABA","MSFT","META","CRCL","TSM","BRK-B","INTU","APLD","ADBE","PYPL","PGR"]
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
def fmt(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone(datetime.timedelta(hours=-4))).strftime("%m-%d %H:%M")
for t in TICKERS:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1m&range=1d&includePrePost=true"
    try:
        req = urllib.request.Request(url, headers=UA)
        d = json.loads(urllib.request.urlopen(req, timeout=15).read())
        r = d["chart"]["result"][0]
        meta = r["meta"]
        closes = [(ts, c) for ts, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c is not None]
        reg_close = meta.get("chartPreviousClose") or meta.get("previousClose")
        last_ts, last_px = closes[-1]
        # regular session last
        reg_px = None
        for ts, c in closes:
            if 9*3600+30*60 <= (ts % 86400) <= 16*3600:
                reg_px = c
        if reg_px is None: reg_px = reg_close
        chg = (last_px/reg_px - 1)*100 if reg_px else 0
        print(f"{t:6s} reg={reg_px:9.2f} ext={last_px:9.2f} ({fmt(last_ts)} ET) chg={chg:+.2f}%")
    except Exception as e:
        print(f"{t:6s} ERROR {e}")
