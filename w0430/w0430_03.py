import oracledb

# DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성. (명령어 기다림)

#sql 실행
sql = ""
cursor.execute(sql)
data = cursor.fetchall()
print(data[0])



conn.close()

