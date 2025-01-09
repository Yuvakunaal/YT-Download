import streamlit as st
import instaloader
import os
import tempfile
import requests

def insta_downloader():
    # Add a title with custom styling
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Instagram Reels Downloader</h1>", unsafe_allow_html=True)

    # Add a subtitle
    st.markdown("<h5 style='text-align: center; color: #FF5733;'>Download your favorite Instagram Reels in MP4 format</h5>", unsafe_allow_html=True)

    # Add an input field for the Instagram Reel URL
    url = st.text_input("Enter Instagram Reel URL")

    # Add a button to download the Reel
    if st.button("Download"):
        if url:
            try:
                with tempfile.TemporaryDirectory() as tmpdirname:
                    loader = instaloader.Instaloader(download_videos=True, download_comments=False, save_metadata=False)
                    shortcode = url.split("/")[-2]
                    post = instaloader.Post.from_shortcode(loader.context, shortcode)
                    
                    if post.is_video:
                        video_url = post.video_url
                        
                        # Download the video file manually
                        video_response = requests.get(video_url)
                        video_filename = os.path.join(tmpdirname, f"{shortcode}.mp4")
                        with open(video_filename, 'wb') as video_file:
                            video_file.write(video_response.content)
                        
                        
                        if os.path.exists(video_filename):
                            # Provide the video as a downloadable file
                            with open(video_filename, 'rb') as file:
                                st.download_button(
                                    label="Download Reel",
                                    data=file,
                                    file_name=os.path.basename(video_filename),
                                    mime='video/mp4'
                                )
                            st.success("Reel processed successfully!")
                        else:
                            st.error("Failed to download the Reel.")
                    else:
                        st.error("The provided URL does not point to a video.")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter a valid Instagram Reel URL")
