#인덱싱[0], 슬라이싱[0:4], len, upper, title, sawpcase, lower

a = [1234,11111,1,145,20,1323456547]
#리스트의 각 숫자의 길이를 출력하시오.
for i in a:
    print('길이: ',len(str(i)))

#짝수만 문자길이 출력
for i in a:
    if i%2==0:
        print('숫자:{}, 길이:{}'.format(i,len(str(i))))
        
#한글자씩 출력
title='혼자공부하는파이썬수업'
for i in range(len(title)):
    print(title[i]) #방에서 가져오기

#역순
title='안녕하세요'
for i in range(len(title)): #5
    print(title[(len(title)-1)-i],end='')

shape_list=['spade','diamond','heart','clover']
for i in shape_list:
    print(i.upper()) #모두 대문자
    print(i.title()) #맨 앞만 대문자
    print(i.swapcase()) #대->소/소->대 변환
    print(i.lower()) #모두 소문자