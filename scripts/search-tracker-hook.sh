#!/bin/bash
# PostToolUse hook on search tools — 追踪搜索工具使用 + 记录每次搜索词到search-log.txt
# gate hook 依据 search-log.txt 行数验证搜索总量是否达标

WORKFLOW_DIR="F:/ai-berkshire/.claude/.workflow"
mkdir -p "$WORKFLOW_DIR"

input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name // ""' 2>/dev/null)
query=$(echo "$input" | jq -r '.tool_input.query // .tool_input.search_query // .tool_input.q // .tool_input.keyword // "unknown"' 2>/dev/null)
timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# 根据工具名创建对应标记
case "$tool_name" in
  *web-search__search*)
    echo "{\"tool\":\"$tool_name\",\"timestamp\":\"$timestamp\"}" > "$WORKFLOW_DIR/mcp-web-search.used"
    ;;
  *kepler*web_search*)
    echo "{\"tool\":\"$tool_name\",\"timestamp\":\"$timestamp\"}" > "$WORKFLOW_DIR/mcp-kepler-search.used"
    ;;
  *web-search-prime*)
    echo "{\"tool\":\"$tool_name\",\"timestamp\":\"$timestamp\"}" > "$WORKFLOW_DIR/mcp-web-search-prime.used"
    ;;
  WebSearch)
    echo "{\"tool\":\"$tool_name\",\"timestamp\":\"$timestamp\"}" > "$WORKFLOW_DIR/builtin-websearch.used"
    ;;
esac

# 追加搜索词日志（每次调用一行，用于gate hook计数验证搜索多样性）
# 行格式: ISO时间 | 工具名 | 搜索词
echo "${timestamp} | ${tool_name} | ${query}" >> "$WORKFLOW_DIR/search-log.txt"

echo '{}'
