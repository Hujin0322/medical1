#성적점수부분함수
def score_update(choice,s_title,stu): #매개변수 타입 확인
    print(f'[ {s_title[choice]} 성적 수정 ]')
    print(f'현재 {s_title[choice]}점수: {stu[choice+1]}')
    print('-'*30)
    stu[choice+1]=int(input('수정 점수를 입력하세요. >> '))
    print('수정된 점수:',stu[choice+1])
    stu[5]=stu[2]+stu[3]+stu[4]
    stu[6]=float('{:.2f}'.format(stu[5]/3))
    print(f'{s_title[choice]} 점수가 수정되었습니다.')


#학생성적수정함수    
def stu_update(choice,s_title,stu):
    print('[ 학생성적수정 ]')
    print('1.국어\t2.영어\t3.수학')
    choice=int(input('원하는 번호를 입력하세요. >> '))
    
    if choice==1:
        score_update(choice,s_title,stu)
        
    elif choice==2:
        score_update(choice,s_title,stu)
                    
    elif choice==3:
        score_update(choice,s_title,stu)