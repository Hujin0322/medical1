# 정규표현식

# . 하나의 문자
# ^ 문자열의 시작
# $ 문자열의 끝
# [ ] 대괄호 내에 일치하길 바라는 문자 입력
# ex) [0-9]: 0~9까지 숫자가 일치하는지 확인
# ex) [a-zA-Z]: 영문자와 일치하는지 확인
# ex) [ㄱ-ㅎ가-힣] 국문자와 일치하는지 확인
# { } 문자의 길이
# ex) {2}: 2자리 문자
# ex) {3,}: 문자 길이 3자리 이상
# ex) {,3} 문자 길이 3자리 까지
# ex) {2,3}: 문자 길이가 2자리부터 3자리까지

# match() 처음부터 모두 일치하는지 확인
# search() 일치하는 것이 있는지 확인
# findall() 일치하는 것이 있는지 리스트로부터 확인 (리스트로 검색)
# group() 일치하면 해당 문자 출력
# compile() 정규식 형태 지정
# sub() 일치하는 데이터 삭제

import re
# ex) 1. match
p = re.compile("lo.k")
word = 'look'
if p.match(word):
    print("매칭됨.",p.match(word).group())
else: print("매칭X",word)

# ex) 2. search
word = "삼성전자는 21일 개선된 AI(인공지능) 기능을 제공하는 '갤럭시 북4 엣지'를 공개했다."
if re.search("지능",word):
    print("매칭O",re.search("지능",word).group())
else: print("매칭되지 않음",word)

# ex) 3. '^[a-z]' #영문자로 시작하는~
word = 'een-1.txt'
if re.match('^[a-z]{2,}',word):
    print(re.match('^[a-z]{2,}',word).group())
else:
    print('매칭 문자X')

# ex) 4. sub 문자, 숫자 제외 나머지 공백으로 처리
words = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]',' ',word) 

# --------------------------------------------------------------------------------------------------------
from sklearn import svm,metrics
from sklearn.neighbors import KNeighborsClassifier # 분류
from sklearn.neighbors import KNeighborsRegressor   # 회귀 - 예측
from sklearn.ensemble import RandomForestClassifier #예측, 분류
from sklearn.linear_model import LinearRegression # 선형 회귀
from sklearn.model_selection import train_test_split 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글 설정
matplotlib.rcParams['font.size'] = 10 #글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

# <머신러닝 구현>
# 1. 데이터 전처리 - Nan, 0, 단위 처리, train_set, test_set 분리
# 모든 데이터 입력은 숫자여야 함.
# 데이터 1개: 리스트 타입
# 데이터 2개: 리스트 타입에 리스트
train_input, test_input, train_target, test_target = train_test_split('데이터')

# 2. 데이터 학습
# 1). svm
clf = svm.SVC() # svm 라이브러리 사용
clf.fit(train_input,train_target) # fit 훈련 시키는 과정(데이터, 결과값) --> list 타입

# 2). KNN 알고리즘 
# - 최근접 이웃 분류
knr = KNeighborsRegressor() # 분류
knr.fit(train_input, train_target)

# - 최근접 이웃 회귀: 근접 이웃의 평균
knr = KNeighborsRegressor() # 회귀 - 예측
knr.fit(train_input, train_target)

# knn 회귀 단점: 훈련세트가 없는 데이터는 예측이 안 됨.
# 과대 적합, 과소 적합 (train score < test score) --> 수동 테스트 필요
knr.n_neighbors = n # 기본 5에서 n개로 변경

# 3). RandomForestClassifier - 예측, 분류
rfc = RandomForestClassifier()
rfc.fit(train_input,train_target)

# 4). LinearRegression - 선형 회귀, 예측
# KNN 단점 보완, 기울기 이용 -> 데이터 확장 가능, 곡선화 (2차원 방정식) -> 0에서 -가 되는 경우 보완 가능.
lr = LinearRegression()
lr.fit(train_input,train_target)

# y = ax + b (a = 기울기, b = y절편) 
# lr.coef_: 기울기 
# lr.intercept_: y절편
# _: 모델을 훈련시켜서 모델에서 제공하는 변수는 '_' 사용

# 4-1). 다항회귀 - 직선 여러번 그리기
# 그래프 출력
# 특성, 제곱을 자동으로 만들어주는 라이브러리
from sklearn.preprocessing import PolynomialFeatures

plt.scatter(train_input,train_target)
x = np.arange(15,50)
plt.plot(x, (1.014*x)**2+-21.55*x+116.05) # 기울기*x**2 + 기울기 * x + y절편

# 3. 데이터 예측
predict = clf.predict(test_input)

# 4. 예측값 구하기 (오차 범위)
score = clf.score(test_input,test_target)

# --------------------------------------------------------------------------------------------------------
# numpy - 평균, 표준편차
mean = np.mean(train_input, axis=0)
std = np.std(train_input,axis=0)

# 표준 점수 = (훈련 데이터 - 평균) / 표준편차
train_scaled = (train_input - mean) / std
train_scaled = (test_input - mean) / std
