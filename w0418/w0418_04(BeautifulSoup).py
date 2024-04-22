import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

    
soup = BeautifulSoup(res.text,"lxml") #text를 html 파싱(=변경)
# print(soup.prettify()) #html 소스를 정렬해서 출력

print("<title>: ",soup.title) #태그 입력 --> 태그 정보 가져옴
print("<title text>: ",soup.title.get_text()) #태그의 글자 가져옴.
print("<title text>: ",soup.title.text) #태그의 글자 가져옴.
print("<a> 태그: ",soup.a)
print("<a> 글자: ",soup.a.text)
print("<a> 속성 전체: ",soup.a.attrs) #태그의 속성값 모두 가져옴

print("<a>[1개 속성]: ",soup.a["href"]) #태그의 1개 속성 가져옴.
