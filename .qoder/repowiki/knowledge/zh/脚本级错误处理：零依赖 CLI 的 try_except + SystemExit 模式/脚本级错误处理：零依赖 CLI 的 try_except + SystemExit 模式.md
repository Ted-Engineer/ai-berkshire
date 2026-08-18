---
kind: error_handling
name: 脚本级错误处理：零依赖 CLI 的 try/except + SystemExit 模式
category: error_handling
scope:
    - '**'
source_files:
    - tools/ashare_data.py
    - tools/morningstar_fair_value.py
    - tools/financial_rigor.py
    - scripts/sync-codex-prompts.py
    - scripts/sync-codex-skills.py
    - tools/xueqiu_scraper.py
---

## 1. 采用的系统/方法
仓库为纯 Markdown 投研文档加少量 Python 工具脚本，不存在统一的错误类型体系、中间件或日志框架。错误处理完全下沉到每个独立脚本内部，遵循零外部依赖的设计约束。
主要手段包括：
- try/except 包裹网络请求与解析逻辑，捕获 Exception 后打印警告并回退；
- 通过 raise ConnectionError 等内置异常向上冒泡；
- 在脚本入口使用 raise SystemExit 表达参数校验失败，退出码由调用方 Skills 感知。

## 2. 关键文件与位置
- tools/ashare_data.py：A 股行情财务抓取，统一用 _curl 封装 curl 调用，失败时 raise ConnectionError；52 周极值年报数据等多处 try/except Exception: continue 做容错回退。
- tools/morningstar_fair_value.py：分页抓取 Morningstar API，逐页 try/except Exception as e 打印警告并 sleep 重试。
- tools/financial_rigor.py：金融严谨性验证 CLI，计算路径用 Decimal 精确运算，表达式求值 eval 包在 try/except Exception as e 中，返回 None 表示失败。
- scripts/sync-codex-prompts.py、scripts/sync-codex-skills.py：同步脚本对未知参数直接 raise SystemExit，并在 --check 模式下以退出码 1 标记不同步。
- tools/xueqiu_scraper.py：雪球爬虫仅用 print 输出错误信息，无结构化异常。

## 3. 架构与约定
- 网络 I/O：所有 HTTP 请求均经 subprocess.run("curl", ...) 执行，returncode != 0 或空响应即 raise ConnectionError；JSON 解析失败走 except Exception 回退。
- 数据解析：对腾讯 GBK/UTF-8 混编用 except UnicodeDecodeError 自动降级；数值字段用 except (ValueError, TypeError) 兜底返回原始字符串。
- 业务校验：不抛自定义异常，而是打印带前缀的中文提示并返回布尔或 None，由上层 Skills 判断是否继续。
- 进程退出：参数错误或不一致状态使用 raise SystemExit(1)，配合 --check 模式让 CI 感知差异。
- 日志：无集中日志系统，全部通过 print 输出到 stdout，便于 Skills 直接捕获。

## 4. 开发者应遵守的规则
1. 新增脚本一律零依赖：只允许 stdlib，错误处理同样只能用内置异常加 print，不要引入第三方库。
2. 网络层统一包装：对外部 API 调用应仿照 _curl/_curl_json，失败时抛出 ConnectionError 或 except Exception 后返回默认值，避免中断整条工作流。
3. CLI 参数校验失败用 SystemExit：保持退出码语义清晰（0=成功，1=用法错误），方便 Skills 通过返回值判断是否重试。
4. 禁止吞掉异常细节：except Exception 至少打印错误信息，保留可追溯信息，便于后续定位上游接口变更。
5. 不使用 panic/recover 等价物：Python 无 panic，也不应在脚本中使用 sys.exit(-1) 等非标准退出码；如需区分错误类别，优先用不同的 except 分支打印不同前缀。