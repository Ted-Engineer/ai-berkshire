import sys, re, html, urllib.parse
n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
data = sys.stdin.read()
results = re.findall(r"<a[^>]*href=\"([^\"]*uddg=[^\"]*)\"[^>]*>(.*?)</a>", data)
snips = re.findall(r"<td class=\"result-snippet\">(.*?)</td>", data, re.S)
if not results:
    # fallback: plain links
    results = re.findall(r"<a[^>]*href=\"(https?://(?!lite\.duckduckgo|duckduckgo\.com)[^\"]+)\"[^>]*>(.*?)</a>", data)
    if not results:
        print("NO_RESULTS (len=%d)" % len(data)); sys.exit(0)
seen = 0
for i, (href, title) in enumerate(results):
    if 'duckduckgo.com' in href: continue
    t = html.unescape(re.sub(r'<[^>]+>', '', title)).strip()
    m = re.search(r'uddg=([^&]+)', href)
    if m: href = urllib.parse.unquote(m.group(1))
    s = html.unescape(re.sub(r'<[^>]+>', '', snips[i])).strip() if i < len(snips) else ''
    print("[%d] %s\n    %s\n    %s" % (seen+1, t, href, s[:300]))
    seen += 1
    if seen >= n: break
