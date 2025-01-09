import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

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
        # Read credentials from environment variables
        creds_dict = {
            "type": os.getenv("GCP_TYPE"),
            "project_id": os.getenv("GCP_PROJECT_ID"),
            "private_key_id": os.getenv("GCP_PRIVATE_KEY_ID"),
            "private_key": os.getenv("GCP_PRIVATE_KEY").replace('\\n', '\n'),
            "client_email": os.getenv("GCP_CLIENT_EMAIL"),
            "client_id": os.getenv("GCP_CLIENT_ID"),
            "auth_uri": os.getenv("GCP_AUTH_URI"),
            "token_uri": os.getenv("GCP_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("GCP_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("GCP_CLIENT_X509_CERT_URL")
        }

        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict)
        client = gspread.authorize(creds)

        sheet = client.open('Feedback').sheet1
        sheet.append_row([name, email, rating, description])

        st.success('Feedback submitted successfully!')
