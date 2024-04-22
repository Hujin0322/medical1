from random import*

#1-10의 숫자만 사용
#1.변수 선언
lotto=[]
mynum=[]

#2. 입력받은 숫자 6개
#mynum=[] input을 이용하여 숫자 6개 넣기
for i in range(6):
    n=int(input('{}번째 숫자를 입력'.format(i)))
    mynum.append(n)

#3. 로또 번호 생성하기
l=[]

for i in range(50):
    tmp=randint(0,9) #0번방-9번방 랜덤한 숫자 생성
    l[0],l[tmp]=l[tmp],l[0]
    
print(l)

# lotto.append(l[0])~ lotto.append(l[5])
for i in range(6):
    lotto.append(l[i])
print(lotto)