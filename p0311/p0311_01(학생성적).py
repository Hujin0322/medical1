students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]
cnt=len(students)+1
sub=['','국어','영어','수학']        
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    
    if not choice.isdigit():
        print(' 숫자를 입력하세요.')
    choice=int(choice)
    
    if choice==1:
        print('[ 학생 성적 입력 ]')
        name=input('학생의 이름을 입력하세요.(0.취소) >> ')
        if name=='0':
            continue
        student={}
        student['stuNo']='S'+'{:03d}'.format(cnt)
        student['name']=name
        kor=int(input('국어 점수를 입력하세요. >> '))
        eng=int(input('영어 점수를 입력하세요. >> '))
        math=int(input('수학 점수를 입력하세요. >> '))
        student['kor']=kor
        student['eng']=eng
        student['math']=math
        total=kor+eng+math
        student['total']=total
        avg=float('{:.2f}'.format(total/3))
        student['avg']= avg
        students.append(student)
        print(students)
    
    elif choice==2:
        print(' [학생 성적 전체 출력 ]')
        print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
        for key in students:
            for value in key:
                print(key[value],end='\t')
            print()
    
    elif choice==3:
        print('[ 학생 성적 검색 ]')
        while True:
            chk=0
            searname=input('검색할 학생의 이름을 입력하세요.(0.취소) >> ')
            if searname=='0':
                print('학생 성적 검색을 취소합니다.')
                break
            else:
                for i in range(len(students)):
                    if searname==students[i]['name']:
                        chk+=1
                        print(f'{searname}학생을 찾았습니다.')
                        print(students[i])
                    elif chk>len(students):
                        print(f'{searname}학생이 존재하지 않습니다.')

    elif choice==4:
        while True:
        # 찾는 부분 프로그램 작성하시오.
            search = input("찾고자 하는 학생의 이름을 입력하세요.(0.취소)")
            chk = 0
            if search == "0":
                break
            for s_dic in students: #5명이 있으면 5번반복
                if s_dic["name"] == search:
                    break
                chk += 1
            
            print("찾고자 하는 학생의 위치 :",chk)
            
            if chk == len(students): #학생수만큼 for문을 돌면
                print(f"{search} 학생은 없습니다. 다시 입력하세요.")    
            else:
                print(f"{search} 학생을 찾았습니다.")
                while True:
                    print("[ 수정할 과목 선택 ]")
                    print("-"*30)
                    print("1.국어\t2.영어\t3.수학")
                    s_input = int(input("수정하려는 과목을 선택하세요.( 0.취소 ) >> "))
        
                    
                    if s_input==1:
                        print(f'{search}의 {sub[s_input]} 점수는 {students[chk]['kor']}점 입니다.')
                        modi_num=int(input('변경할 점수를 입력하세요. >> '))
                        students[chk]['kor']=modi_num
                        students[chk]['total']=students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                        students[chk]['avg']='{:.2f}'.format(students[chk]['total']/3)
                        print(f'{students[chk]['name']}의 점수가 변경되었습니다.')
                        print('-'*50)
                        print(students[chk])
                            
                    elif s_input==2:
                        print(f'{search}의 {sub[s_input]} 점수는 {students[chk]['kor']}점 입니다.')
                        modi_num=int(input('변경할 점수를 입력하세요. >> '))
                        students[chk]['eng']=modi_num
                        students[chk]['total']=students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                        students[chk]['avg']='{:.2f}'.format(students[chk]['total']/3)
                        print(f'{students[chk]['name']}의 점수가 변경되었습니다.')
                        print('-'*50)
                        print(students[chk])
                        
                        
                    elif s_input==3:
                        print(f'{search}의 {sub[s_input]} 점수는 {students[chk]['kor']}점 입니다.')
                        modi_num=int(input('변경할 점수를 입력하세요. >> '))
                        students[chk]['math']=modi_num
                        students[chk]['total']=students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                        students[chk]['avg']='{:.2f}'.format(students[chk]['total']/3)
                        print(f'{students[chk]['name']}의 점수가 변경되었습니다.')
                        print('-'*50)
                        print(students[chk])    
    
    elif choice==6:
        while True:
            print(' [학생 성적 삭제 ]')
            print('-'*50)
            delname=input('성적을 삭제할 학생의 이름을 입력하세요.(0.취소) >> ')
            chk=0
            if delname=='0':
                print('학생 성적 삭제를 취소합니다.')
                break
            
            for s_dic in students:
                if s_dic['name']==delname:
                    break
                chk+=1    
                
            print("찾고자 하는 학생의 위치 :",chk)

            if chk>=len(students):
                print('학생이 존재하지 않습니다.')
                
            else:
                print(f'{delname}학생을 찾았습니다.')
                print('-'*50)
                ch=input(f'{delname}학생을 삭제하시겠습니까?(0.취소, 1.실행) ')
            
                if ch !='1':
                    print('삭제를 취소합니다.')
                    break
            
                else:
                    print(f'{delname}학생을 삭제합니다.')
                    del students[chk]
                    print(f'{delname}학생을 삭제했습니다.')
                    print(students)

    elif choice==5:
        print('[ 등수 처리 ]')
        rank=int(input('등수 처리를 실행하시겠습니까? (0.취소, 1. 실행)'))
        if rank==0:
            print('등수 처리를 취소합니다.')
            break
        
        elif rank==1:
            for i, s_dic in enumerate(students):
                ranknum=1
                for i_dic in students:
                    if s_dic['total']<i_dic['total']:
                        ranknum+=1           
                s_dic['rank']=ranknum
                print(f'{s_dic['name']}:{s_dic['rank']}등')
            print('등수 처리를 완료했습니다.')
            
        
    elif choice==0:
        print('학생성적입력프로그램을 종료합니다.')
        break
                        
            
            
                            
                

    
               
        