#국어,영어,수학을 입력받아
#합계를 출력하시오.
students=[]
for i in range(0,2):
    student=[] #초기화 ([] 분리 위함)
    student.append(input('이름 입력. >> '))
    student.append(int(input('국어 점수 입력. >> ')))
    student.append(int(input('영어 점수 입력. >> ')))
    student.append(int(input('수학 점수 입력. >> ')))
    sum=student[1]+student[2]+student[3]
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))
    students.append(student)
#합계
print(student)
#전체학생출력
print('[학생성적 출력]')
print('-'*40)
print('이름\t국어\t영어\t수학\t합계\t평균\n')
print('-'*40)
#전체출력
for stu in students:
    for s in stu:
        print(s,end='\t')
    print()
print('-'*50)


#2차원 리스트는 for문을 2번 사용함.
#총학생의 총국어,총영어,총수학점수, 총합계, 총평균
kors=0
engs=0
maths=0
totals=0
avgs =0
for i, stu in enumerate(students):
    kors=kors+stu[1]
    engs=engs+stu[2]
    maths=maths+stu[3]
    totals=totals+stu[4]
    
avgs=totals/len(students)
print('\t')
print(kors,engs,maths,totals,avgs,sep='\t')
    
'''
for stu in students:
    for s in stu:
        print(s,end='\t')
    print()
print('-'*50)
      '''  
