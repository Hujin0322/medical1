#함수 선언 def 이름() 정의
#함수값은 return
#함수 호출 이름()
#매개변수: 힘수로 데이터 전달하는 변수, 매개변수 개수는 항상 같아야 함.
#가변매개변수 선언 *values, 가변매개변수는 일치하지 않아도 됨.
#리스트, 딕셔너리 매개변수는 주소값이 전달 됨.

#퀴즈.1
#함수를 사용하여 두 수를 입력받아, 더하기, 빼기, 곱하기, 나누기 결과값을 출력하시오.

def cal(num1,num2,c): #받을 값
    if c==1:
        result=num1+num2
    elif c==2:
        result=num1-num2
    elif c==3:
        result=num1*num2
    elif c==4:
        result=num1/num2
    return result
            
#두 수 입력 받아 값을 리턴 받은 다음, 출력하기.
result=0
num1=int(input('첫번재 숫자를 입력하세요. >> '))
num2=int(input('두번째 숫자를 입력하세요. >> '))    
print('1.더하기 2.빼기 3.곱하기 4.나누기')
c=int(input('숫자를 선택하세요. >> '))

result=cal(num1,num2,c) #리턴받을 값 = 이름(보내줄 값)
print(f'결과값:{result}') 