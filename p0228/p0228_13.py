#1. 변수 선언
score=[[80,90,85],[70,80,90],[84,92,80],[72,81,76]]
name=['홍길동','유관순','이순신','김구']
total=[]
#2. 코딩
#2-1)요소 하나하나 출력하기
for i in range(len(score)):
    print(score[i])
    for j in range(len(score[i])):
        print(score[i][j])
        
#2-2) 작은 요소의 합을 구해서 total에 넣기

for i in range(len(score)):
    #print(score[i])
    s=0
    for j in range(len(score[i])):
        s=s+score[i][j]
    total.append(s)
print(total)       
#     total=[255,240,256,229] 

#3. 출력
#3-1) total=[255,240,256,229]
#3-2) 250 미만 불합격/ 250이상 합격 ex) 홍길동님 합격입니니다. 출력
for i in range(4):
    if total[i]>=250:
        print('{}님 총합 {}점으로 합격입니다.'.format(name[i],total[i]))
    else:
        print('{}님 총합 {}점으로 불합격입니다.'.format(name[i],total[i]))