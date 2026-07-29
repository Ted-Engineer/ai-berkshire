# SaaS 双层架构：Java SaaS 层 + Python Worker（Claude Agent SDK）

现有 ai-berkshire 投研能力以 Claude Code Skill + Python 工具形式存在。SaaS 化时选择 Java + Python 双层分离：Java Spring Boot 负责 SaaS 层（认证、配额、任务、SSE），Python Worker 使用 Claude Agent SDK 执行投研工作流，通过 Redis 通信。放弃了纯 Java 重写 prompt 编排和纯 Python 全栈两个方案——前者需要用 Java 重写全部 Skill 编排逻辑，后者缺少企业级 SaaS 框架生态。
