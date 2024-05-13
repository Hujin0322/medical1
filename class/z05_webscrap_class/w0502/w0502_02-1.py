import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,"lxml")

# with open ("melon.html","r",encoding="utf-8") as f:
#     f.write(soup.prettify())

# with open ("melon.html","r",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,"lxml")


tbody = soup.find("tbody")
ranks = tbody.find_all("tr")
for i in range(len(ranks)):
    #순위
    rank1 =ranks[i].find("span",{"class":"rank"})
    rank = int(rank1.text)
    print(rank)

    #변동 순위
    v_rank1 = ranks[i].find("span",{"class":"rank_wrap"})
    v_rank2 = v_rank1.find("span",{"class":"none"}).text
    if v_rank2 == '순위 동일':
        v_rank = 0
        print(v_rank)
        
    elif v_rank2 == '단계 상승':
        v_rank3 = v_rank1.find("span",{"class":"up"})
        v_rank = int(v_rank3.text)
        print(v_rank)
        
    elif v_rank2 == '단계 하락':
        v_rank3 = v_rank1.find("span",{"class":"down"})
        v_rank = int(v_rank3.text)*-1
        print(v_rank)
        
    elif v_rank2 == '순위 진입':
        v_rank = 0
        print(v_rank)

    #이미지 링크
    img = ranks[i].find("img")['src']
    print(img)

    #제목
    title = ranks[i].find("div",{"class":"ellipsis rank01"})
    title = title.text.replace("'","")
    print(title)

    #가수
    singer1 = ranks[i].find("span",{"class":"checkEllipsis"})
    singer = singer1.text
    print(singer)

    #좋아요 수
    likeNum1 = ranks[i].find("span",{"class":"cnt"})
    likeNum2 = likeNum1.text.strip()[4:]
    likeNum = int(likeNum2.replace(",",""))
    print(likeNum)
    
    print("-"*40)
    
    # DB저장
    sql = f"insert into melon values (melon_seq.nextval,{rank},{v_rank}\
    ,'{img}','{title}','{singer}',{likeNum})"
    cursor.execute(sql)
    
print("-"*30)


cursor.execute('commit')
cursor.close()
conn.close()
