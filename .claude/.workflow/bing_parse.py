import re, html, sys
n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
data = sys.stdin.buffer.read().decode('utf-8', errors='ignore')
items = re.findall(r'<li class="b_algo"(.*?)</li>', data, re.S)
out = 0
for i, it in enumerate(items):
    m = re.search(r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', it, re.S)
    if not m:
        continue
    href, title = m.group(1), re.sub(r'<[^>]+>', '', m.group(2))
    sm = re.search(r'<p[^>]*>(.*?)</p>', it, re.S)
    snip = re.sub(r'<[^>]+>', '', sm.group(1)) if sm else ''
    print('[%d] %s\n    %s\n    %s' % (out+1, html.unescape(title).strip(), href, html.unescape(snip).strip()[:280]))
    out += 1
    if out >= n:
        break
if out == 0:
    print('NO_RESULTS len=%d items=%d' % (len(data), len(items)))
