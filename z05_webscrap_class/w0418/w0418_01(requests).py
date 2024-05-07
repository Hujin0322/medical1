#기본 구문 -----------------------------------------------------
import requests #웹 정보, 소스 가져오는 라이브러리
url = "http://www.google.com"
# url = "http://www.melon.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러코드 발생 시 프로그램 종료  ------
#---------------------------------------------------------------



# => if res.status_code == requests.codes.OK: #응답코드: 200
if res.status_code == 200: #응답코드: 200
    print("정상적인 페이지 호출")
else:
    print("접근 할 수 없음[에러코드: ",res.status_code,"]")
