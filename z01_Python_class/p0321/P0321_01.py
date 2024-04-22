class Student:
   
    # def __init__(self,name,kor):
    #     self.name=name
    #     self.kor=kor
        
    def stu_print(self):
        print('학생 성적 출력합니다.')
        
class Lotto():
    pass
        
def s_print():
    print('class 밖에 있는 함수')

#클래스 내부 함수는 객체선언 해야 사용 가능 (self 필수)
s=Student()
s2=Lotto()
if isinstance(s2,Student):
    print('Student 클래스 변수입니다.')
elif isinstance(s2,Lotto):
    print('Lotto 클래스 변수입니다.')
s.stu_print() 

print(type(s2))