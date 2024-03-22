import co

coffee=0

while True:
    print('1.보통 커피')
    print('2.설탕 커피')
    print('3.블랙 커피')
    coffee=int(input('어떤 커피를 드릴까요?'))
    print()
    # 함수 호출
    co.machine(coffee)