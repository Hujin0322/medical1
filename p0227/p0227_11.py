from random import *
n1=randrange(1,10) #1-10 사이의 정수
n2=randrange(10) # 0-10 사이의 정수
n3=randint(1,10) #1-10사이의 정수

print(n1,n2,n3)

lotto=[]
#lotto에 1-10사이의 랜덤한 숫자 6개 넣기
for i in range(6):
    n2=randrange(1,10)
    lotto.append(n2)    
print(lotto)

#내가 직접 입력한 숫자 6개를 넣기.
mynum=[]
for i in range(6):
    n1=int(input(' >> '))
    mynum.append(n1)
print(mynum)