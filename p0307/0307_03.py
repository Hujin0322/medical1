students={'stuNo':1, 'stuName':'홍길동','tel':'010-0000-0000',
          'gender':'male','id':'aaa','pw':1111}

#키 값 없는 데이터를 가져오면 에러
if 'studentNo' in students:
    print('키가 있습니다.')
    students['studentNo']=students['studentNo']+1
    print(students['studentNo'])
else:
    print('키 존재X')
