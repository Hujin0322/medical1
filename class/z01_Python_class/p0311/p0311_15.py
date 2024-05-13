#함수 선언
def cal(num1,num2):
    sum=0
    tmp=0
    if num1>num2:
        #num1,num2=num2,num1 #파이썬에서만 가능
        tmp=num1
        num1=num2
        num2=tmp
    for i in range(num1,num2+1):
        sum+=i
    return sum
    

#ex) 1-10 --> 55
#두 수를 입력받아, 입력한 사이의 합계를 구하는 프로그램 구현.
sum=0
num1=int(input('첫번째 숫자를 입력하세요. >> '))
num2=int(input('두번째 숫자를 입력하세요. >> '))

sum=cal(num1,num2)
print('합계:',sum)