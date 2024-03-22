# 리스트: 대괄호로 감싸서 0개 이상의 원소가 저장될 수 있음. (여러 형태의 변수를 섞어서 사용 가능/0부터 시작)

listA=[1,2]
listB=[]

n1=1
n2=2
n3=3
n4=4
n5=5

list1=[1,2,3,4,5]
list2=['사과','복숭아','딸기','배','포도','수박']
list3=[1,'홍길동',99.1]

print(list2)
print(list2[1]) # 복숭아
print(list1[3]) # 4
print(list3[2]) # 99.1

#리스트의 마지막 요소부터 음수로 표현 가능
print(list2[-1]) #수박
print(list2[-2]) #포도

#리스트의 길이 출력 --> len()
a=len(list2)
print(a)
# => print(len(list2))

#딸기 출력
print(list2[2])
print(list2[-4])
print(list2[len(list2)-1]) #수박

#리스트 슬라이싱
aa=[0,1,2,3,4,5,6,7,8,9,10]
print(aa)
print(aa[1:4]) #1이상, 4미만 출력 --> [1,2,3]
print(aa[3:8]) #3이상 8미만 --> [3, 4, 5, 6, 7]
print(aa[2:]) #2번 부터 끝까지 --> [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(aa[:7]) #처음부터 7미만까지
print(aa[:]) #처음부터 끝까지 =print(aa)
print(aa[1:-1]) # 끝번호 빼고 --> [1, 2, 3, 4, 5, 6, 7, 8, 9] 

#요소 확인: 내부 포함 여부 확인 방법 제공
#in, not in
print('포도' in list2) #True
print(11 in aa) #False
print(0 not in aa) #False

listc=[1,2,3,['a','b','c'],[4,5]]
#      0 1 2       3         4
print(listc[3]) #['a', 'b', 'c']
print(1 in listc) #True
print(4 in listc) #False
print([4,5] in listc) #True

