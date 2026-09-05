#!/bin/bash
# SessionStart hook — 清理上次会话遗留的工作流状态
WORKFLOW_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)/.claude/.workflow"
rm -rf "$WORKFLOW_DIR"/*.done 2>/dev/null
rm -f "$WORKFLOW_DIR/active" 2>/dev/null
echo '{}'
