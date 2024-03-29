#복습

#출력 print()
print('문자열') #문자열 출력
print(10.123) #숫자 출력
print(123*111) #사칙연산 후 출력

# %d --> 정수/ %f --> 실수/ %s --> 문자열
print('%d %f %s'%(10,12.234,'문자'))
print('%.2f'%(22.35848)) #소수 둘째자리까지 출력

# srt.format()
print('문자열을 쓰고 {}'.format(1))

#정수
print('{0:d}'.format(123)) 
print('{0}'.format(123)) #동일
print('{}'.format(123)) #동일

#실수
print('{0:f}'.format(123.123243))
print('{0}'.format(123.123243)) #동일
print('{}'.format(123.123243)) #동일
print('{0:.2f}'.format(123.123243))

#문자
print('{0:s}'.format('문자'))
print('{0}'.format('문자'))
print('{}'.format('문자'))

print('{0} {1} {2}'.format('빨','주','노'))
print('{0} {2} {1}'.format('빨','주','노'))

#변수
num=10 #정수: int
pi=3.14 #실수: float
result=True #bool: True, False
str1='문장입니다.' #string
ch='A' #문자
print(num)

s1='1+1=2'
print(s1)
s2='{}+{}={}'.format(1,1,2)
print('{}+{}={}'.format(1,1,2)) 

a=100
a+=1 # a=a+1
#+=, -=, /=, *=, //=, %=

#True, False
a,b=10,20
print(a==b) #일치
print(a!=b) #일치X
print(a>b)
print(a>=b)

#논리 연산자
#and 둘 다 참/ or 둘 중에 하나만 참이어도 참.
#not (참->거짓, 거짓->참)
a,b,c=100,200,150
result=((a>c) and (b>c)) #false and true
print(result)

#입력 받기 input()
name=input('이름을 입력하세요')
print('당신의 이름은 {}입니다'.format(name))

#input()의 결과값은 문자형
age= int(input('나이를 입력하세요'))
print('당신은 내년에 {}살입니다.'.format(age+1))

#if 조건문
#if 조건문1:
#   실행문1
#[else:
#   실행문2]
#조건문1이 참이면 실행문1을 실행 후 종료
#조건문1이 거짓이면 실행문2를 실행 후 종료
f='apple'
if f=='apple':
    print('먹는다')
else:
    print('버린다')
