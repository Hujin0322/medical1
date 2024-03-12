# 1-25까지 숫자를 램덤으로 섞은 다음 2차원 리스트에 넣어보기
#[
    # [1,2,3,4,5],
    # [6,7,8,9,10]
    # [11,12,13,14,15]
    # [16,17,18,19,20]
    # [21,22,23,24,25]
    # ]

#1. 1-25까지 리스트 생성
#2. 랜덤으로 섞기
#3. 2차원 리스트에 넣기

import random
num=random.randint(1,100)
n=0 #도전 횟수
save_num=[]

#숫자맞추기 프로그램 구현
#1-10까지 숫자 랜덤으로 생성, 숫자를 맞추는 프로그램입니다.
while True:
    in_num=int(input('1-100까지의 숫자를 입력하세요. >> '))
    save_num.append(in_num) #저장
    n+=1
    if num>in_num:
        print('입력한 숫자보다 더 큽니다.')
    elif num<in_num:
        print('입력한 숫자보다 더 작습니다.')
    else:
        print('정답입니다.')
        print('{}번의 기회를 사용했습니다.'.format(n))
        print('정답:',num)
        break


        