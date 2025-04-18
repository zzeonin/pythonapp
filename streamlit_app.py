import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GDP 애니메이션 대시보드", layout="wide")
st.title("🌍 연도별 국가별 GDP 애니메이션 시각화")

uploaded_file = st.file_uploader("💾 gdp_data.csv 파일 업로드", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head())

    st.subheader("📊 애니메이션 차트 보기")

    fig = px.bar(df,
                 x='gdp',
                 y='country',
                 color='country',
                 orientation='h',
                 animation_frame='year',
                 range_x=[0, df['gdp'].max() * 1.1],
                 title='연도별 국가별 GDP 변화')

    st.plotly_chart(fig, use_container_width=True)

    st.success("✅ 완성! 이건 진짜 발표 때 써먹어 보세요")