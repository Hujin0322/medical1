import oracledb
import math

#연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
#명령창 = cursor/ conn의 명령창에 연결
cursor = conn.cursor()


# 최초 번호
num = 0
perCount = 10
startrow = 1 #1,11,21,31....
endrow = 10 #10,20,30 .....
limit = 0

search = input("검색할 학생 이름을 입력하세요. >> ")
sql = f'''select count(*)
        from (select row_number() over (order by no) rnum, a.* 
        from stu_score a
        where id like '%{search}%')
        '''
cursor.execute(sql)
all_count = cursor.fetchone()
limit = math.ceil(all_count[0]/perCount)  

while True:
    if num != 0:
        print("< 이전 ",end="\t") #이전 데이터 10개 가져오기
        print("다음 > ") #다음 데이터 10개 가져오기
        no = input("원하는 번호를 입력하세요.")
        if no == '1': 
            if num == 1: num =1
            else: num -= 1
        else: 
            num += 1
            if num > limit: num = limit

        startrow = (num-1) *perCount+1 #1,11,21,31....
        endrow = startrow + perCount-1 #10,20,30 .....
        
    else: num += 1 
    
    sql = f'''select * from (
            select row_number() over (order by no) rnum, a.* from stu_score a
            where id like '%{search}%') 
            where rnum >= {startrow} and rnum <= {endrow}
            '''
    cursor.execute(sql)
    data = cursor.fetchall()

    ## 10개씩 나눠서 보여주도록 구성
    print("[ 학생 검색 데이터 ]")
    for d in data:
        print(d)
        
    print("-"*30)
    print("검색된 페이지 : ",num-1," / 검색된 데이터 수: ",all_count[0])
    
    