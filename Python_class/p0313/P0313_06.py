import os

print('현재 운영체제: ',os.name)
print('현재 폴더: ',os.getcwd())
print('현재 폴더 내 파일들 표시: ',os.listdir())

#폴더 생성
# os.mkdir('hello')

#폴더 삭제
# os.rmdir('hello')

#파일 생성
# with open ('students.txt','w') as f:
#     f.write("1, '홍길동', 100, 90, 99, 289, 96.33, 2")
    
str1="1, '홍길동', 100, 90, 99, 289, 96.33, 2"
s_list=str1.split(',')
for i in s_list:
    print(i)