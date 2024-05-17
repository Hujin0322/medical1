import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
import pandas as pd
import requests
import oracledb

matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 표시
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows 사용자
# matplotlib.rcParams['font.family'] = 'AppleGothic' #Mac 사용자
matplotlib.rcParams['font.size'] = '15' # 글자 크기

x = [1,2,3]
y1 = [2,4,8]
y2 = [1,4,9]
y3 = [7,5,2]

# 다중 꺾은 선 그래프 그리기 
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

# 상단 타이틀 - 제목 넣기
plt.title('막대 그래프')

plt.show() # 그래프만 화면에 보임. 실행하는 문구 사라짐.

#상단 타이틀 글꼴, 크기 변경
plt.title('막대그래프',fontdict={'family':'HYGunSo-Bold','size':30})

# 축, 범례 ---------------------------------------------------------------------
# x, y축 제목의 위치, 색상 변경
plt.xlabel('국어',loc='center',color='red') #left, center, right
plt.ylabel('이름',loc='center',color='green') #top, center, bottom

#범례 이름지정
plt.plot(x,y1,label='국어')
plt.plot(x,y2,label='영어')
plt.plot(x,y3,label='수학')

#범례 표시, 위치 설정(=loc), 범례 가로 설정(=ncol: 1줄에 범례 3개씩 출력)
# plt.legend(loc='upper left')
plt.legend(loc=2,ncol=3) # upper left = 1

# ---------------------------------------------------------------------
# linewidth: 선 두께/ label: 범례 
# marker: 표시('o'=점)/ markersize(ms): 점 크기/ markeredgecolor(mec): 점 테두리 색/ markerfacecolor(mfc): 점 내부 색. 
# alpha: 투명도/ linestyle(ls): 선 모양
plt.plot(x, y1, linewidth=5, marker='o', markersize=10, markeredgecolor='black', markerfacecolor='yellow', label='국어')
plt.plot(x,y1,linewidth=5,marker='*',ms=20,mec='black',mfc='blue',label='국어',alpha=0.7,ls=':')

# x, y축 표시 간격 조정
plt.yticks([5,7,9,11,13,15])
plt.xticks([1,2,3])

# 그래프 눈금 범위 지정
plt.ylim(165,210) 

# 화면 해상도 크기 조절
plt.figure(dpi=200)

# 그래프 크기 조절
plt.figure(figsize=(10,5))

plt.plot(x,y1,label='국어',marker='D')
plt.plot(x,y2,label='영어',marker='o',ls='--')
plt.plot(x,y3,label='수학',marker='s',ls='-.')

# x축 이름 회전
plt.xticks(rotation=45)

# 눈금 표시 
plt.grid(axis='y',alpha=0.2,linestyle='--',linewidth=2,color='purple')
plt.grid(alpha=0.2,linestyle='--',linewidth=2,color='purple')

# 좌표에 해당값 출력
for i, txt in enumerate(y1):
    plt.text(x[i],y1[i]+0.2,txt,ha='center',color='blue')
    
# 그래프 저장 (dpi: 크기)
plt.savefig('이름',dpi=300)

# 막대--------------------------------------------------------------------
# bar: 바로 선 막대 그래프/ barh: 누운 막대 그래프
plt.barh(x,y1,label='키')
# 크기 조절
bar = plt.bar(x,y3,label='국어',width=0.2,alpha=0.5)
# 패턴 넣기
bar[0].set_hatch('/')
bar[1].set_hatch('..')
bar[2].set_hatch('+')

# 누적 막대-------------------------------------------------------------
plt.bar(x,y1,label='국어')
plt.bar(x,y2,bottom=y1,label='영어')
plt.bar(x,y3,bottom=y1+y2,label='수학')

# 값 표시
for i, txt in enumerate(y1):
    plt.text(x[i],y1[i]-12,txt,ha='center')
    
for i, txt in enumerate(y2):
    plt.text(x[i],y1[i]+y2[i]-15,txt,ha='center')

for i, txt in enumerate(y3):
    plt.text(x[i],y1[i]+y2[i]+y3[i]-9,txt,ha='center')
    
# 원 그래프--------------------------------------------------------------
values = [30,25,20,13,10,2] #알아서 비율 맞춤
labels = ['Python','Java','Javascript','C#','C','ETC']
explode = [0.1,0,0,0,0,0]
wedgeprops = {'width':0.7,'edgecolor':'w','linewidth':2}
colors= ['lightcyan','cyan','darkcyan','lightseagreen','aquamarine','turquoise']
# value: 값
# labels: 표시(글자)
# explode: 파이 사이 간격
# autopct: 파이 내 글자 및 퍼센트 표시
# pctdistance: 파이 내 글자 표시 위치
# startangel: 데이터 시작 위치
# colors: 그래프 색상
# counterclock: 그래프 내 데이터 배치 - 시계(False), 반시계 방향
# wedgeprops: 부채꼴 영역의 스타일 설정
plt.pie(values,labels=labels,explode=explode,autopct='%.2f%%',startangle=90,counterclock=False,
        wedgeprops=wedgeprops,pctdistance=0.7,colors=colors)

# scatter ------------------------------------------------------------------
import pandas as pd
df = pd.read_excel('../z20_data/xlsx/score.xlsx',index_col='지원번호')
plt.scatter(df['영어'],df['수학'])

sizes = np.random.rand(8)*1000
# s: 산점도 그래프 점의 크기 조절
plt.scatter(df['영어'],df['수학'], s=sizes)

# 학년 별 크기 조절 (1학년 - 1*500, 2학년 - 2*500, 3학년 - 3*500)
sizes = df['학년']*500

# 학년(c)에 따라 색상(cmap) 넣기
plt.scatter(df['영어'],df['수학'], s=sizes, c=df['학년'],cmap='viridis')

# 컬럼바 눈금표시: ticks/ 라벨 표시: label/ 
# 컬러바 크기 조절: shrink/ 컬러바 위치 조정: orientation (하단: horizontal)
plt.colorbar(ticks=[1,2,3], label='학년', shrink=0.3, orientation='horizontal')

# subplots ------------------------------------------------------------------
# subplots: 여러 개 그래프 생성
fig,axs = plt.subplots(2,2,figsize=(10,10))

#0,0 번째 그래프 작성
# 범례: label
axs[0,0].bar(df['이름'],df['국어'],label='국어점수')
# 범례 출력
axs[0,0].legend()
# 상단 타이틀: set_title
axs[0,0].set_title('국어 그래프')
# x, y축 글자 표시
axs[0,0].set(xlabel='이름',ylabel='국어점수')
# 그래프 내 색상: set_facecolor
axs[0,0].set_facecolor('#efefef')
# 격자 표시: grid
axs[0,0].grid(linestyle='--',alpha=0.5)

#  1개의 그래프에 2가지 내용 넣기 ------------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(10,5))

# 상단 타이틀 출력
fig.suptitle('출생아 수 및 합계 출산율')

# 1번 막대 그래프
ax1.bar(x,y1,color='#ff812d')

# 2번 꺾은선 그래프
ax2 = ax1.twinx() 
ax2.plot(x,y2)

# ------------------------------------------------------------------
# 상관 관계 표시
df.corr()
data_corr = df.corr()
fig = plt.figure(figsize=(16,16))

#sns.heatmap: 색에 따른 상관 관계 확인
sns.heatmap(data_corr,annot=True) #annot: 각 항목 수치 출력

# 히스토그램 그래프
df['Age'].hist()

# 컬럼의 데이터 구성 확인
df.hist(figsize=(14,14))

# Json 데이터 변환------------------------------------------------------------------
# https --> 보안키 적용된 상태, http로 변경 해야 데이터 넘어옴.
url = "Json url"
res = requests.get(url)
res.text

# Json 데이터 변경
json_data = res.json()
json_data

datas = json_data['response']['body']['items']['item'] # 원하는 데이터의 위치 찾기
df = pd.DataFrame(datas)

