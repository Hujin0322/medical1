#랜덤으로 숫자 1개 생성

#입력한 숫자보다 크면 작은 수를 입력하시오.
#입력한 숫자보다 작으면 큰 수를 입력하시오. 출력

import random
ran_num=random.randint(1,100)
in_num=0
cnt=1
try_list=[]

print('[ 랜덤 숫자 맞추기 게임 ]')
while True:
    in_num=int(input(f'도전{cnt}. 1-100까지의 숫자를 입력하세요. >> '))
    try_list.append(in_num)
    if ran_num > in_num:
        print('입력한 숫자보다 큰 수를 입력하세요.')
    
    elif ran_num < in_num:
        print('입력한 숫자보다 작은 수를 입력하세요.')
    
    else:
        print('정답입니다.')    
        break
    
    cnt+=1
    
#----------- 종료 ------------
#총 입력한 횟수: ()회 
print(f'입력 횟수: {cnt}')
#현재까지 입력한 숫자: ()
print('시도 숫자: {}'.format(try_list))