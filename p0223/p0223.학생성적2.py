print('-'*35)
print('[학생성적프로그램]')
print('-'*35)
print('1. 학생성적입력')
print('4. 학생성적전체출력')
print('0. 프로그램 종료')
print('-'*35)
choice=int(input('원하는 번호를 입력하세요 >> '))

stu1=[1,'홍길동',100,100,100,300,100,1]
stu2=[2,'유관순',90,90,90,270,90,2]

choice=(input('원하는 번호를 입력하세요. >> '))
if choice==1:
    stu_03=int(input('학생의 번호를 입력하세요. >> '))
    stu3_name=input('학생의 이름을 입력하세요. >> ')
    kor3=int(input('학생의 국어 점수를 입력하세요. >> '))
    eng3=int(input('학생의 영어 점수를 입력하세요. >> '))
    math3=int(input('학생의 수학 점수를 입력하세요. >> '))
    stu3=[stu_03,stu3_name,kor3,eng3,math3,(kor3+eng3+math3),((kor3+eng3+math3)/3)]
    print(stu3)
elif choice==4:
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]))
elif choice==0:
    print('프로그램을 종료합니다.')