import requests
from bs4 import BeautifulSoup
url ="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

table = soup.find("table",{"class":"item_list"})
tds = table.select("tr > td > label")

for i in tds:
    print(i.text)

