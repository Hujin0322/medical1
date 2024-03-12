print('2단 출력')
for i in range(1,10):
    print('2*{}={}'.format(i,2*i))

#원하는 단을 입력받아 구구단을 입력하시오.
for _ in range(5):
    n=int(input('숫자를 입력하세요.: '))
    for i in range(1,10):
        print('{}*{}={}'.format(n,i,i*n))