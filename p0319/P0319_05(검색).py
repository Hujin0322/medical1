#검색어가 포함되어 있는 모두 검색하는 방법
name=['홍길동','유관순','이순신','김구','강감찬','홍길순','김땡땡']


while True:
    search=input('이름을 입력하세요. >> ')
    search_list=[] #찾은 사람의 위치 저장  
    cnt=0
    
    #검색어로 검색
    for n in name:
        if n.find(search) != -1: #검색어 포함 여부 확인
            # print('찾는 학생이 존재합니다. 위치:',cnt)
            search_list.append(cnt)
        cnt+=1

    #검색된 사람들 출력        
    if len(search_list)==0:
        print('존재하지 않습니다.')
    else:
        print(f'{search}(으)로 검색된 사람: ',end='')
        for i in search_list:
            print(name[i],end=' ')
        print()
        print()
            