import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_icon="👻",
    page_title="인바디 이미지 분석",
    layout="wide",
)

# 페이지 헤더, 서브헤더 제목 설정
st.title("인바디 이미지 분석 사이트")

st.header("서비스 소개")
st.text("안녕하십니까. DeepHealth-Invadors 팀 입니다. 저희의 캡스톤 디자인 2의 주제는 '인바디 이미지를 분석해 건강을 지도해주는 애플리케이션 제작' 입니다.")

st.header("기술 스택 & 팀원 소개")
st.text("임수혁 : 딥러닝 분류 모델 설계") 
st.text("김의찬 :  웹 파트 1") 
st.text("민선익 :  웹 파트 2")




