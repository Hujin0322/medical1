#0-20 사이의 5의 배수로 이루어진 list 만들기
#출력:[0,5,10,15,20]
num=[]
for i in range(21):
    if i%5==0:
        num.append(i)

print(num)

 
lan=['c','prthon','java','jquery','css']
#1. 하나하나 출력 for문 이용
#1). in 리스트명  사용
for i in lan:
    print(i)
#2). in range() 사용
for i in range(len(lan)):
    print(lan[i])
    
#2. 카운터 변수 i 사용하기
# 1.c, 
# 2.python 출력
for i in range(len(lan)): #for i in range(5)
    print('{}. {}'. format(i+1, lan[i]))

num=[1,-1,2,3,-4,5,6,-8,9,-10]
#양수면 양수, 음수면 음수 출력
#1: 양수
#-1: 음수
#2: 양수..

for i in range(10):
    if num[i] >= 0:
        print('{} : 양수'.format(num[i]))
    else:
        print('{}: 음수'.format(num[i]))

for i in num:
    print(i, end=':')
    if i >= 0:
        print('{}'.format('양수'))
    else:
        print('{}'.format('음수'))
        