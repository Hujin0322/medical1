fruits=[['딸기','사과','자몽','포도','수박','자몽']]

#자몽 삭제 원함
#1) 리스트명.remove('요소명')
#2) del(리스트명[번호])
del(fruits[5]) # 정확한 위치의 요소 삭제함.
print(fruits)

for index, elem in enumerate(fruits):
    print('{}는 {}번째에 있습니다.'.format(elem,index))