#!/usr/bin/env bash
# =============================================================================
# run-investment-team-all.sh — 按持仓权重顺序，逐一执行 /investment-team 团队投研
#
# 用法（Git Bash，在仓库根目录）：
#   ./scripts/run-investment-team-all.sh              # 全部持仓，按默认顺序
#   ./scripts/run-investment-team-all.sh META BABA    # 只跑指定票
#   ./scripts/run-investment-team-all.sh --list       # 只看今日进度，不执行
#   FORCE=1 ./scripts/run-investment-team-all.sh      # 已有今日报告也重跑
#
# 两种执行模式：
#   1) 自动模式：设置 ZCODE_CMD 环境变量为「可无头执行的 CLI + 参数前缀」，
#      脚本会逐票调用：$ZCODE_CMD "/investment-team <TICKER>"
#      例：  ZCODE_CMD='zcode -p' ./scripts/run-investment-team-all.sh
#            ZCODE_CMD='claude -p --permission-mode acceptEdits' ./scripts/...
#      （当前机器未发现可无头调用的 zcode 二进制；若你的 ZCode 版本支持
#        无头模式，把确切命令填进 ZCODE_CMD 即可，无需改脚本。）
#   2) 手动模式（默认）：逐票打印应粘贴的命令，人工回车推进下一只——
#      适配 GUI 交互式会话，同样享受断点续跑（今日已有报告的票自动跳过）。
#
# 断点续跑：reports/*/最终报告-*<TICKER>*-<今天日期>.md 已存在则跳过，
#           FORCE=1 可强制重跑。日志在 reports/investment-team-batch/<日期>/。
# =============================================================================
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

TODAY="$(date +%Y%m%d)"
LOG_DIR="reports/investment-team-batch/${TODAY}"
SLEEP_SECS="${SLEEP_SECS:-10}"   # 自动模式下两只票之间的间隔秒数

# 默认持仓清单：权重降序（来源 reports/portfolio-latest.md，2026-08-17 调仓执行版：CI出、NRG进）
# 调仓后请同步更新此数组。
DEFAULT_TICKERS=(META BABA MSFT ADBE AVGO BRK.B INTU TSM PYPL VST NRG)

# -----------------------------------------------------------------------------
report_exists() {  # 今日已有该票的最终报告 → 0
  local t="$1"
  compgen -G "reports/*/最终报告-*${t}*-${TODAY}.md" > /dev/null
}

usage() {
  sed -n '2,23p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit 0
}

# -----------------------------------------------------------------------------
# 参数解析
MODE="run"
if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then usage; fi
if [[ "${1:-}" == "--list" ]]; then MODE="list"; shift; fi

if [[ $# -gt 0 ]]; then
  TICKERS=("$@")
else
  TICKERS=("${DEFAULT_TICKERS[@]}")
fi

# -----------------------------------------------------------------------------
if [[ "$MODE" == "list" ]]; then
  echo "=== /investment-team 今日进度（${TODAY}）==="
  for t in "${TICKERS[@]}"; do
    if report_exists "$t"; then
      echo "  [x] $t  → $(compgen -G "reports/*/最终报告-*${t}*-${TODAY}.md" | head -1)"
    else
      echo "  [ ] $t"
    fi
  done
  exit 0
fi

DONE_LIST=(); SKIP_LIST=(); FAIL_LIST=()
FORCE="${FORCE:-0}"

echo "=== /investment-team 批量执行（${TODAY}，共 ${#TICKERS[@]} 只）==="
if [[ -n "${ZCODE_CMD:-}" ]]; then
  echo "模式：自动（ZCODE_CMD='${ZCODE_CMD}'，间隔 ${SLEEP_SECS}s）"
else
  echo "模式：手动（未设置 ZCODE_CMD——逐票打印命令，回车推进；--list 可查进度）"
fi
echo

for t in "${TICKERS[@]}"; do
  if [[ "$FORCE" != "1" ]] && report_exists "$t"; then
    echo "[$t] 今日报告已存在，跳过（FORCE=1 可重跑）"
    SKIP_LIST+=("$t")
    continue
  fi

  if [[ -n "${ZCODE_CMD:-}" ]]; then
    mkdir -p "$LOG_DIR"
    echo "[$t] 执行：${ZCODE_CMD} \"/investment-team ${t}\" ..."
    # shellcheck disable=SC2086  # ZCODE_CMD 有意按词拆分（命令+固定参数）
    if $ZCODE_CMD "/investment-team ${t}" > "${LOG_DIR}/${t}.log" 2>&1; then
      echo "[$t] ✅ 完成，日志：${LOG_DIR}/${t}.log"
      DONE_LIST+=("$t")
    else
      echo "[$t] ❌ 失败（exit $?），日志：${LOG_DIR}/${t}.log —— 继续下一只"
      FAIL_LIST+=("$t")
    fi
    sleep "$SLEEP_SECS"
  else
    echo "--------------------------------------------------------------"
    echo "[$t] 请在 ZCode 会话中粘贴执行："
    echo
    echo "    /investment-team ${t}"
    echo
    read -r -p "完成后回车继续下一只（s=跳过，q=退出）：" ans
    case "$ans" in
      q|Q) echo "已手动退出。"; break ;;
      s|S) SKIP_LIST+=("$t"); continue ;;
      *)   DONE_LIST+=("$t") ;;
    esac
  fi
done

# -----------------------------------------------------------------------------
echo
echo "=== 汇总（${TODAY}）==="
echo "  完成：${DONE_LIST[*]:-无}"
echo "  跳过：${SKIP_LIST[*]:-无}"
echo "  失败：${FAIL_LIST[*]:-无}"
[[ ${#FAIL_LIST[@]} -eq 0 ]] || exit 1
exit 0
