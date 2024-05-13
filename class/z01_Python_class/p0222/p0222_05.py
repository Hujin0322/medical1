# 국어, 영어, 수학 점수를 입력받아 평균 출력
# 출력:평균은: 95점입니다.
#변수: kor, eng, math
kor=100
eng=90
math=80
avg=(kor+eng+math)/3

kor=input('국어 점수 >>')
eng=input('영어 점수 >>')
math=input('국어 점수 >>')
kor,eng,math=int(kor), int(eng), int(math)
avg=(kor+eng+math)/3
print('평균은: {}점 입니다.'.format(avg))