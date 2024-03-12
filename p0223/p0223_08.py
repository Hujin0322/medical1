#점수를 입력받아 90점 이상 [A] 80점 이상이면 [B], 70점 이상이면 [C], 나머지는 [F]를 출력
a=int(input('점수를 입력하세요.'))
if a>100:
    print('점수를 다시 입력하세요.')
elif a>=90:
    print('90점 이상입니다.')
    if a>=98:
        print('A+')
    elif a>=94:
        print('A')
    else:
        print('A-')
elif a>=80:
    print('80점 이상입니다.')
    if a>=88:
        print('B+')
    elif a>=84:
        print('B')
    else:
        print('B-')
elif a>=70:
    print('70점 이상입니다.')
    if a>=78:
        print('C+')
    elif a>=74:
        print('C')
    elif a>=70:
        print('C-')
else:
    print('F\n과락입니다.')

