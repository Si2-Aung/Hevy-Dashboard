import streamlit as st
import streamlit_antd_components as stac
from src.utils.load_css import load_css
from src.contact_page.email_form import handle_email_sending

# --- Function to initialize session state ---
def initialize_session_state():
    if "email_sent" not in st.session_state:
        st.session_state.email_sent = False

def create_credentials():
    stac.buttons([
    stac.ButtonsItem(label='GitHub', icon='github',  href="https://github.com/Si2-Aung"),
    stac.ButtonsItem(label='LinkedIn', icon='linkedin', href="https://www.linkedin.com/in/si-thu-aung-31203532a/", color = 'blue'),
    stac.ButtonsItem(label='Hevy', icon='share-fill', href="https://www.hevy.com", color='red')
    ], label='', align='left',color='black')

def main():
    load_css("assets/contact_styles.css")
    initialize_session_state()
    handle_email_sending()
    create_credentials()
