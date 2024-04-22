#학생 이름, 국어, 영어, 수학 점수 입력 받아서 아래와 같이 출력
#만약에 평균이 80점 이상이면 [합격입니다.]를 출력하시오.

stu1_name=str(input('이름을 입력하시오. '))
kor1=int(input('국어 점수를 입력하시오. '))
eng1=int(input('영어 점수를 입력하시오. '))
math1=int(input('수학 점수를 입력하시오. '))
avg1=(kor1+eng1+math1)/3
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t {}\t {}\t {}\t {}\t{:.1f}\t {}'.format(1,stu1_name,kor1,eng1,math1,kor1+eng1+math1,avg1,1))

if avg1>=80:
    print('평균은 {}점 입니다.'.format(avg1))
    print('축하드립니다.\n합격입니다.')
else:
    print('불합격입니다.')