import csv
# v5.4候选合并：当前池（v5.4各路来源）+ 归档v5.0池（同日早前同矩阵搜索产物，v5.4矩阵已重扫覆盖同名标的）
cur='.claude/.workflow/candidates.csv'
arch='.claude/.workflow/arch_pool.csv'
rows=[r for r in csv.reader(open(cur,encoding='utf-8')) if r and not r[0].startswith('ticker')]
seen={r[0] for r in rows}
added=0
try:
    for r in csv.reader(open(arch,encoding='utf-8')):
        if not r or r[0].startswith('ticker') or '?' in r[0]: continue
        if r[0] in seen: continue
        seen.add(r[0])
        src=r[3] if len(r)>3 else ''
        # 来源重标注：v5.4矩阵/B路/H/I/C/D同结构重扫已覆盖同名标的，归并标注
        rows.append([r[0],r[1],r[2],'v54-并入池('+src.split('-')[0]+')'])
        added+=1
except FileNotFoundError:
    print('归档池不存在')
with open(cur,'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['ticker','company','gics_sector','source'])
    for r in rows: w.writerow(r[:4])
print(f'并入{added}，唯一候选总数:{len(rows)}，达标={len(rows)>=300}')
import collections
src=collections.Counter(r[3].split('-')[0].split('(')[0] for r in rows if len(r)>3)
print('来源分布:',dict(src))
ai=sum(1 for r in rows if len(r)>2 and ('AI' in r[2] or (len(r)>3 and ('AI' in r[3] or 'H爆发' in r[3]))))
print(f'AI相关:{ai}/{len(rows)}={ai/len(rows)*100:.0f}%（≤65%）')
