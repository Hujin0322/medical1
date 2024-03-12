# 성별, 키를 입력받아 남자일 경우 [m], 172.5이상 이면 [평균 이상], 이하면 [평균 이하]
#여자일 경우 [f], 159.6 이상이면 [평균 이상], 이하면 [평균 이하]

g=str(input('성별을 입력하세요. >> '))
h=float(input('키를 입력하세요. >> '))

if (g=='m') or (g=='M'):
    print('남자')
    if h>=172.5:
        print('평균 이상')
    else:
        print('평균 이하')
elif (g=='f') or (g=='F'):
    print('여자')
    if h>=159.6:
        print('평균 이상')
    else:
        print('평균 이하')
else:
    print('성별은 "f/F" 또는 "m/M"으로 입력해주세요.')