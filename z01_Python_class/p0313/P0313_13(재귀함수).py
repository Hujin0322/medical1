def count(num):
    if num>=1:
        print(num,end=' ')
        count(num-1) #자신의 함수를 다시 호출: 재귀함수
    else:
        return 
    
count(3)

# n=int(input('숫자 입력. >> '))
# for i in range(n,0,-1):
#     print(i,end=' ')    
    