import datetime
#퀴즈
#1). 데이터 입력받기
#2). p_(현재날짜).txt --> ex)p_0320.txt 형식으로 파일 생성
#3). 입력받은 데이터 저장시키기

now=datetime.datetime.now()
print(now.strftime('%m%d')) #--> 0320 형식 

a=input('글자를 입력하세요.')
fileName='p_'+now.strftime('%m%d')+'.txt'

f=open(fileName,'w',encoding='utf-8')
f.write(a)
