import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email_validator as EmailValidator

# Function to render the form
def render_email_form():
    with st.form(key="email_form"):
        sender_email = st.text_input("Your Email", value="", placeholder="Enter your email", max_chars=50, key="email")
        subject = st.text_input("Subject", value="", placeholder="Enter the email subject", max_chars=100, key="subject")
        message = st.text_area("Message", value="", placeholder="Enter your message", max_chars=777, key="message")
        submit_button = st.form_submit_button(label="💌 Send Email")
        
        return submit_button, sender_email, subject, message

# Function to validate the form
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

# Function to send email
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

# Main handler for email sending
def handle_email_sending():
    if st.session_state.email_sent:
        st.success("Email has been sent. You can not send more emails.")
        return

    # Render the email form
    submit_button, sender_email, subject, message = render_email_form()

    if submit_button:
        if not validate_form(sender_email, subject, message):
            return

        if send_email(sender_email, subject, message):
            st.session_state.email_sent = True
            st.success("Email sent successfully!")
            st.rerun()
