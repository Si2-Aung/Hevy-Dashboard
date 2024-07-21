import streamlit as st
import pandas as pd
import home_page
from streamlit_option_menu import option_menu
import data_cleaning as dc

def main():
    workout_data = get_csv_file()
    if workout_data is None:    
        how_to_upload()
    else:
        dc.clean(workout_data)
        selected_option = option_menu(
            menu_title = None,
            options = ["Home", "Statistic", "Contact"],
            icons=["house", "book", "phone"],
            menu_icon="th-large",
            default_index=0,
            orientation="horizontal"
        )

        if selected_option == "Home":
            home_page.main(workout_data)

        elif selected_option == "Statistic":
            st.title("Welcome to Statistic Page")

        elif selected_option == "Contact":
            st.title("Welcome to Contact Page")


def get_csv_file():
    workout_data = None
    if 'uploaded_data' not in st.session_state:
        csv_file = st.file_uploader(" ", type="csv", label_visibility="collapsed")
        if csv_file is not None:
            st.success("Data uploaded successfully")
            workout_data = pd.read_csv(csv_file)
            # Store the uploaded file in the session state
            st.session_state.uploaded_data = workout_data
            st.rerun()
    else:
        return st.session_state.uploaded_data
    
def how_to_upload():
    st.title("📘 How to Use This App")

    st.markdown("""
    **1.** Log in at [hevy.com](https://hevy.com) to **download your CSV file** from your browser 😃

    **2.** Navigate to **Settings** and select **'Export Data'** to download your CSV file 📥

    **3.** **Upload your CSV file** here 📤

    **4.** **Enjoy the app** 🎉
    """)


main()
