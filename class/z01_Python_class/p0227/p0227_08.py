for i in range(3):
    print('안녕')
    #i=0 일 때
    #i=1 일 때
    #i=2 일 때
    
for i in range(3): #i=0,1,2
    print(i)
sum1=0
for i in range(1,6,1):
    sum1=sum1+i

#숫자 한 개를 입력받아 1부터 입력한 수까지의 합 구하기
n1=int(input('숫자 한 개를 입력하시오: '))
n=0 #총합 넣을 변수 선언
for i in range(1,n1+1):
    n=n+i

print('{}부터 {}까지의 합은 {}입니다.'.format(1,n1,n))

#짝수의 합만 구하기 (100까지)
a=0
for i in range(0,101,2):
    a=a+i

print('합: {}'.format(a))  
  
print()

#짝수만 출력
for i in range(1,n+1):
    if i%2==0:
        a=a+i
print('{}부터 {}까지의 합은 {}입니다.'.format(1,n1,a))
    
print()

#1-10까지의 곱
c=1
for i in range(1,11):
    c=c*i
print('{}부터 {}까지의 곱은 {}입니다.'.format(1,n1,c))
