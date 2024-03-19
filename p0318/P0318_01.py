#클래스: 사용자정의 변수 - 함수 포함
#클래스의 첫글자는 대문자 사용
#클래스: 설계도

class Car: 
    color='white'
    door=5
    length=4710
    width=1800
    displace=1600
    speed=0
    
    def upSpeed(self,sp):
        self.speed+=sp
        
    def downSpeed(self,sp):
        self.speed-=sp
        
#객체선언 할때마다 제품이 한개씩 생산
c1=Car() #객체 선언
print('색상:',c1.color)
c1.color='red'
print('변경 후 색상:',c1.color)
c2=Car() 
print('색상:',c2.color)


