# 01 — 项目脚手架 + 基础设施

**What to build:** 搭建 ai-berkshire-saas 仓库的三项目骨架和本地开发环境。初始化 Java Spring Boot 3 后端、Python Worker（claude-agent-sdk）、Next.js 15 前端三个子项目，配置 Docker Compose 启动 MySQL 8 + Redis 7，三个项目各自能启动并连通数据库和缓存。后端有 `/health` 端点返回 200，Worker 能连接 Redis，前端能访问后端 API。

**Blocked by:** None — can start immediately

**Status:** ✅ complete

- [ ] 创建 `ai-berkshire-saas/` 仓库，包含 `backend/`、`worker/`、`frontend/` 三个子目录
- [ ] Java Spring Boot 3 项目初始化，配置 Spring Data JPA + MySQL 驱动 + Spring Data Redis
- [ ] Python Worker 项目初始化，安装 claude-agent-sdk + redis 依赖
- [ ] Next.js 15 项目初始化，配置 shadcn/ui + Tailwind CSS 4
- [ ] `docker-compose.yml` 包含 MySQL 8 + Redis 7 服务，`docker-compose up` 一键启动
- [ ] 后端 `/health` 端点返回 200，数据库连接池正常
- [ ] Worker 能连接 Redis 并执行 PING
- [ ] 前端能请求后端 `/health` 并显示状态
