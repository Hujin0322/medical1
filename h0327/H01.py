while True:
    print('[ 로그인 ]')
    print('-'*20)
    id=input('아이디: ')
    pw=input('패스워드: ')
    print('-'*20)
    
    #파일에서 아이디, 패스워드 확인
    chk=0
    with open ("member.csv","r",encoding="utf-8") as f:   
        while True:
            text=f.readline()
            if text=='': break
            mem=text.split(',')
        #아이디, 패스워드 비교    
            if id==mem[1] and pw==mem[2]:
                chk=1
                break            
    
    #id,pw X --> chk==0, id,pw O --> chk==1
    if chk==1:
        print('로그인이 되었습니다.')
        break
    else:
        print('id or pw가 일치하지 않습니다.\n다시 입력하세요.')
        
while True:
    print("[ 학생성적프로그램 ]")
    print('-'*30) 
    print('1. 학생성적입력')
    print('0. 종료')
    choice=int(input('원하는 번호를 입력하세요. >> '))
    if choice==1:
        print('학생성적입력을 진행합니다.')
    elif choice==0:
        print('프로그램을 종료합니다.')
        break       