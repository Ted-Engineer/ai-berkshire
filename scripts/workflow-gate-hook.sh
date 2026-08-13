#!/bin/bash
# Stop hook — Agent尝试停止时，检查所有必需skill是否已执行
# 如果缺失，阻止停止并注入具体反馈

WORKFLOW_DIR="F:/ai-berkshire/.claude/.workflow"
ACTIVE_FILE="${WORKFLOW_DIR}/active"

# 如果没有活跃工作流，直接放行
if [ ! -f "$ACTIVE_FILE" ]; then
  echo '{}'
  exit 0
fi

# 如果今天已有定稿的portfolio-action报告，说明本轮工作流已完成
# （workflow-cleanup-hook.sh在报告写入时按完成语义删除.done标记和active；
#  若用户随后重新激活工作流，active会重建但标记已清，此处避免对已完成工作重复拦截）
TODAY_REPORT="F:/ai-berkshire/reports/portfolio-action-$(date +%Y%m%d).md"
if [ -f "$TODAY_REPORT" ]; then
  echo '{}'
  exit 0
fi

# 检查必需的skill类型
missing=()
found_details=""

# 1. /investment-team（持仓分析，至少1个）
team_count=$(ls "${WORKFLOW_DIR}"/investment-team-*.done 2>/dev/null | wc -l)
if [ "$team_count" -eq 0 ]; then
  missing+=("/investment-team（持仓四大师分析）")
else
  team_list=$(ls "${WORKFLOW_DIR}"/investment-team-*.done 2>/dev/null | sed 's|.*/investment-team-||;s|\.done||' | tr '\n' ', ' | sed 's/,$//')
  found_details+="investment-team: ${team_list}; "
fi

# 2. /investment-checklist（候选准入，至少1个）
checklist_count=$(ls "${WORKFLOW_DIR}"/investment-checklist-*.done 2>/dev/null | wc -l)
if [ "$checklist_count" -eq 0 ]; then
  missing+=("/investment-checklist（巴菲特六关准入）")
else
  checklist_list=$(ls "${WORKFLOW_DIR}"/investment-checklist-*.done 2>/dev/null | sed 's|.*/investment-checklist-||;s|\.done||' | tr '\n' ', ' | sed 's/,$//')
  found_details+="investment-checklist: ${checklist_list}; "
fi

# 3. /industry-funnel（行业漏斗）
if ! ls "${WORKFLOW_DIR}"/industry-funnel-*.done >/dev/null 2>&1; then
  missing+=("/industry-funnel（行业漏斗筛选）")
fi

# 4. /bottleneck-hunter（瓶颈扫描）
if ! ls "${WORKFLOW_DIR}"/bottleneck-hunter-*.done >/dev/null 2>&1; then
  missing+=("/bottleneck-hunter（瓶颈扫描）")
fi

# 5. mcp__web-search 必须使用过
if [ ! -f "${WORKFLOW_DIR}/mcp-web-search.used" ]; then
  missing+=("mcp__web-search__search（必须至少使用一次此MCP搜索工具）")
fi

# 6. 候选股票数量检查（≥200下限，250理想）
CANDIDATE_FILE="${WORKFLOW_DIR}/candidates.csv"
if [ -f "$CANDIDATE_FILE" ]; then
  candidate_count=$(tail -n +2 "$CANDIDATE_FILE" 2>/dev/null | grep -c '[A-Z]' 2>/dev/null || echo 0)
  if [ "$candidate_count" -lt 200 ]; then
    missing+=("候选股票数量不足：当前${candidate_count}只，要求≥200只（理想250只）。请继续扫描更多GICS行业组和交叉维度。")
  fi
else
  missing+=("候选累积文件不存在（.claude/.workflow/candidates.csv）。搜索时必须维护此文件，每发现一只候选追加一行。")
fi

# 7. 推荐标的覆盖检查：recommended-buys.txt中每个ticker必须有对应checklist .done
RECOMMENDED_FILE="${WORKFLOW_DIR}/recommended-buys.txt"
if [ ! -f "$RECOMMENDED_FILE" ]; then
  missing+=("推荐清单文件不存在（.claude/.workflow/recommended-buys.txt）。输出最终方案前必须创建，每行一个ticker，列出所有推荐买入/新建/换仓的新标的。如无新买入推荐，写入 '# no new buys'。")
else
  unvalidated=""
  while IFS= read -r ticker; do
    # 跳过空行和注释
    [ -z "$ticker" ] && continue
    [[ "$ticker" == \#* ]] && continue
    # 去除首尾空格
    ticker=$(echo "$ticker" | xargs)
    [ -z "$ticker" ] && continue
    if ! ls "${WORKFLOW_DIR}"/investment-checklist-${ticker}-*.done >/dev/null 2>&1; then
      unvalidated+="${ticker}, "
    fi
  done < "$RECOMMENDED_FILE"
  if [ -n "$unvalidated" ]; then
    unvalidated=$(echo "$unvalidated" | sed 's/, $//')
    missing+=("以下推荐标的未通过 /investment-checklist 验证：${unvalidated}。对比研究≠准入验证，推荐买入的每个新标的必须先跑 /investment-checklist 并创建 .done 标记文件。")
  fi
fi

# 8. 搜索总量检查（≥80次，防止AI/非AI关键词片面性——2026-08-13用户反馈）
SEARCH_LOG="${WORKFLOW_DIR}/search-log.txt"
if [ -f "$SEARCH_LOG" ]; then
  search_count=$(wc -l < "$SEARCH_LOG" 2>/dev/null || echo 0)
  if [ "$search_count" -lt 80 ]; then
    missing+=("搜索总量不足：当前${search_count}次，要求≥80次。构成：GICS 25组×2视角=50 + AI赛道15×2=30 + 非AI主题≥8 + 7维补充。搜索词自动记录于search-log.txt，按prompt.md「搜索总量硬指标」补齐")
  fi
else
  missing+=("搜索日志不存在（.claude/.workflow/search-log.txt）。每次MCP/WebSearch调用会自动追加一行；若无任何搜索记录说明未联网扫描")
fi

# 如果有缺失，阻止停止
if [ ${#missing[@]} -gt 0 ]; then
  missing_formatted=$(IFS='、'; echo "${missing[*]}")
  cat << EOF
{"decision":"block","reason":"⚠️【工作流关卡检查 · 未通过】\n\n以下必需skill尚未执行：\n${missing_formatted}\n\n已完成的skill：${found_details:-无}\n\n请先执行缺失的skill再尝试结束。每一步都必须通过Skill工具调用，不可用WebSearch替代。参见 prompt.md 中的「Skill执行铁律」。"}
EOF
else
  # 全部通过，放行
  echo '{}'
fi
