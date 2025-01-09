import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def feedback():
    st.title("Feedback Form")
    st.write("Please provide your feedback below:")

    with st.form(key='feedback_form'):
        name = st.text_input(label='Name')
        email = st.text_input(label='Email')
        rating = st.slider('Rating', 1, 5, 3)
        description = st.text_area(label='Description')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open('Feedback').sheet1
        sheet.append_row([name, email, rating, description])

        st.success('Feedback submitted successfully!')