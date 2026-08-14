#!/bin/bash
# PostToolUse hook on Skill — 自动记录每次skill调用到 .claude/.workflow/
# 每次Agent调用Skill工具后触发，写标记文件

WORKFLOW_DIR="F:/ai-berkshire/.claude/.workflow"

input=$(cat)
skill_name=$(echo "$input" | jq -r '.tool_input.skill // ""' 2>/dev/null)
skill_args=$(echo "$input" | jq -r '.tool_input.args // "all"' 2>/dev/null)

# 跳过非投研skill（如 update-config, using-superpowers 等元skill）
if echo "$skill_name" | grep -qiE 'update-config|using-superpowers|skill-creator|findskill|save-progress'; then
  echo '{}'
  exit 0
fi

# 标准化args为安全文件名
safe_args=$(echo "$skill_args" | tr ' /' '__' | tr -cd '[:alnum:]_-' | head -c 30)
if [ -z "$safe_args" ]; then
  safe_args="general"
fi

# 写标记文件
mkdir -p "$WORKFLOW_DIR"
marker_file="${WORKFLOW_DIR}/${skill_name}-${safe_args}.done"
timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"skill\":\"$skill_name\",\"args\":\"$skill_args\",\"timestamp\":\"$timestamp\"}" > "$marker_file"

# 静默通过
echo '{}'
