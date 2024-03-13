#인터프리터: 한 줄씩 변환->노출 위험(실행파일X), 가볍고 상대적으로 느림 ex)파이썬, 자바스크립트 -> 함수 선언이 먼저 되어야 함.
#컴파일러: 전체 소스 코드를 한 번에 기계어로 변환(컴파일), 무겁고 빠름 ex) java,C 
#두 수를 입력받아, 두 수 사이의 합계를 구하시오.

#1. 두 수 입력받기
#2. 함수 호출
#3. 1,10 입력받은 경우 1+......+10
#4. 합계 리턴받음
#5. 합계 출력

#1-10 더하기, 빼기, 곱하기의 결과값 출력하기

def plus(s_list):
    # if n1>n2:
        # n1,n2=n2,n1
    #더하기
    for i in range(s_list[0],s_list[1]+1):
        s_list[2]+=i
        s_list[3]-=i
        s_list[4]*=i
        

sum=0
minus=0
multi=1
n1=int(input('첫번째 수를 입력하시오. >> '))
n2=int(input('두번째 수를 입력하시오. >> '))
s_list=[n1,n2,sum,minus,multi]
plus(s_list)
print('더하기 결과값: ',s_list[2])
print('빼기 결과값: ',s_list[3])
print('곱하기 결과값: ',s_list[4])
# plus(s_list) #전역변수
# print('s_list:',s_list)
