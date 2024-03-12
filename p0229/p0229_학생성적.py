students=[]
cnt=0
while True:
    print('-'*35)
    print('\t'+'[학생성적프로그램]') 
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력')
    print('5. 학생검색출력')
    print('6. 등수처리')
    print('0. 프로그램 종료')
    print('-'*35)
    choice=int(input('원하는 번호를 입력하세요, >> '))
    print('입력하신 번호는 {}입니다.'.format(choice))
    
    if choice==1:
        print('학생 성적 입력입니다.')
        name=str(input('학생의 이름을 입력하세요. >> '))
        kor=int(input('국어 점수를 입력하세요. >> '))
        eng=int(input('영어 점수를 입력하세요. >> '))
        math=int(input('수학 점수를 입력하세요. >> '))
        cnt=cnt+1
        m=[cnt,name,kor,eng,math,(kor+eng+math),((kor+eng+math)/3),0]
        students.append(m)    
    
    if choice==2:
        print('학생 성적 수정입니다.')
        print('어떤 정보를 수정하시겠습니까? >> ')
        
    
    if choice==3:
        print('학생 성적 삭제입니다.')
        delname=input('삭제할 학생의 이름을 입력하세요. >> ')
        ck=0
        for a, m in enumerate(students):
            if delname in m:
                del(m[a])
                print('{} 학생 성적을 삭제했습니다.'.format(delname))
                
    if choice==4:
        print('학생 성적 전체 출력입니다.')
        print('번호\t이름\t국어\t영어\t수학\t총합\t평균\t0')
        for i in range(len(students)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(students[i][0],students[i][1],students[i][2],students[i][3],
                                                      students[i][4],students[i][5],students[i][6],students[i][7]))
    
    if choice==5:
        print('학생 검색 출력입니다.')
        searname=input('검색할 학생의 이름을 입력하세요. >> ')
        ck=0
        for b, m in enumerate(students):
            if searname in m:
                print('{}학생은 존재합니다.'.format(searname))
                ck=1
            
    if choice==6:
        print('등수 처리입니다.')
    
    if choice==0:
        print('프로그램 종료합니다.')
        break