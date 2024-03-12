#중첩 for
#for 안에 for
for i in range(3):
    print('i=',i)
    for j in range(2):
        print('j=',j)


#for문을 이용하여 2단 출력
n=9
for i in range(1,10):
    print('{}*{}={}'.format(n,i,n*i))
#입력받은 숫자의 단을 출력하세요.
#n=int(input('숫자를 입력하세요. >> '))
for i in range(2,10): #총 2단부터 9단까지 출력
    print('[{}단]'.format(i))
    for j in range(1,10):
        print('{}*{}={}\t'.format(i,j,i*j), end='')
    print()    
    
'''  
for j in range(5):
    print(j+1,'번째 출력')
    for i in range(1,6):
        print(i,end='')
    print()
    '''
    
#짝수단만 출력
for i in range(2,10):
    if i%2==0:
        print('[{}단]'.format(i))
        for j in range(1,10):
            print('{}*{}={}\t'.format(i,j,i*j), end='')
        print()

#(*1,3,5,7,9) 출력
for i in range(2,10):
    if i%2==1:
        print('[{}단]'.format(i))
        for j in range(1,10,2):
            print('{}*{}={}\t'.format(i,j,i*j), end='')
        print()
        