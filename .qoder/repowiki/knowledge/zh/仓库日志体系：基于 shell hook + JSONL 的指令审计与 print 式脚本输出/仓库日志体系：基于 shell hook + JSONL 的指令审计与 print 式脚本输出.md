---
kind: logging_system
name: 仓库日志体系：基于 shell hook + JSONL 的指令审计与 print 式脚本输出
category: logging_system
scope:
    - '**'
source_files:
    - tools/log-command.sh
    - scripts/skill-enforcement-hook.sh
    - logs/.gitignore
---

## 1. 使用的系统/方法

本仓库**没有统一的 Python logging 框架**。所有 Python 脚本（`tools/`、`scripts/`、根级 `.py`）均以 `print()` / `sys.stderr.write()` 直接输出，无结构化日志库、无日志级别、无集中配置。唯一的“日志系统”是位于仓库根目录的 `logs/` 目录，由一个独立的 shell hook 脚本 `tools/log-command.sh` 负责将 Claude Code 的用户指令以 **JSONL 格式**追加写入 `logs/command-log.jsonl`。

## 2. 核心文件与位置

- `tools/log-command.sh`：唯一被纳入版本控制的日志采集器，作为 Claude Code 的 `UserPromptSubmit` hook 调用，从 stdin 读取用户 prompt，截取前 200 字符，写入 `logs/command-log.jsonl`，并维护 `logs/.counter` 计数文件。
- `logs/`：日志持久化目录，包含 `command-log.jsonl` 和 `.counter`；该目录本身在 `.gitignore` 中被忽略（见下文），避免污染仓库。
- `scripts/skill-enforcement-hook.sh`：另一个 Claude Code hook，用于在检测到投资研究关键词时注入强制提醒，不写日志但体现 hook 机制。
- 各 Python 脚本（如 `tools/*.py`、`scripts/fetch_stocks.py`、`reports/*/fetch_*.py`）通过 `print(..., file=sys.stderr)` 输出进度/错误信息，属于“控制台输出”，不被视为可查询日志。

## 3. 架构与约定

- **采集入口单一**：仅 `log-command.sh` 负责捕获用户指令，其他组件不主动写日志。
- **存储格式固定**：每条记录为单行 JSON，字段固定为 `time`（`%Y-%m-%d %H:%M:%S`）和 `prompt`（截断至 200 字符、换行替换为空格、双引号替换为单引号）。这是硬编码的契约，新增字段需修改脚本。
- **幂等追加**：使用 `>>` 追加到同一文件，无轮转、无压缩、无锁机制，并发写入未做保护。
- **计数器旁路**：独立 `logs/.counter` 文件记录累计条数，每 10 条通过 stdout 输出一条提示消息给 Claude，便于人工感知累积量。
- **空输入跳过**：当 stdin 为空时直接 `exit 0`，不产生垃圾记录。
- **路径约定**：日志目录硬编码为 `$HOME/ai-berkshire/logs`，依赖运行环境变量 `$HOME`。

## 4. 约定与约束

- **Python 代码不使用任何 logging 模块**：全仓 `print()` 输出，无 `import logging`、无 logger 实例、无日志级别管理。这意味着无法按严重性过滤或路由日志。
- **日志仅覆盖“用户指令”**：`log-command.sh` 只记录用户提交给 Claude 的 prompt，不记录工具执行结果、API 响应、错误堆栈等运行时状态。
- **无结构化字段扩展**：当前只有 `time` 和 `prompt` 两个字段，如需增加 `user`、`session_id`、`tool_name` 等上下文，必须修改脚本逻辑。
- **无日志轮转策略**：`command-log.jsonl` 会无限增长，脚本中无任何清理或归档逻辑。
- **stderr 输出不可检索**：Python 脚本的错误/进度信息通过 `print(..., file=sys.stderr)` 输出到终端，不会被收集到 `logs/` 目录，也无法事后分析。
- **Hook 模式是强制约束**：`skill-enforcement-hook.sh` 展示了如何通过 Claude Code 的 hook 机制在特定关键词触发时注入行为，这种模式可复用到日志采集场景（例如自动记录工具调用），但目前未被采用。

## 5. 适用性判断

该仓库存在一个最小化的日志子系统（shell hook + JSONL 文件），但它仅服务于“用户指令审计”，并非通用的应用日志框架。Python 侧完全缺失结构化日志能力，因此本卡片描述的是仓库中实际存在的、有限的日志实践，而非一个完整的日志系统。