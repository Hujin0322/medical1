import oracledb

#DB 연결
conn = oracledb.connect(user="ora_user", password='1111',dsn="localhost:1521/xe")
cursor = conn.cursor()

sql = "create table mem(id varchar2(30) primary  key, pw number, name varchar(30), mdate date)"
cursor =conn.cursor(sql)

# ddl 명령어: commit이 없음, create, alter 
# dml 명령어: insert, update, delete

#DB연결 해제
cursor.close()
conn.close()
