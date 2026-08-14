#!/bin/bash
# Skill执行铁律 hook — 当用户输入包含投资研究关键词时，自动注入skill强制提醒
# 安装于 .claude/settings.local.json 的 UserPromptSubmit hook

input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt // ""' 2>/dev/null)

# 检测投资研究相关关键词
if echo "$prompt" | grep -qiE 'prompt\.md|持仓|调仓|投资研究|portfolio|investment.*research|stock.*analysis'; then
  # 激活工作流（创建active标记，供Stop hook检查）
  WORKFLOW_DIR="F:/ai-berkshire/.claude/.workflow"
  mkdir -p "$WORKFLOW_DIR"
  if [ ! -f "$WORKFLOW_DIR/active" ]; then
    echo "{\"activated\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",\"trigger\":\"$(echo "$prompt" | head -c 50 | tr -cd '[:alnum:]_-')\"}" > "$WORKFLOW_DIR/active"
  fi
  cat << 'HOOKJSON'
{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"⚠️【SKILL执行铁律 · harness层强制提醒】\n\n本任务涉及投资研究，以下skill调用是硬性要求：\n\n1. ❌ 直接用WebSearch分析股票=未执行 → 必须通过Skill工具调用\n2. 持仓分析 → /investment-team（4个Agent并行）\n3. 候选验证 → /investment-checklist + /investment-team 双重验证（缺一不可）\n4. 行业扫描 → /industry-funnel + /bottleneck-hunter\n5. WebSearch配额用尽 → 立即切换：mcp__web-search__search → mcp__kepler__web_search → mcp__web-search-prime__web_search_prime\n6. 无skill调用证据（Agent ID/skill输出）= 步骤未完成 = 报告无效\n\n参见 prompt.md 中的「Skill执行铁律」和「WebSearch MCP fallback链」。"}}
HOOKJSON
else
  echo '{}'
fi
