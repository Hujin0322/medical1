import random


#random.random(): 0-1사이의 랜덤실수 생성
print(random.random())

#1-45 정수형 랜덤숫자 생성.
print(random.randint(1,45))

#1-2 랜덤 숫자 생성
print(random.randrange(1,3))

#리스트 랜덤 섞기
list=[1,2,3,4,5,6,7]
random.shuffle(list)
print(list)

#list에서 1개를 램덤으로 추출
print(random.choice(list))

#리스트에서 해당 개수만큼 랜덤 추출 (중복X 상태)
print(random.sample(list,2))

w_list=['토마토','바나나','사과','배','수박','메론','복숭아']
print(random.sample(w_list,3))

