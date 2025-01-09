import streamlit as st
from home import home
from about import about
from yt_downloader import yt_downloader
from insta_downloader import insta_downloader
from feedback import feedback

st.set_page_config(
    page_title="YT Downloader",  # Title shown in the browser tab
    page_icon="💠",            # Emoji or URL to an image
    layout="wide"              # Optional: 'centered' or 'wide'
)

st.sidebar.title("YT -> MP4")
page = st.sidebar.radio("Go to", ["Home", "About", "YouTube Video Downloader", "Insta Video Downloader"])

if page == "Home":
    home()
elif page == "About":
    about()
elif page == "YouTube Video Downloader":
    yt_downloader()
elif page == "Insta Video Downloader":
    insta_downloader()

