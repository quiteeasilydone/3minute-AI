import streamlit as st
from streamlit_modal import Modal
from st_pages import hide_pages

st.set_page_config(
    initial_sidebar_state="collapsed"
)

hide_pages(["main_page", "feedback", "interview", "upload_portfolio", "information"])