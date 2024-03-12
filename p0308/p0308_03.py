#1차원 배열 생성
# a_list=[]*52
# c_list=[0 for i in range(52)]
# b_list=[]
# for i in range(52):
#     b_list.append(0)

#2차원 배열 생성
aa=[[0]*1]*52 #얕은 복사 사용X
bb=[[0]*2 for i in range(52)]

cc=[]
for i in range(52):
    dd=[]
    for i in range(2):
        dd.append(0)
    cc.append(dd)
print(cc)