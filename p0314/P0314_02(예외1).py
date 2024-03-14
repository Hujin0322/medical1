#외부와의 데이터 전송, 데이터 받기, 외부기기 연결, 다른 프로그램 연결 
# 외엔 되도록 오류 발생되지 않도록 하는 것이 가장 좋음.

print('프로그램 실행')
try:
    print(1)
    print(2)
    # print(1/0) #에러 발생
    print(3)
except: #예외 발생 --> 실행
    print(4)
    print(5)

print(6)
print('프로그램 종료')
