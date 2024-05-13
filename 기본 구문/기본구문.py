import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')

df.describe()   # 컬럼별 대략적 정보 (최소, 최대값, 평균 등)
df['키'].max()
df['키'].min()
df['키'].mean()
df['키'].count()

df[['키','이름']][1:4]
df[df.columns[[1,3,4]]][1:4]

df.head()       # 상단 5개 출력
df.tail()       # 하단 5개 출력
df.info()       # 컬럼별 타입, 크기 정보
df.values       # rows 데이터 배열로 출력
df.index        # index 정보
df.columns      # 컬럼 정보
df.shape        # 데이터 크기 정보 (8,9)

df.shape[0] # row의 갯수
df.shape[1] # 컬럼의 갯수

# 컬럼 호출 방법
df['키']
df['이름']
df[['이름','키']]


df['키'].nlargest(4)
df['키'].nsmallest(3) 

# rows 데이터 가져오기
df[:3]
df[5:]
# df[[0,1,3]] #error
df.iloc[[0,1,3]] # rows 데이터 부분적으로 가져오기

df.head()
df.tail(2)


### row 출력
# df.loc['1번'] = df.iloc[0]
df.loc[['1번','5번']]                  # 2개의 row데이터 출력
df.loc['1번','키']                     # 1번 학생의 키 값만 출력
df.loc['1번',['이름','키']]             # 1번 학생의 이름, 키 출력
df.loc[['1번','5번'],['이름','키']]     # 1번과 5번 학생의 이름과 키 출력
df.loc['1번':'5번','국어':'사회']       #row데이터 슬라이싱


# 조건문
# 국어 85점 이상, 영어 85점 이상 이름, 학교, 국어, 영어 출력
# pandas: &, | / 제외 출력: ~
# python: and, or
filt = (df['국어'] >= 85) & (df['영어'] >= 85)
df.loc[filt,['이름','학교','국어','영어']] # 조건에 해당
df.loc[~filt,['이름','학교','국어','영어']] # 조건의 반대

# 문자열 함수
data ={"idx":['안녕하세요.','반갑습니다.','고마워요다음에봐요']}
df_str = pd.DataFrame(data)
df_str

df_str['idx']

# slice: 문자열 자르기
df_str['idx'].str.slice(1,3)
# map(함수), lambda: 익명함수
# df_str['idx'].map(lambda x:x[1:3]) #--> 슬라이싱

# split: 문자열 분리
a_list = ['데이터,분석가','영희,철수,바둑이','국어,영어,수학,과학']
data = {"d_split":a_list}
df_str = pd.DataFrame(data)
s_data = df_str['d_split'].str.split(',') #배열로 분리되어 리턴
s_data

#replace: 문자열 처리, strip: 공백 제거

# startswith, contains, lower, upper
# 문자열함수 적용 - lower()
lang = ['python','java']
df['SW특기'].str.upper()
df['SW특기'].str.lower()

# isin(리스트): 2개 이상의 검색
filt = df['SW특기'].str.lower().isin(lang)
filt = df['SW특기'].str.lower().str.contains('java',na=True)

#Q. id에 a포함, 평균-역순정렬, 국어-순차정렬
filt = df['id'].str.lower().str.contains('a')
df[filt].sort_values(['avg','kor'],ascending=[False,True])

#컬럼 지정
name = ['aaa','bbb','ccc','ddd','eee']
births = [968,155,77,578,973]
custom = [1,5,25,13,23232]
bSet = list(zip(name,births,custom))
df = pd.DataFrame(data=bSet,columns=['name','births','custom'])

# nan 적용
import numpy as np
df.loc['3번','영어'] = np.nan
df.loc['5번',['영어','국어']] = np.nan

# fillna
df.fillna('없음',inplace=True)            #데이터 전체 Nan에 적용
df['SW특기'].fillna('없음',inplace=True)  #특정 컬럼 Nan에 적용

# 개별 갯수 확인
df['학교'].count(): #전체 갯수
df['학교'].value_counts() #중복 갯수


#---------------------------------------------------------------------
import pandas as pd
df = pd.read_excel('../z20_data/score.xlsx',index_col='지원번호')

# columns 추가: 없는 컬럼에 데이터 입력
df['합계'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
df['결과'] = '불합격'

# columns 삭제
df.drop(columns='사회',inplace=True)            #1개 삭제
df.drop(columns=['국어','과학'],inplace=True)   #여러 개 삭제

# columns 수정
df['학교'] = df['학교'] + '등학교'                  #전체 수정
df['SW특기'] = df['SW특기'].str.upper()             #전체 대문자로 수정
df['학교'].replace({"구로고등학교":"디지털고","단지고등학교":"영등포고"},inplace=True) #여러개 수정


# index 추가 (rows 기준)
df.loc['9번'] = ['홍길동','디지털고',191,90,80,70,60,90,'python']

# index 삭제 (rows 기준)
df.drop(index='5번',inplace=True)                     # 1개 삭제
df.drop(index=['1번','3번'],inplace=True)             # 여러개 삭제
df.drop(index=df[df['국어']<80].index, inplace=True)  # 조건부 삭제
filt = df['국어']<80
df.drop(index=df[filt].index, inplace=True)

# index 수정 - 위치점 검색 후 수정할 데이터 입력. (rows 기준)
df.loc['5번',['학교','키']] = ['디지털고',190]      # 5번의 학교와 키 수정
df.loc[['4번','5번'],'SW특기'] = ['Java','python'] # 4,5번 학생의 SW특기에 각각 java, python
#---------------------------------------------------------------------

# 최솟값 출력
df['영어'].min()
# 최솟값 가진 index명 출력
df['영어'].idxmin()
df.loc[df['영어'].idxmin()]

# 컬럼의 최대 values값 출력
df['영어'].max()
# 최댓값 출력
df['영어'].idxmax()
df.loc[df['영어'].idxmax()]