##파일 읽어와서 출력하기
#medical 폴더 안 member.csv
#상대경로: h0327/aaa/member2.csv
#절대경로: c:/workspace/medical1/h0327/aaa/member2.csv

with open ("c:/workspace/medical1/h0327/aaa/member2.csv","r",encoding="utf-8") as f:
        
    while True:
        text=f.readline()
        if text=='': break
        mem=text.split(',')
        print(mem[0],mem[1])
        
            