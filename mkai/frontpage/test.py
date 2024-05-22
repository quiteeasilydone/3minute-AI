import streamlit as st
import speech_recognition as sr
import threading
import time

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

def on_click():
    st.session_state.button_clicked = True


def progress():
    progress_text = "면접 질문에 대한 답변을 말해주세요. 남은 시간 60s"
    progress_bar = st.progress(100, text=progress_text)
    for percent_complete in range(1,61):
        time.sleep(1)
        nowtime = str(60 - percent_complete)
        progress_bar.progress(1 - percent_complete*(1/60), text=progress_text[:-3] + nowtime + 's')
        
# Function to plot audio waveform
def get_audio_input():
    r = sr.Recognizer()
    r.pause_threshold = 60
    r.non_speaking_duration = 60

    with sr.Microphone() as source:
        audio = r.listen(source, timeout=60)
        
    return audio

def f1():
    placeholder1 = st.empty()
    for i in range(60):
        time.sleep(0.1)
        placeholder1.write('function1:' + str(i))

def f2():
    placeholder2 = st.empty()
    for i in range(60):
        time.sleep(0.1)
        placeholder2.write('function2:' + str(i))

def run_threads():
    t1 = threading.Thread(target=f1)
    t2 = threading.Thread(target=f2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
        

# if not st.session_state.button_clicked:
if st.button("마이크 켜기", on_click=on_click):
        run_threads()
        # st.write(user_input)