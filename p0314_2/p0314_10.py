f=open('k001.csv','r',encoding='utf-8')
sum=0
cnt=0
while True:
    content=f.readline()
    if cnt==0:
        cnt+=1
        continue
    if content=="": break
    c_list=content.split(',')
    c_list[4]=int(c_list[4])
    sum+=c_list[4]
print(sum)
    