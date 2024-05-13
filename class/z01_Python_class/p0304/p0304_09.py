students=[[1, '홍길동', 100, 100, 99, 299, 99.67,1], 
          [2, '유관순', 99, 99, 100, 298, 99.33,1], 
          [3, '이순신', 90, 70, 50, 210, 70.0,1],
          [4, '김구', 96, 96, 95, 287, 95.67,1], 
          [5, '김유신', 97, 98, 97, 292, 97.33,1],
          [6, '강감찬', 100, 100, 100, 300, 100,1]]

while True:
    search=input('삭제하고자 하는 학생을 입력하세요. >> ')
    #이름찾기
    cnt=0 #찾은 학생의 위치
    for stu in students:
        if stu[1]==search:
            break
        cnt+=1
        
    if cnt==len(students): #전체 학생 수
        print('{} 학생이 없습니다.'.format(search))
        
    else:
        print('{} 학생을 찾았습니다.'.format(search))
        
    print('찾은 위치:',cnt)
    del students[cnt]
    print(students)    
    print('-'*40)
            