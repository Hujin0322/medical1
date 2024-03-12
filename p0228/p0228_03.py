member=[]

#입력: 이름, 점수 (input) ['홍길동',90]
#총 3명의 정보를 member리스트에 넣으세요.
'''
print(member) #[['홍길동',90],['유관순',90],['이순신',90]]

for i in range(3):
    name=input('이름을 입력하세요. >> ')
    score=int(input('점수를 입력하세요. >> '))
    member.append([name, score]) 
print(member)
'''

member= [['홍길동',55],['유관순',80],['이순신',90]]
#60점 이상이면 홍길동님 합격입니다. 유관순님 합격입니다.
#member 변수 사용, for if
for i in range(3): #for i in range(len(member)):
    if member[i][1]>=60:
        print('{}님 {}점으로 합격입니다.'.format(member[i][0],member[i][1]))  
    else:
        print('{}님 {}점으로 불합격입니다.'.format(member[i][0],member[i][1]))  

#name=member[i][0] score=member[i][1] --> 지정 후 이용도 가능
    