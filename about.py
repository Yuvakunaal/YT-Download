import streamlit as st

def about():
    # Add a title with custom styling
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>About This App</h1>", unsafe_allow_html=True)

    # Add a subtitle
    st.markdown("<h3 style='text-align: center; color: #FF5733;'>Learn more about what this app offers</h3>", unsafe_allow_html=True)

    # Add some descriptive text
    st.markdown("""
    <div style='text-align: center;'>
        <p style='font-size: 18px;'>Our app includes feature like YouTube video downloading</p>
    </div>
    """, unsafe_allow_html=True)
