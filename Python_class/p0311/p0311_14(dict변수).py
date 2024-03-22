#변수 1개는 return필요/ 리스트 변수는 returnX
def stu_update(student): #지역변수 --> 주소값이 저장됨.
    student['stuNo']=2
    student['name']='유관순'
    student['total']=student['kor']+student['eng']+student['math'] #지역변수
    student['avg']=student['total']/3
    
#프로그램 구현
student={'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 0, 'avg': 0}

#함수호출
stu_update(student) #전역변수

print('학생 1번:',student)
