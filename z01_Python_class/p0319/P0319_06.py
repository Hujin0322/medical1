stu=[
    ['홍길동',100],
    ['유관순',98],
    ['이순신',95],
    ['김구',50],
    ['강감찬',99],
    ['김유신',90],
    ['홍길순',80],
    ['홍길자',70],
]

#이름으로 검색 -> '홍'이 들어가는 사람 모두 검색 출력
#이름으로 검색 -> '신'이 들어가는 사람 모두 검색 출력
while True:
    print('[ 학생성적검색 ]')
    print('1. 이름 검색')
    print('2. 점수 검색')
    cnt=0
    choice=int(input('원하는 번호를 입력하세요. >> '))
    
    if choice==1:
        print('[ 이름 검색 ]')
        search=input('이름을 검색하세요. >> ')
        stu_list=[]
        for s in stu:
            if s[0].find(search) != -1: #존재 여부 + 찾은 위치까지 저장 가능
            #if search in s[0] --> 존재 여부만 확인 가능
                stu_list.append(cnt)
            cnt+=1
            
        if stu_list==0:
            print('존재하는 학생이 없습니다.')
                
        else:
            print(f'{search}(으)로 검색된 사람:',end=' ')
            for i in stu_list:
                print(stu[i][0],end=' ')
        print()
        
        
    elif choice==2:
        print('[ 점수 검색 ]')
        score=int(input('점수를 입력하세요. >> '))
        stu_list=[]
        for s in stu:
            if s[1]>=score:
                stu_list.append(cnt)
            cnt+=1
            
        if stu_list==0:
            print('존재하는 학생이 없습니다.')
                
        else:
            print(f'{score}점 이상 학생:',end='\n')
            for i in stu_list:
                print(stu[i])
        print()
        
    
    
    
    
    
    
    


        
        
            