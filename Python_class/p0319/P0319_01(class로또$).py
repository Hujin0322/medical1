import random

#class 선언: 설계도
class Card:
    def __init__(self,kind,number):
        self.kind=kind
        self.number=number
        
        
#52장의 카드
#SPADE,DIAMOND,HEART,CLOVER
#A,1,2,3,4,5,6,7,8,9,10,11,12,13
kind_list=['SPADE','DIAMOND','HEART','CLOVER']
number_list=['A',1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list=[]

def random_one():
    num=random.randint(0,51)
    print('랜덤카드 1장: ',num, card_list[num].kind,card_list[num].number)
    return card_list[num]

#52장의 카드 생성
for i in range(4):
    for j in range(13):
        card_list.append(Card(kind_list[i],number_list[j])) #객체선언

#52장의 카드 출력        
for i in range(52):
    print('카드: ',card_list[i].kind,card_list[i].number)
    
#랜덤으로 1장 뽑기
# random_one()

#중복없이 랜덤카드 5장 뽑기

#1. 방법: 순차 정렬 섞고 뽑기
print('-'*50)
random.shuffle(card_list)
for i in range(5):
    print('랜덤섞기 카드: ',card_list[i].kind,card_list[i].number)
print('-'*50)


#2. 5장 랜덤 뽑기
ran_list=random.sample(card_list,5)
for i in ran_list:
    print(i.kind,i.number)
print('-'*50)


#3. tmp_list 저장장소 1개 만들고, 랜덤뽑기 1장의 카드를 저장장소 리스트와 비교
tmp_list=[]
cnt=0
while True:
    if cnt==5: break #뽑은 카드가 5장일 경우 종료 
    c=random_one()
    for i in tmp_list:
        if c.kind==i.kind and c.number==i.number: #같은 카드가 있으면 다음으로 넘어감
            continue
    
    #중복카드가 없으면 추가
    tmp_list.append(c)
    cnt+=1

    
for i in tmp_list:
    print('랜덤 1장 카드: ',i.kind,i.number)

