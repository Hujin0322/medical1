class Student:
    count=1
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo==0:
            self.stuNo=Student.count
        else:
            self.stuNo=stuNo
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math 
        self.avg=float('{:.2f}'.format(self.total/3))
        self.rank=rank
    
    def __str__(self):
        return f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'

students=[]       
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    # 1,홍길동,99,99,87,285,95.0,1
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close()

Student.count=len(students)+1 
search_list=['','검색할 학생의 이름을 입력하세요. >> ','몇 점 이상을 검색하시겠습니까? >> ','몇 점 이하를 검색하시겠습니까? >> ']

def stu_main_print():
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체입력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print("5. 학생성적삭제")
    print("6. 등수처리")
    print("0. 종료")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    choice = int(choice)
    return choice
    
def stu_input():
    while True:
        print('[ 학생성적입력 ]')
        name=input(f"{len(students)+1}번째 이름을 입력하세요.(0.취소). >> ")
        if name=='0':
            print('학생성적 입력을 취소합니다.')
            break        
        kor=int(input('국어 성적을 입력하세요. >> '))
        eng=int(input('영어 성적을 입력하세요. >> '))
        math=int(input('수학 성적을 입력하세요. >> '))
        s=Student(name,kor,eng,math)
        students.append(s)
        print("입력 데이터 :",s)

def stu_print():
    print('-'*60)
    print('\t\t[ 학생성적전체출력 ]')
    print('-'*60)
    print('번호\t이름\t국어\t영어\t수학\t총합\t평균\t등수')
    
def stu_all_print():
    for i in students:
        print(i)
        
def stu_search():
    while True:
        print("\t[ 학생성적 검색 ]")
        print("-"*40)
        print("1. 학생이름으로 검색")
        print("2. 총점이상 검색")
        print("3. 총점이하 검색")
        print("0. 이전화면 이동")
        choice = int(input("원하는 번호를 입력하세요.>> "))
        
        if choice==1:
            search=input(search_list[choice])
            s_list = []
            for i in students:
                if i.name.find(search) != -1: 
                    s_list.append(i)
                    
        elif choice==2:
            search=int(input(search_list[choice]))
            s_list = []
            for i in students:
                if i.total >= search:
                    s_list.append(i)
            
        elif choice==3:
            search=int(input(search_list[choice]))
            s_list = []
            for i in students:
                if i.total <= search:
                    s_list.append(i)
        
        elif choice==0:
            print('학생검색을 종료합니다.')
            break
        
        stu_print()
        stu_all_print()
    
        
def stu_update():
    while True:
        print('[ 학생성적수정 ]')
        search=input('수정할 학생의 이름을 입력하세요.(0.취소) >> ')
        if search=='0':
            print('수정을 취소합니다.')
            break
        else:
            cnt=0
            for i in students:
                if search == i.name:
                    break
                cnt+=1
            if cnt>=len(students):
                print('검색한 학생이 없습니다.')
            else:
                print('1. 국어')
                print('2. 영어')
                print('3. 수학')
                sub_num=int(input('수정할 과목을 입력하세요. >> '))
                
                if sub_num==1:
                    print(f'{search}학생의 국어 성적은 {students[cnt].kor}입니다.')
                    students[cnt].kor=int(input('수정할 점수를 입력하세요. >> '))
                    students[cnt].total=students[cnt].kor+students[cnt].eng+students[cnt].math
                    students[cnt].avg=float('{:.2f}'.format(students[cnt].total/3))
                
                elif sub_num==2:
                    print(f'{search}학생의 영어 성적은 {students[cnt].eng}입니다.')
                    students[cnt].eng=int(input('수정할 점수를 입력하세요. >> '))
                    students[cnt].total=students[cnt].kor+students[cnt].eng+students[cnt].math
                    students[cnt].avg=float('{:.2f}'.format(students[cnt].total/3))
                
                elif sub_num==3:
                    print(f'{search}학생의 수학 성적은 {students[cnt].math}입니다.')
                    students[cnt].math=int(input('수정할 점수를 입력하세요. >> '))
                    students[cnt].total=students[cnt].kor+students[cnt].eng+students[cnt].math
                    students[cnt].avg=float('{:.2f}'.format(students[cnt].total/3))
                stu_print()

def stu_delete():
    while True:
        print('[ 학생성적삭제 ]')
        search=input('삭제할 학생의 이름을 입력하세요.(0.취소) >> ')
        if search=='0':
            print('수정을 취소합니다.')
            break
        else:
            cnt=0
            for i in students:
                if search == i.name:
                    break
                cnt+=1
            if cnt>=len(students):
                print('검색한 학생이 없습니다.')
            else:
                choice=int(input(f'{search}학생을 삭제하시겠습니까? (1.진행 0.취소)'))
                if choice != 1:
                    print('삭제를 취소합니다.')
                else:
                    print('삭제를 진행합니다.')
                    del students[cnt]
        stu_print()

def stu_rank():
    print('[ 등수 처리 ]')
    for s in students:
        rank_cnt=1
        for i in students:
            if s.total<i.total:
                rank_cnt+=1
        s.rank=rank_cnt
    print('등수처리 완료')
    stu_print()

#-------------------------------------------------------------------------------------
while True:
    choice=stu_main_print()
        
    if choice==1:
        stu_input()

    elif choice==2:
        stu_print()
               
    elif choice==3:
        stu_search()
            
    elif choice==4:
        stu_update()
                    
    elif choice==5:
        stu_delete()       
        
    elif choice==6:
        stu_rank()

    elif choice==0:
        print('프로그램을 종료합니다.')
        break
