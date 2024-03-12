import operator

fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter={} #딕셔너리 생성

for f in fruit:
    if f not in counter: #딕셔너리에 키 존재여부 확인
        counter[f]=0 #딕셔너리 키가 없을 시 키 추가
    counter[f]+=1 #키의 value값 1증가
    
print(counter)

#딕셔너리 정렬 --> operator 이용, key순으로 정렬
print(sorted(counter.items(),key=operator.itemgetter(0))) #순차 정렬
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True)) #역순 정렬

#딕셔너리 정렬 --> operator 이용, value순으로 정렬
print(sorted(counter.items(),key=operator.itemgetter(1))) #순차 정렬
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True)) #역순 정렬


