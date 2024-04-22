#리스트 만드는 방법 1. append 
a_list=[]
a_list.append(0) #리스트.append추가는 속도 느림
a_list.append(1)
a_list.append(2)
a_list[0]=3 #리스트에 값을 집어 넣는 것이 속도 빠름
print(a_list)

#2. 공간 만든 후 for문 돌리기
list=[0]*10
for i in range(10):
    list[i]=i+1
print(list)

#3. 컴프리헨션 사용
list1=[i+1 for i in range(10)]
print(list1)
#3차원 리스트 - 크기 지정X

