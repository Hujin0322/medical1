#변수
#기본형: bool, int, float. string
#list, tuple, dict
a=True
b=False
print('bool형은 {},{}가 있다.'.format(a,b))

c=45
print('int형은 정수 {:d}'.format(c))
print('%d'%(c))

d=3.123455
print('float형은 실수 {:2f}와 같이 소수점이 있는 숫자'.format(d))

e='문자' 
print('문자열입니다.')
print(e+'입니다.')
print(e,'입니다.')
print('{:s}'.format(e))

#input() - 콘솔창에서 입력을 받는다.
print('글자를 콘솔창에 보여준다.')
str1=input('입력하세요. >> ')
print('{}은 입력한 변수값입니다.'.format(str1))
n1=input('첫번째 숫자를 입력하세요. >> ')
n2=int(input('두번째 숫자를 입력하세요. >> '))
print(int(n1)*n2)

