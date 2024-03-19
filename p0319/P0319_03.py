import os

class Student:
    count=1 #클래스변수: 모든 객체에 공통으로 사용 (저장소 1개, 주소로 이용)
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo==0:
            self.nstuNo=Student.count
        else:
            self.stuNo=stuNo
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=float('{:.2f}'.format(self.total/3))
        if rank !=0:
            self.rank=rank

    def __str__(self): #객체 호출 시 출력
        return f'학생성적: {self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'


#파일 불러와서 저장
students=[]
f=open('stu.txt','r',encoding='utf-8')
while True:
    txt=f.readline()
    if txt=='': break
    txt_list=txt.split(',')
    s=Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))    
    students.append(s)
    
#리스트 출력
for stu in students:
    print(stu)

   
        
        