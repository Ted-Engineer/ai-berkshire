---
kind: external_dependency
name: Claude Code 客户端集成
slug: claude-code
category: external_dependency
category_hints:
    - vendor_identity
scope:
    - '**'
---

### Claude Code 客户端集成
- AI Berkshire 作为 Claude Code commands 安装，通过 `./scripts/install-claude-commands.sh` 将 skills/*.md 复制到 Claude Code 全局 commands 目录
- 支持 `--dangerously-skip-permissions` 模式减少频繁授权确认
- 与 Codex 共享同一套 canonical workflow，保持输出格式一致