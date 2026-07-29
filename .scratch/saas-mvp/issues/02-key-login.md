# 02 — 密钥登录端到端

**What to build:** 用户在密钥登录页输入密钥字符串，后端验证密钥有效性并返回剩余次数，前端将密钥存入 LocalStorage 并跳转到控制台展示剩余次数。同时实现管理员 API 批量生成密钥（配置密码认证）。这是整个系统的身份入口 — 没有密钥验证就没有后续一切功能。

**Blocked by:** 01 — 项目脚手架 + 基础设施

**Status:** ✅ complete

- [ ] MySQL `access_keys` 表：id, key_string (unique), quota_total, quota_used, status (UNUSED/ACTIVE/EXHAUSTED), created_at
- [ ] `POST /api/keys/verify` — 验证密钥字符串，返回 `{valid, remaining}`；无效或已耗尽返回 401
- [ ] `POST /admin/keys/generate` — 管理员批量生成密钥，接受 `{count, quota}`，返回生成的密钥列表；用配置文件中的密码做 Bearer Token 认证
- [ ] 密钥格式 `BRK-XXXXXXXX`（8 位随机字母数字）
- [ ] 首次验证时状态从 `UNUSED` 转为 `ACTIVE`
- [ ] 前端 `/login` 页面：密钥输入框 + 提交按钮，验证成功跳转 `/dashboard`
- [ ] 前端 `/dashboard` 页面：显示剩余次数，未登录时重定向到 `/login`
- [ ] 密钥存于 LocalStorage，每次 API 请求携带
- [ ] 集成测试：验证有效密钥、无效密钥、已耗尽密钥三种场景
- [ ] 集成测试：管理员生成 10 个配额为 1 的密钥，验证全部可查询
