list=[1,2,3]

#alist=list 같은 공간 이용.

#깊은 복사 방법
alist=[*list] #1번
alist=list[:] #2번


list[0]=100

a=100
b=a
a=10

print(b)
