# 04 — 真实 Skill 编排（Claude Agent SDK）

**What to build:** 将 Worker 的占位逻辑替换为真实的 Claude Agent SDK 编排。用户提交股票代码后，Worker 依次执行：① 行业预判断（小 LLM 调用确定股票所属行业）② 并行执行 investment-team + industry-research ③ 串行执行 investment-checklist（引用前两份结论）。三个 Skill 的 Markdown 副本和 Python 工具副本内嵌在 Worker 中。最终产出三份真实 Markdown 研究报告。

**Blocked by:** 03 — 报告提交 + 配额扣减 + 任务生命周期

**Status:** ✅ complete

- [ ] 从 ai-berkshire 仓库复制 3 个 Skill 文件到 Worker 的 `skills/` 目录
- [ ] 从 ai-berkshire 仓库复制 Python 工具到 Worker 的 `tools/` 目录
- [ ] 配置 ANTHROPIC_API_KEY 环境变量
- [ ] 实现行业预判断模块：输入股票代码 → 调用 SDK 轻量 prompt → 返回行业名称
- [ ] 实现并行执行：asyncio.gather 同时启动 investment-team 和 industry-research 的 SDK query
- [ ] 实现串行汇合：等待两者完成后，将结论注入 investment-checklist 的 prompt 上下文
- [ ] Skill 的 SDK 调用使用 ClaudeAgentOptions 加载 CLAUDE.md + Skills + allowed_tools
- [ ] 产出的 Markdown 写入报告文件，路径回写到 MySQL reports 表
- [ ] Worker 单元测试：mock SDK query()，验证编排序列（预判断 → 并行 → checklist）
- [ ] Worker 单元测试：验证 checklist 的 prompt 包含前两份报告的结论引用
- [ ] Worker 单元测试：验证某个 Skill 失败时正确触发退款通知
