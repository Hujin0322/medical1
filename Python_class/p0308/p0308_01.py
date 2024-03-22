#리스트 [1-9]
#1) 방법
list=[]
for i in range(1,11):
    list.append(i)

#2) 방법
list=[i for i in range(1,11)]    

#3) 방법
list=[0]*10 #공간 만들기
for i in range(0,10):
    list[i-1]=i+1
