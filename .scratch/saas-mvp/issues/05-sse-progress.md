# 05 — SSE 实时进度流

**What to build:** 用户提交报告生成后跳转到进度页，通过 SSE 实时看到三阶段分析进度。Worker 解析 SDK 的结构化 JSON 消息流，翻译为进度事件发布到 Redis 频道；Java 后端订阅频道并通过 SSE 推送到前端；前端用 EventSource 接收并展示三阶段进度条 + 实时日志文本。

**Blocked by:** 04 — 真实 Skill 编排（Claude Agent SDK）

**Status:** ready-for-agent

- [ ] 定义进度事件协议：`{type: STAGE_START|STAGE_PROGRESS|STAGE_COMPLETE|BUNDLE_COMPLETE|ERROR, stage: INDUSTRY_PREJUDGE|INVESTMENT_TEAM|INDUSTRY_RESEARCH|CHECKLIST, message: "..."}`
- [ ] Worker 解析 SDK 的 `async for message in query(...)` 流，根据 message.type 翻译为进度事件
- [ ] Worker 将进度事件以 JSON 发布到 Redis 频道 `task:{taskId}`
- [ ] Java 后端 `GET /api/reports/{id}/stream` — 返回 SseEmitter，订阅 Redis 频道 `task:{taskId}`
- [ ] Redis 消息转发到 SSE 客户端
- [ ] 任务完成时发送 `BUNDLE_COMPLETE` 事件并关闭 SSE 连接
- [ ] 任务失败时发送 `ERROR` 事件并关闭 SSE 连接
- [ ] 前端 `/generate/[id]` 页面：三阶段进度条（行业预判断 → 并行阶段 → 买入检查）
- [ ] 前端实时日志区域：滚动展示 message 文本
- [ ] 前端收到 `BUNDLE_COMPLETE` 后自动跳转到 `/report/[id]`
- [ ] 集成测试：模拟 Redis 进度事件，验证 SSE 端点正确推送
- [ ] 前端 E2E：mock SSE 流，验证进度条更新和跳转
