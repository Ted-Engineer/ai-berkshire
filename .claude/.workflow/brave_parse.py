import re, html, sys
n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
data = sys.stdin.buffer.read().decode('utf-8', errors='ignore')
# Brave organic: <div class="snippet ..."><a href="URL">...<div class="title">TITLE</div>...<div class="snippet-description">SNIP</div>
blocks = re.split(r'<div[^>]*class="snippet[ "]', data)[1:]
out = 0
seen = set()
for b in blocks:
    m = re.search(r'<a[^>]+href="(https?://[^"]+)"', b)
    tm = re.search(r'class="title[^"]*"[^>]*>(.*?)</div>', b, re.S)
    dm = re.search(r'class="snippet-description[^"]*"[^>]*>(.*?)</div>', b, re.S)
    if not m or not tm:
        continue
    url = m.group(1)
    if url in seen or 'brave.com' in url:
        continue
    seen.add(url)
    title = html.unescape(re.sub(r'<[^>]+>', '', tm.group(1))).strip()
    desc = html.unescape(re.sub(r'<[^>]+>', '', dm.group(1))).strip() if dm else ''
    print('[%d] %s\n    %s\n    %s' % (out+1, title, url, desc[:280]))
    out += 1
    if out >= n:
        break
if out == 0:
    print('NO_RESULTS len=%d' % len(data))
