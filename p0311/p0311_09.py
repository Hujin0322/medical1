input1=int(input('1번째 숫자를 입력하시오 >> '))
input2=int(input('2번째 숫자를 입력하시오 >> '))
#함수의 return을 사용해서 입력된 두 수의 사칙연산 출력
print('1.+ 2.- 3.* 4./')
um=input('사칙연산 골라라')

def cal(input1,input2):
    result1=input1+input2
    result2=input1-input2
    result3=input1*input2
    result4=input1/input2
    return result1,result2,result3,result4
result1,result2,result3,result4=cal(input1,input2)
print('더하기:',result1)
print('빼기:',result2)
print('곱하기:',result3)
print('나누기:',result4)

data=cal(input1,input2)
    
    
           


#i:지역변수 (함수 벗어나면 0부터 다시 시작)
for i in range(10):
    sum=0
    sum+=i

for i in range(5):
    result=1
    result+=i
 
print(sum)
print(result)   


def plus(v1,v2):
    v1=v1+100
    v2=v2+200
    return v1,v2  #함수 밖에서 사용하기 위해선 return 값 돌려줘야 함.  
        
#함수 호출
v1=1
v2=2
plus(v1,v2)

#출력
print(v1,v2)