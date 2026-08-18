import re, html, sys
n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
data = sys.stdin.buffer.read().decode('utf-8', errors='ignore')
items = re.findall(r'<item>(.*?)</item>', data, re.S)
out = 0
for it in items[:n]:
    t = re.search(r'<title>(.*?)</title>', it, re.S)
    l = re.search(r'<link>(.*?)</link>', it, re.S)
    d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    s = re.search(r'<description>(.*?)</description>', it, re.S)
    title = html.unescape(t.group(1)).strip() if t else ''
    desc = html.unescape(s.group(1)).strip()[:220] if s else ''
    print('[%d] %s\n    %s | %s\n    %s' % (out+1, title, l.group(1).strip() if l else '', d.group(1).strip() if d else '', desc))
    out += 1
print('(total %d items)' % len(items))
