import random

def idpw():
    eng='abedefghijklmnopqrstuvwxyz'
    pw='1234567890'
    member=[['aaa','1111']]
    for i in range(10):
        tmp_id=random.sample(eng,3) #아이디 생성
        tmp_pw=random.sample(pw,4) #비밀번호 생성
        member.append([tmp_id[0]+tmp_id[1]+tmp_id[2],
                    tmp_pw[0]+tmp_pw[1]+tmp_pw[2]+tmp_pw[3]])
    return(member)

#랜덤함수를 사용하여 
#3자리 아이디를 10개 생성 e_list에 추가
#4자리 패스워드 10개 생성 p_list에 추가
