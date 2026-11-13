#!/usr/bin/env bash
# Stage gate for the portfolio-rebalance workflow (ZCode/hook-free fallback).
#
# Contract (referenced by skills/portfolio-rebalance.md 阶段门禁点):
#   bash scripts/workflow-gate-hook.sh step2|step3|step5
#
# Reads workflow state from .claude/.workflow/ and prints a JSON verdict.
# decision:block = the stage did not pass; fix per reasons before proceeding.
# Always exits 0 (the decision field governs).
set -uo pipefail

STAGE="${1:-}"
WF=".claude/.workflow"

json_escape() { printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'; }

pass="true"
reasons=""
check() { # name ok detail
  local name="$1" ok="$2" detail="$3"
  printf '    {"name": "%s", "ok": %s, "detail": "%s"},\n' \
    "$(json_escape "$name")" "$ok" "$(json_escape "$detail")"
  if [ "$ok" != "true" ]; then
    pass="false"
    reasons="${reasons}${name}: ${detail}; "
  fi
}

count_done() { ls "$WF" 2>/dev/null | grep -c "$1" || true; }
count_lines() { [ -f "$1" ] && wc -l < "$1" | tr -d ' ' || echo 0; }

case "$STAGE" in
  step2)
    n=$(count_done '^investment-team-.*\.done$')
    check "investment_team_done" "$([ "${n:-0}" -ge 1 ] && echo true || echo false)" "found ${n:-0} investment-team .done markers (need >=1)"
    ;;
  step3)
    n=$(count_done '^investment-team-.*\.done$')
    check "investment_team_done" "$([ "${n:-0}" -ge 1 ] && echo true || echo false)" "found ${n:-0} investment-team .done markers (need >=1)"
    n=$(count_done '^investment-checklist-.*\.done$')
    check "checklist_done" "$([ "${n:-0}" -ge 1 ] && echo true || echo false)" "found ${n:-0} checklist .done markers (need >=1)"
    n=$(count_done '^industry-funnel-.*\.done$')
    m=$(count_done '^bottleneck-hunter-.*\.done$')
    check "funnel_bottleneck_done" "$([ $((n + m)) -ge 1 ] && echo true || echo false)" "funnel=${n:-0} bottleneck=${m:-0} (need >=1 combined)"
    cands=$(count_lines "$WF/candidates.csv")
    check "candidates_pool" "$([ "${cands:-0}" -ge 300 ] && echo true || echo false)" "candidates.csv has ${cands:-0} lines (need >=300)"
    searches=$(count_lines "$WF/search-log.txt")
    check "search_volume" "$([ "${searches:-0}" -ge 110 ] && echo true || echo false)" "search-log.txt has ${searches:-0} entries (need >=110)"
    h=$(grep -c "H-爆发股" "$WF/candidates.csv" 2>/dev/null || echo 0)
    i=$(grep -c "I-" "$WF/candidates.csv" 2>/dev/null || echo 0)
    check "hunter_sources" "$([ "${h:-0}" -ge 1 ] && [ "${i:-0}" -ge 1 ] && echo true || echo false)" "H-burst=${h:-0} I-repair=${i:-0} (need >=1 each)"
    used=$(ls "$WF"/*.used 2>/dev/null | head -1)
    check "search_tool_marker" "$([ -n "$used" ] && echo true || echo false)" "no .used marker found in $WF"
    ;;
  step5)
    rb="$WF/recommended-buys.txt"
    if [ ! -f "$rb" ]; then
      check "recommended_buys" "false" "missing $rb"
    elif grep -q "^# no new buys" "$rb"; then
      check "recommended_buys" "true" "no new buys declared"
    else
      missing=""
      while read -r t; do
        [ -z "$t" ] && continue
        ls "$WF"/investment-checklist-"$t"-*.done >/dev/null 2>&1 || missing="$missing $t"
      done < "$rb"
      check "recommended_buys" "$([ -z "$missing" ] && echo true || echo false)" "missing checklist .done for:${missing:- none}"
    fi
    ;;
  *)
    echo '{"stage": "'"$(json_escape "$STAGE")"'", "decision": "block", "reasons": "unknown stage; use step2|step3|step5"}'
    exit 0
    ;;
esac

decision=$([ "$pass" = "true" ] && echo pass || echo block)
printf '{\n  "stage": "%s",\n  "decision": "%s",\n  "reasons": "%s",\n  "checks": [\n' \
  "$(json_escape "$STAGE")" "$decision" "$(json_escape "$reasons")"
# drop trailing comma of last check line
awk 'NR>1{print prev} {prev=$0} END{sub(/,$/, "", prev); print prev}'
printf '  ]\n}\n'
