import streamlit as st
import os


# 페이지 기본 설정
st.set_page_config(
    page_icon="🦾",
    page_title="GPT쌤의 PT 상담소",
    layout="wide",
)


# 스타일링 CSS 정의
header_style = """
    color:  #00FF00; 
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
"""

subheader_style = """
    color: #4a4a4a;
    text-align: center;
    font-size: 24px;
    margin-bottom: 20px;
"""

text_style = """
    color: #4a4a4a;
    text-align: left;
    font-size: 16px;
"""

# 페이지 헤더, 서브헤더 제목 설정
st.markdown("<h1 style='{}'>어서오세요~GPT GYM 입니다 🎉".format(header_style), unsafe_allow_html=True)


st.markdown(
    """
    ## GPT 쌤의 유쾌한 PT 상담소 🏋️‍♂️💬

    안녕하세요! GPT 쌤 여기 상담소에 오신 여러분을 환영합니다! 🎉

    여기서는 인바디 이미지를 분석하여 건강을 지도해주는 애플리케이션을 제작하는 DeepHealth-Invadors 팀의 멋진 프로젝트를 소개합니다. 😊

    제가 여러분의 PT 쌤으로 함께 건강을 책임지고 즐겁게 지도해드릴게요! 🌟

    이미지를 업로드하고, 팀원들과 함께 여러 기술을 활용하여 건강한 삶을 위한 팁을 제공합니다. 건강한 몸과 마음으로 여러분을 기다리고 있어요! 💪💖

    왼쪽의 inbody 탭을 눌러 인바디 사진을 업로드만 하면 끝나니까 얼른 해보세요😊!
    """
)

st.markdown("<h2 style='{}'>개발진 소개</h2>".format(subheader_style), unsafe_allow_html=True)

# 이미지 파일들이 있는 디렉토리 경로
image_dir = "C:/Users/user-pc/PycharmProjects/inbody-image-instruction/image"

# 이미지 파일들의 이름 리스트
image_names = ["임수혁.png", "김의찬.png", "민선익.png"]

# 각 이미지를 스트림릿에 표시 및 역할 추가
col1, col2, col3 = st.columns(3)

for i, image_name in enumerate(image_names):
    with eval(f"col{i+1}"):
        # 각 이미지를 스트림릿에 표시
        image_path = os.path.join(image_dir, image_name)
        image = open(image_path, "rb").read()
        st.image(image, caption=None, use_column_width=True)

        # 팀원 역할 텍스트 추가
        st.markdown("<h3 style='{}'>{}</h3>".format(subheader_style, image_name.replace('.png', '')), unsafe_allow_html=True)
        if i == 0:
            st.markdown("<p style='{}'>🎨 프론트엔드 디자인과 구현<br>🖥 사용자 인터페이스(UI) 담당</p>".format(text_style), unsafe_allow_html=True)
        elif i == 1:
            st.markdown("<p style='{}'>🚀 이미지 처리 및 결과 표시<br>🧠 이미지 검출 모델 설계 및 구현 담당</p>".format(text_style), unsafe_allow_html=True)
        elif i == 2:
            st.markdown("<p style='{}'>🛠 백엔드 시스템 아키텍처 설계 및 구현<br>🌐 외부 API와의 통합 담당</p>".format(text_style), unsafe_allow_html=True)




