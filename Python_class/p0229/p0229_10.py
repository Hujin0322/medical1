'''
str1='10'
print(str1.isdigit()) #True

str2='a'
print(str2.isdigit()) #False


while True:
    n=input('원하는 번호를 적어주세요. >> ')

    if n.isdigit(): #숫자지만 문자열 ex) 'i', '0'
        n=int(n)
    else:
        print('문자가 입력되었습니다. 다시 입력 부탁')
    
    if n==0:
        print('숫자 0 입력됨, 다시')
'''


#이름 검색 후 삭제
students=[[1,'홍길동',100],[2,'이순신',90],[3,'유관순',85],[4,'김유신',70],[5,'김구',95]]
i = 0
while True:
    
    print('1. 학생 검색 ')
    print('2. 학생 삭제 ')
    print('3. 프로그램 종료')
    ch=(input('원하는 번호를 입력해주세요. >> '))

    if ch.isdigit(): #입력한 게 숫자면 True
        ch=int(ch)
        # searchName=input('검색할 학생의 이름을 입력해주세요. >> ')
        # for stu in students:
        #    if searchName in stu:
        #        print('O')
        #   else:
        #        print('X')
    if ch==1:
        searchName=input('검색할 학생의 이름을 입력하세요 >> ')
        ck=0 #학생이 존재하지 않음
        for stu in students:
            if searchName in stu:
                print('{} 학생이 존재합니다.'.format(searchName))
                print(stu)
                ck=1 #학생이 존재함.

        if ch==0:
            print('존재X')
            
    elif ch==2:
        delName=input('삭제하고 싶은 학생을 입력하세요. >> ')
        chk=0
        for i, stu in enumerate(students):
            if delName in stu:
                del(students[i])
                chk=1
                # print(delName, 학생이 삭제되었습니다.'.format(delName))
                print(stu)
                
        # for i in enumerate(students):
        #     if delName in stu:
        #         del(students=[i])
        print(students)
    
    elif ch==3:
        print('프로그램이 종료되었습니다.')
        break
    else:
        print('잘못 입력하셨습니다.')