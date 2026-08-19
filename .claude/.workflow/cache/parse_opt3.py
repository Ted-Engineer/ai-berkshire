import re,html
d=open('F:/ai-berkshire/.claude/.workflow/cache/mb_opt.html',encoding='utf-8',errors='ignore').read()
t=re.sub(r'<[^>]+>',' ',d); t=html.unescape(re.sub(r'\s+',' ',t))
idxs=[m.start() for m in re.finditer(r'9/4/2026',t)]
print('occurrences:',len(idxs))
for i in idxs[:6]:
    print('---')
    print(t[i:i+220])
