#리스트 공간 초기화 필요
#a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
a=[[0]*5 for _ in range(5)] #컴프리헨션
#a=[[0]*5]*5
value=1
for i in range(0,5):
    for j in range(0,5):
        a[i][j]=value #(5*i)+j+i
        value+=1
print(a)