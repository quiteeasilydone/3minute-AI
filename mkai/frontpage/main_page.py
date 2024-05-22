import streamlit as st
from st_pages import hide_pages
from pyparsing import empty

st.set_page_config(layout = "wide",
    initial_sidebar_state="collapsed"
)

hide_pages(["main_page", "feedback", "interview", "upload_portfolio", "information"])

empty1,title,empty2 = st.columns([0.3,1.0,0.3])
empyt1,header,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con1,empty2 = st.columns([0.3,1.0,0.3])
empyt1,info,uplo,empty2 = st.columns([0.3,0.5,0.5,0.3])

def main():
    with empty1:
        empty()
    
    with empty2:
        empty()
        
    with title:
        st.title("AI 면접 피드백 서비스")
    
    with header:
        st.header("면접은 까보기 전까지 모른다!")
    
    with con1:
        st.write("면접이 처음이신 분, 면접 준비가 잘 안되시는 분, 면접 질문에 어떻게 대답해야할지 모르겠는 분!")
        st.write("그런들을 위한 AI 면접 피드백 서비스 입니다.")

    with info:
        st.page_link("pages/information.py", label="사용방법", icon="✔️")
            
    with uplo:
        st.page_link("pages/upload_portfolio.py", label="이력서 제출하러 가기", icon="✔️")
        
if __name__ == "__main__":
    main()