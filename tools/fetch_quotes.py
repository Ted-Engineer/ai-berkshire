#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Real-time quote fetcher with timestamp (hard prerequisite for research).

Contract (referenced by skills/investment-checklist.md 第一步¾):
    python tools/fetch_quotes.py GOOG MSFT

Primary source: Yahoo v8 chart API (1m/1d, includePrePost).
Fallback on failure (e.g. 403): Tencent qt.gtimg.cn (US: usXXX, HK: hkXXXXX).
Prints one line per ticker:
    GOOG | 296.41 | USD | 2026-11-12T16:00:00-05:00 | source=yahoo
Exit codes: 0 = at least one quote fetched, 1 = all failed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request

UA = "Mozilla/5.0 (ai-berkshire research)"


def fetch_yahoo(ticker: str):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?interval=1m&range=1d&includePrePost=true")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    result = data["chart"]["result"][0]
    meta = result["meta"]
    stamps = result.get("timestamp") or []
    closes = (result.get("indicators", {}).get("quote", [{}])[0].get("close")) or []
    price, when = None, None
    for ts, close in zip(reversed(stamps), reversed(closes)):
        if close is not None:
            price, when = float(close), int(ts)
            break
    if price is None:
        price = float(meta["regularMarketPrice"])
        when = int(meta.get("regularMarketTime", 0))
    return price, meta.get("currency", "?"), when


def fetch_tencent(ticker: str):
    code = ticker.upper()
    if re.fullmatch(r"\d{4,5}", code):
        symbol = f"hk{code}"
    else:
        symbol = f"us{code}"
    url = f"https://qt.gtimg.cn/q={symbol}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw = resp.read().decode("gbk", errors="replace")
    parts = raw.split("~")
    if len(parts) < 5 or not parts[3]:
        raise ValueError(f"tencent payload missing price: {raw[:80]}")
    return float(parts[3]), parts[2] or "?", 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch real-time quotes with timestamps")
    parser.add_argument("tickers", nargs="+")
    args = parser.parse_args()

    ok = 0
    for ticker in args.tickers:
        price = currency = None
        ts = 0
        source = "none"
        for name, fetch in (("yahoo", fetch_yahoo), ("tencent", fetch_tencent)):
            try:
                price, currency, ts = fetch(ticker)
                source = name
                break
            except Exception as exc:  # noqa: BLE001 - try next source
                print(f"  [{name}] {ticker} failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        if price is None:
            print(f"FAIL {ticker} | all sources unavailable")
            continue
        ok += 1
        from datetime import datetime, timezone
        stamp = (datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
                 if ts else "unknown-time")
        print(f"{ticker.upper()} | {price} | {currency} | {stamp} | source={source}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
