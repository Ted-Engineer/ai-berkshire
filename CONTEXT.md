# AI Berkshire SaaS

面向 C 端用户的 AI 投研报告生成平台，基于现有 ai-berkshire 投研框架能力构建。

## Language

**研报套餐 (Research Bundle)**:
一次密钥消耗交付的标准报告组合：1 份深度分析（/investment-team）+ 1 份行业研究（/industry-research）+ 1 份买入检查（/investment-checklist）。
_Avoid_: 报告包, 套餐, package

**密钥 (Access Key)**:
预付次数兑换码，同时充当身份凭证和使用配额载体。免注册，凭密钥直接使用。
_Avoid_: 卡密, 激活码, license, token

**报告生成 (Report Generation)**:
用户输入股票代码，系统编排三个 Skill 依次/并行执行，产出研报套餐的完整流程。
_Avoid_: 跑报告, 生成任务

**编排 (Orchestration)**:
研报套餐的执行流程：先做行业预判断（30秒），然后 investment-team 和 industry-research 并行执行，两者都完成后串行执行 investment-checklist（引用前两份结论）。
_Avoid_: 调度, workflow, pipeline

**Worker 引擎 (Worker Engine)**:
Python Worker 使用 Claude Agent SDK（Python 版，原名 Claude Code SDK）作为投研 Skill 执行引擎，而非 CLI 子进程。SDK 以 Python 库形式内嵌，提供结构化 JSON 消息流，原生加载 Skills/CLAUDE.md/工具。
_Avoid_: CLI 子进程, subprocess, stdout 解析

**配额扣减 (Quota Deduction)**:
扣减前置 + 失败自动退款。提交报告生成时立即扣 1 次密钥次数，生成成功则确认扣减，失败则自动退还。防止并发提交超额使用。
_Avoid_: 计费, billing
