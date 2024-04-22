import operator 
#클래스 정렬
'''
a=[5,7,4,8,1,9,3,2]
a.sort() #순차 정렬
print(a)
print('-'*50)
b=[5,7,4,8,1,9,3,2]
b.sort(reverse=True ) #역순 정렬
print(b)

#3개의 숫자를 입력받아 순서대로 출력하시오.
num=[0,0,0]
for i in range(3):
    num[i]=int(input(f'{i+1}번째 숫자를 입력하세요. >> ')) #f --> format 형태

num.sort()
print(num)

#제일 큰 수 출력 (*변수 --> 전개연산자)
print('최대값:',max(*num))
print('최소값:',min(*num))
'''
#딕셔너리 정렬
t_dic={}
t_list=[]
t_dic={'peach':'복숭아','orange':'오렌지','apple':'사과',
       'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

t_list= sorted(t_dic.items(),key=operator.itemgetter(0),reverse=True) #--> 0번방 기준 역순 정렬
print(t_list)
# print(sorted(t_dic.items(),key=operator.itemgetter(1))) --> 1번방 기준 정렬

print(t_dic.keys()) #--> key값
print(t_dic.values()) #--> value값
print(t_dic.items()) #--> 튜플


