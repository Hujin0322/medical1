#파일 열기
f=open('mem.txt','r',encoding='utf-8')
#파일 닫기

#로그인
tmp=0
while True:
    if tmp ==1: break # 프로그램 종료
    print('\t\t[ 로그인 ]')
    print('-'*40)
    print('*먼저 로그인을 해주세요')
    c_id=input('ID를 입력하세요. >> ')
    c_pw=input('PASSWORD를 입력하세요. (0.종료) >> ')
    
    if c_pw=='0': break #0.종료
    
    #로그인 확인
    #mem.txt파일을 불러와서 아이디와 패스워드 비교
    #for문으로 비교
    success_flag=0
    #파일 읽기
    while True:
        txt=f.readline()
        if txt=='': break
        m=txt.split(',')
        m[0]=m[0].strip()
        m[1]=m[1].strip()
        if c_id==m[0] and c_pw==m[1]:
            success_flag=1
            break
    #파일닫기
    f.close()
    
    if success_flag==1: #로그인 성공
        print('로그인 되었습니다.')
        print()
        #학생성적프로그램 구현
        while True:                    
            print('-'*40)
            print('[ 학생성적 프로그램 ]')
            print('-'*40)
            print('1. 학생성적데이터 읽어오기')
            print('2. 학생성적입력')
            print('3. 학생성적출력')
            print('0. 프로그램 종료')
            print('-'*40)
            choice=int(input('원하는 번호를 입력하세요. >>'))
            if choice==1:
                print(' [ 학생성적데이터 읽어오기 ]')
                
            elif choice==2:
                pass
            
            elif choice==3:
                pass
                            
            elif choice==0:
                tmp=1 #프로그램 종료
                break
            
        
        
        
    
                
                
    
    
    
    
    
    
    else: #로그인 실패
        print('ID 또는 PASSWORD가 일치하지 않습니다.\n다시 로그인 해주세요.')
        print() 

#최종 종료
print('프로그램을 종료합니다.')
