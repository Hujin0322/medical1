#산술 연산자
# +,-,*,/
#//=몫, %=나머지, **=제곱
result=7//5
print(result)

c=10
d=20
print(c**d)

# 괄호 사용 추천함.
r2=2-(2/2)

#다른 자료형으로 연산
str1='문자열'
n1=10

print(str1*n1)

#print(str1+n1) --> error

#문자열이 정수나 실수일 경우 int(), float()를 사용해서 변환
s1='100'
s2='10.123'
print(int(s1)+1)
print(float(s2)+1)

#n=int('안녕하세요') --> error

#숫자를 문자로 바꾸고 싶으면 str() 사용
s1='100'
s2='10.123'
print(int(s1)+1)
print(float(s2)+1)

p=12341234
print('010'+str(p))

#숫자 2개 입력받아서 나누기값, 몫, 나머지 값 구하기
#ex) n1=4, n2=2
n1=4
n2=2
n1=input('숫자를 입력하세요 >>')
n2=input('숫자를 입력하세요 >>')
n1,n2=int(n1),int(n2)
print('{}/{}={}'.format(n1,n2,n1/n2))
print('{}//{}={}'.format(n1,n2,n1//n2))
print('{}%{}={}'.format(n1,n2,n1%n2))
print('나누기값:{:.1f}\n몫:{}\n나머지:{}'.format(n1/n2,n1//n2,n1%n2))

