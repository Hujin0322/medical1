#관계 연산자 --> 크고 작음 비교
#참=True/ 거짓=false --> 주로 조건문, 반복문에서 사용
#수식1==수식2: 수식 1과 2가 같은지 평가
print(3==6) #--> 3이 6과 같은가요?
#수식1!=수식2: 수식1과 2가 같지 않음(!=부정)
print(3!=6)
#수식1>=수식2: 수식1이 수식2값보다 크거나 같은가를 평가

num=95
print(num > 90) 
print(num <= 90)
print(num == 90) 
print(num != 90)

print(90<=num <100)

#논리 연산자
# and(그리고), or(또는), not(부정)
# and: 둘 중 하나라도 참이면 참
# or: 둘 중 하나라도 참이면 참
#not: 참이면 거짓,거짓이면 참 

kor=90
avg=80
print(kor >80)
print(avg > 90)
print(kor>80 and avg>90) #--> 거짓
print(kor>80 or avg>90) #--> 참
