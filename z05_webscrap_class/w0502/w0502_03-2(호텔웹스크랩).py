# 이미지, 제목, 평점, 평가 수, 금액 저장 --> 따로 해보기
# yanolja 테이블 
# yno, img, title, grade, grade_num, price  

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

url = "https://www.yanolja.com/search/%ED%98%B8%ED%85%94?keyword=%ED%98%B8%ED%85%94&searchKeyword=%25ED%2598%25B8%25ED%2585%2594"
browser.get(url)
time.sleep(2)

# yno, img, title, grade, grade_num, price  
soup = BeautifulSoup(browser.page_source,"lxml")
divs = soup.find("div",{"class":"PlaceListBody_itemGroup__1V8Q3 PlaceListBody_textUnitList__HEDb3"})
div = divs.find_all("div",{"class":"PlaceListItemText_area__3l67D"})

img = div[0].find("div",{"class":"PlaceListImage_imageText__2XEMn"})['style']
loc = img.find("http")
print(img[loc:-3])

title = div[0].find("div",{"class":"PlaceListTitle_container__qe7XH"})
print(title.text)

grade = div[0].find("span",{"class":"PlaceListScore_rating__3Glxf"})
print(grade.text)

grade_num = div[0].find("span",{"class":"PlaceListScore_reviewInfo__3QSCU"})
print(grade_num.text[1:-1].replace(",",""))

price = div[0].find("span",{"class":"PlacePriceInfoV2_bottomInfo__2h62q"})
if price.text == '예약마감':
    print("0")
else:
    print(price.text)