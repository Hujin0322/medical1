#기존 변수를 이용한 출력
'''
stu_no1=1
stu_name1='홍길동'
kor1=100
eng1=100
math1=100
total1=kor1+eng1+math1
avg1=total1/3
rank1=0
'''

#리스트를 사용한 출력
stu_no1=input('학생의 번호를 입력해주세요. >> ')
stu_name1=input('학생의 이름을 입력해주세요. >> ')
kor1=int(input('학생의 국어 점수를 입력해주세요. >> '))
eng1=int(input('학생의 영어 점수를 입력해주세요. >> '))
math1=int(input('학생의 수학 점수를 입력해주세요. >> '))
total1=kor1+eng1+math1
avg1=(kor1+eng1+math1)/3
rank1=int(input('학생의 등수를 입력해주세요. >> '))
stu1=[stu_no1,stu_name1,kor1,eng1,math1,total1,avg1]

print('[학생 성적 출력]')
print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu[0],stu[1],stu[2],stu[3])) 

stu1=[1,홍길동,100,100,100,300,100,1]
stu2=[2,유관순,90,90,90,270,90,2]