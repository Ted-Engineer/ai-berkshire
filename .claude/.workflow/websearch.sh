#!/bin/bash
# General web search fallback (builtin WebSearch & webReader MCP exhausted until 8-22).
# Usage: bash .claude/.workflow/websearch.sh "query" [n]
# Channel: Brave HTML -> Google News RSS fallback
Q="$1"; N="${2:-8}"
W="F:/ai-berkshire/.claude/.workflow"
mkdir -p "$W/tmp"
ENC=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$Q")
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
curl -s -m 25 -A "$UA" -H "Accept-Language: en-US,en;q=0.9" "https://search.brave.com/search?q=${ENC}" -o "$W/tmp/br.html" -w "brave:%{http_code}/%{size_download}\n"
python "$W/brave_parse.py" "$N" < "$W/tmp/br.html"
