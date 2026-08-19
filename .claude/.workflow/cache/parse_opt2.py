import re,html
d=open('F:/ai-berkshire/.claude/.workflow/cache/mb_opt.html',encoding='utf-8',errors='ignore').read()
t=re.sub(r'<[^>]+>',' ',d); t=html.unescape(re.sub(r'\s+',' ',t))
# looser: find all rows starting with date then strike
pat=re.compile(r'(9/4/2026)\s+\$([0-9.]+)\s+\$([0-9.]+)\s+(Put|Call)(.{0,180}?)([0-9]{2,3}\.[0-9]{2})%')
rows=pat.findall(t)
print('9/4 rows:',len(rows))
for dt,k,last,pc,mid,iv in rows:
    sk=float(k)
    if 350<=sk<=430:
        print(dt,k,pc,'last',last,'IV',iv+'%')
