import base64, re, sys

def decode_gnews_url(url):
    m = re.search(r'articles/([^?/]+)', url)
    if not m:
        return None
    s = m.group(1)
    s2 = s + '=' * (-len(s) % 4)
    try:
        raw = base64.urlsafe_b64decode(s2)
    except Exception as e:
        return ["ERR " + str(e)]
    urls = re.findall(rb'https?://[\x20-\x7e]{10,}', raw)
    return [u.decode('utf-8', 'ignore') for u in urls]

if __name__ == "__main__":
    for u in sys.argv[1:]:
        print(decode_gnews_url(u))
