---
kind: build_system
name: AI 投研技能分发与安装系统
category: build_system
scope:
    - '**'
source_files:
    - scripts/sync-codex-skills.py
    - scripts/sync-codex-prompts.py
    - scripts/install-codex-skills.sh
    - scripts/install-codex-prompts.sh
    - scripts/install-claude-commands.sh
---

本仓库没有传统意义上的编译/打包/发布构建系统（无 Makefile、Dockerfile、CI 流水线等），而是围绕「AI 投研技能」的**源码分发与安装**构建了一套轻量脚本体系。其核心思想是：**以 `skills/*.md` 为唯一权威源，通过 Python 同步脚本生成 Codex prompts/skills，再由 Bash/Batch 安装脚本复制到 Claude Code / Codex 的用户目录。**

## 1. 使用到的工具与框架
- **Python 3**：`scripts/sync-codex-skills.py`、`scripts/sync-codex-prompts.py` 负责从 `skills/` 解析 frontmatter 和正文，生成目标格式。
- **Bash + Batch**：`install-*.sh` / `install-*.bat` 负责创建目标目录、复制文件、设置可执行权限。
- **Markdown + YAML frontmatter**：技能定义采用 Markdown 文档，可选以 `---` 包裹的 YAML frontmatter 声明 name/description。

## 2. 关键文件与职责
| 文件 | 作用 |
|------|------|
| `skills/*.md` | 单一权威 Skill 源，Claude Code 直接读取；也是所有生成的根 |
| `scripts/sync-codex-skills.py` | 遍历 `skills/*.md`，为每个技能在 `codex-skills/<name>/SKILL.md` 写入带 metadata 的适配版 |
| `scripts/sync-codex-prompts.py` | 基于同一份 `skills/*.md` 生成 `codex-prompts/<name>.md` 斜杠命令提示词 |
| `scripts/install-codex-skills.sh` / `.bat` | 运行 sync 脚本后，将 `codex-skills/*` 整体拷贝到 `$HOME/.codex/skills/` |
| `scripts/install-codex-prompts.sh` / `.bat` | 运行 sync 脚本后，将 `codex-prompts/*.md` 拷贝到 `$HOME/.codex/prompts/` |
| `scripts/install-claude-commands.sh` / `.bat` | 直接将 `skills/*.md` 拷贝到 `$HOME/.claude/commands/`（Claude Code 原生支持） |

## 3. 架构与约定
- **单向生成流**：`skills/` → `sync-*` → `codex-skills/` + `codex-prompts/` → `install-*` → 用户目录。开发者只维护 `skills/`，其余均为派生产物。
- **frontmatter 兼容**：两个 sync 脚本都实现 `split_frontmatter()`，若源文件已有 frontmatter 则保留并补全缺失字段（如 description），否则自动生成。
- **Codex 适配器注释**：`sync-codex-skills.py` 在每个生成的 SKILL.md 头部插入「Codex adapter note」，把 Claude-only 概念（Task/Agent/WebSearch 等）映射到 Codex 等价能力，并统一要求调用 `tools/` 下的共享脚本。
- **幂等与校验**：sync 脚本支持 `--check` 模式，仅比对内容差异并返回非零退出码，便于 CI 或 pre-commit 检查。
- **跨平台**：每个流程同时提供 `.sh` 与 `.bat` 版本，Windows 下通过环境变量 `CLAUDE_COMMANDS_DIR` / `CODEX_HOME` 覆盖默认安装路径。

## 4. 开发者应遵循的规则
1. **只改 `skills/*.md`**：新增/修改技能时仅编辑该目录下的 Markdown 文件；不要手动编辑 `codex-skills/` 或 `codex-prompts/`。
2. **使用 frontmatter 声明元数据**：建议为每个技能添加 `name:` 和 `description:`，sync 脚本会据此生成更准确的标题与说明。
3. **引用工具时使用相对路径**：在 skills 中调用 `tools/` 下的脚本时，写 `python3 tools/xxx.py ...`，由 Codex 适配器自动定位仓库根。
4. **运行安装前先生成**：先执行 `python3 scripts/sync-codex-skills.py && python3 scripts/sync-codex-prompts.py`，再执行对应 `install-*.sh`。
5. **用 `--check` 做一致性校验**：在提交前运行 `python3 scripts/sync-codex-skills.py --check` 与 `python3 scripts/sync-codex-prompts.py --check`，确保派生产物与源一致。
6. **不引入外部依赖**：sync 与 install 脚本仅依赖 Python 标准库与 POSIX/Batch 内置命令，无需 `pip install`。