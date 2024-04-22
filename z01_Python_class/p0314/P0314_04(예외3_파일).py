#파일 1개 저장

#file open
file=open('memo.txt','w',encoding='utf-8')
try:
    #file write
    file.write('안녕하세요1.\n')
    file.write('안녕하세요2.\n')
    print(1/0)
    file.write('안녕하세요3.\n')
    file.write('안녕하세요4.\n')
except Exception as e: #Exception(예외 설명 출력) as 별칭
    print('저장 중 에러 발생')
    print(e) #에러 정보 확인 가능
finally:
    #파일 닫기
    file.close() #예외 발생 시에도 무조건 실행.