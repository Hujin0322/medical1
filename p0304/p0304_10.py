a=10
b=a #변수 복사
b=100
print(a) #10
print(b) #100
print('-'*40)

a_list=[1,2,3] #->주소값 생성됨
b_list=a_list #리스트 복사 --> 같은 주소 공유 (얕은 복사)
b_list[0]=200
print(a_list[0]) #200
print(b_list[0]) #200

print(a_list)
