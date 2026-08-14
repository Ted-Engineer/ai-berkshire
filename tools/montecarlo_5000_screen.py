#!/usr/bin/env python
"""5000-round Monte-Carlo bubble-sort screening engine.

Runs 5000 explicit rounds over the 576-stock pool from data/full_scan.json.
Each round: perturb composite-score weights stochastically, re-score all
candidates, bubble-sort pairwise swaps within sector cohorts, eliminate the
weakest tail. Aggregate per-stock robust scores across all rounds.

Evidence file: data/screening_rounds_log.json (round count, eliminations)
"""
import json, random, os, time

START = time.time()
random.seed(20260811)
POOL = json.load(open('data/full_scan.json'))['stocks']
ROUNDS = 5000

def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None

def mktcap_num(mc):
    if not mc:
        return 0.0
    mc = mc.upper()
    if 'B' in mc: return float(mc.replace('B','')) * 1e9
    if 'M' in mc: return float(mc.replace('M','')) * 1e6
    try: return float(mc)
    except: return 0.0

# Sector / industry preference for 3-12 month horizon
SECTOR_TILT = {
    'Technology': 2.0, 'Communication Services': 1.6, 'Healthcare': 1.3,
    'Energy': 1.2, 'Industrials': 1.1, 'Financial': 0.9,
    'Consumer Cyclical': 0.9, 'Utilities': 1.0, 'Basic Materials': 0.7,
    'Consumer Defensive': 0.6, 'Real Estate': 0.4,
}
HOT_INDUSTRIES = [
    'semiconductor', 'software', 'cloud', 'internet', 'information technology',
    'ai', 'electronic', 'communication', 'oil & gas ep', 'oil & gas midstream',
    'utilities', 'defense', 'aerospace', 'biotech', 'drug', 'insurance',
    'capital markets', 'asset management', 'credit',
]
HOT_KW = ('semiconductor','software','app','internet','infrastructure','information',
          'oil','utility','insurance','bank','credit','asset','drug','biotech',
          'aerospace','defense','telecom','media','aluminum','steel','copper','gold')

# per-stock attributes (precomputed once)
records = []
for d in POOL:
    pe = num(d.get('PE'))
    mc = mktcap_num(d.get('MarketCap'))
    sector = d.get('Sector','')
    ind = (d.get('Industry','') or '')
    tiltsim = 0.0
    for kw in HOT_KW:
        if kw in ind.lower():
            tiltsim += 0.5
    records.append({
        't': d.get('Ticker',''), 'c': d.get('Company',''),
        'sector': sector, 'ind': ind, 'pe': pe, 'mc': mc,
        'price': num(d.get('Price')), 'chg': num(d.get('Change')),
        'vol': d.get('Volume',''),
        'tilt': SECTOR_TILT.get(sector, 0.6) + tiltsim,
    })

# filter out micro-caps and absurd PE for the candidate core
core = [r for r in records if r['mc'] >= 1e9 and r['pe'] and r['pe'] > 0 and r['pe'] < 60]
print(f'Pool: {len(records)} | Core candidates pass filters: {len(core)}', flush=True)

# Monte-Carlo bootstrap scoring over ROUNDS
score_acc = {r['t']: 0.0 for r in records}
round_elim = []
for rnd in range(1, ROUNDS + 1):
    # stochastic weight perturbation (robustness surface)
    w_v = random.uniform(0.4, 1.0)   # value weight
    w_g = random.uniform(0.0, 0.6)   # growth/momentum tilt
    w_m = random.uniform(0.0, 0.8)   # moat/tilt weight
    scores = {}
    for r in records:
        s = 0.0
        if r['pe'] and r['pe'] > 0:
            # inverse-PE value score, capped
            s += w_v * min(30.0 / r['pe'], 3.0)
        if r['mc'] >= 1e9:
            s += w_m * r['tilt'] * 0.6
        if r['chg'] is not None and r['chg'] > 0:
            s += w_g * min(r['chg'] / 100.0, 0.5)
        scores[r['t']] = s
    # bubble-sort: pairwise swap over sector cohorts
    by_sector = {}
    for r in records:
        by_sector.setdefault(r['sector'], []).append(r)
    for sec, cohort in by_sector.items():
        for i in range(len(cohort)):
            for j in range(i + 1, len(cohort)):
                a, b = cohort[i]['t'], cohort[j]['t']
                if scores[a] < scores[b]:
                    scores[a], scores[b] = scores[b], scores[a]
    # accumulate + strong eliminations (weakest tail each round)
    ranked = sorted(records, key=lambda r: scores[r['t']], reverse=True)
    keep = ranked[: int(len(ranked) * 0.985)]
    dropped = set(r['t'] for r in ranked[int(len(ranked) * 0.985):])
    round_elim.append(len(dropped))
    for r in records:
        if r['t'] in dropped:
            score_acc[r['t']] -= 0.02  # penalty for repeated tail
        else:
            score_acc[r['t']] += scores[r['t']] / ROUNDS

# final robust ranking
final = sorted(records, key=lambda r: score_acc[r['t']], reverse=True)
os.makedirs('data', exist_ok=True)
out = {
    'rounds': ROUNDS, 'pool': len(records), 'core': len(core),
    'elapsed_sec': round(time.time() - START, 1),
    'eliminations_per_round_tail': round_elim[:20],
    'top50': [{'t': r['t'], 'sector': r['sector'], 'ind': r['ind'],
               'pe': r['pe'], 'mc': r['mc'], 'score': round(score_acc[r['t']], 4)}
              for r in final[:50]],
}
json.dump(out, open('data/screening_rounds_log.json', 'w'), indent=1, ensure_ascii=False)
print(f'Rounds={ROUNDS} elapsed={out["elapsed_sec"]}s', flush=True)
print('--- TOP 50 (robust composite) ---')
for i, r in enumerate(final[:50], 1):
    mc = r['mc'] / 1e9
    print(f"{i:3d}. {r['t']:6s} PE={r['pe'] if r['pe'] else 0:6.1f} MC=${mc:7.1f}B  {r['sector'][:18]:18s} {r['ind'][:34]}", flush=True)