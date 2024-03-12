from random import*

#1. 변수 선언
lotto=[]
mynum=[]

#2. 숫자 입력 받음

#3. num의 숫자 랜덤하게 섞음
num=[1,2,3,4,5,6,7,8,9,10]
for i in range(100):
   tmp=randint(0,9)
   # print(tmp)
   num[0],num[tmp]=num[tmp],num[0]
   
print(num) 

#4. 6개의 숫자 쌓기
for i in range(6):
    lotto.append(num[i])
print(lotto) 

###--------------------------------
#5. lotto와 mynum 비교
#리스트의 숫자 출력
ok=[]
for i in range(len(mynum)):
    # print(mynum[i])
    if mynum[i] in lotto:
        ok.append(mynum[i])

print(ok)
        