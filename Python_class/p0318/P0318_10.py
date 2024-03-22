class Card:
    kind=''
    number=''
    
    def __init__(self,kind,number):
        self.kind=kind
        self.number=number

#클래스를 이용하여 52장의 카드 생성
c_list=[]
kind=['SPADE','DIAMOND','HEART','CLOVER']
number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4):
    for j in range(13):
        c=Card(kind[i],number[j])
        c_list.append(c)


for i in range(52):
    print('카드출력: ',c_list[i].kind,c_list[i].number)


# #리스트 이용 --> 52장의 카드 생성
# c_list=[]
# kind=['SPADE','DIAMOND','HEART','CLOVER']
# number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# for i in range(4):
#     for j in range(13):
#         c=[kind[i],number[j]]
#         c_list.append(c)
        
# for i in range(4):
#     for j in range(13):
    
#     print('카드 출력: ',kind[i],number[i])
    





#1. 1개 변수로 선언
# kind='spade'
        
# #c1에 숫자를 5로 변경하여 c1출력
# c1=Card('spade',1)
# print(f'{c1.kind},{c1.number}')
# c1.number=5
# print(c1.kind,c1.number)

# #c2 'heart','A'
# c2=Card('heart','A')
# c2.kind='diamond'
# print(c2.kind,c2.number)


# #c2모양을 다이아몬드로 바꾸기
