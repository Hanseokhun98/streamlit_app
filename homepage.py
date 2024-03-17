import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

df = pd.read_csv('CU전체통합_파생.csv')
# matplotlib 한글 폰트 설정
plt.rc('font', family='NanumGothic')
test_df = df.iloc[:10].copy()

st.markdown('# 편의점 :red[**고객 패턴 분석**] 을 통한 매출 증대 전략')
st.header('빅데이터 아카데미 :blue[25]기 :blue[C1]조', divider='gray')
st.markdown('#### **1. 데이터셋 구조** ')

data_inference = """
해당 데이터셋은 편의점 고객 패턴 분석을 통해 매출 증대 전략을 수립하기 위해
구축한 사용자 정보,판매 데이터,상품 데이터,날씨 데이터를 통합한 데이터셋 입니다.
"""


def stream_data():
    for word in data_inference.split(" "):
        yield word + " "
        time.sleep(0.02)

    test_df

if st.button("데이터 미리보기"):
    st.write_stream(stream_data)

# 'AgeGroup'과 'Gender'로 그룹화하고, 각 그룹의 크기(빈도) 계산
grouped_data = df.groupby(['AgeGroup', 'Gender']).size().unstack(fill_value=0)
# 'ItemName' 별로 집계하고 상위 10개 선택
item_sales = df['ItemName'].value_counts().head(10)

st.divider()
st.markdown('#### **2. 데이터 분석** ')

if st.button("연령별 분포 확인"):
    fig, ax = plt.subplots(figsize=(10, 6))  # 그래프 크기 설정
    grouped_data.plot(kind='bar', ax=ax, rot=45)  # 연령대와 성별에 따른 분포를 바 차트로 그림
    ax.set_xlabel('연령대 및 성별',fontsize=22)
    ax.set_ylabel('인원 수',fontsize=18)
    ax.set_title('연령대별 및 성별 분포',fontsize=18)
    ax.axhline(y=100000, color='r', linestyle='--', linewidth=2)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    st.pyplot(fig)

if st.button("인기 아이템 조회"):
    fig, ax = plt.subplots(figsize=(10, 6))
    item_sales.plot(kind='bar', ax=ax)
    ax.set_title('가장 많이 팔린 10개 아이템',fontsize=22)
    ax.set_xlabel('아이템 이름',fontsize=18)
    ax.set_ylabel('판매 수량',fontsize=18)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(rotation=45)
    # ax 객체의 patches를 사용하여 상위 3개 품목 위에 빨간색 점선 박스를 그립니다.
    for rect in ax.patches[:3]:  # 상위 3개 바에 대해서만 실행
        height = rect.get_height()
        width = rect.get_width()
        x = rect.get_x()
        y = rect.get_y()
        
        # 빨간색 점선 박스를 추가합니다.
        ax.add_patch(patches.Rectangle((x, y), width, height, linewidth=2, edgecolor='r', facecolor='none'))
    
    st.pyplot(fig)

st.divider()

