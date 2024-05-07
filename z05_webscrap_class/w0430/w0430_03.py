import oracledb

# DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성. (명령어 기다림)

# sql 실행
# Q. employees 테이블에서 사번, 이름, 월급, 실제 월급, 실웝급(월급+(월급*커미션)), 원화 환산 월급(월급*1410) 천 단위 표시 출력
# sql = '''select employee_id, emp_name, salary, 
#         salary+(salary*nvl(commission_pct,0)) salary2, 
#         to_char((salary*1410),'999,999,999') kor_salary 
#         from employees'''


# Q. 부서별 평균월급, 최대월급, 최소 월급 출력
sql = '''select department_id, round(avg(salary),2), max(salary), min(salary) 
        from employees
        where department_id is not null
        group by department_id
        order by department_id'''

cursor.execute(sql)
data = cursor.fetchall()

print("[데이터 출력]")
print("-"*40)
for d in data:
    print('')
    print(d[0],end="\t")
    print(d[1],end="\t")
    print(d[2],end="\t")
    print(d[3])


# print("사번\t사원명\t월급\t실월급\t원화환산")
# print("-"*40)
# for d in data:
#     print(d[0],end="\t")
#     print(d[1],end="\t")
#     print(d[2],end="\t")
#     print(d[3],end="\t")
#     print("￦",d[4].strip())
    
conn.close()

