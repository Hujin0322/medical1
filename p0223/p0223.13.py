#빈 리스트 생성
cont=[]

c1=input('1. 나라를 입력해주세요. >> ')
c2=input('2. 나라를 입력해주세요. >> ')
c3=input('3. 나라를 입력해주세요. >> ')
c4=input('4. 나라를 입력해주세요. >> ')

#1. []이용
cont=[c1,c2,c3,c4]

#2. append 이용
cont.append(c1)
cont.append(c2)
cont.append(c3)
cont.append(c4)
#print(cont)

#미국-영국-프랑스-이탈리아
print('{}-{}-{}-{}'.format(cont[0],cont[1],cont[2],cont[3])) #=(c1,c2,c3,c4)

#과일 리스트
#내가 입력한 과일 3개 이상으로 리스트 채우기
a=input('1. 좋아하는 과일을 입력하세요. >> ')
b=input('2. 좋아하는 과일을 입력하세요. >> ')
c=input('3. 좋아하는 과일을 입력하세요. >> ')

#방법1
f=[]
f.append(a)
f.append(b)
f.append(c)

#방법2
f=[a,b,c]
print('{}-{}-{}'.format(a,b,c))
print('{}-{}-{}'.format(f[0],f[1],f[2]))

#내가 좋아하는 과일은 a,b,c입니다.
print('내가 좋아하는 과일은 "{},{},{}" 입니다.'.format(a,b,c))