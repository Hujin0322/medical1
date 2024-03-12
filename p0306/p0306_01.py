import operator

fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter={} #딕셔너리 생성

# 딕셔너리 추가
counter['복숭아']=5
counter['바나나']=4 #추가
counter['바나나']=1 #수정
# print(counter['딸기']) #딕셔너리에 없는 키값 출력 시 에러
print(counter['바나나'])    

if '딸기' not in counter: #키 값의 존재여부 확인
    counter['딸기']=0 #키 생성

else:
    print(counter['딸기'])  #키의 value값 출력  

del counter['복숭아'] #삭제

print(counter)

print(counter.keys()) #class type
print(type(counter.keys())) #type 확인
print(counter.values()) #values가 list타입으로
print(counter.items())

# a_list =[3,5,7,4,1,24,6,78]
# print(sorted(a_list)) # =print(a_list.sort)

#딕셔너리 정렬 --> operator 이용, key순으로 정렬
print(sorted(counter.items(),key=operator.itemgetter(0)))
