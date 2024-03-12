# #크기가 10인 리스트 생성, 7개는 0/ 3개는 1로 채우시오.
# #[1,1,1,0,0,0,0,0,0,0]

# #방법1)
# list=[0]*10
# for i in range(3):
#     list[i]=1
# print(list)

# #방법2)
# list=[1 for i in range(3)]+[0 for i in range(7)]
# print(list)

# #크기가 100인 리스트 생성, 10개는 1로 채우기
# #랜덤으로 섞어서 출력하시오.
import random

#방법1)
aList=[0]*100

for i in range(10):
    aList[i]=1
    random.shuffle(aList)
print(aList)

# #방법2)
# list1=[0 for i in range(90)]+[1 for i in range(10)]
# random.shuffle(list1)
# print(list1)

# a=10
# print(a+10) #비파괴형태
# a=a+10 #파괴형태
# print('a: ',a)

# #[10*10] 2차원 배열 생성하기
# #방법1)
# List=[0 for i in range(10)]
# a_list=[List for i in range(10)]
# print(a_list)
# #방법2)
# bList=[[0]*10 for i in range(10)]
# print(bList)

# 1이 10개인 10*10 생성.
bLists=[]
bList=[]
for i, j in enumerate(aList):
    if (i+1)%10 ==0:
        bList.append(j)
        bLists.append(bList)
        bList=[] #초기화
    else:
        bList.append(j)

newLists = [["추첨"]*10 for _ in range(10)]

while True:    
    cnt=0
    print("[ 10*10 좌표 ]")
    print("-"*60)
    #print(bLists)
    print('',0,1,2,3,4,5,6,7,8,9,sep="     ")
    print("-"*60)
    for i, b in enumerate(newLists):
        print(i,end='  ')
        for bb in b:
            print(bb,end="  ")
        print()
    print("-"*60)
    
    
    #bLists-값 비교/ newLists-표시
    while True: 
        x=int(input('가로 좌표 입력. >> '))
        y=int(input('세로 좌표 입력. >> '))
        cnt+=1     
        if bLists[x][y]==1:
            newLists[x][y]='당첨'  
        else:
            newLists[x][y]='[꽝]'
            cnt+=1 
            print('-'*50)
        print('{}번 남았습니다.'.format(10-cnt))
            
        if cnt==10:
            print('10번의 기회를 모두 사용하셨습니다. 종료합니다.')
            break
            