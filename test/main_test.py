from streamlit.testing.v1 import AppTest

def test_main():
    # Initialize the AppTest from the streamlit app file
    app = AppTest.from_file("streamlit_app.py")
    # Run the app
    app.run()
    # Assert that the app does not raise any exceptions
    assert not app.exception

