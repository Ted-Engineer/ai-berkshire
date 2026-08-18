import sys, json, re, urllib.request, urllib.parse


def decode(gnews_url):
    m = re.search(r'articles/([^?]+)', gnews_url)
    if not m:
        return None
    aid = m.group(1)
    inner = '["' + aid + '"]'
    freq = json.dumps([[[ 'Fbv4jx', json.dumps(inner), 'null', 'null', 'null', None, 'en-US']]])
    req = urllib.request.Request(
        'https://news.google.com/_/DotsSplashUi/data/batchexecute',
        data=urllib.parse.urlencode({'f.req': freq}).encode(),
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'})
    body = urllib.request.urlopen(req, timeout=25).read().decode('utf-8', 'ignore')
    lines = [l for l in body.split('\n') if l.strip()]
    for m2 in re.finditer(r'"(https?://[^"]+?)"', lines[-1]):
        return m2.group(1)
    return None


if __name__ == '__main__':
    print(decode(sys.argv[1]))
