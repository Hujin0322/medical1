ss='파이썬 공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다.'
#존재하는 문자가 몇 번 나왔는지 확인
print(ss.count('공부'))
print(ss.count('자바')) #없을 땐 0 

print(ss.find('공부')) #존재하는 문자열의 위치값 출력
print(ss.find('자바')) #없을 땐 -1
print(ss.find('공부',7)) #문자열 7번째자리부터 검색시작해서 위치값 출력
print(ss.rfind('공부'))
print('-'*50)
print(ss.index('공부'))
print(ss.rindex('공부'))


print(ss.startswith('파이썬')) #시작하는 문자열 True/False
print(ss.startswith('자바')) 

print(ss.endswith('파이썬')) #끝나는 문자열 True/False
print(ss.endswith('자바'))
