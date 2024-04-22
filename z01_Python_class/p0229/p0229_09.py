num=[[10,200],[30,40],[50,60]]

#요소 한 개씩 접근 
for i in range(len(num)):
    for j in range(len(num[i])):
        print(num[i][j])
     
#while
i=0
while i<len(num):
   j=0
   while j<len(num[i]):
       print(num[i][j])
       j=j+1
    i=i+1 