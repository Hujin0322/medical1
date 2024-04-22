students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]

# 학생성적입력 구현
# cnt=5
# while True:
#     name=input('학생의 이름을 입력하세요.(0.취소) >> ')
#     if name=='0':
#         break
#     student={}
#     cnt+=1
#     kor=int(input('국어 점수를 입력하세요. >> '))
#     eng=int(input('영어 점수를 입력하세요. >> '))
#     math=int(input('수학 점수를 입력하세요. >> '))
#     student['stuNo']=('S{:03d}'.format(cnt))
#     student['name']=name
#     student['eng']=eng
#     student['math']=math
#     total=kor+eng+math
#     avg=total/3
#     student['total']=total
#     student['avg']=('{:.2f}'.format(avg))
#     students.append(student)
    
#     print(student)


#학생 성적 전체 출력
count=0
print('번호\t학번\t이름\t국어\t영어\t수학\t총합\t평균')
for s_dic in students:
    for s_key in s_dic:
        print(f'{s_dic['stuNo']}\t{s_dic['name']}')
        