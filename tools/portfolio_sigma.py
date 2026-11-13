#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Portfolio sigma / volatility-target calculator.

Contract (referenced by skills/portfolio-rebalance.md):
    python tools/portfolio_sigma.py report \
        --weights '{"GOOG":25.6,"MSFT":4.0,"CASH":26.4}' \
        --vols '{"GOOG":32,"MSFT":22}' \
        --corr '{"GOOG-MSFT":0.55}' \
        --heat-floor 25 --crypto '["MSTR","CAN","CRCL"]'

Rules:
  sigma_p = sqrt(w' * Sigma * w) over assets listed in --vols
  (assets in --weights but absent from --vols are treated as 0-vol, i.e. cash).
  allowed_equity_exposure = min(100, target_sigma / sigma_p * 100)
  vol_cash_floor = 100 - allowed_equity_exposure
  effective_cash_floor = max(heat_floor, vol_cash_floor)

Exit codes: 0 = ok, 2 = hard constraint violated (single position > 15%,
or single crypto position > 10%). Pure stdlib; exact arithmetic, no mental math.
"""

from __future__ import annotations

import argparse
import json
import math
import sys


def parse_corr(spec: dict) -> dict:
    """Accept flat {"A-B": rho} / {"A|B": rho} or nested {"A": {"B": rho}}."""
    pairs: dict = {}
    for key, value in spec.items():
        if isinstance(value, dict):
            for inner, rho in value.items():
                pairs[(key, inner)] = float(rho)
                pairs[(inner, key)] = float(rho)
        else:
            sep = "|" if "|" in key else "-"
            left, right = key.split(sep, 1)
            pairs[(left.strip(), right.strip())] = float(value)
            pairs[(right.strip(), left.strip())] = float(value)
    return pairs


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001 - keep default stream when unsupported
        pass
    parser = argparse.ArgumentParser(description="Volatility-target portfolio calculator")
    sub = parser.add_subparsers(dest="command", required=True)
    report = sub.add_parser("report")
    report.add_argument("--weights", required=True, help="JSON {ticker: weight_percent}")
    report.add_argument("--vols", required=True, help="JSON {ticker: annualized vol_percent}")
    report.add_argument("--corr", default="{}", help="JSON correlation map")
    report.add_argument("--heat-floor", type=float, default=0.0, help="heat-based cash floor percent")
    report.add_argument("--crypto", default="[]", help="JSON list of crypto-related tickers")
    report.add_argument("--leveraged", default="[]", help="JSON list of leveraged-structure tickers (cap 8 percent)")
    report.add_argument("--target-sigma", type=float, default=25.0, help="sigma target percent (default 25)")
    args = parser.parse_args()

    weights = {k: float(v) for k, v in json.loads(args.weights).items()}
    vols = {k: float(v) for k, v in json.loads(args.vols).items()}
    corr = parse_corr(json.loads(args.corr) if args.corr else {})
    crypto = set(json.loads(args.crypto))
    leveraged = set(json.loads(args.leveraged))

    checks = []
    hard_violations = []

    for ticker, weight in sorted(weights.items(), key=lambda kv: -kv[1]):
        if ticker in leveraged and weight > 8.0:
            hard_violations.append(f"leveraged position {ticker} {weight:.2f}% > 8% cap")
        elif ticker in crypto and weight > 10.0:
            hard_violations.append(f"crypto position {ticker} {weight:.2f}% > 10% cap")
        elif ticker not in crypto and weight > 15.0:
            hard_violations.append(f"single position {ticker} {weight:.2f}% > 15% cap")

    risk_assets = [t for t in weights if t in vols]
    variance = 0.0
    for i in risk_assets:
        for j in risk_assets:
            rho = corr.get((i, j), 1.0 if i == j else 0.0)
            wi, wj = weights[i] / 100.0, weights[j] / 100.0
            variance += wi * wj * (vols[i] / 100.0) * (vols[j] / 100.0) * rho
    sigma_p = math.sqrt(variance) * 100.0

    allowed = min(100.0, (args.target_sigma / sigma_p * 100.0) if sigma_p > 0 else 100.0)
    vol_cash_floor = 100.0 - allowed
    effective_floor = max(args.heat_floor, vol_cash_floor)

    equity_weight = sum(weights[t] for t in risk_assets)
    checks.append({"name": "single_position_caps", "ok": not hard_violations,
                   "detail": "; ".join(hard_violations) or "all within caps"})
    checks.append({"name": "equity_exposure_vs_allowed",
                   "ok": equity_weight <= allowed + 1e-9,
                   "detail": f"equity {equity_weight:.2f}% vs allowed {allowed:.2f}%"})

    line = (f"σ_实际={sigma_p:.2f}% | 允许暴露={allowed:.2f}% | "
            f"波动率现金下限={vol_cash_floor:.2f}% | 热度现金下限={args.heat_floor:.2f}% | "
            f"有效现金下限={effective_floor:.2f}%")
    blocked = bool(hard_violations)
    result = {
        "command": args.command,
        "sigma_percent": round(sigma_p, 4),
        "target_sigma_percent": args.target_sigma,
        "allowed_equity_exposure_percent": round(allowed, 4),
        "vol_cash_floor_percent": round(vol_cash_floor, 4),
        "heat_cash_floor_percent": args.heat_floor,
        "effective_cash_floor_percent": round(effective_floor, 4),
        "checks": checks,
        "decision": "block" if blocked else "pass",
        "reasons": hard_violations,
    }
    print(line)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
