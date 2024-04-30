import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# selenium으로 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
# with open ("webtoons2.html","w",encoding="utf-8")as f:
#     f.write(soup.prettify())
# print("완료")

list_ul = soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
lis = list_ul.find_all("li")
for li in lis:
    w_rank = li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text
    print("등수: ",li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
    print("제목: ",li.find("span",{"class":"text"}).text)
    print("작가: ",li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
    img_url = li.find("img",{"class":"Poster__image--d9XTI"})['src']
    print("이미지 링크: ",img_url)
    
    #이미지 파일 저장 방법
    img_poster = requests.get(img_url,headers=headers)
    with open("webtoons_{}.jpeg".format(w_rank),"wb")as f:
        f.write(img_poster.content)
    print("-"*40)
    
