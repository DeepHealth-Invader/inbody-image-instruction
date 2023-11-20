import streamlit as st
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import re
from openai import OpenAI
from pages.config import OPENAI_API_KEY
# 페이지 기본 설정
st.set_page_config(
    page_icon="🦾",
    page_title="GPT쌤의 PT 상담소",
    layout="wide",
)


st.markdown("""
<style>


.big-font {
    font-size: 50px !important;
    color: #5a9;
    text-align: center;
    padding-top: 50px;
}
.file-uploader {
    display: flex;
    justify-content: center;
    padding: 50px;
}
.button {
    background-color: #5a9;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
}
.button:hover {
    background-color: #3c6;
}
.result-header {
    color: #5a9;
    font-size: 30px;
}
.result-text {
    font-size: 20px;
    color: #555;
}
.description {
    font-size: 20px;
    text-align: center;
}
.waiting {
    text-align: center;
    font-size: 24px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<p>
    <div class="big-font">
        회원 상담실 🦾
    </div>
</p>    
""", unsafe_allow_html=True)

st.markdown("""
<div class="description">
    <p>안녕하세요! GPT 쌤이에요~ 🌟<br />
    여러분의 인바디 사진을 주시면,<br />
    체중, 골격근량, 체지방량을 멋지게 분석해드려요! 📸✨<br />
    사진 업로드 하시면 분석 들어갈께요 ~🔄💻.</p> 
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("네,회원님 여기에다가 업로드 부탁드릴께요~😊", type=["jpg", "png"], key="1")

if uploaded_file is not None:
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    height, width, _ = img.shape
    part_height = height // 3
    img_parts = [img[part_height * i:part_height * (i + 1), :] for i in range(3)]

    weights, muscles, fats = [], [], []
    for i, img_part in enumerate(img_parts):
        data = pytesseract.image_to_data(img_part, lang='eng', output_type=Output.DICT)
        numbers = [(float(num), data['height'][j]) for j, num in
                   enumerate(re.findall('\d+\.\d', ' '.join(data['text']))) if num]
        if numbers:
            num, _ = max(numbers, key=lambda x: x[1])
            if i == 0:
                weights.append(num)
            elif i == 1:
                muscles.append(num)
            else:
                fats.append(num)

    weight = max(weights) if weights else None
    muscle = max(muscles) if muscles else None
    fat = max(fats) if fats else None

    st.markdown("<h2 class='result-header'>회원님</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='result-text'>체중: {weight} kg 이시고</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='result-text'>골격근량: {muscle} 이렇게 되시고 ..</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='result-text'>체지방량: {fat} 이시네요 !</p>", unsafe_allow_html=True)

    st.markdown("<h2 class='result-header'>분석한 이미지 부분</h2>", unsafe_allow_html=True)
    for i, img_part in enumerate(img_parts):
        st.image(img_part, channels="BGR", use_column_width=True)

    st.markdown("<p class='result-header'>제가 직접 하나하나 세세하게 적어드릴테니까 회원님 잠시만 기다려주세요 ~ ! 😉  </p>", unsafe_allow_html=True)

    # GPT API KEY 정보
    client = OpenAI(api_key=OPENAI_API_KEY)

    # gpt-3.5-turbo 를 사용하여 message 형식 만들기
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a personal trainer."},
            {"role": "user", "content": f"체중: {weight}, 골격근량: {muscle}, 체지방량: {fat}. 이렇게 되는데 어떻게 운동 방식을 가져가야하는지와 식단조절 및 방법을 회원님께 설명해줘."}
        ]
    )

    # Waiting for GPT response animation
    st.markdown("<div class='waiting'>GPT썜 적는 중 ...</div>", unsafe_allow_html=True)

    # GPT 응답 결과 텍스트
    gpt_response = completion.choices[0].message.content

    # 결과 출력
    st.markdown("<h2 class='result-header'>자 회원님 한번 같이 봐보실까요 ?💻 </h2>", unsafe_allow_html=True)
    st.markdown(gpt_response)

    # 결과를 파일로 저장
    with st.expander("회원님 지인 소개시 10% 할인 들어가시는데 어떻게 하시겠어요 ?🦾😊 "):
        # 결과를 파일로 저장
        result_file_path = "gpt_response.txt"
        with open(result_file_path, "w", encoding="utf-8") as result_file:
            result_file.write(gpt_response)

        # 결과 파일 다운로드 링크 생성
        st.markdown(
            f"[**결과 다운로드**](sandbox:/view/{result_file_path})",
            unsafe_allow_html=True
        )
