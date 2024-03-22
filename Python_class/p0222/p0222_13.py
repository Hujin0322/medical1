#1. 숫자를 입력받아서 양수면 양수, 아니면 음수 출력 (n조건문)
n=-10
n=int(input('숫자를 입력하세요 >> '))
if n>0:
    print('입력하신 숫자 {}는 양수입니다.'.format(n))
else:
    print('음수')

n=-10
n=int(input('숫자를 입력하세요 >> '))
if n==0:
    print('0입니다.')
else:
    print('0이 아닙니다.')

n=str(input('어떤 거?'))
if n=='국수' or n=='밥':
    print('먹어')