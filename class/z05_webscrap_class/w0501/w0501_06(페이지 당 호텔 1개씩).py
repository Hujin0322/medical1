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

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

browser = webdriver.Chrome()
browser.maximize_window()

for i in range(5):
    url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page={i+1}"
    browser.get(url)
    time.sleep(2)

    soup=BeautifulSoup(browser.page_source,"lxml")
    # # 파일 저장
    # with open("yeogi.html","w",encoding="utf-8")as f:
    #     f.write(soup.prettify())

    hotels = soup.find_all("div",{"class":"css-gvoll6"})
    # print("전체 갯수: ", len(hotels))
    title = hotels[0].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
    print("title: ",title.text)
    print("지역: ",hotels[0].find("div",{"class":"css-19li9i9"}))
    print("평점: ",hotels[0].find("div",{"class":"css-wtzmcu"}).text)
    print("평가 수: ",hotels[0].find("span",{"class":"css-oj6onp"}).text)
    print("이미지 링크: ",hotels[0].find("img",{"class":"thumbnail-image desktop:hover:bg-backgroundOverlayDarkInactive"}).attrs['src'])
    print("가격: ",hotels[0].find("div",{"class":"css-yeouz0"}).text)
    print("-"*50)



# title = soup.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
# print("title: ",title.text)


