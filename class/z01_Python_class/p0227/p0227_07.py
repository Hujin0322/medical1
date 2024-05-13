#1-5까지 합계를 구하시오.
sum=1+2+3+4+5

total=0
total=total+1 #t=1
total=total+2 #t=1+2
total=total+3 #t=1+2+3
total=total+4 #t=1+2+3+4
total=total+5 #t=1+2+3+4+5

t=0
for i in range(1,6,1): #i=1,2,3,4,5
    t+=i
print(total) 

#1-10까지의 합 구하기 (for)
a=0
for i in range(1,11,1):
    a+=i #a+i=a
    print(a)
print('1부터 10까지의 합: {}입니다'.format(a))
#1-100까지의 합 구하기
b=0
for i in range(1,101,1):
    b+=i
print('1부터 100까지의 합: {}입니다'.format(b))

#n1-n2까지의 합 구하기
n1=int(input('첫번째 숫자: '))
n2=int(input('두번째 숫자: '))
sum1=0
for i in range(n1,n2+1,1):
    sum1=sum1+i
print('합: {}'.format(sum1))

