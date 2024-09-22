from streamlit.testing.v1 import AppTest
from unittest.mock import patch, MagicMock
import pandas as pd
import streamlit as st

# Mock data for testing
mock_csv_data = pd.DataFrame({
    'exercise': ['Push Up', 'Squat'],
    'reps': [10, 15],
    'weight': [0, 50]
})

def test_main():
    # Initialize the AppTest from the streamlit app file
    app = AppTest.from_file("streamlit_app.py")

    # Run the app
    app.run()
    # Assert that the app does not raise any exceptions
    assert not app.exception

def test_get_csv():
    # Initialize the AppTest from the streamlit app file
    app = AppTest.from_file("streamlit_app.py").run()
    assert 'uploaded_data' not in app.session_state

    app.session_state["uploaded_data"] = mock_csv_data
    assert app.session_state["uploaded_data"] is not None




