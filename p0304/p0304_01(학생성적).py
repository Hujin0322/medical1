students=[] #학생성적저장

students=[[1, '홍길동', 100, 90, 99, 289, 96.33], 
          [2, '유관순', 99, 99, 100, 298, 99.33], 
          [3, '이순신', 97, 98, 97, 292, 97.33],
          [4, '김구', 96, 96, 95, 287, 95.67], 
          [5, '김유신', 8, 55, 70, 133, 44.33]] #학생성적저장

cnt=len(students) #학번

while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생성적검색')
    print('4. 학생성적수정')
    print('5. 등수처리')
    print('6. 학생성적삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice=input('원하는 번호를 입력하세요. >> ')
    
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue #반복문 멈춤 후 처음부터 다시 실행
    choice=int(choice)
#-------------------------------------------------------------
    #1. 학생성적입력 프로그램
    if choice==1:
        #무한 반복
        while True:  
            print('학생 성적을 입력합니다.')
            print('-'*10)
            student=[]
            name=(input('이름 입력. (-1. 취소) >> '))
            if name=='-1':
                break
            cnt+=1 #학번, 중간에 빠져나갈 경우 생각 --> break 다음 위치
            student.append(cnt) 
            student.append(name)
            student.append(int(input('국어 점수 입력. >> ')))
            student.append(int(input('영어 점수 입력. >> ')))
            student.append(int(input('수학 점수 입력. >> ')))
            sum=student[2]+student[3]+student[4]
            #합계 저장
            student.append(sum)
            #평균 저장
            student.append('{:.2f}'.format(sum/3))
            student.append(1)
            students.append(student)
            #출력
            print(students)
#---------------------------------------------------------------------------------            
    #2. 학생성적출력 프로그램
    elif choice==2:
        print('[학생 성적 출력]')
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
        print('-'*50)
        #전체출력
        for stu in students:
            for s in stu:
             print(s,end='\t')
            print()
        print('-'*50)
#-----------------------------------------------------------------------------------        
    #3. 학생성적검색
    elif choice==3:
        while True:
    #멈춤
            search=input('검색하고 싶은 학생의 이름을 입력하시오. >> (0.취소) ')
            chk=0 #찾는 정보확인
            count=0
            if search=='0':
                break
            for stu in students: #홍길동, 유관순, 이순신
                if search in stu:
                    chk=1 #정보를 찾았을 때 정보를 1로 변경
                    break
                count+=1
                
            if (chk==1):
                #전체학생 정보출력
                print('[학생 성적 출력]')
                print('{}의 학생정보를 찾았습니다.'.format(search))
                print('-'*50)
                print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                print('-'*50)
                for i in students[count]:
                    print(i,end='\t')
                print()
                
            else:
                print('찾는 학생 정보가 없습니다.')          
#-------------------------------------------------------------------------------------- 
    elif choice==4:
        while True:
            search=input('찾는 학생의 이름을 입력하세요. (0.취소) >> ')
            if search==0:
                break
            chk=0
            count=0
            for stu in students:
                if search in stu:
                    chk=1
                    break
                count+=1 #찾는 학생의 위치값
                
            if chk==0:
                print('찾는 학생의 정보가 없습니다.')
            else:
                print('입력한 학생 {}을(를) 찾았습니다.'.format(search))
                print('[변경 과목 선택]')
                num=int(input('1.국어 2.영어 3.수학 0.취소'))
                if num==1:
                #성적수정 프로그램 구현 
                    print('국어를 선택하셨습니다.')
                    print('현재 국어 점수:{}'.format(students[count][2]))
                    num=int(input('변경할 점수를 입력하세요. >> '))
                    students[count][2]=num
                    print('국어 점수가 변경되었습니다.')
                    students[count][5]=students[count][2]+students[count][3]+students[count][4]
                    students[count][6]=float('{:.2f}'.format(students[count][5]/3))
                    #출력
                    print(students)
                    
                    
                elif num==2:
                    print('영어를 선택하셨습니다.')
                    #성적수정 프로그램 구현
                    print('현재 영어 점수:{}'.format(students[count][3]))
                    num=int(input('변경할 점수를 입력하세요. >> '))
                    students[count][3]=num
                    print('영어 점수가 변경되었습니다.')
                    students[count][5]=students[count][3]+students[count][2]+students[count][4]
                    students[count][6]=float('{:.2f}'.format(students[count][5]/3))
                    #출력
                    print(students)
                    
                    
                elif num==3:
                    print('수학을 선택하셨습니다.')
                    #성적수정 프로그램 구현
                    print('현재 수학 점수:{}'.format(students[count][4]))
                    num=int(input('변경할 점수를 입력하세요. >> '))
                    print('수학 점수가 변경되었습니다.')
                    students[count][4]=num
                    students[count][5]=students[count][3]+students[count][2]+students[count][4]
                    students[count][6]=float('{:.2f}'.format(students[count][5]/3))
                    #출력
                    print(students)

                else:
                    print('성적 수정 취소를 선택하셨습니다.')
#--------------------------------------------------------------------------------------------     
   
    # elif choice==5:
    #     #등수처리프로그램 (합계 비교)
    #     while True:
    #         choice=input('등수처리를 실행하시겠습니까? (1.실행 0.취소)')
    #         if choice =='0':
    #             print('등수처리를 취소하셨습니다.')
    #             break
    #         else:
    #             #등수처리 진행
    #             for i_stu in (students):
    #                 no=1 #초기화 /등수처리 실행 시 리스트 7번에 '1'추가
    #                 #students[i][7]=no
    #                 for j_stu in (students):
    #                     #각각의 총합 비교
    #                     if i_stu[5] < j_stu[5]:
    #                         no+=1 #비교 대상 총합이 더 크면 1증가 !!!!!!!확인 필요!!!!!!!
    #                 i_stu[7]=no #등수위치에 no 저장
    #         print('등수처리가 완료되었습니다.')
    #         print('-'*40)
    #         print('[ 등수확인 ]')
    #         print(students)

#--------------------------------------------------------------------------------------------  
#학생 삭제    
    elif choice==6:
        while True:
            search=input('삭제하고자 하는 학생을 입력하세요. >> ')
            #이름찾기
            cnt=0 #찾은 학생의 위치
            for stu in students:
                if stu[1]==search:
                    break
                cnt+=1
                
            if cnt==len(students):
                print('{} 학생이 없습니다.'.format(search))
                
            else:
                print('{} 학생을 찾았습니다.'.format(search))
                d=input('삭제하시겠습니까? 1.삭제 0.취소. >> ')
                if d=="1":
                    print('{} 학생의 데이터가 삭제되었습니다.'.format(search))
                    del students[cnt] 
                else:
                    print('삭제가 취소되었습니다.')
                                       
            print(students)    
#--------------------------------------------------------------------------------------------             
    elif choice==0:
        print('프로그램을 종료합니다.')
        break #반복문 종료