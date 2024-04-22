#1-100까지의 합 구하기
n=0
for i in range(1,101):
    n=n+i
print('합은 {}'.format(n))

#짝수의 합
sum1=0
for i in range(2,101,2):
    sum1=sum1+i
print('1-100까지 짝수의 합은 {}'.format(sum1))

s1=0
s2=0
s3=0
for i in range(1,101):
    s1=s1+i
    if i%2==0:
        s2=s2+i
    else:
        s3+=i
print('1-100까지의 합은 {}'.format(s1)) #홀수의 합
print('1-100까지 짝수의 합은 {}'.format(s2)) #짝수의 합
print('1-100까지 홀수의 합은 {}'.format(s3)) #홀수의 합

num=[1,2,3,4,5,6,7,8,9,10]
sum=0
#num리스트 안에 있는 값들의 합
for i in num:
    sum=sum+i
print(sum)
