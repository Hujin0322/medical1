#학생성적 입력

#변수 사용
stu_name=input('이름을 입력하세요.')
kor=int(input('국어 점수를 입력하세요.'))
eng=int(input('영어 점수를 입력하세요.'))
math=int(input('수학 점수를 입력하세요.'))
total=kor+eng+math
avg=(kor+eng+math)/3

#입력 받아서 총점과 평균을 계산하고 출력
print('이름\t국어\t영어\t수학\t합계\t평균')
print('{}\t{}\t{}\t{}\t{}\t{:.1f}'.format(stu_name,kor,eng,math,total,avg))

stu =[1,'홍길동',100,100,100,300,100.0,]
stu1=[2, stu_name, kor, eng, math, total,avg]
 
print(stu)
print(stu1)
