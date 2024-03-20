class Student:

    def __init__(self,name,total):
        self.name=name
        self.total=total

    # def __str__(self):
    #     return f'이름: {self.name}, 총점: {self.total}'
        
    def __del__(self):
        return '클래스가 소멸될 때 실행' 
        
    def __add__(self,s):
        return self.total+s.total
    
    def __gt__(self,s): #크거나 같다라고 비교할 때
        return self.total>s.total
        
    def __eq__(self,s):
        return self.name==s.name and self.total==s.total
            
    
        
s1=Student('홍길동',100)
s2=Student('유관순',90)
s3=Student('이순신',95)
s4=Student('홍길동',100)
print(s1) #class 출력 시 __str__함수 호출 (__str__X --> 주소값 출력)
print(s1+s2) #클래스를 더하기 할 때, __add__함수 호출

#클래스는 비교 불가 but, __gt__ 메소드 생성하면 호출
print(s1>s2)
print(s2>s3)

print(s1)
print(s4)

# __eq__
print('s1==s4: ',s1==s4)   
print('s1==s2: ',s1==s2)