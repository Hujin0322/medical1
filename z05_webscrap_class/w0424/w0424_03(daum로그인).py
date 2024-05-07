import random
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.daum.net/"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)

elem = browser.find_element(By.CLASS_NAME,'btn_login').click()
time.sleep(random.randint(2, 5))


input_js = 'document.getElementById("loginId--1").value="{id}";\
            document.getElementById("password--2").value="{pw}";\
            '.format(id="aaa",pw="1111")
time.sleep(random.randint(2, 5))
browser.execute_script(input_js)
time.sleep(random.randint(2, 5))

elem = browser.find_element(By.CLASS_NAME,'btn_g highlight')
# elem.click()

time.sleep(100)