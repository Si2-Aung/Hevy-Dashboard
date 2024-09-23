from streamlit.testing.v1 import AppTest
import pandas as pd

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

def test_display_selected_page():
    app = AppTest.from_file("streamlit_app.py").run()
    sidebar = app.get("sidebar")
    assert sidebar is not None

    assert 'page_index' not in app.session_state
    app.session_state["page_index"] = 0
    assert app.session_state["page_index"] == 0
