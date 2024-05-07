import oracledb

# 데이터베이스 연결 함수
def connection():        
    conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
    cursor = conn.cursor() #커서 생성 - 명령어 입력 받는 함수
    return cursor, conn
    
def close(cursor, conn):
    conn.close()

# employees의 이름으로 검색 로직 구현
# ex) 홍 검색 시 홍 관련 이름 모두 출력
# 무한 반복, -1 --> 프로그램 종료

while True:
    print("1. 이름으로 검색")
    print("2. 이름으로 같은 부서에서 근무하는 사원 조회")
    print("-1. 종료")
    choice = input("번호를 입력하세요.>> ")
    if choice == '-1':
        break
    elif choice == '1':
        search = input("이름을 입력하세요. >> ")   
        print("-"*40)
        sql=f"select * from employees where emp_name like '%{search}%' order by employee_id"
        cursor,conn = connection()
        cursor.execute(sql)
        data = cursor.fetchall()

        for d in data:
            print(d[0],end="\t")
            print(d[1],end="\t")
            print(d[4],end="\t")
            print(d[5],end="\t")
            print(d[6],end="\t")
            print(d[9])
        print("-"*40)
    
    elif choice == '2':
        search = input("이름을 입력하세요. >> ")   
        sql = f'''select b.employee_id, a.department_id, c.department_name, b.emp_name 
                from employees a, employees b, departments c
                where a.department_id = b.department_id and a.emp_name like '%{search}%' 
                and a.department_id = c.department_id'''
                
        cursor,conn = connection()
        cursor.execute(sql)
        data = cursor.fetchall()

        for d in data:
            print(d[0],end="\t")
            print(d[1],end="\t")
            print(d[2],end="\t")
            print(d[3])
        print("-"*40)
    
    #db연결 해제
    close(cursor,conn)
print("[ 프로그램을 종료합니다. ]")