import random

#카드 종류:SPADE, DIAMOND, HEART, CLOVER
#카드 숫자:A,2,3,4,5,6,7,8,9,10,J,Q,K
#카드 총 수: 52장 

cardshape=['SPADE', 'DIAMOND', 'HEART', 'CLOVER']
cardnum=[0]*13
for i in range(13):
    cardnum[i]=i+1
cardnum[0]='A'
cardnum[11]='J'
cardnum[12]='Q'
cardnum[13]='K'

def card_create(cardlist):
    cnt=0
    for i in range(4):
        for j in range(13):
            cardlist[cnt]=[cardshape[i],cardnum[j]]
            cnt+=1
    print(cardlist)

def card_shuffle(cardlist):
    random.shuffle(cardlist)
    print(cardlist)
    
    
def card_shard(cardlist,arrnum):
    arrnum=0
    for i in range(5):
        arrnum+=1
        
def card_print(cardlist,arrnum):
    print(cardlist[arrnum])

#--------------------------------------------------------------

cardlist=[[0]*2 for i in range(52)]
arrnum=0

while True:    
    print('[ 카드 프로그램 ]')
    print('1. 카드생성')
    print('2. 카드섞기')
    print('3. 카드5장 나눠주기')
    print('4. 카드5장 확인하기')
    print('0. 종료')
    print('-'*40)
    choice=int(input('원하는 번호를 입력하세요. >> '))

    if choice==1:
        card_create(cardlist)
        
    elif choice==2:
        card_shuffle(cardlist)
        
    elif choice==3:
        card_shard(cardlist,arrnum)
        
    elif choice==4:
        card_print(cardlist,arrnum)

    else:
        print('프로그램을 종료합니다.')
        break