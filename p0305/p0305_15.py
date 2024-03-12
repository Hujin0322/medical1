import operator 
fruit=['바나나','바나나','바나나','딸기','딸기','딸기','딸기','딸기',
         '배','사과','사과','바나나','바나나','바나나','딸기','딸기',
         '딸기','딸기','딸기','배','사과','사과']
counter={}

for fru in fruit:
    if fru not in counter:
        counter[fru]=0
    counter[fru]+=1
print(counter)    

print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))
