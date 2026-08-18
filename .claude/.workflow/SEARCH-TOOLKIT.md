# 8-17 搜索工具链说明（builtin WebSearch 与 webReader MCP 配额耗尽，8-22 重置）

本会话可用的搜索通道（全部经 Bash curl 验证可用）：

## 1. 通用网页搜索（Brave）
```bash
bash .claude/.workflow/websearch.sh "search query" 8
```
输出：[序号] 标题 / URL / 摘要。Brave 无配额限制，支持任意查询词。

## 2. 新闻搜索（Google News RSS）
```bash
bash .claude/.workflow/gnews.sh "news query" 8
```
输出：[序号] 标题 / 链接 | 发布时间 / 描述。适合财报、异动、事件查询。

## 3. 行情与财务数据（Yahoo Finance API，SSL已关闭验证）
```bash
# 实时/收盘行情（含52周高低）
python tools/fetch_quotes.py TICKER1,TICKER2
# 当日涨跌幅榜单
curl -sk -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved?scrIds=day_gainers&count=25"
# 新闻+相关股票
curl -sk -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v1/finance/search?q=QUERY&newsCount=8"
```

## 4. 抓取具体网页正文
```bash
curl -sL -m 20 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0" "URL" | python -c "import sys,re,html;d=sys.stdin.read();t=re.sub(r'<script.*?</script>|<style.*?</style>','',d,flags=re.S);t=re.sub(r'<[^>]+>',' ',t);print(html.unescape(re.sub(r'\s+',' ',t))[:8000])"
```
注：seekingalpha 403；stockanalysis.com / macrotrends / finviz 通常可用。

## 已验证不可用（勿浪费时间重试）
- 内置 WebSearch 工具：429，2026-08-22 00:22 重置
- mcp__web_reader__webReader：429（同一上游），8-22 重置
- Bing（www/cn）：返回机器人检测干扰页（无关缓存结果）
- DDG lite/html：间歇 202

## 搜索日志
每次搜索后追加（主 Agent 统一维护）：
`printf '%s | brave/gnews/yahoo | query\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> .claude/.workflow/search-log.txt`
