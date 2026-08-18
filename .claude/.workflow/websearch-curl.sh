#!/bin/bash
# DDG-lite search fallback when WebSearch/webReader MCP quotas are exhausted.
# Usage: bash .claude/.workflow/websearch-curl.sh "search query" [result_count]
Q="$1"
N="${2:-8}"
ENC=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$Q")
curl -s -m 20 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36" "https://lite.duckduckgo.com/lite/?q=${ENC}" | python - "$N" <<'PYEOF'
import sys, re, html, urllib.parse
n = int(sys.argv[1])
data = sys.stdin.read()
# DDG lite: links like <a rel="nofollow" href="...uddg=ENCODED..." class='result-link'>Title</a>
results = re.findall(r"<a[^>]*href=\"([^\"]*uddg=[^\"]*)\"[^>]*>(.*?)</a>", data)
snips = re.findall(r"<td class=\"result-snippet\">(.*?)</td>", data, re.S)
if not results:
    print("NO_RESULTS (len=%d)" % len(data))
    sys.exit(0)
seen = 0
for i, (href, title) in enumerate(results):
    if 'duckduckgo.com' in href:
        continue
    t = html.unescape(re.sub(r'<[^>]+>', '', title)).strip()
    m = re.search(r'uddg=([^&]+)', href)
    if m:
        href = urllib.parse.unquote(m.group(1))
    s = html.unescape(re.sub(r'<[^>]+>', '', snips[i])).strip() if i < len(snips) else ''
    print("[%d] %s\n    %s\n    %s" % (seen+1, t, href, s[:300]))
    seen += 1
    if seen >= n:
        break
PYEOF
