import streamlit as st
from streamlit_modal import Modal
from st_pages import hide_pages

st.set_page_config(
    initial_sidebar_state="collapsed"
)

hide_pages(["main_page", "feedback", "interview", "upload_portfolio", "information"])

st.markdown("1. 이력서를 업로드")
st.markdown("- 이력서를 기반으로 면접 대상의 직무, 경력, 전공 등을 파악합니다.")                    
st.markdown("- 사진(jpg, jpeg, png) 파일로 된 이력서를 업로드 해주세요.")
st.markdown("- 사이트(notion 등)로 만들어진 이력서 업로드 또한 가능합니다.")