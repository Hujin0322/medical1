import os

# 1). 파일 생성
f= open ('students.txt','w',encoding='utf-8')
f.write("1, '홍길동', 100, 90, 99, 289, 96.33, 2\n")
f.write("2, '유관순', 99, 99, 100, 298, 99.33, 3")
f.close() #파일 닫기

# #2). 파일 생성 with 사용 시 f.close() 사용하지 않아도 됨.
# with open('students.txt','w') as f:
#     f.write("1, '홍길동', 100, 90, 99, 289, 96.33, 2")

# 파일읽기
t_list=[]
out_f=open('students.txt','r',encoding='utf-8')
while True:
    txt=out_f.readline() #1줄씩 읽어오기
    # print(type(txt))
    if txt=='':
        break
    print(txt,end='')
    t_list.append(txt)
print()
print(t_list)

out_f.close()

#파일 삭제
os.remove('students.txt')

#폴더가 존재하는지 확인
# if os.path.exists('hello'):
#     os.mkdir('hello')
# else:
#     os.rmdir('hello')
# # os.rmdir('hello')