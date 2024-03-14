import random
c_number = [0]*13
for i in range(13):
    c_number[i] = i+1
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#   랜덤으로 2개를 뽑아서 출력하시오.
num=random.sample(c_number,k=2)
#   랜덤숫자 2 >> 1번방에 있습니다.
#   랜덤숫자 9 >> 8번방에 있습니다.
#   큰수: 9, 작은수: 2
for i in range(2):
    print(f'랜덤 숫자 {num[i]} >> {num[i]-1}번 방에 있습니다.')
if num[0]>num[1]:
    print(f'큰 수:{num[0]}, 작은 수:{num[1]}')
else:
    print(f'큰 수:{num[1]}, 작은 수:{num[0]}')
    
#---------------------------------------------------------------------
import random
c_number = [0]*13
for i in range(13):
    c_number[i] = i+1
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#   랜덤으로 2개를 뽑아서 출력하시오.
num=random.sample(c_number,k=2)
#   랜덤숫자 2 >> 1번방에 있습니다.
#   랜덤숫자 9 >> 8번방에 있습니다.
#   큰수: 9, 작은수: 2
for i, j in enumerate(c_number):
    if num[0]==j:
        print(f'랜덤 숫자 {j} >> {i}번 방에 있습니다.')
    if num[1]==j:
        print(f'랜덤 숫자 {j} >> {i}번 방에 있습니다.')
if num[0]>num[1]:
    print(f'큰 수:{num[0]}, 작은 수:{num[1]}')
else:
    print(f'큰 수:{num[1]}, 작은 수:{num[0]}')