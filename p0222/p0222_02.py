num1=10
print(num1)
print(10)

num3=0b101010
print(num3)

#변수 사용
#변수 - bool/int/float/str 형 (대소문자 구분)
#단독 사용 변수=소문자/ 클래스=대문자
#변수는 언더바 포함, 숫자로 시작X
#예약어 사용X (ex) if, True 등)
#변수는 마지막으로 입력된 값 저장.
a=10
a=5
print(a)
a,b=1,2
print(a)
print(b)

#입력 받기 = input() -> 문자열로 입력 가능
name=input("이름을 입력하세요:")
print('당신의 이름은',name+'입니다')

age=input('나이를 입력하세요:')

#숫자로 바꿔주기 
#1. age=int(input('나이를 입력하세요:'))
#2. age=int(age)
#3. format(int(age)+1)
print('당신은 내년에 {}살입니다.'.format(int(age)+1))

#연습: 숫자 하나 입력 > 구구단 출력
#문자열 출력 > 변수 만들어서 출력 > 입력 받아서 출력해라?
n=input('구구단을 입력하세요')
print('2*1={}'.format(int(n)*2))

