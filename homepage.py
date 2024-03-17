import streamlit as st
import pandas as pd

view = [100,150,30]
st.write('# 편의점 고객 패턴 분석을 통한 매출 증대 전략')
st.write('## 빅데이터 아카데미 25기 C1조')
st.bar_chart(view)
s_view = pd.Series(view)
s_view