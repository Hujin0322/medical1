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

url = "https://jumin.mois.go.kr/ageStatMonth.do"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
with open ("jumin.html","w",encoding="utf-8")as f:
    f.write(soup.prettify())


tbody = soup.find_all("tbody")
trs = tbody[2].find_all("tr")
seoul2 = trs[1].find_all("td")
seoul = seoul2[2].text
print('서울특별시 인구 수: ',seoul)
incheon2 = trs[4].find_all("td")
incheon = incheon2[2].text
print('인천광역시 인구 수: ',incheon)
kyuggi2 = trs[9].find_all("td")
kyuggi = kyuggi2[2].text
print('경기도 인구 수: ',kyuggi)

total = int(seoul.replace(",",""))+int(incheon.replace(",",""))+int(kyuggi.replace(",",""))
print("수도권 인구수: ",format(total,","))
