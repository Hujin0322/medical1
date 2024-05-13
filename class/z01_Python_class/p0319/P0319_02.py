class Car:

    def __init__(self,color,door,tire,speed):
        self.color=color
        self.door=door
        self.tire=tire
        self.__speed=speed #class내부에서만 접근 가능하게 제한 = 캡슐화 (__변수)
                            # 함수통해서만 변경 가능

    def upspeed(self,smartkey):
        if smartkey=='0X1100':
            self.__speed +=10 
        else:
            print('스마트키가 다릅니다.')
            
    def downspeed(self):
        self.__speed -=10
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed += speed
        
        
c1=Car('white',5,4,0)
# c2=Car('red',4,4,0)
c1.upspeed('0X1100')
c1.upspeed('0X1111')
c1.set_speed(500)

#클래스 변수에 직접 접근 불가
#get 통해서만 접근 가능.
print(c1.get_speed()) 

        