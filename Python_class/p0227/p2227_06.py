#입력: 이름,아이디,비밀번호 (input)
#5명을 입력받아서 member 리스트 만들기
member=[] # [[홍길동,aaa,1111],[유관순,bbb,2222]]
'''
#member list를
이름  아이디  비밀번호
홍길동 aaaa   1111
이순신 bbbb   2222

for m in range(5):
    print('{}\t{}\t{}'.format(n1,n2,n3))
'''
#입력 5명 받기=반복(for문)/

for i in range(2):
    n1=input('이름을 적어주세요. >> ')
    n2=input('아이디를 적어주세요. >> ')
    n3=input('비밀번호를 적어주세요. >> ')
    m=[n1,n2,n3]
    member.append (m)

print(member)
    
print('이름\t아이디\t비밀번호')
for i in range(2):
    print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))
    
