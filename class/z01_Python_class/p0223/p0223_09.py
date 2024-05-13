import datetime

now=datetime.datetime.now()
print(now)

month=6

#현재의 계절
if 12>=month>=1:
    if 3<=month<=5:
        print('봄')
    elif 6<=month<=8:
        print('여름')
    elif 9<=month<=11:
        print('가을')
    else:
        print('겨울')