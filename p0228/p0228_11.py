#n1단부터 n2단까지 출력하기
n1=int(input('숫자를 입력하세요. >> '))
n2=int(input('숫자를 입력하세요. >> '))
#크기 비교해서 n1 더 크면 n2,n1 값 바꾸기
if n1>n2:
    n1,n2=n2,n1
    
for i in range(n1,n2+1):
    print('[{} 단]'.format(i))
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print()   

for i in range(1,10):
    for j in range(2,10):
        print('{}*{}={}'.format(j,i,i*j),end='\t')
    print()   
        

#2,4단만 나오도록 출력
for i in range(1,10):
    if i%2==0:
        if 2<=i<=4:
            print('[{} 단]'.format(i))
            for j in range(1,10):
                print('{}*{}={}'.format(i,j,i*j), end='\t')
            print()    
    