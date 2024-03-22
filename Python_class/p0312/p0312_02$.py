#1. 번호 생성
#2. 번호 섞기
#3. 번호 뽑기
#4. 번호 확인
import random

#화면출력함수
def screen():
    print('[ 로또 번호 맞추기 프로그램 ]')
    print('1. 번호 생성')
    print('2. 번호 섞기')
    print('3. 나의 로또 번호 입력')
    print('4. 번호 확인')
    print('-'*30)
    choice=int(input('원하는 번호를 입력하세요. >> '))
    return choice    

#번호생성함수
def num_generater(lotto):
    print('[ 번호 생성 ]')
    # lotto = [ i for i in range(1,45+1)] #지역변수로 변환, 새롭게 재정의
    for i in range(45):
        lotto[i] = i+1
    print(lotto)

def num_shuffle(lotto):
    print('[ 번호 섞기 ]')
    random.shuffle(lotto)
    print(lotto)

def num_input(my_lotto):
    print('[ 나의 로또 번호 입력 ]')
    for i in range(6):
        my_num = int(input(f'{i+1}번째 로또 번호를 입력하세요. >> '))
        my_lotto[i]=my_num
        
    print('내가 입력한 번호: ',my_lotto)

def num_check(lucky_lotto,my_lotto,win_num,win_amount):
    # win_num=[] #지역변수로 인식, 주소값 다시 세팅함.
    for i in range(6):
        lucky_lotto[i]=lotto[i]            
    print('[ 번호 확인 ]')
    print('로또 번호: ',lucky_lotto)
    print('내가 입력한 번호: ',my_lotto)
    
    #몇 개 맞췄는지 확인소스
    for i in my_lotto:
        if i in lucky_lotto:
          win_num.append(i) #
    print('당첨된 번호: ',win_num)
    
    #당첨 금액 출력
    print('당첨 금액: {}원'.format(win_amount[len(win_num)]))
    print('-'*40)
    print()
            

#----------------------------------------------------------------------
lotto = [0]*45 #전체 45개 숫자
lucky_lotto=[0]*6 #당첨번호 6개 숫자
my_lotto=[0]*6 #내가 입력한 6개 숫자
win_num=[] #내 번호 중 당첨된 번호
win_amount=[0,0,1000,10000,100000,1000000,10000000] #당첨금액

while True:
    # 화면출력함수 호출
    choice=screen()
    if choice==1:
        #번호생성함수 호출
        num_generater(lotto)
        
    elif choice==2:
        #번호섞기 함수 호출
        num_shuffle(lotto) 
        
    elif choice==3:
        num_input(my_lotto)
        
    elif choice==4:
        win_num=[]
        num_check(lucky_lotto,my_lotto,win_num,win_amount)
        