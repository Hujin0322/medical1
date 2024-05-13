import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성. (명령어 기다림)

#이름 2번째에 a가 있는 학생 출력. (학번으로 순차정렬)
# sql = "select * from stu_score"
sql = "select no, name from stu_score where name like '_a%' order by no"
cursor.execute(sql) # cursor에 select한 결과값 저장 (결과값: list)
data = cursor.fetchall() #fatchall(): 모든 데이터 가져옴. fatchone(): 1개의 데이터 가져옴.


print("[ 모든 데이터 출력 ]")
# print(data)
for d in data:
    print(d)
    # print("학번: ",d[0])
    # print("이름: ",d[1])
    # print("국어: ",d[2])
    # print("영어: ",d[3])
    # print("수학: ",d[4])
    print("-"*40)
print("-")
print("타입: ",type(data))

conn.close()