# Worker 引擎选 Claude Agent SDK 而非 CLI 子进程

最初考虑用 Python Worker 通过子进程调用 Claude Code CLI 执行投研 Skill。调研后发现 Claude Agent SDK（原名 Claude Code SDK）以 Python 库形式提供，输出结构化 JSON 消息流而非文本 stdout，原生加载 Skills/CLAUDE.md/工具，与自定义应用的定位完全匹配。CLI 是为交互式开发设计的，SDK 是为生产自动化和自定义应用设计的。选择 SDK 获得了可靠性（零 stdout 解析）、可控性（结构化消息类型）和生产适用性。
