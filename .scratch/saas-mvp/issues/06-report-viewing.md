# 06 — 报告查看

**What to build:** 用户点击历史报告列表中的报告，进入报告详情页，通过 Tab 切换查看三份报告（深度分析/行业研究/买入检查）。报告内容以 Markdown 格式渲染，支持表格、代码块、标题等格式。用户可随时凭密钥登录回看所有历史报告。

**Blocked by:** 04 — 真实 Skill 编排（Claude Agent SDK）

**Status:** ✅ complete

- [ ] `GET /api/reports/{id}` — 返回报告详情，包含三份报告的 Markdown 内容
- [ ] 权限校验：只能查看属于当前密钥的报告
- [ ] 前端 `/report/[id]` 页面：三个 Tab（深度分析 / 行业研究 / 买入检查）
- [ ] 使用 react-markdown + remark-gfm 渲染 Markdown 内容
- [ ] Markdown 元素样式适配 Tailwind（标题、表格、代码块、引用块）
- [ ] 报告加载中状态 + 错误状态处理
- [ ] 前端历史报告列表项可点击跳转到报告详情页
- [ ] 集成测试：请求不属于自己的报告返回 403
- [ ] E2E：从控制台点击报告 → 验证 Tab 切换 → 验证 Markdown 渲染
