#예외 - 프로그램 실행 시 *알 수 없는 오류*로 인한 프로그램 종료 방지 위함.
#프로그램 에러 - 프로그램 실행하며 수정해야 함.

#try: 프로그램에서 오류 발생 예상 소스
#except: 예외 발생O --> 처리 구문 소스
#except Exception as e: 예외 발생 시 발생한 예외 확인 가능.
#예외 종류별로 except 처리 가능
#종류: ValuseError, IndexError, ZeroDivisionError...등 
#else: 예외발생X --> 처리 소스
#finally: 무조건 실행 소스
#raise: 예외 강제 발생 raise '메모내용'
 

print('1. 학생성적입력')
print('2. 학생성적출력')
print('3. 학생성적수정')
num=int(input('숫자를 입력하세요. >> '))
if num==1:
    print('학생성적입력 완성')
    
elif num==2:
    # print('김과장이 해야 할 부분')
    raise'김과장에게 소스 받아야 함' #알림 형태로 사용
elif num==3:
    print('이대리가 해야 할 부분')
