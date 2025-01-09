import streamlit as st
from home import home
from about import about
from yt_downloader import yt_downloader
from feedback import feedback

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.sidebar.title("YT -> MP4")
page = st.sidebar.radio("Go to", ["Home", "About", "YouTube Video Downloader"])

if page == "Home":
    home()
elif page == "About":
    about()
elif page == "YouTube Video Downloader":
    yt_downloader()
