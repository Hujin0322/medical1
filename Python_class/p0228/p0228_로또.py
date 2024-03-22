from random import*

#1-45 숫자를 넣어서 겹치지 않는 숫자 1-6개 
mynum=[] #1-45 숫자 입력 받기
lotto=[] #1-45사이의 랜덤한 숫자 6자리 입력
ok_num=[]

for i in range(6):
    n=int(input('숫자를 입력하세요. >> '))
    mynum.append(i)

l=[] 
#3. 1-45까지 리스트 생성
for i in range(1,46):
    l.append(i)
print('로또 숫자:{}'.format(l))    

# 로또 번호 생성하기
#4. 1-45 랜덤, 중복X 숫자 생성
for i in range(100): #100번 섞어줌
    tmp=randint(0,44)
    l[0],l[tmp]=l[tmp],l[0]
    
print('로또 숫자:{}'.format(l))    
#l은 중복없이 섞여있는 상태

#4. l=[1-45] 속 6개를  lotto에 list 생성
for i in range(6):
    lotto.append(l[i])  #랜덤하고 중복없는 숫자 6개 생성.
print('로또 숫자:{}'.format(lotto))    


#lotto[1,2,3,4,5,6], mynum[1,2,3,4,5,6]
m=[1,2,3]
ok=[]
for i in range(6):
    if mynum[i] in lotto: #mynum의 i번째가 lotto에 있는가
        ok.append(mynum[i])
    
print(mynum)
print(lotto)
print(ok)
