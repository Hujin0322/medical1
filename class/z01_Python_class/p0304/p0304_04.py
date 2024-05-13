students=[['홍길동',100,100,99,299,99.97],['유관순',100,100,99,299,99.97],['이순신',100,100,99,299,99.97]]
kors=0
#students 2차원배열
#stu 1차원 배열
for i, stu in enumerate(students):
    kors+=stu[1]

print(kors)
    