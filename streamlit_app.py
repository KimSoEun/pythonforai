import streamlit as st

st.title("Streamlit 웹앱")
st.header("사용자 입력")
name = st.text_input("이름을 입력하세요")
age = st.slider("나이", 0, 120, 25)

if st.button("확인"):
    st.success(f"{name}님은 {age}세입니다.")
    st.button("에러 버튼")
else:
    st.error('에러입니다!')