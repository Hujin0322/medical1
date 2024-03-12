#딕셔너리
students={'stuNo':1,'stuName':'홍길동','kor':100}

students['eng']=100 #딕셔너리 추가
students['kor']=50 #딕셔너리 수정
del students['stuName'] #딕셔너리 삭제
print(students)

#타입 변환: list, dict, int, float, str
print(list(students.keys())) #리스트로 형 변환 출력
print(students.values())
print(students.items())

#토플: 수정, 삭제 불가능



list=[1,2,3]

list.append(4)
print(list)
del list[0]
print(list)
list[0]=100
print(list)