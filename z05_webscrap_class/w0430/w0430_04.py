import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

#홍길동 --> 홍과 관련된 이름 모두 출력하도록
# 프로그램을 반복 형태로 구성, -1 입력 시 종료
while True:
    #검색어 입력부분
    search = input("찾고자 하는 이름을 입력하세요.(-1: 종료) >> ")
    if search == '-1':
        print("프로그램을 종료합니다.")
        break
    #검색 부분
    else:
        sql = f"select * from stu_score where name like '%{search}%'"
        cursor.execute(sql)
        data = cursor.fetchall()

        for d in data:
            print(d)
            
        print("검색된 데이터 갯수: ",len(data))

conn.close()