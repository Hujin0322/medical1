class Student:
  
    def __init__(self,name='',total=0):
        self.name=name
        self.__total=total
    
    def __str__(self):
        return (f'이름:{self.name}, 총합:{self.__total}')

    def set_total(self,total,login_id):
        if login_id=='admin':
            self.__total=total
        else:
            print('admin 관리자가 아니면 수정 불가')

    def get_total(self):
        return self.__total

    def stu_print(self):
        print('학생 성적 출력합니다.')
    
    # def __gt__(self,s):
    #     return self.total>s.total
        
        
s=Student('홍길동',95)
s2=Student('유관순',100)

s.set_total(400,'admin')
# print(s.__total) #접근제한으로 오류 발생
print(s.get_total())