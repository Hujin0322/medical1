import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#화면 나타는 것 확인에 사용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui 

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)
# 출발지 선택
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()

# 국내 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()

#김포 국제 공항 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(1)
elem.click()

# 도착지 선택
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()

# 국내 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()

#김포 국제 공항 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
time.sleep(1)
elem.click()

#가는 날 부분 선택 
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]').click()
time.sleep(1)

#가는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
print('14일 갯수: ',len(elem))
time.sleep(1)
elem[1].click()
time.sleep(1)

#오는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
time.sleep(1)
elem[1].click()

#인원수 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[contains(text(),"성인")]')
elem.click()
time.sleep(1)

# 성인 인원 수 추가
elem = browser.find_element(By.XPATH,'//button[@class="searchBox_outer__9n6IB"]').click()
time.sleep(1)

# 인원수 닫기
elem = browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()
time.sleep(1)

# 항공권 검색 선택
elem = browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()
time.sleep(1)

# 화면 대기 시간 함수
#time.sleep(7)
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
print(elem)
print(elem[0].text)

# 화면 스크롤 내리기
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이: ",prev_height)

#스크롤 이동 자동화
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    #스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print("현재 높이: ",curr_height)


#웹 스크래핑
soup = BeautifulSoup(browser.page_source,"lxml")
with open ("flight.html","w",encoding="utf-8")as f:
    f.write(soup.prettify())
    

input("Enter 키를 입력하면 프로그램을 종료합니다.")
browser.quit()
#time.sleep(100)
