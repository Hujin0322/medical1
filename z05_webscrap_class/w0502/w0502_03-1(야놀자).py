# 야놀자 홈페이지 이동
# 검색창에 '호텔' 입력 
# 날짜 선택: 6/5 - 6/6 날짜 
# 확인 버튼 클릭 
# 검색창 클릭 > enter 키 입력
# 검색 진행
# 스크롤 이동 반복
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

url = "https://www.yanolja.com/"
browser.get(url)
time.sleep(2)

#1. 검색창
elem = browser.find_element(By.XPATH,'//span[text()="무엇을 하고 놀까요?"]').click()
time.sleep(2)

#2. 호텔 입력
elem = browser.find_element(By.CLASS_NAME,"SearchInput_input__342U2")
elem.send_keys("호텔")
time.sleep(1)

#3. 숙박 시작 날 선택
elem = browser.find_element(By.XPATH,'//button[@class="NavFilterButton_container__20Hr2 NavFilterButton_collapse__3JGvV SearchInput_calendarButton__3sNMZ"]').click()
time.sleep(1)


#4. 6월 5일 선택
elem = browser.find_elements(By.XPATH,'//td[text()="5"]')
elem[1].click()
time.sleep(1)

#5. 6월 6일 선택
elem = browser.find_elements(By.XPATH,'//td[text()="6"]')
elem[1].click()
time.sleep(1)

#6. 확인 선택
elem = browser.find_element(By.XPATH,'//button[text()="확인"]').click()
time.sleep(1)

#7. 검색
elem = browser.find_element(By.XPATH,'//button[@class="SearchInput_button__tUMEN SearchInput_buttonSubmit__3D83k"]').click()
time.sleep(1)

#8. 로딩 
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="PlaceListItemText_container__fUIgA text-unit"]')))

#9. 스크롤 이동
prev_hight = browser.execute_script("return document.body.scrollHight")

#스크롤 이동 자동화
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_hight == curr_height:
        break
    prev_hight = curr_height
    



time.sleep(100)
