#Car 클래스 선언
class Car:
    carCount=0
    carNo=0
    
    def __init__(self,carNo,color,door,tire,speed):
        self.color=color
        self.door=door
        self.tire=tire
        self.speed=speed
        Car.carCount+=1
        self.carNo=Car.carCount
        
    def upspeed(self):
        self.speed+=10
    
    def downspeed(self):
        self.speed-=10
    
    def car_print(self):
        print(f'{self.carNo},{self.color},{self.door},{self.tire},{self.speed}')
        
        
#carNo에는 carCount 숫자를 이용하여 carNo 넣기    
#변수 선언: carNo, color=white, door=5, tire=4,speed 
#upspeed 함수 호출 시 무조건 10씩 증가
#downspeed 함수 호출 시 무조건 10씩 감소


#c1-white,5,4,0-> speed 30으로
c1=Car(0,'white',5,4,0)
c1.upspeed()
c1.upspeed()
c1.upspeed()
c1.car_print()

#c2-red,5,4,0 -> speed 100으로
c2=Car(0,'red',5,4,0)
for i in range(10):
    c2.upspeed()
c2.car_print()

#c3-silver,5,4,0 -> speed 70으로
c3=Car(0,'silver',5,4,0)
for i in range(7):
    c3.upspeed()
c3.car_print()

#car_list에 추가
car_list=[]
car_list.append(c1)
car_list.append(c2)
car_list.append(c3)


#car_list에 있는 모든 객체의 모든 color,door,tire,speed 모두 출력
for i in range(3):
    print('출력:',car_list[i].carNo,car_list[i].color,car_list[i].door,car_list[i].tire,car_list[i].speed)
# car_list.car_print()
