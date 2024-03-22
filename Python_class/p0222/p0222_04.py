#사칙연산 출력
#변수n1, n2
#출력
# 10+3=13
# 10-3=7

#문자열 출력
print('{}+{}={}'.format(10,3,10+3))

#변수 만들어서 출력
n1=10
n2=3
print('{}+{}={}'.format(n1,n2,n1+n2))
print('{}-{}={}'.format(n1,n2,n1-n2))
print('{}*{}={}'.format(n1,n2,n1*n2))
print('{}/{}={}'.format(n1,n2,n1/n2))

#입력 받아서 출력
n1=input('원하는 숫자를 입력하세요 >>')
n2=input('원하는 숫자를 입력하세요 >>')
n1,n2=int(n1),int(n2)
print('{}+{}={}'.format(n1,n2,n1+n2))
print('{}-{}={}'.format(n1,n2,n1-n2))
print('{}*{}={}'.format(n1,n2,n1*n2))
print('{}/{}={}'.format(n1,n2,n1/n2))
