import os

#Student 클래스
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
            
    def __str__(self): #객체 호출 시 출력
        return f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'


#---------------------------------------------------------------------------------------------------------------------
#파일 불러오기-------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
students=[]
f = open("stu.txt","r",encoding="utf-8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list=txt.split(",")
    s=Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))    
    students.append(s)
f.close()

#파일 불러오기 한 후 학생수 +1
Student.count=len(students)+1

#---------------------------------------------------------------------------------------------------------------------
#함수부분
#---------------------------------------------------------------------------------------------------------------------
search_txt=[
                '',
                '검색할 학생의 이름을 입력하세요.',
                '[총점] 몇 점 이상 검색하시겠습니까? >> ',
                '[총점] 몇 점 이하 검색하시겠습니까? >> '
            ]

s_sub=['','국어','영어','수학'] 


def main_title_print(): #메인화면
    print('-'*60)
    print('\t[학생성적프로그램]')
    print('-'*60)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생성적검색')
    print('4. 학생성적수정')
    print('5. 성적등수처리')
    print('6. 학생성적삭제')
    print('7. 학생성적 파일저장')
    print('0. 프로그램 종료')
    print('-'*60)
    choice=input('원하는 번호를 입력하세요. >> ')
    choice=int(choice)
    return choice
    

def stu_main_print(): 
    print('-'*60)
    print('[ 학생성적출력 ]')
    print('-'*60)
    print('학번\t이름\t국어\t영어\t수학\t총합\t평균\t등수')
    print('-'*60)


#1. 학생성적입력
def stu_insert(): 
    while True:
        print('-'*40)
        print('[ 학생성적입력 ]')
        print('-'*40)
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
        if name=="0":
            print("학생 입력을 취소합니다.")
            break
        name=input('학생의 이름을 입력하세요. >> ')
        kor=int(input('국어성적을 입력하세요 >> '))
        eng=int(input('영어성적을 입력하세요 >> '))
        math=int(input('수학성적을 입력하세요 >> '))
        students.append(Student(name,kor,eng,math))
        s=Student(name,kor,eng,math)
        students.append(s)
        print('입력데이터: ',s)


#2. 학생성적출력
def stu_print():
    stu_main_print()
    for i in students:
        print(i) #객체출력 --> __str__ 출력
    print()


#3-1. 학생성적검색
def search_title_print():
    print('-'*60)
    print('\t[ 학생성적검색 ]')
    print('-'*60)
    print('1. 이름 검색')
    print('2. 총점 이상 검색')
    print('3. 총점 이하 검색')
    print('0. 이전화면 이동')
    choice=int(input('원하는 번호를 입력하세요. >> '))
    return choice

#3-2. 부분검색
def stu_search(choice):
    if choice==1:
        search=input(search_txt[choice])
    else:
        search=int(input(search_txt[choice]))
        
    #전체리스트에서 검색
    s_list=[]
    for s in students:
        if choice==1:
            if s.name.find(search) != -1:
                s_list.append(s)
                
        elif choice==2:
            if s.total >= (search):
                s_list.append(s)
                
        elif choice==3:
            if s.total <= (search):
                s_list.append(s)
                
    if len(s_list) == 0:
        print('존재하지 않습니다.')
    else:
        print(f'{search}(으)로 검색된 사람: ',end='\n')
        stu_main_print() 
        for i in s_list:  
            print(i)
                
    
    
#---------------------------------------------------------------------------------------------------------------------
#프로그램 시작
#---------------------------------------------------------------------------------------------------------------------
while True:
    choice=main_title_print() #메인화면
    
#1. 학생성적입력--------------------------------------------------------------------------
    if choice==1: stu_insert()
              
#2. 학생성적출력--------------------------------------------------------------------------
    elif choice==2: stu_print()
               
#3. 학생성적검색 --------------------------------------------------------------------------------
    elif choice==3:
        while True:
            choice=search_title_print()
            if choice==0:
                print('이전화면으로 이동합니다.')
                break
            stu_search(choice)

#4. 학생성적수정----------------------------------------------------------------------------------
    elif choice==4:
        cnt=0
        print('[ 학생성적수정 ]')
        s_list=[]
        search= input('검색할 학생의 이름을 입력하세요. >> ')
        for s in students:
            if s.name==search:
                s_list.append(s)
            cnt+=1
                
        if len(s_list)==0:
            print('존재하지 않습니다.')
            
        else:
            stu_main_print() 
            for i in s_list:  
                print(i)
        
        print('1.국어 2.영어 3.수학')
        choice_sub=int(input('변경할 과목의 번호를 입력하세요. >> '))
        
        if choice_sub==1:
            print(f'{s_sub[choice_sub]}를 선택하셨습니다.')
            print(f'{search}학생의 {s_sub[choice_sub]}점수는 {i.kor}입니다.')
            score=int(input('변경할 점수를 입력하세요.'))
            s[cnt].kor=score
            s[cnt].total=s[cnt].kor+s[cnt].eng+s[cnt].math
            s[cnt].avg=float('{:.2f}'.format(s[cnt].total/3))
            
            stu_print()
        
        
                
            

        
