import random
# 0으로 25개 1차원 리스트 생성
aList = [0]*25

# 1로 5개를 변경
for i in range(5):
    aList[i] = 1   
    
# 랜덤섞기
random.shuffle(aList)
print(aList)
checklist = [[0]*5 for i in range(5)] #5*5의 공간을 생성

# 5*5 2차원 리스트에 넣기
for i in range(5):
    for j in range(5):
       checklist[i][j] = aList[5*i+j] 

#추첨 5*5 2차원 배열
viewlist=[['추첨']*5 for i in range(5)]

#5. viewlist 출력

cnt=0
print('기회는 5번입니다.')
#7. 좌표 입력 후 확인
while True:
    print('\t[ 5*5 viewlist 좌표]')
    print('-'*40)
    print('',0,1,2,3,4,sep='\t')
    print('-'*40)

    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(viewlist[i][j],end='\t')
        print()
    print('-'*40) 
    
    print(f'기회는 {5-cnt}번 남았습니다.')
    cnt+=1
    x=int(input('가로 좌표 입력. >> '))
    y=int(input('세로 좌표 입력. >> '))

    if checklist[x][y]==1:
        viewlist[x][y]='당첨'
        print(f'{x,y}: 당첨입니다.')
    else:
        viewlist[x][y]='[꽝]'
        print(f'{x,y}: 꽝입니다.')
    
    if cnt==5:
        print('기회가 끝났습니다. 게임 종료')
        break
    
        

    