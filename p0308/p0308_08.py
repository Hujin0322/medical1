import random

a='123456'
b='777776'

print(a[0])
print(a[-1])

first_num=random.randint(1,9)
last_num=random.randint(0,999999)
# lotto='1조740042'
lotto=str(first_num)+'조'+'{:06d}'.format(last_num)
# print(lotto)
cnt=0
for i in range(len(a),0,-1):
    if i==2: continue #조는 건너뛰기
    if a[i-1]==b[i-1]:
        break
    else:
        cnt+=1

if cnt==0:
    print('완전 꽝')
elif cnt==1:
    print('6번째 자리 맞음, 당첨금액: 1만원')
elif cnt==2:
    print('5, 6번째 자리 맞음, 당첨금액: 10만원')
elif cnt==3:
    print('4, 5 , 6번째 자리 맞음, 당첨금액: 100만원')
elif cnt==4:
    print('3,4,5,6번째 자리 맞음, 당첨금액: 1000만원')
elif cnt==5:
    print('2,3,4,5,6번째 자리 맞음, 당첨금액: 1억원')
elif cnt==6:
    print('1,2,3,4,5,6번째 자리 맞음, 당첨금액: 10억원')
elif cnt==7:
    print('1,2,3,4,5,6번째 자리 맞음, 당첨금액: 10억원')

        
        