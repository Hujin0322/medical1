member=[]
cnt=0
i=0
#이름 입력받아 [[1.홍길동],[2.유관순],[3. 이순신]]
while True:
    print('-'*25)
    print('1. 입력')
    print('2. 전체 출력')
    print('3. 검색 출력')
    print('4. 검색 삭제')
    print('5. 수정')
    print('0. 종료')
    ch=input('원하는 번호를 선택하세요. > ')
    print('-'*25)
    ch=int(ch)
    if ch==1:
        print('입력')
        name=input('이름을 입력하세요 ')
        cnt+=1
        m=[cnt,name]
        member.append(m)
        
    elif ch==2:
        print('번호\t이름')
        for i in range(len(member)):
            print('{}\t{}'.format(member[i][0],member[i][1]))
      
    elif ch==3:
        searchName=input('검색할 이름을 입력하세요. > ')
        for i, m in enumerate(member):
            if searchName in m:
                print('[{}]학생이 존재합니다.'.format(searchName))  
    
    elif ch==4:
        delname=input('삭제를 원하는 이름을 입력하세요. > ')
        for i, m in enumerate(member):
            if delname in m:
                del(member[i])
                print('{}님을 삭제했습니다.'.format(delname))

    elif ch==5:
        print('어떤 정보를 수정하시겠습니까. >> ')
        reName=input('수정하고 싶은 학생의 이름을 입력하세요. >> ')
        for i, m in enumerate(member):
            if reName in m:
                print(reName, '님을 선택하셨습니다.')
                ch_num=input('수정하고 싶은 항목을 선택해 주세요 (1. 번호 수정, 2. 이름 수정)')
                if ch_num=='1':
                    print(reName,'번호 수정을 선택하셨습니다.')
                    print(reName, '님의 번호는',member[i][0],'입니다.')
                    stu_num=int(input('어떤 번호로 수정하시겠습니까? >> '))
                    member[i][0]=stu_num
                elif ch_num=='2':
                    print('이름 수정을 선택하셨습니다.')
                    print(reName, '님의 이름은',member[i][1],'입니다.')
                    stu_name=str(input('어떤 이름으로 수정하시겠습니까? >> '))
                    member[i][1]=stu_name
                    
    elif ch==0:
        print('종료')
        break
    else:
        print('다시 입력')