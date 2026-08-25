#!/bin/bash
# gnfetch.sh "query" N_INDEX -> resolve gnews redirect #N and dump article text
cd "$(dirname "$0")/../.."
Q="$1"; IDX="${2:-1}"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
ENC=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$Q")
XML=".claude/.workflow/tmp/gn2.xml"
mkdir -p .claude/.workflow/tmp
curl -s -m 20 -A "$UA" "https://news.google.com/rss/search?q=${ENC}&hl=en-US&gl=US&ceid=US:en" -o "$XML"
LINK=$(python3 -c "
import re,sys
data=open('$XML',encoding='utf-8',errors='ignore').read()
items=re.findall(r'<item>(.*?)</item>',data,re.S)
i=int('$IDX')-1
if i<len(items):
    m=re.search(r'<link>(.*?)</link>',items[i],re.S)
    t=re.search(r'<title>(.*?)</title>',items[i],re.S)
    import html
    print(html.unescape(t.group(1)).strip() if t else '')
    print(m.group(1).strip() if m else '')
")
TITLE=$(echo "$LINK" | head -1)
URL=$(echo "$LINK" | sed -n 2p)
echo "TITLE: $TITLE"
REAL=$(curl -s -m 25 -L -o /dev/null -w "%{url_effective}" -A "$UA" "$URL")
echo "RESOLVED: $REAL"
curl -sL -m 25 -A "$UA" "$REAL" | python3 -c "import sys,re,html;d=sys.stdin.read();t=re.sub(r'<script.*?</script>|<style.*?</style>','',d,flags=re.S);t=re.sub(r'<[^>]+>',' ',t);print(html.unescape(re.sub(r'\s+',' ',t))[:6000])"
