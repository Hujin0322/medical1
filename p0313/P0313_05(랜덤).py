import random

#from random import* #random 모듈명을 안붙여도 됨.
#-> print(random())

#0.000000- 9.999999 랜덤 소수점의 결과값 리턴
print(random.random())

#10과 20사이의 랜덤 float 결과값 리턴
print(random.uniform(10,20)) 

#1-2까지의 랜덤 숫자 리턴
print(random.randrange(1,3)) 

#리스트 내 랜덤 선택
print(random.choice([1,2,3,4,5]))

#리스트 내 랜덤으로 k개 선택, k가 list 개수보다 많으면 에러
print(random.sample([1,2,3,4,5],k=3))

#리스트의 요소를 랜덤으로 섞음
a_list=[1,2,3,4,5]
random.shuffle(a_list) # 출력X, 결과 저장
print(a_list)

#1-10, 범위 내 랜덤 int 1개 선택 
print(random.randint(1,10))




#import math

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))

