import streamlit as st
from unittest import mock
import src.contact_page.contact_main as contact_main
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email_validator as EmailValidator
import pytest


@mock.patch("smtplib.SMTP_SSL")
def test_send_email_success(mock_smtp):
    mock_smtp_instance = mock_smtp.return_value
    mock_smtp_instance.sendmail.return_value = None  # Simulate successful send

    st.secrets = {
        "email_settings": {
            "email": "test@example.com",
            "password": "password",
            "smtp_server": "smtp.example.com",
            "smtp_port": 465
        }
    }

    result = contact_main.send_email("user@example.com", "Test Subject", "Test Message")
    assert result is True

@mock.patch("smtplib.SMTP_SSL")
def test_send_email_failure(mock_smtp):
    mock_smtp_instance = mock_smtp.return_value
    mock_smtp_instance.sendmail.side_effect = Exception("SMTP failed")  # Simulate failure

    st.secrets = {
        "email_settings": {
            "email": "test@example.com",
            "password": "password",
            "smtp_server": "smtp.example.com",
            "smtp_port": 465
        }
    }

    result = contact_main.send_email("user@example.com", "Test Subject", "Test Message")
    assert result is False

@pytest.mark.parametrize(
    "sender_email, subject, message, expected_result",
    [
        ("", "Test Subject", "Test Message", False),  # Empty email
        ("test@example.com", "", "Test Message", False),  # Empty subject
        ("test@example.com", "Test Subject", "", False),  # Empty message
        ("invalid-email", "Test Subject", "Test Message", False),  # Invalid email format
        ("valid@example.com", "Test Subject", "Test Message", True),  # All fields correct
    ],
)
def test_validate_form(sender_email, subject, message, expected_result):
    with mock.patch("streamlit.error") as mock_st_error, mock.patch("email_validator.validate_email") as mock_validate_email:
        if sender_email == "invalid-email":
            mock_validate_email.side_effect = EmailValidator.EmailNotValidError("Invalid email")
        else:
            mock_validate_email.return_value.email = sender_email  # Mock valid email
        
        result = contact_main.validate_form(sender_email, subject, message)
        
        assert result == expected_result
        
        # If expected result is False, we should see some error handling
        if not expected_result:
            mock_st_error.assert_called()
        else:
            mock_st_error.assert_not_called()