#1. 숫자 2개 입력 받아서 나누기 값, 몫값, 나머지값 출력
n1=int(input('처음 숫자를 입력하세요 >> '))
n2=int(input('두번째 숫자를 입력하세요 >> '))
나누기=n1/n2
몫=n1//n2
나머지=n1%n2
print('{:.2f}\n{}\n{}'. format(나누기,몫,나머지))

#2. 3개 수의 합을 구하시오.
s1,s2,s3=int(100), float(100.123),float(99.9)
result=int(s1)+float(s2)+float(s3)
print('합은 {}입니다.'.format(result))
