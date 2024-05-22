import streamlit as st
from st_pages import hide_pages
import time
import speech_recognition as sr

st.set_page_config(
    initial_sidebar_state="collapsed"
)

if "thinking_process_bool" not in st.session_state:
    st.session_state["thinking_process_bool"] = True
if "progress_process_bool" not in st.session_state:
    st.session_state["progress_process_bool"] = True
if "reload_button" not in st.session_state:
    st.session_state["reload_button"] = False
if "mic_button" not in st.session_state:
    st.session_state["mic_button"] = False
if "interview_num" not in st.session_state:
    st.session_state["interview_num"] = 0

hide_pages(["main_page", "feedback", "interview", "upload_portfolio", "information"])

interviwe_questions = ["1. 간단한 자기소개 부탁드립니다.", "2. 직무에 지원한 계기가 무엇입니까?"]

def get_audio_input():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio = r.listen(source)

def thinking():
    thinking_text = "면접 질문을 읽고 답변을 생각해주세요. 남은 시간 30s"
    thinking_bar = st.progress(100, text=thinking_text)
    for percent_complete in range(1,31):
        time.sleep(1)
        nowtime = str(30 - percent_complete)
        thinking_bar.progress(1 - percent_complete*(1/30), text=thinking_text[:-3] + nowtime + 's')

def progress():
    progress_text = "면접 질문에 대한 답변을 말해주세요. 남은 시간 60s"
    progress_bar = st.progress(100, text=progress_text)
    for percent_complete in range(1,61):
        time.sleep(0.1)
        nowtime = str(60 - percent_complete)
        progress_bar.progress(1 - percent_complete*(1/60), text=progress_text[:-3] + nowtime + 's')

def main():
    st.write(st.session_state)
    interview_num = st.session_state['interview_num']
    st.write(interviwe_questions[interview_num])
    if st.session_state["thinking_process_bool"]:
        thinking()
        st.session_state["thinking_process_bool"] = False
        st.session_state["mic_button"] = True

    if st.session_state["mic_button"]:
        mic_input = st.button("답변하기")
        if mic_input:
            get_audio_input()
    process = progress()
    if interview_num == 19:
        st.page_link("pages/feedback.py", label="면접 끝! 수고하셨습니다!", icon="✔️")
    else:
        if st.button("다음 질문"):
            st.session_state["interview_num"] += 1
            st.session_state["thinking_process_bool"] = True
    
        
if __name__ == "__main__":
    main()