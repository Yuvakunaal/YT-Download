import streamlit as st
from yt_dlp import YoutubeDL
import os
import tempfile
import io

def yt_downloader():
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>YouTube Video Downloader</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: #FF5733;'>Download your favorite YouTube videos in MP4 format</h5>", unsafe_allow_html=True)

    url = st.text_input("Enter YouTube video URL")

    if st.button("Download"):
        if url:
            try:
                # Create a temporary directory to store the video
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
                        video_title = info_dict.get('title', 'video')
                        video_filename = ydl.prepare_filename(info_dict)

                    # Read the downloaded video into a BytesIO buffer
                    with open(video_filename, 'rb') as file:
                        video_bytes = file.read()

                    # Provide the video for downloading via Streamlit
                    st.download_button(
                        label="Download Video",
                        data=video_bytes,
                        file_name=os.path.basename(video_filename),
                        mime='video/mp4',
                    )
                    st.success("Video processed successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter a valid YouTube URL")
