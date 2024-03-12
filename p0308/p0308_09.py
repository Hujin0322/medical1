import random
random_num=str(random.randint(10000,99999))
print('[ 랜덤숫자 맞추기 ]')
print('랜덤 숫자:',random_num)
num=str(input('숫자 입력. >> '))

#12345
#43324
cnt=0
#숫자 자리로 맞춘 개수 출력
for i in range(len(random_num)):
    if random_num[i]==num[i]:
        cnt+=1
print(f'맞춘 갯수:{cnt}')
    