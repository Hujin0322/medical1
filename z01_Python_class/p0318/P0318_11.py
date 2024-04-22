class Student:
    stuCount=0 #클래스 변수
    stuNo=0 #인스턴스 변수 ->객체 선언마다 데이터 값 다름.
    
    #생성자:__init__
    #클래스에 대해 개체선언을 하면 제일 먼저 호출되는 함수
    def __init__(self,name='',kor=0,eng=0,math=0): 
        self.name=name
        if kor>100:
            self.kor=100
        else:
            self.kor=kor
            
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=float('{:.2f}'.format(self.total/3))
        self.rank=0
        Student.stuCount+=1 #클래스변수선언
        self.stuNo=Student.stuCount  
        
    def stu_print(self):
        print(self.stuNo,self.name,self.kor,self.eng,
              self.math,self.total,self.avg,self.rank,sep='\t')
        
    #객체를 print하면 __str__함수를 제일 먼저 호출함    
    def __str__(self):
        return f'{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'


#매개변수가 있는 객체선언 (객체=인스턴스)
s1=Student('홍길동',100,100,99) #객체선언
s2=Student('유관순',99,99,98)

print(s1) #__str__함수 호출, 없으면 주소값 출력
s1.stu_print()
s2.stu_print()


