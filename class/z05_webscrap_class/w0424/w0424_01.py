import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "http://www.google.com"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# with open ("google.html","w",encoding="utf-8")as f:
#     f.write(soup.prettify())

#파일에서 가져오기
with open ("google.html","r",encoding="utf-8")as f:
    soup = BeautifulSoup(f,"lxml")
print("title: ",soup.find("title").text)