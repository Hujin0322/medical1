#5. 등수처리

students=[[1, '홍길동', 100, 100, 99, 299, 99.67,1], 
          [2, '유관순', 99, 99, 100, 298, 99.33,1], 
          [3, '이순신', 90, 70, 50, 210, 70.0,1],
          [4, '김구', 96, 96, 95, 287, 95.67,1], 
          [5, '김유신', 97, 98, 97, 292, 97.33,1],
          [6, '강감찬', 100, 100, 100, 300, 100,1]]


#등수처리프로그램 (합계 비교)
while True:
    choice=input('등수처리를 실행하시겠습니까? (1.실행 0.취소)')
    if choice =='0':
        print('등수처리를 취소하셨습니다.')
        break
    else:
        #등수처리 진행
        for i_stu in (students):
            no=1 #초기화
            for j_stu in (students):
                #각각의 총합 비교
                if i_stu[5] < j_stu[5]:
                    no+=1 #비교 대상 총합이 더 크면 1증가
            i_stu[7]=no #등수위치에 no 저장
    print('등수처리가 완료되었습니다.')
    print('-'*40)
    print('[ 등수확인 ]')
    print(students)               
            