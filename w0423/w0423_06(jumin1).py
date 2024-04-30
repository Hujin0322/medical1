# https://jumin.mois.go.kr/ageStatMonth.do
# 서울특별시, 인천광역시, 경기도 3개의 인구를 웹스크래핑해서
# 서울특별시: 인구
# 인천광역시: 인구
# 경기도: 인구
# 합계: 인구를 출력하시오.

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get("https://jumin.mois.go.kr/ageStatMonth.do")
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,"lxml")

url = "https://jumin.mois.go.kr/ageStatMonth.do"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

table = soup.find_all("table")
trs = table[2].find_all("tr")
print(trs[4].find("td",{"class":"td_admin th1"}).text,':',trs[4].find("td",{"title":"2024년 03월 / 계"}).text+"명")
print("-"*40)
print(trs[7].find("td",{"class":"td_admin th1"}).text,':',trs[7].find("td",{"title":"2024년 03월 / 계"}).text+"명")
print("-"*40)
print(trs[12].find("td",{"class":"td_admin th1"}).text,':',trs[12].find("td",{"title":"2024년 03월 / 계"}).text+"명")

