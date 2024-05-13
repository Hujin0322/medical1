#퀴즈.1
#함수를 사용하여 두 수를 입력받아, 더하기, 빼기, 곱하기, 나누기 결과값을 출력하시오.

def cal(num1,num2): #받을 값
    r_list=[0]*6
    r_list[0]=num1
    r_list[1]=num2
    r_list[2]=num1+num2
    r_list[3]=num1-num2
    r_list[4]=num1*num2
    r_list[5]=num1/num2
    return r_list


save_list=[]
while True:
    num1=int(input('첫번재 숫자를 입력하세요.(0.종료) >> '))
    if num1==0:
        break
    num2=int(input('두번째 숫자를 입력하세요. >> '))    
    
    #함수 호출  
    r_list=cal(num1,num2) #리턴받을 값 = 이름(보내줄 값)
    save_list.append(*r_list)
    ##save_list에 r_list 저장

    print('{},{} 결과값: {},{},{},{}'.format(*r_list)) 

#현재까지 입력한 숫자와 결과값을 모두 출력 하시오.
for s in save_list:
    print('[ 현재까지 입력한 숫자{}, 결과값 ]')
    print('{},{} 결과값: {},{},{},{}'.format(*save_list))
