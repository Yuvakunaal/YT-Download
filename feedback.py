import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def feedback():
    st.title("Feedback Form")
    st.write("Please provide your feedback below:")

    with st.form(key='feedback_form'):
        name = st.text_input(label='Name', placeholder="Enter your name")
        email = st.text_input(label='Email', placeholder="Enter your email")
        rating = st.slider('Rating', 1, 5, 3)
        description = st.text_area(label='Description', placeholder="Share your feedback")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
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
            "client_x509_cert_url": os.getenv("GCP_CLIENT_X509_CERT_URL"),
        }

        try:
            # Authorize credentials
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict)
            client = gspread.authorize(creds)

            # Open the Google Sheet
            sheet = client.open('Feedback').sheet1
            sheet.append_row([name, email, rating, description])

            st.success('Feedback submitted successfully!')
        except gspread.exceptions.APIError as api_error:
            st.error("API Error: Ensure the spreadsheet exists and the service account has access.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    feedback()
