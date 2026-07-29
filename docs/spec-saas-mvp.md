# Spec: AI Berkshire SaaS MVP

## Problem Statement

C 端用户无法自助获取专业级 AI 投研报告。现有 ai-berkshire 项目拥有成熟的四大师投研 Skill 框架，但只能通过 Claude Code/Codex 客户端由开发者使用，无法触达普通用户。用户需要一个低门槛的 Web 平台：输入密钥 + 股票代码，即可获得一套完整的深度投研报告。

## Solution

构建一个独立的 SaaS Web 项目（ai-berkshire-saas），采用 Java + Python 双层架构：Java Spring Boot 负责 SaaS 层（密钥认证、配额管理、任务调度、实时进度推送），Python Worker 使用 Claude Agent SDK 执行投研工作流。用户通过预付充值卡密钥免注册登录，输入股票代码后实时观看分析进度，最终获得三合一研报套餐（深度分析 + 行业研究 + 买入检查）。

## User Stories

### 密钥与认证

1. 作为 C 端用户，我想输入密钥登录系统，以便无需注册账号即可使用投研服务
2. 作为 C 端用户，我想看到密钥剩余使用次数，以便了解还能生成几份报告
3. 作为 C 端用户，我想在输入无效密钥时收到明确提示，以便知道密钥是否正确
4. 作为 C 端用户，我想在密钥次数用尽时看到友好提示，以便知道需要获取新密钥

### 报告生成

5. 作为 C 端用户，我想输入任意股票代码（A股/港股/美股），以便分析我关注的股票
6. 作为 C 端用户，我想在提交后看到实时分析进度（"正在分析商业模式..."→"正在计算估值..."），以便知道系统正在工作
7. 作为 C 端用户，我想看到三个分析阶段的独立进度（行业预判断 → 深度分析+行业研究并行 → 买入检查），以便了解当前执行到哪一步
8. 作为 C 端用户，我想在报告生成失败时自动退还使用次数，以便不会因为系统故障白白损失配额
9. 作为 C 端用户，我想在提交后可以离开页面稍后回来查看，以便不需要一直等待

### 报告查看

10. 作为 C 端用户，我想通过 Tab 切换查看三份报告（深度分析/行业研究/买入检查），以便分别阅读不同维度的分析
11. 作为 C 端用户，我想看到格式美观的 Markdown 渲染报告，以便舒适地阅读长篇分析
12. 作为 C 端用户，我想查看该密钥下所有历史报告列表，以便回看之前生成的报告
13. 作为 C 端用户，我想随时凭同一密钥登录查看历史报告，因为报告永久保留

### 管理

14. 作为管理员，我想通过配置密码登录管理面板，以便批量生成密钥
15. 作为管理员，我想指定生成数量和每个密钥的次数配额，以便灵活控制发卡策略
16. 作为管理员，我想查看已生成密钥的状态（未使用/已使用/已过期），以便跟踪密钥分发情况

## Implementation Decisions

### 项目结构

- 独立仓库 `ai-berkshire-saas/`，与 ai-berkshire 仓库物理隔离
- 三个子项目：`backend/`（Java）、`worker/`（Python）、`frontend/`（Next.js）
- Worker 内嵌 3 个 Skill 副本和 Python 工具副本，独立于原仓库维护

### 技术栈

- **Java 后端**: Spring Boot 3, Spring Security, Spring Data JPA, Spring Web (SSE)
- **Python Worker**: claude-agent-sdk (Python), asyncio
- **前端**: Next.js 15 (App Router), shadcn/ui, Tailwind CSS 4, react-markdown
- **数据库**: MySQL 8（密钥、任务、报告元数据）
- **消息中间件**: Redis 7（Pub/Sub 进度推送 + 任务队列）
- **报告存储**: 文件系统（Markdown 文件），元数据存 MySQL

### 密钥系统

- 密钥格式：`BRK-XXXXXXXX`（前缀 + 随机字符串）
- 密钥状态机：`UNUSED` → `ACTIVE`（首次使用）→ `EXHAUSTED`（次数用尽）
- 免注册：密钥字符串本身就是身份凭证，存于 HTTP-only Cookie 或 LocalStorage
- 每个密钥绑定固定次数（生成时指定，默认 1 次）

### 配额扣减

- 扣减前置：提交报告生成时立即扣 1 次（数据库事务）
- 失败自动退款：Worker 报告失败后，Java 后端事务退还次数
- 防并发：利用 MySQL 行锁确保同一密钥不会超额扣减

### 编排流程

```
用户提交股票代码
    │
    ├─ [阶段1] 行业预判断（~30秒，小 LLM 调用）
    │
    ├─ [阶段2-并行] investment-team（8-12分钟）
    └─ [阶段2-并行] industry-research（5-8分钟）
    │
    ↓ 两者都完成（汇合点）
    │
    ├─ [阶段3-串行] investment-checklist（2-3分钟，引用前两份结论）
    │
    ↓
    汇总为研报套餐，交付用户
```

### API 契约

**用户 API:**
- `POST /api/keys/verify` — 验证密钥，返回剩余次数
- `POST /api/reports/generate` — 提交报告生成（需密钥认证）
- `GET /api/reports` — 获取历史报告列表（按密钥聚合）
- `GET /api/reports/{id}` — 获取报告详情
- `GET /api/reports/{id}/stream` — SSE 实时进度流

**管理员 API:**
- `POST /admin/keys/generate` — 批量生成密钥（配置密码认证）
- `GET /admin/keys` — 查看密钥状态列表

### 实时进度推送

- Python Worker 解析 SDK 的结构化 JSON 消息，翻译为进度事件，publish 到 Redis 频道
- Java 后端订阅 Redis 频道，通过 SSE（SseEmitter）推送到前端
- 前端用 EventSource 接收，展示三阶段进度条 + 实时日志
- 进度事件类型：`STAGE_START`、`STAGE_PROGRESS`、`STAGE_COMPLETE`、`BUNDLE_COMPLETE`、`ERROR`

### 前端页面

```
/login          → 密钥输入页（一个输入框 + 提交按钮）
/dashboard      → 控制台（剩余次数 + 提交表单 + 历史报告列表）
/generate/[id]  → 生成进度页（实时 SSE 流 + 三阶段进度条）
/report/[id]    → 报告详情页（三份报告 Tab 切换 + Markdown 渲染）
```

### Worker 与 Java 通信

- Java → Worker：任务通过 Redis 队列下发（JSON 格式：股票代码 + 任务 ID + 密钥 ID）
- Worker → Java：进度通过 Redis Pub/Sub 推送（频道名 = `task:{taskId}`）
- Worker 完成后报告文件写入共享卷，MySQL 记录报告元数据

### 部署

- Docker Compose 一体化，5 个服务：backend, worker, frontend, mysql, redis
- Nginx 反向代理统一入口，SSL 终结
- Worker 和 Backend 共享报告存储卷

## Testing Decisions

### 接缝 1：Java 后端 API 集成测试（最高优先级）

- 使用 Spring Boot Test + TestContainers（真实 MySQL + Redis 容器）
- 测试密钥验证、配额扣减/退款的事务一致性
- 测试 SSE 流的连接和消息推送
- 测试并发提交的配额安全性
- 只测外部行为（HTTP 响应），不测内部实现

### 接缝 2：Worker 编排单元测试

- Mock Claude Agent SDK 的 query() 函数
- 验证编排序列：行业预判断 → 并行 investment-team + industry-research → 串行 checklist
- 验证进度事件正确发布到 Redis
- 验证失败场景的退款触发

### 接缝 3：前端 E2E 浥试

- Playwright 驱动完整用户旅程
- 密钥登录 → 提交股票代码 → 等待进度 → 验证报告展示
- Mock SSE 流以避免依赖真实 Worker

## Out of Scope

- 在线支付系统（微信/支付宝对接）— MVP 手动分发密钥
- 用户账号注册体系 — MVP 免注册
- PDF 报告导出 — MVP 仅 Markdown 渲染
- 报告到期自动删除 — MVP 永久保留
- 微信/邮件通知 — MVP 使用 SSE 实时流
- 卡密平台对接 — 后续阶段
- Kubernetes 部署 — Docker Compose 足够 MVP
- 用户取消报告生成 — SSE 单向推送，不支持中途取消

## Further Notes

- Worker 中的 3 个 Skill 副本可能需要针对 SaaS 场景定制（去掉 GitHub 推送逻辑、调整输出格式适配前端 Markdown 渲染）
- Claude Agent SDK 需要 ANTHROPIC_API_KEY 环境变量配置
- 行业预判断需要一个轻量的股票代码→行业映射逻辑（小 LLM 调用或静态查表）
- 后续可从充值卡模式演进到卡密平台寄售，Java 后端的密钥生成 API 接口已预留
