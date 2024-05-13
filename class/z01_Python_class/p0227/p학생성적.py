student=[]
for i in range(3):
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch=input('원하는 번호를 입력하세요. >> ')
    if ch=='1':
        print('학생성적입력')
        name=input('이름을 입력하세요. >> ')
        kor=int(input('국어 점수를 입력하세요. >> '))
        eng=int(input('영어 점수를 입력하세요. >> '))
        math=int(input('수학 점수를 입력하세요. >> '))
        stu=[1, name, kor, eng, math,(kor+eng+math),((kor+eng+math)/3)]
        student.append(stu)
        print(student)       
    elif ch=='4':
        print('학생성적전체출력')
        print('번호\t이름\t국어\t영어\t수학\t총합\t평균\t등수')
        for stu in range(len(student)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[i][0],student[i][1],student[i][2],student[i][3],student[i][4],student[i][5],student[i][6],student[i][7]))
            
    elif ch=='0':
        print('프로그램을 종료합니다. ')
    else:
        print('잘못 입력하셨습니다.')
    