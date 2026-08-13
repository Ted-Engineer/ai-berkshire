#!/bin/bash
# PostToolUse hook on Write — 当portfolio-action报告写入后，清理工作流状态
# 同时也在SessionStart时清理上次遗留的状态

WORKFLOW_DIR="F:/ai-berkshire/.claude/.workflow"

input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // ""' 2>/dev/null)

# 如果写入的是 portfolio-action 报告，说明工作流完成，清理标记
if echo "$file_path" | grep -q "portfolio-action"; then
  rm -rf "${WORKFLOW_DIR:?}"/*.done 2>/dev/null
  rm -f "$WORKFLOW_DIR/active" 2>/dev/null
  rm -f "$WORKFLOW_DIR/search-log.txt" 2>/dev/null
fi

echo '{}'
