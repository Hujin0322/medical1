#다른 파일에 있는 함수를 사용할 때
# 1) impot math -> 사용방법: math,floor() 이름, 함수명()
# 2) from math import * #이름 생략 가능
# 3) import lotto
# from lotto import *

# 4). import 함수명 as 별칭
import math as m #모듈명을 줄여서 사용 가능. 별칭부여
import lotto as lo 

l=[0]*45
# while True:
#     lotto.screen()
lo.screen()
lo.num_generate(l)

# #math.ceil():올림
print(m.ceil(12.2))
# #math.floor():버림
print(m.floor(12.2))
# #round():반올림
# print(round(12.6))

print(dir(m)) #모듈 목록 확인