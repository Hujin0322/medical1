import random
#주택복권
# 2조 711
# 1조 740
#1-9(조 앞의 숫자)
#0-999999(조 뒤의 수)

first_num=random.randint(1,9)
last_num=random.randint(0,999999)
# lotto='1조740042'
lotto=str(first_num)+'조'+'{:06d}'.format(last_num)
print(lotto)
l_input=input('복권을 입력하세요.(ex 1조111111) >> ')
#비교하는 프로그램 구현
#자리수 활용
cnt=0
for i in range(len(lotto)):
    if lotto[i]==l_input[i]:
        cnt+=1
print('{}개 맞았습니다.'.format(cnt-1))

