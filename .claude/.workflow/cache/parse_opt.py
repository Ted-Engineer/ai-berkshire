import re,html
d=open('F:/ai-berkshire/.claude/.workflow/cache/mb_opt.html',encoding='utf-8',errors='ignore').read()
t=re.sub(r'<[^>]+>',' ',d); t=html.unescape(re.sub(r'\s+',' ',t))
pat=re.compile(r'(9/4/2026|8/19/2026|9/11/2026|8/21/2026)\s+\$([0-9.]+)\s+\$([0-9.]+)\s+(Put|Call)\s+([0-9]+)\s+[^%]*?([0-9]{2,3}\.[0-9]{2})%')
rows=pat.findall(t)
for dt,k,last,pc,vol,iv in rows:
    sk=float(k)
    if 350<=sk<=430:
        print(dt,k,pc,'last',last,'IV',iv+'%')
