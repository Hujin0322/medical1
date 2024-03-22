from random import*

n1=randrange(1,11)
n2=randint(1,10)

lotto=[]
mynum=[]
#랜덤한 숫자 6개 lotto리스트에 넣고 내가 입력한 숫자는 mynum에 넣기
for i in range(6):
    n=int(input('{}번째 숫자를 입력하세요. >> '.format(i+1)))
    mynum.append(n)
print('입력된 숫자는 {}입니다.'.format(mynum))


for i in range(6):
    tmp=randrange(1,10)
    if tmp not in lotto:
        lotto.append(tmp)
        
print('출력된 숫자는 {}입니다.'.format(lotto))

