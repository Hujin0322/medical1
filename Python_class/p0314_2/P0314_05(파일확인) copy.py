import os
list=[]
while True:
    print('[ 윈도우 탐색기 ]')
    print('-'*40)
    print('1. 폴더 내 파일 확인')
    print('2. 파일 불러오기')
    print('3. 파일 저장')
    print('-'*40)
    choice=int(input('원하는 번호를 입력하세요. >> '))
    
    if choice==1:
        print('[ 폴더 내 파일 확인 ]')
        for f_list in os.listdir():
            if f_list.endswith('.txt'):
                print(f_list)
        
    elif choice==2:
        for f_list in os.listdir():
            if f_list.endswith('.txt'):
                print(f_list)
        print('-'*40)        
        
        f_name=input('원하는 파일을 입력하세요 >> ')
        f=open(f_name,'r',encoding='utf-8')
        while True:
            content=f.readline()
            if content=='': break
            print(content,end='\n')
    
    elif choice==3:
        print('[ 파일 저장 ]')
        num=
            
            