---
kind: external_dependency
name: OpenAI Codex 客户端集成
slug: codex
category: external_dependency
category_hints:
    - vendor_identity
scope:
    - '**'
---

### OpenAI Codex 客户端集成
- 通过 `./scripts/install-codex-skills.sh` 生成并安装 Codex skill 包到 ~/.codex/skills
- 可选安装 Codex slash prompts 到 ~/.codex/prompts，获得接近 Claude Code 的 /investment-research 体验
- 使用 `prompts:<name>` 语法调用，如 `/prompts:investment-research 腾讯`
- 由 `scripts/sync-codex-skills.py` 从 skills/*.md 自动生成