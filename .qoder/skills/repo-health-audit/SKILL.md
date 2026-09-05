---
name: repo-health-audit
description: 对 ai-berkshire 仓库执行分层工程健康审查与修复：并行深读+逐条核验缺陷、按严重度分级、分逻辑批次修复提交、全量门禁验证、隔离用户未提交改动。当用户说"审查项目/工程健康检查/清理仓库/全修了"，或大规模改动后想验证各层一致性时调用。
---

# 工程健康审查与修复（repo-health-audit）

## Overview

本仓库的结构性风险是**层间漂移**：22 个投研 skill 源（`skills/*.md`）镜像到 6 个运行时、4 个 config 被多个 skill 读写、hooks 与 Stop 门禁依赖文件状态、多份文档自称"口径权威"。本 skill 提供一套可重复的审查→核验→修复→提交→披露流程。

## 第零步：git 基线与 WIP 隔离（必须最先做）

1. 把 `git status --porcelain` 输出存入临时文件，作为本次会话的基线。
2. 识别**用户未提交改动**（典型：`skills/portfolio-*.md`、`config/*.md`、其 6 个镜像、`reports/` 未跟踪文件）。这些是用户的进行中工作：
   - 全程不 stage、不 checkout、不覆盖；
   - 提交时按精确路径 add（按 skill 目录逐个），禁止 `git add -A` / `git add .`；
   - 镜像重生成后，只提交本次实际修改的 skill 对应目录，用户的 WIP 镜像改动留在工作区。
3. 注意：`.claude/settings.local.json` 是 gitignored 本地文件——直接修改即生效，但无法提交，不要强行 `git add -f`。

## 第一步：分层深读（并行 Explore + 亲自核验）

并行派出多个 Explore agent 分头深读，分工按层：

| 层 | 审查什么 |
|---|---|
| skills + 6 镜像 | 规范源与镜像是否一致；sync 脚本 DESCRIPTIONS 字典是否缺键（缺键会静默生成无信息兜底描述，`--check` 检不出） |
| tools/ | 零调用的死工具；CLI 示例与 argparse 是否匹配；退出码语义（❌ 应为 1）；恒真/循环论证式校验；GBK 控制台崩溃 |
| config/ | 4 个文件的实际消费者（grep skills/*.md 核实，勿信文档声明）；版本号与自称"口径权威"的文档（prompt.md）是否分叉 |
| harness | hooks 硬编码绝对路径；门禁可否空转（空输入/空 JSON 是否放行）；validate 脚本检查的标记名是否真的有人写入 |
| 文档与产出 | README/CLAUDE/AGENTS 数字与实际数量；.gitignore 声明与 `git ls-files` 实际跟踪是否矛盾（重点：隐私敏感文件）；空目录/畸形目录名/临时残留 |

**核验铁律：agent 的报告不是事实。** 所有将进入修复清单的缺陷，必须用直接命令复验（跑 CLI 看退出码、`git ls-files` 查跟踪、grep 查引用）。未经复验的只能标"待核验"，不得断言。

## 第二步：缺陷分级

- **🔴 需用户决策**：涉及隐私（如被跟踪的持仓文件）、破坏性操作（删大量文件、改写历史）、影响共享状态（push/PR）。
- **🟠 已验证缺陷**：会直接导致执行失败或门禁失效（不存在的 CLI 参数、恒 0 退出码、空结果放行、永远无法满足的检查）。
- **🟡 一致性债**：文档数字漂移、快照过期、重复副本。修复但优先级低。

## 第三步：修复纪律（铁律）

1. **禁止把有状态副作用的脚本当冒烟测试跑。** 教训：跑 `workflow-session-cleanup.sh` 验证路径可移植性，顺带删了 `.claude/.workflow/*.done`；随后 `git checkout -- .claude/.workflow/` 又把未提交的 `candidates.csv`（~1000 行候选池）、`search-log.txt` 退回 HEAD。测试 hook 只用无副用的 `bash -n` 或在临时目录验证只读路径。
2. 修改 `skills/*.md` 后必跑 6 个 sync 脚本（codex/codex-prompts/trae/dsh/zcode/qoder），并补齐对应 DESCRIPTIONS 字典键。
3. **分逻辑批次提交**：tools 修复 / harness 修复 / skills+镜像 / 文档同步 / CI / 清理，各自独立 commit，消息写清"为什么"。
4. 删除文件前核对 `git ls-files` 跟踪状态：tracked 用 `git rm`（可经历史恢复），untracked 用 `rm`（不可恢复，更谨慎）。
5. 用户只授权"修复"时，报告内容（reports/ 下的研究产出）不删——AGENTS.md 规定保留现有报告，除非任务明说。

## 第四步：全量门禁（提交后、汇报前必跑）

```bash
python -m unittest discover -s tests          # 单元测试
python -m py_compile tools/*.py scripts/*.py  # 语法
for f in scripts/*.sh; do bash -n "$f"; done  # shell 语法
python scripts/sync-codex-skills.py --check   # 以及 trae/dsh/zcode/qoder/codex-prompts 五个 --check
git status --porcelain | grep -v "^??"       # 剩余改动应只有用户 WIP
```

任何一项不过，回到第三步。CI（`.github/workflows/ci.yml`）在 push 后还会再跑一遍。

## 第五步：如实披露

最终汇报必须包含四部分：**修了什么**（附证据：测试结果、命令输出）、**没动什么**（用户 WIP 清单）、**副作用与损失**（如有，如实写，不淡化）、**留给用户的决定**（如历史中的隐私文件是否 filter-repo、是否 push）。
