import operator

fruits = [
    "apple","banana","kiwi","pear","peach",
    "apple","apple","kiwi","kiwi","peach", "peach",
    "apple","pear","apple","apple","pear","pear","pear",
     "peach", "banana","banana"    ]

counter={}
#dict에 방 없으면 방 만들어.
for n in fruits:
    if n not in counter:
        counter[n]=0
    counter[n]+=1
    
print(counter)
print(counter.items()) #튜플형태의 리스트
#items의 0번째 값을 가지고 순차정렬
print(sorted(counter.items(),key=operator.itemgetter(0))) 
print(sorted(counter.items(),key=operator.itemgetter(1))) 




# numbers = [1,2,3,4,5,5,6,7,4,3,2,12,67,8,9]

# counter={}

# for n in numbers:
#     if n not in counter:
#         counter[n]=0
#     counter[n]+=1
# print(counter)