class Car:
    car_name='드뉴아반떼'
    color='white'
    door=0
    length=0
    width=0
    speed=0
    
    def __init__(self,car_name='',color='',door=5,length=1000,width=1000,speed=0): #키워드 매개변수
        self.car_name=car_name
        self.color=color
        self.door=door
        self.length=length
        self.width=width
        self.speed=speed
        
    def up_speed(self,s):
        self.speed += s



#생성자를 사용한 객체=인스턴스선언
c1=Car('드뉴아반떼','wthie',5,2000,1000,60) 
print('철수 차 성능:',c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed) 

c2=Car('드뉴아반떼','green',5,2000,1000,100)
print('영희 차 성능:',c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed) 

c3=Car('디올뉴그랜져','화이트펄',5,2400,1400,150)
print('반장 차 성능:',c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed) 

        
# c1=Car()
# c1.car_name='드뉴아반떼'
# c1.color='white'
# c1.door=5
# c1.length=2000
# c1.width=1000
# c1.up_speed(60) #기존 속도에 더함
# c1.up_speed(40) #현재 100
# c1.speed=50 #현재 50


# #철수의 차 1대 생산
# car_name='드뉴아반떼'
# color='white'
# door=5
# length=2000
# width=1000
# speed=0

# color='red'
# speed=60

# print('차 성능:',car_name,color,door,length,width,speed)

#영희의 차 1대 생산, green, 나머지 동일 ,speed=100 설정 출력
# c2=Car()
# c2.car_name2='드뉴아반떼'
# c2.color2='green'
# c2.door2=5
# c2.length2=2000
# c2.width2=1000
# c2.speed2=100

# #반장 차
# c3=Car()
# c3.car_name3='디올뉴그랜저'
# c3.color3='화이트펄'
# c3.door3=5
# c3.length3=2500
# c3.width3=1400
# c3.speed3=150


# print('차 성능:',c1.car_name1,c1.color1,c1.door1,c1.length3,c3.width3,c3.speed3)
# print('차 성능:',c3.car_name2,c3.color2,c3.door2,c3.length3,c3.width3,c3.speed3)
# print('차 성능:',c3.car_name3,c3.color3,c3.door3,c3.length3,c3.width3,c3.speed3)
