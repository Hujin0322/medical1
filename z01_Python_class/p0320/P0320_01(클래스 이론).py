class Car:
    count=0 #클래스 변수 인식 (주소값 1개)
     
    def __init__(self,color='',speed=0):
        self.color=color #init 안에 변수선언 - 인스턴스변수 인식
        self.speed=speed  
        #클래스 변수 선언
        # Car.count=0      
        
#class사용 --> 인스턴스 선언 필요
c1=Car() #인스턴스 선언
c1.color='white'
Car.count=10 #클래스변수 10으로 변경

c2=Car()
c2.count=1 #기존 클래스변수 지우고 인스턴스 변수 다시 생성 (c2.count만 클래스변수 사용X)
print(c1.count) #10
print(c2.count) #10
Car.door=4 #이후 변수선언도 가능 (자제요망)
print(c2.door) #4
print(c1.door) #4


