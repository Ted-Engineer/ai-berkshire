# AI Berkshire Qoder Plugin

AI Berkshire 投研框架的 Qoder 插件包：23 个投研 skills + 配套可执行工具。
由 `scripts/build-qoder-plugin.sh` 从仓库唯一事实源组装生成（`skills/*.md` →
`codex-skills/` → 本目录），请勿手改 `skills/`、`tools/`、`scripts/` 子目录。

## 内容

- **skills/**：23 个投研 skill（组合管理/调仓、四大师研究、财报精读、行业漏斗、
  时代α、瓶颈猎手、论文追踪、公众号写作等）。每个 SKILL.md 的适配注记说明
  Claude 专用能力如何映射到 Qoder 能力。
- **tools/**（skills 引用的全部 8 个工具，纯 Python 标准库）：
  - `financial_rigor.py` — 精确算术/估值/市值交叉验证/三情景
  - `report_audit.py` — 报告数字抽检准出
  - `terminal_value.py` — 十年折现与 flip 敏感性
  - `portfolio_sigma.py` — 组合波动率与 σ_target=25% 目标制核算
  - `indep_audit.py` — SEC EDGAR XBRL 独立复核（防自我验证）
  - `fetch_quotes.py` — 实时行情+时间戳（Yahoo→腾讯回退）
  - `twstock_data.py` — 台股 FinMind 数据
  - `xueqiu_scraper.py` — 雪球存档抓取
- **scripts/workflow-gate-hook.sh** — portfolio-rebalance 阶段门禁（JSON 判定）

## 前置要求

- Python 3（Windows 无 `python3` 别名时用 `python`）。
- 搜索能力使用宿主环境（Qoder 内置 WebSearch / 已配置的 MCP 搜索），
  本插件不捆绑 MCP 服务。

## 构建与安装

```bash
bash scripts/build-qoder-plugin.sh
# 产物：dist/ai-berkshire-plugin-<version>.zip
```

在 Qoder 中安装：设置 → 扩展 → 导入本地插件 zip，或由助手调用
`qoder-settings.install_extension`（`source=local, kind=plugin`）。

## 来源与状态说明

skills 来自本仓库 `skills/`（含 2026-11 转正的实战增强版与
portfolio-rebalance v8.0：情绪指数 + 活跃方向动态发现 + 三期限候选分层）。
`portfolio_sigma.py`、`indep_audit.py`、`fetch_quotes.py`、
`workflow-gate-hook.sh` 为按 skill 内文档契约重新实现（原 WorkBuddy 实现从未入库，
且已弃用）；`indep_audit.py` 依赖 SEC EDGAR 公开接口，网络不可达时返回 WARN。
本项目仅供学习研究，不构成投资建议。
