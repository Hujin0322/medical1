#해보세요
#수식을 입력하면 숫자 입력
n1=int(input('첫번째 숫자를 입력하세요.'))
n2=int(input('두번째 숫자를 입력하세요.'))    
cal=input('수식을 입력하세요. (+,-,*,/) >> ')
if cal=='+':
    print((n1+n2))
elif cal=='-':
    print((n1-n2))
elif cal=='*':
    print((n1*n2))
elif cal=='/':
    print((n1/n2))
else:
    print('명시된 수식을 입력하세요.')
