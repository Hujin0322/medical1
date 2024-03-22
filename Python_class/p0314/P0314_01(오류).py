#구문 오류: 프로그램 구현 중, 잘못된 코드 
#런 타임 오류: 프로그램 실행 중, 발생 오류

#예외처리 -> 오류 발생 시에도 프로그램 종료X
while True:    
    print('[ 리스트 출력 프로그램 ]')
    try: #오류 발생 예상 지점
        num=int(input('숫자를 입력하세요. >> '))
        a_list=[1,2,3,4,5]
        for i in range(num):
            print(a_list[i])
    except:
        print('구문에 오류가 났습니다.')

