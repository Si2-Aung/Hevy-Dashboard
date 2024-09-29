import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email_validator as EmailValidator

# --- Function to initialize session state ---
def initialize_session_state():
    if "email_sent" not in st.session_state:
        st.session_state.email_sent = False
    if "last_sent_time" not in st.session_state:
        st.session_state.last_sent_time = None

# --- Function to render the form ---
def render_email_form():
    with st.form(key="email_form"):
        sender_email = st.text_input("Your Email", value="", placeholder="Enter your email", max_chars=50)
        subject = st.text_input("Subject", value="", placeholder="Enter the email subject", max_chars=100)
        message = st.text_area("Message", value="", placeholder="Enter your message", max_chars=1000)
        submit_button = st.form_submit_button(label="Send Email")
        
        return submit_button, sender_email, subject, message

# --- Function to validate the form ---
def validate_form(sender_email, subject, message):
    if not sender_email or not subject or not message:
        st.error("All fields are required!")
        return False
    try:
        valid = EmailValidator.validate_email(sender_email)
        sender_email = valid.email  # Use normalized version
    except EmailValidator.EmailNotValidError as e:
        st.error(f"Invalid email address: {e}")
        return False

    return True

def send_email(user_email, subject, message):
    sender_email = st.secrets["email_settings"]["email"]  
    receiver_email = st.secrets["email_settings"]["email"]  
    password = st.secrets["email_settings"]["password"]
    smtp_server = st.secrets["email_settings"]["smtp_server"]
    smtp_port = st.secrets["email_settings"]["smtp_port"]
    
    full_message = f"From: {user_email}\n\n{message}"

    msg = MIMEMultipart()
    msg['From'] = sender_email  
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(full_message, 'plain'))
    
    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

def handle_email_sending():
    st.header("Contact me")

    # Check if the email has already been sent or if we are within cooldown
    if st.session_state.email_sent:
        st.success("Email has already been sent. You cannot send more emails.")
        return

    # Render the email form
    submit_button, sender_email, subject, message = render_email_form()

    # Handle form submission
    if submit_button:
        # First validate the form fields
        if not validate_form(sender_email, subject, message):
            return

        # Send the email if validation passes
        if send_email(sender_email, subject, message):
            st.session_state.email_sent = True
            st.success("Email sent successfully!")
            st.rerun()

def create_buttons():
    st.header("Explore my professional networks")
    col1, col2, col3 = st.columns([4, 4, 3])
    logo_width = 100

    # GitHub
    with col1:
        github_logo = "https://pngimg.com/uploads/github/github_PNG23.png"
        st.image(github_logo, width=logo_width)
        st.markdown('<a href="https://github.com/Si2-Aung" target="_blank"><button style="background-color:#24292e;color:white;width:100px;margin-top:1px;">GitHub</button></a>', unsafe_allow_html=True)

    # LinkedIn
    with col2:
        linkedin_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/LinkedIn_logo.svg/800px-LinkedIn_logo.svg.png"
        st.image(linkedin_logo, width=logo_width)
        st.markdown('<a href="https://www.linkedin.com/in/si-thu-aung-31203532a/" target="_blank"><button style="background-color:#0a66c2;color:white;width:100px;margin-top:10px;">LinkedIn</button></a>', unsafe_allow_html=True)

    # Hevy
    with col3:
        hevy_logo = "https://www.hevyapp.com/wp-content/uploads/hevy-logo.svg"
        st.image(hevy_logo, width=logo_width)
        st.markdown('<a href="https://www.hevy.com" target="_blank"><button style="background-color:#f44336;color:white;width:100px;margin-top:10px;">Hevy</button></a>', unsafe_allow_html=True)

# --- Main application logic ---
def main():
    initialize_session_state()
    handle_email_sending()
    create_buttons()