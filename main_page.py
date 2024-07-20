import streamlit as st
import pandas as pd
import home_page
from streamlit_option_menu import option_menu
import data_cleaning as dc

def main():
    workout_data = get_csv_file()
    if workout_data is not None:
        dc.clean(workout_data)
        selected_option = option_menu(
            menu_title = None,
            options = ["Home", "Statitstic", "Contact"],
            icons=["house", "book", "phone"],
            menu_icon="th-large",
            default_index=0,
            orientation="horizontal"
        )

        if selected_option == "Home":
            home_page.main(workout_data)

        elif selected_option == "Statitstic":
            st.title("Welcome to Statitstic Page")

        elif selected_option == "Contact":
            st.title("Welcome to Contact Page")


def get_csv_file():
    # Allow the user to upload a CSV file
    csv_file = st.file_uploader(" ",type="csv",label_visibility="collapsed")
    if csv_file is not None:
        st.success("Data uploaded successfully")
        workout_data = pd.read_csv(csv_file)
    else:
        if 'uploaded_data' in st.session_state:
            workout_data = st.session_state['uploaded_data']
        else:
            workout_data = None
    return workout_data

main()