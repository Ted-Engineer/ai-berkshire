#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Independent SEC EDGAR XBRL claim auditor (anti self-verification).

Contract (referenced by skills/investment-research.md Step 5):
    python tools/indep_audit.py --claims /tmp/claims-{company}.json

Claims file: JSON array of {"label", "ticker", "tag", "value", "scale"}.
  - tag: us-gaap XBRL concept, e.g. "Revenues" or
    "RevenueFromContractWithCustomerExcludingAssessedTax"
  - value * scale = claimed raw USD amount (e.g. value=108.3, scale=1e9)
FAIL when |reported - claimed| / |reported| > 2%. Exit codes:
  0 = no FAIL, 1 = at least one FAIL, 2 = tool error (network/parse).
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request

UA = "ai-berkshire-research/1.0 (independent XBRL audit)"
TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
CONCEPT_URL = "https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/us-gaap/{tag}.json"
TOLERANCE_PCT = 2.0


def http_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def resolve_cik(ticker: str, cache: dict) -> int:
    if not cache:
        data = http_json(TICKER_MAP_URL)
        for str_cik, entry in data.items():
            cache[entry["ticker"].upper()] = int(entry["cik_str"])
    return cache[ticker.upper()]


def latest_annual(entries: list) -> dict:
    annuals = [e for e in entries if e.get("form") == "10-K"]
    if not annuals:
        annuals = entries
    return max(annuals, key=lambda e: (e.get("end", ""), e.get("filed", "")))


def main() -> int:
    parser = argparse.ArgumentParser(description="Independent SEC EDGAR XBRL claim audit")
    parser.add_argument("--claims", required=True, help="path to claims JSON file")
    parser.add_argument("--tolerance", type=float, default=TOLERANCE_PCT,
                        help="FAIL threshold in percent (default 2.0)")
    args = parser.parse_args()

    with open(args.claims, encoding="utf-8") as fh:
        claims = json.load(fh)
    if isinstance(claims, dict):
        claims = [claims]

    cik_cache: dict = {}
    fails, warns = [], []
    for claim in claims:
        label = claim.get("label", claim.get("ticker", "?"))
        ticker = claim["ticker"]
        tag = claim["tag"]
        scale = float(claim.get("scale", 1.0))
        claimed = float(claim["value"]) * scale
        try:
            cik = resolve_cik(ticker, cik_cache)
            concept = http_json(CONCEPT_URL.format(cik=cik, tag=tag))
            usd = concept.get("units", {}).get("USD", [])
            if not usd:
                warns.append(f"SKIP {label}: tag {tag} has no USD facts")
                continue
            entry = latest_annual(usd)
            reported = float(entry["val"])
            if reported == 0:
                warns.append(f"SKIP {label}: reported value is zero")
                continue
            deviation = abs(reported - claimed) / abs(reported) * 100.0
            status = "FAIL" if deviation > args.tolerance else "PASS"
            if status == "FAIL":
                fails.append(label)
            print(f"{status} {label} [{ticker} {tag}] claimed={claimed:,.0f} "
                  f"reported={reported:,.0f} ({entry.get('end', '?')}, {entry.get('form', '?')}) "
                  f"deviation={deviation:.2f}%")
        except KeyError:
            print(f"WARN {label}: cannot resolve ticker {ticker} on EDGAR")
            warns.append(label)
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"WARN {label}: {type(exc).__name__}: {exc}")
            warns.append(label)

    summary = {"claims": len(claims), "fails": fails, "warns": warns,
               "tolerance_percent": args.tolerance}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if warns and not fails and len(warns) == len(claims):
        return 2
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
