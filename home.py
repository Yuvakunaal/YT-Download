import streamlit as st

def home():
    # Add a title with custom styling
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Welcome to the Amazing App</h2>", unsafe_allow_html=True)

    # Add a subtitle
    st.markdown("<h3 style='text-align: center; color: #FF5733;'>Your one-stop solution for all your needs</h3>", unsafe_allow_html=True)

    # Add an image
    st.image("https://www.pushengage.com/wp-content/uploads/2022/02/Best-Website-Welcome-Message-Examples.png", use_container_width=True)

