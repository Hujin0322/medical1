import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By #요소 선택
from selenium.webdriver.common.keys import Keys #키워드 입력
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url ="https://www.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

'''
1. 네이버 페이지 이동
2. 검색창에 '네이버 항공권' 입략
3. 검색창 엔터키 입력
-- 네이버 항공권 검색 이동
4. 네이버 항공권 클릭
-- 네이버 항공권 페이지 이동
5. 출발 지역 선택 - 서울
6. 도착지역 선택 - 제주
7. 가는 날 (5/5) 선택
8. 오는 날 (5/6) 선택
9. 성인 2인 선택
10. 항공권 검색 버튼 클릭
11. 검색 동안 대기
12. 검색된 항공권 스크롤 해서 하단 이동 반복 (끝까지)
13. 13만원 이하 항공권 정보 저장
'''