import os, json, datetime, urllib3
urllib3.disable_warnings()
import requests
TICKERS = ["BABA","MSFT","META","CRCL","TSM","BRK-B","INTU","APLD","ADBE","PYPL","PGR"]
def fmt(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone(datetime.timedelta(hours=-4))).strftime("%H:%M")
out = {}
for t in TICKERS:
    try:
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1m&range=1d&includePrePost=true'
        r = requests.get(url, verify=False, timeout=15, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'})
        if r.status_code != 200:
            print(f"{t:6s} ERR HTTP {r.status_code}"); continue
        res = r.json()["chart"]["result"][0]
        meta = res["meta"]
        ts_list = res.get("timestamp") or []
        closes = res["indicators"]["quote"][0]["close"]
        pts = [(ts,c) for ts,c in zip(ts_list, closes) if c is not None]
        reg_close = meta.get("chartPreviousClose") or meta.get("previousClose")
        last_ts, last_px = pts[-1] if pts else (None, reg_close)
        chg = (last_px/reg_close-1)*100 if reg_close else 0
        out[t] = {"reg_close": reg_close, "ext": last_px, "chg_pct": round(chg,2)}
        print(f"{t:6s} close={reg_close:9.2f} ext={last_px:9.2f} ({fmt(last_ts)} ET) chg={chg:+.2f}%")
    except Exception as e:
        print(f"{t:6s} ERR {str(e)[:80]}")
with open(".claude/.workflow/ext_prices_r2.json","w") as f: json.dump(out, f, indent=1)
