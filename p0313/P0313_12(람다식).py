# #람다식함수 = 무명함수
# def sum(num1,num2): -->변수에 넣기 불가
#     return num1+num2 

# print(sum(10,20))

# def sum(num1,num2):
#     return num1+num2 

a = lambda num1,num2:num1+num2 #--> 변수에 넣기 가능:리턴의 값이 1개라 가능
print(a(10,20))