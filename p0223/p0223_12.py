fruits=['사과','복숭아','딸기','포도',' 배']

#리스트에 요소 추가 --> append 함수 사용
fruits.append('한라봉')
print('한라봉' in fruits )

if '딸기' in fruits:
    print('딸기가 있습니다.')
else:
    print('딸기가 없습니다.')

temp=[]
print(temp)
temp.append(1)
print(temp)
temp.append(2)
print(temp)
temp.append('홍길동')
print(temp)

#과일 리스트에 '체리' 추가하기
fruits.append('체리')
print(fruits)

#요소 제거하기 --> remove
fruits.remove('사과')
print(fruits)

#변수
a=2
b=3
c=a+b
print('{}+{}={}'.format(a,b,c))

l1=[1,2,3,4,5] #리스트를 사용해서 2+3=5의 값을 출력하기
a1=l1[1]
b1=l1[2]
c1=l1[4]
print('{}+{}={}'.format(a1,b1,c1)) #2+3=5

#list l1의 숫자들 합 구하기
d=l1[0]+l1[1]+l1[2]+l1[3]+l1[4]
print(d)
