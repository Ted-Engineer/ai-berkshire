import io
p='reports/50pct-upside-final-20260808.md'
s=io.open(p,encoding='utf-8').read()
# renumber the ORIGINAL body sections (which now collide with the new 二/三)
# order matters: do longest/most specific first
pairs=[
 ('## 二、漏斗执行记录（第一阶段）','## 四、漏斗执行记录（第一阶段）'),
 ('## 三、瓶颈扫描结论（bottleneck-hunter，第一阶段）','## 五、瓶颈扫描结论（bottleneck-hunter，第一阶段）'),
 ('## 四、方法论修正（本轮最重要的技术发现）','## 六、方法论修正（本轮最重要的技术发现）'),
 ('## 五、四家终选对比（第四阶段：冒泡排序）','## 七、四家终选对比（第四阶段：冒泡排序）'),
 ('## 六、#1 ADBE Adobe','## 八、#1 ADBE Adobe'),
 ('## 七、（已剔除）CRM Salesforce','## 九、（已剔除）CRM Salesforce'),
 ('## 七之二、#2 INTU Intuit','## 十、#2 INTU Intuit'),
 ('## 八、持仓股留/弃逐一评估（不自动排除）','## 十一、持仓股留/弃逐一评估（不自动排除）'),
 ('## 九、组合验证与仓位建议（第五阶段）','## 十二、组合验证与仓位建议（第五阶段）'),
 ('## 十、三情景估值（第三阶段，financial_rigor.py 输出）','## 十三、三情景估值（第三阶段，financial_rigor.py 输出）'),
 ('## 十一、信息充分度自评','## 十四、信息充分度自评'),
 ('## 十二、AI 研究偏见自检','## 十五、AI 研究偏见自检'),
 ('## 十三、大师语录点评','## 十六、大师语录点评'),
 ('## 十四、最终操作建议','## 十七、最终操作建议'),
 ('## 十五、诚实的最后一段','## 十八、诚实的最后一段'),
]
# apply in reverse order of target number to avoid collisions
for a,b in reversed(pairs):
    if a in s: s=s.replace(a,b,1)
    else: print('MISS',a)
# fix internal cross-refs
s=s.replace('详见第十一节《重大更正记录》','详见文末《重大更正记录》')
io.open(p,'w',encoding='utf-8').write(s)
print('renumbered, len',len(s))
