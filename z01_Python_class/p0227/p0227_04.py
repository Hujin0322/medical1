''' 반복문 - for, while
for 변수 in 반복 가능한 데이터:
    수행문
    
for 카운터 변수 in range(시작값, 끝값+1, 증감값):
    수행문
'''

for i in range(0,10,1): #0~9까지=10번 반복.
    print('증감1: 수행문입니다.')

for i in range(0,10,2): #0,2,4,6,8
    print(i, '증감2: 수행문입니다.')

for i in range(0,3): #증감값이 1일 때는 생략 가능
    print('두번째 수행문입니다.')

for i in range(5): #5번 반복해라.
    print('세번째 수행문입니다.')

print('-'*35)
for i in range(3): #3번 반복, 1증가 생략, 0부터 생략
    print(i)
#카운터 변수i를 사용하지 않을 때 _로 사용 가능.
for _ in range(7): #안녕하세요 7번 반복
    print('안녕하세요.')

for i in range(10,0,-2):#10부터 0까지 2씩 줄어들어라.
    print(i,'증감 2: 수행문입니다.')#10부터 0까지 2씩 줄어들어라.

l1=[100,200,300,400,500]
#리스트 안 요소 확인 in/not in

'''
for 변수 in 리스트명:
    실행문

for 변수 in range(len(리스트명)):
    실행문
    리스트명[변수]
'''

for n in l1:
    print(n)

for i in range(len(l1)):
    print(i)#0,1,2,3,4~
    print(l1[i]) #l1[0], l1[1], l1[2]~
    
#for문을 사용하여 1-100 사이의 홀수 출력하기
#1) if 사용X(증감 사용)
for i in range(1,101,2):
    print(i, end=" ")

print() #줄 바꿈

#2) if 사용
for i in range(100):
    if (i+1)%2==1:
        print(i+1, end=' ')

print() #줄 바꿈

#50 1 사이의 6의 배수를 역순으로 출력하기
for i in range(48,0,-6):
    print(i, end=' ')

print() #줄 바꿈

#input 사용, 입력: 두 개의 숫자를 입력받음
#출력: 사칙 연산
#a+b=c
#a-b=d 
#a*b=e
#a/b=f
#계산을 10번 반복하는 코드 만들기 (입력도 10번 반복)
#(숫자 입력과 사칙연산)*10
for i in range(10):
    n1=int((input('1번 숫자를 입력하세요. >>')))
    n2=int((input('2번 숫자를 입력하세요. >>')))
    print('{}+{}={}'.format(n1,n2,n1+n2))
    print('{}-{}={}'.format(n1,n2,n1-n2))
    print('{}*{}={}'.format(n1,n2,n1*n2))
    print('{}/{}={}'.format(n1,n2,n1/n2))   

#연산자 입력 받아서 if문 사용하여 출력
for i in range(10):
    n1=int((input('1번 숫자를 입력하세요. >>')))
    n2=int((input('2번 숫자를 입력하세요. >>')))
    cal=input('연산자를 입력하세요. >> ')
    if cal=='+':
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif cal=='-':
        print('{}-{}={}'.format(n1,n2,n1-n2))
    elif cal=='*':
        print('{}*{}={}'.format(n1,n2,n1*n2))
    elif cal=='/':
        print('{}/{}={}'.format(n1,n2,n1/n2)) 
    else:
        print('다시 입력')
#a+b
#a-b=d 
#a*b=e
#a/b=f

