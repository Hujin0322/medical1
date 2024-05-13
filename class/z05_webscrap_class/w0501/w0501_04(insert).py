import oracledb

while True:

    id= input("아이디를 입력하세요.(-1.종료) >> ")
    if id == '-1':
        break
    
    # id 먼저 검색 후 데이터 입력하도록 해야 함.
    conn = oracledb.connect(user="ora_user", password='1111',dsn="localhost:1521/xe")
    cursor = conn.cursor()
    
    sql = f"select * from member where id = '{id}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    #아이디 존재 여부 확인
    if len(data) != 0:
        print("다시 입력하세요. >> ")
        continue
    
    # 아이디 존재X, 계속 입력
    pw= input("패스워드를 입력하세요. >> ")
    name= input("이름을 입력하세요. >> ")
    gender= input("성별을 입력하세요. >> ")

    #DB 연결, 해제
    sql = f"insert into member values(member_seq.nextval,'{id}',{pw},'{name}','{gender}',sysdate)"
    conn = oracledb.connect(user="ora_user", password='1111',dsn="localhost:1521/xe")
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.execute('commit')
    
    print("입력이 완료되었습니다.")
    print()

    cursor.close()
    conn.close()
    
print("프로그램을 종료합니다.")