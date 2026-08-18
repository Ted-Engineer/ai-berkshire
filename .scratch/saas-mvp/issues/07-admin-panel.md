# 07 — 管理面板

**What to build:** 管理员通过配置密码登录管理页面，在 Web 界面上指定生成数量和配额，批量生成密钥，并以表格形式查看所有已生成密钥的状态（未使用/活跃/已耗尽）。这将 02 中的管理员 API 升级为可视化操作界面，方便运营人员自助发卡。

**Blocked by:** 02 — 密钥登录端到端

**Status:** ✅ complete

- [ ] 前端 `/admin/login` 页面：密码输入框 + 登录按钮
- [ ] 前端 `/admin` 管理面板：密钥生成表单（数量 + 配额）+ 密钥状态表格
- [ ] 管理员认证：密码存于后端配置文件，前端登录后存 admin token 到 LocalStorage
- [ ] 密钥生成表单调用 `POST /admin/keys/generate`，展示生成结果（可复制）
- [ ] `GET /admin/keys` — 返回所有密钥列表及其状态
- [ ] 密钥状态表格：展示 key_string、quota_total、quota_used、status、created_at
- [ ] 表格支持按状态筛选
- [ ] 未登录时重定向到 `/admin/login`
- [ ] 集成测试：管理员登录 + 生成密钥 + 查看列表全流程
