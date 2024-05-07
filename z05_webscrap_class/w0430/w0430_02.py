import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성. (명령어 기다림)

#Q. board 테이블 id 포함 모든 컬럼, member 테이블의 name 컬럼 가져오기
# board 테이블 id, member 테이블 name
# sql = "select bno, a.id, name, btitle, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile \
#         from board a, member b where a.id = b.id"

#Q. stu_score에서 avg >= 90 'A', >=80 'B', C, D, < 60 'F'
# 학번, 이름, 합계, 평균, 성적 
# sql = '''select no, name, total, avg,
#         case
#         when avg >= 90 then 'A'
#         when avg >= 80 then 'B'
#         when avg >= 70 then 'C'
#         when avg >= 60 then 'D'
#         else 'F'
#         end as grade
#         from stu_score'''

# sql = "select * from stu_score"
# # 평균을 가지고 파이썬에서 프로그램 하여 학점 출력
# # 학번, 이름, 합계, 평균, 학점을 프로그램해서 출력하시오.

# cursor.execute(sql) # cursor에 select한 결과값 저장 (결과값: list)
# data = cursor.fetchall() #fatchall(): 모든 데이터 가져옴. fatchone(): 1개의 데이터 가져옴.

# for i in data:
#     print(i[0],i[1],i[5],i[6])
#     if i[6] >= 90: 
#         print("A")
#     elif i[6] >= 80: 
#         print(i[0],i[1],i[5],i[6],"B")
#     elif i[6] >= 70:
#         print(i[0],i[1],i[5],i[6],"C")
#     elif i[6] >= 60:
#         print(i[0],i[1],i[5],i[6],"D")
#     else: 
#         print(i[0],i[1],i[5],i[6],"F")


#Q. salary 평균 출력
sql = "select round(avg(salary),2)as salary from employees"
cursor.execute(sql)
data = cursor.fetchone()
print(data[0])



conn.close()

