class Car:
    car_name=''
    color=''
    door=0
    length=0
    width=0
    speed=0
    
    #생성자(전달받은 값)
    def __init__(self,car_name,color,door,length,width,speed):
        pass
    
    def up_speed(self,s):
        self.speed += s