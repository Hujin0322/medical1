# str.txt 파일의 내용을 모두 출력하시오.
f= open('str.txt','r',encoding='utf-8')
ff=open('str1.txt','a',encoding='utf-8')
while True:
    content=f.readline() #파일 내용 읽어오기
    if content.strip()=='': break #읽을 게 더 없으면 --> 공백이면 끝
    ff.write(content) #파일 내용 추가하기

f.close()
ff.close()

