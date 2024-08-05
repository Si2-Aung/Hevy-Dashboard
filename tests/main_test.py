import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import streamlit as st

# Assume the file's methods are imported correctly
from streamlit_app import main, get_csv_file, how_to_upload, create_selection_bar

class TestMainPy(unittest.TestCase):

    @patch('streamlit.file_uploader')
    @patch('streamlit.session_state')
    @patch('streamlit.success')
    @patch('streamlit.rerun')
    def test_get_csv_file(self, mock_rerun, mock_success, mock_session_state, mock_file_uploader):
        # Mock the file uploader and session state
        mock_file_uploader.return_value = MagicMock()
        mock_session_state.uploaded_data = None
        
        # Call the method
        result = get_csv_file()
        
        # Check if the file uploader was called
        mock_file_uploader.assert_called_once()
        
        # Check if the rerun was called when file is uploaded
        mock_success.assert_called_once_with("Data uploaded successfully")
        mock_rerun.assert_called_once()
        
        # Test the case when the session state already has data
        mock_session_state.uploaded_data = pd.DataFrame()
        result = get_csv_file()
        self.assertIsInstance(result, pd.DataFrame)
        
    
    @patch('home_page.home_page_main.main')
    @patch('statistic_page.stats_page_main.main')
    @patch('streamlit_option_menu.option_menu')
    @patch('streamlit.title')
    def test_create_selection_bar(self, mock_title, mock_option_menu, mock_stats_page_main, mock_home_page_main):
        # Mock the option menu
        mock_option_menu.return_value = "Home"
        
        # Call the method
        create_selection_bar(pd.DataFrame())
        
        # Check if the home page main method was called
        mock_home_page_main.assert_called_once()
        
        # Change the selected option and check the statistics page
        mock_option_menu.return_value = "Statistic"
        create_selection_bar(pd.DataFrame())
        mock_stats_page_main.assert_called_once()

    @patch('main.get_csv_file')
    @patch('main.how_to_upload')
    @patch('main.create_selection_bar')
    def test_main(self, mock_create_selection_bar, mock_how_to_upload, mock_get_csv_file):
        # Mock the get_csv_file method
        mock_get_csv_file.return_value = None
        
        # Call the main method
        main()
        
        # Check if how_to_upload was called when get_csv_file returns None
        mock_how_to_upload.assert_called_once()
        
        # Change the return value of get_csv_file
        mock_get_csv_file.return_value = pd.DataFrame()
        
        # Call the main method again
        main()
        
        # Check if create_selection_bar was called when get_csv_file returns data
        mock_create_selection_bar.assert_called_once()

if __name__ == '__main__':
    unittest.main()
