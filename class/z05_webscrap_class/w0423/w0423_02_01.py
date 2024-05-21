import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# selenium으로 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
# with open ("webtoons2.html","w",encoding="utf-8")as f:
#     f.write(soup.prettify())
# print("완료")

ul = soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
li = ul.find_all("div",{"class":"AsideList__info_area--PVPwn"})
n=0
for i in li:
    n += 1
    # rank = i.find("div",{"class":"AsideList__raking_area--aQX3C"})
    # print("순위: ",i.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
    print('순위: ',n)
    title = i.find("span",{"class":"text"}).text
    print('제목: ',title)
    author = i.find("a",{"class":"ContentAuthor__author--CTAAP"}).text
    print('작가: ',author)
    img_url = i.find("div",{"class":"Poster__bullet_wrap--VcWFJ"})
    print('img_url: ',img_url.img['src'])
    print("-"*40)

# #requests 정보 가져오기
# url = "https://comic.naver.com/bestChallenge"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())
# with open ("webtoons1.html","w",encoding="utf-8")as f:
#     f.write(soup.prettify())
# print("완료")


# browser = webdriver.Chrome()
# browser.get("https://www.naver.com/")

# time.sleep(10)

# elem = browser.find_element("MyView-module__link_login___HpHMW")
# elem
# elem.click()