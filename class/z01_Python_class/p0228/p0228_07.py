a,b=10,8
a,b=b,a

n1=[0,1,2,3,4,5]
#0의 위치와 3의 위치 바꾸기
n1[0],n1[3]=n1[3],n1[0]

#2와 5의 위치 바꾸기
n1[2],n1[-1]=n1[-1],n1[2]

print(n1)

con=['미국','영국','일본','중국','스페인']

#영국과 중국의 위치 바꾸기
con[1],con[-2]=con[-2],con[1]

print(con)

#랜덤하게 섞기
from random import*
n1=[1,2,3,4,5,6,7,8,9,10]

for i in range(100):
    tmp=randint(0,9) #랜덤한 인덱스 만들기
    n1[0],n1[tmp]=n1[tmp],n1[0] #숫자 서로 섞어주기
    print(tmp)
    print(n1)
    