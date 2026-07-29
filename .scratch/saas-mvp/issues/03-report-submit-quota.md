# 03 — 报告提交 + 配额扣减 + 任务生命周期

**What to build:** 用户在控制台输入股票代码并提交，后端在事务中扣减 1 次配额并创建报告生成任务，任务推入 Redis 队列。Worker 消费队列，执行占位逻辑（echo 股票代码），完成后回写任务状态和占位报告。任务经历 pending → running → done/failed 全生命周期。失败时自动退还配额。用户在控制台看到历史报告列表。

**Blocked by:** 02 — 密钥登录端到端

**Status:** ✅ complete

- [ ] MySQL `report_tasks` 表：id, access_key_id, stock_code, status (PENDING/RUNNING/DONE/FAILED), created_at, updated_at
- [ ] MySQL `reports` 表：id, task_id, report_type (INVESTMENT_TEAM/INDUSTRY_RESEARCH/CHECKLIST), content_path, created_at
- [ ] `POST /api/reports/generate` — 接受 `{stock_code}`，密钥认证；事务内扣减配额 + 创建 PENDING 任务 + 推入 Redis 队列
- [ ] 配额不足时返回 402 Payment Required
- [ ] Worker 消费 Redis 队列，标记任务 RUNNING，执行占位逻辑，产出 3 个占位 Markdown 文件
- [ ] Worker 完成后标记任务 DONE，记录报告文件路径
- [ ] Worker 失败时通过 Redis 通知 Java 后端，后端事务退还配额 + 标记 FAILED
- [ ] `GET /api/reports` — 返回当前密钥下的历史报告列表
- [ ] 并发安全测试：同一密钥（配额=1）同时提交两个请求，只有一个成功
- [ ] 退款测试：模拟 Worker 失败，验证配额被正确退还
- [ ] 前端 `/dashboard` 提交表单：股票代码输入框 + 提交按钮
- [ ] 前端历史报告列表组件
