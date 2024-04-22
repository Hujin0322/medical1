num=[]
#for문을 사용하여 1-10까지 숫자를 채우시오.
for i in range(1,11):
    num.append(i)
print(num)

num2=[]
#1-10까지의 짝수를 num2리스트에 넣으세요.
#1). 방법
for i in range(2,11,2):
    if i%2==0:
        num2.append(i)
print(num2)

#2). 방법
num1=[ i for i in range(1,11)]
print(num1)

#1~10까지의 합을 for문을 사용해서 구하기
num=[1,2,3,4,5,6,7,8,9,10]
n1=0

#방법1.
for i in num:
    n1=n1+i
print('{}부터 {}까지의 합은 {}이다.'.format(num[0],num[-1],n1)) 

#방법2.
for i in range(len(num)):
    n1=n1+num[i]
    
#num2리스트 내 숫자들의 합 구하기
n=0
#방법1
for a in num2:
    n=n+a
print('{}부터 {}까지의 합은 {}이다.'.format(num2[0],num2[-1],n)) 
