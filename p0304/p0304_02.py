# 숫자 6개 입력받아 출력하시오.
'''
num=int(input('숫자를 입력하세요. >> ')) #str
num2=int(input('숫자를 입력하세요. >> ')) #str
print(num)
print(num2)
print(num+num2)
'''
nums=[]
for i in range(5):
    nums.append(int(input('숫자를 입력하세요. >> '))) #str
print(nums)

sum=0
for num in nums:
    sum+=num
print('합계:',sum)
    