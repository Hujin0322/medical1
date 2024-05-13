import oracledb




#평균 점수를 입력 받아 입력한 평균 점수 이상 이하 선택해서 학생을 출력하시오.
#반복 진행, -1 입력 시 종료
search = input("평균 점수를 입력하세요. >> ")
while True:
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor()
    search = input("평균 점수를 입력하세요.(-1.종료) >>")

    if search == '-1': 
        break    
    
    print("1. 점수 이상")
    print("2. 점수 미만")
    num_str = input("번호를 선택하세요. >> ")
    if  num_str == '1':       
        sql= f"select * from stu_score where avg >= {search}"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d)
                
    elif num_str == '2': 
        search = input("평균 점수를 입력하세요. >>")
        sql= f"select * from stu_score where avg < {search}"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d)
    
    print("프로그램을 종료합니다.")
    

conn.close()