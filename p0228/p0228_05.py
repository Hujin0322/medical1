n1=int(input('첫번째 숫자를 입력하세요. >> '))
n2=int(input('두번째 숫자를 입력하세요. >> '))
sum=0

#n1과 n2비교하여 작은 수를 n1에 넣기
if n1>n2:
    n1,n2=n2,n1

#n1-n2까지의 합 구하기
for i in range(n1,n2+1):
    sum=sum+i
print(sum)

#n1-n2까지의 홀수 값 저장.
odd_list=[]
for i in range(n1,n2+1):
    if i%2==1:
        odd_list.append(i)
print(odd_list)