import streamlit as st
from yt_dlp import YoutubeDL
import os
import tempfile

def yt_downloader():
    # Add a title with custom styling
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>YouTube Video Downloader</h1>", unsafe_allow_html=True)

    # Add a subtitle
    st.markdown("<h5 style='text-align: center; color: #FF5733;'>Download your favorite YouTube videos in MP4 format</h5>", unsafe_allow_html=True)

    # Add an input field for the YouTube URL
    url = st.text_input("Enter YouTube video URL")

    # Add a button to download the video
    if st.button("Download"):
        if url:
            try:
                with tempfile.TemporaryDirectory() as tmpdirname:
                    ydl_opts = {
                        'format': 'best',
                        'outtmpl': os.path.join(tmpdirname, '%(title)s.%(ext)s'),
                        'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                        },
                    }
                    with YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(url, download=True)
                        video_title = info_dict.get('title', None)
                        video_filename = ydl.prepare_filename(info_dict)
                    
                    with open(video_filename, 'rb') as file:
                        st.download_button(
                            label="Download Video",
                            data=file,
                            file_name=os.path.basename(video_filename),
                            mime='video/mp4'
                        )
                    st.success("Video processed successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter a valid YouTube URL")
