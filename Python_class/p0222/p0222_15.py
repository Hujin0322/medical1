import datetime #날짜 관련 기능 가져오기
now= datetime.datetime.now()

print(now) # => 2024-02-22 17:08:21.967157
print(now.year) #연도
print(now.month) #월
print(now.day) #일

print(now.hour)
print(now.minute)
print(now.second)

#시간을 사용해서 지금이 오전이면, 오전입니다. 오후면 오후입니다. 출력
#현재는 17시로 오후입니다.
h= now.hour
if (h<12) and (h==00):
    print('현재는 {}시로 오전입니다.'.format(h))
else:
    print('현재는 {}시로 오후입니다.'.format(h))

#1. 짝수달입니다. 홀수달입니다.
m= now.month
if m%2==0:
    print('짝수달입니다.')
    
#2. 월 이용/ 겨울입니다. 겨울이 아닙니다.
if 3<=m<=11:
    print('겨울이 아닙니다.')
else:
    print('겨울입니다.')

# print(type(m)) --> int인지 str인지 헷갈릴 때
#3. 계절 나누기
m=int(input('현재는 몇 월입니까? '))
if 3<=m<=5:
    print('봄입니다.')
if 6<=m<=8:
    print('여름입니다.')
if 9<=m<=11:
    print('가을입니다.')
elif m==12 or m==1 or m==2:
    print('겨울입니다.')