#!/bin/bash
# Google News RSS search (works reliably from this network).
# Usage: bash .claude/.workflow/gnews.sh "query" [n]
Q="$1"; N="${2:-8}"
W="F:/ai-berkshire/.claude/.workflow"
mkdir -p "$W/tmp"
ENC=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$Q")
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
curl -s -m 20 -A "$UA" "https://news.google.com/rss/search?q=${ENC}&hl=en-US&gl=US&ceid=US:en" -o "$W/tmp/gn.xml" -w "gnews:%{http_code}/%{size_download}\n"
python "$W/gnews_parse.py" "$N" < "$W/tmp/gn.xml"
