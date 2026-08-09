#!/usr/bin/env bash
# SessionStart hook: 把 .learnings/ 知识库摘要注入每个新会话的上下文。
# 保证 Claude 每次都"看到"已沉淀的学习/错误/待办，而不是靠自觉去读。
# 输出符合 Claude Code hook JSON 规范：hookSpecificOutput.additionalContext
# 注入模型上下文；.learnings/ 不存在时静默退出（clone 到其他机器不报错）。
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LD="$ROOT/.learnings"

if [ ! -d "$LD" ]; then
  exit 0
fi

LRN_N=$(grep -c '^## \[LRN' "$LD/LEARNINGS.md" 2>/dev/null || echo 0)
ERR_N=$(grep -c '^## \[ERR' "$LD/ERRORS.md" 2>/dev/null || echo 0)
FEAT_N=$(grep -c '^## \[FEAT' "$LD/FEATURE_REQUESTS.md" 2>/dev/null || echo 0)

DIGEST="<learnings-digest>
这是本项目 .learnings/ 知识库摘要（由 scripts/learnings-digest.sh 在会话启动时注入）。
涉及相关任务时按条目查阅对应文件详情；如需完整摘要读 .learnings/session-summary-2026-08-09.md。

## 知识/最佳实践/修正 (.learnings/LEARNINGS.md) — ${LRN_N} 条
$(grep '^## \[LRN' "$LD/LEARNINGS.md" | sed 's/^/  /' | head -25)
## 已知错误 (.learnings/ERRORS.md) — ${ERR_N} 条
$(grep '^## \[ERR' "$LD/ERRORS.md" | sed 's/^/  /' | head -12)
## 用户需求 (.learnings/FEATURE_REQUESTS.md) — ${FEAT_N} 条
$(grep '^## \[FEAT' "$LD/FEATURE_REQUESTS.md" | sed 's/^/  /' | head -10)
</learnings-digest>"

# 用 jq 构造合规的 hook JSON；无 jq 时退化为明文输出（SessionStart stdout 也会进上下文）
if command -v jq >/dev/null 2>&1; then
  jq -n --arg ctx "$DIGEST" '{hookSpecificOutput: {hookEventName: "SessionStart", additionalContext: $ctx}}'
else
  printf '%s\n' "$DIGEST"
fi
