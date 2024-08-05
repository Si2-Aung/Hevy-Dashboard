import streamlit as st
import pandas as pd
import utils.data_cleaning as data_cleaning
import utils.themes as themes
import home_page.home_page_main as home_page
import statistic_page.stats_page_main as stats_page
from streamlit_option_menu import option_menu 


def main():
    workout_data = get_csv_file()
    if workout_data is None:    
        display_how_to_upload()
    else:
        data_cleaning.clean(workout_data)
        selected_option = create_selection_bar()
        themes.set_page_theme(selected_option)
        display_selected_page(selected_option, workout_data)
    
def get_csv_file():
    if 'uploaded_data' not in st.session_state:
        csv_file = st.file_uploader(" ", type="csv", label_visibility="collapsed")
        if csv_file is not None:
            st.success("Data uploaded successfully")
            st.session_state.uploaded_data = pd.read_csv(csv_file)
            st.rerun()
    else:
        return st.session_state.uploaded_data
    return None
    
def display_how_to_upload():
    st.title("📘 How to Use This App")
    st.markdown("""
    **1.** Log in at [hevy.com](https://hevy.com) to **download your CSV file** 😃

    **2.** Navigate to **Settings** and select **'Export Data'** to download your CSV file 📥

    **3.** **Upload your CSV file** here 📤

    **4.** **Enjoy the app** 🎉
    """)

def create_selection_bar():
    page_index = 0
    if 'page_index' in st.session_state:
        page_index = st.session_state.page_index
        
    selected_option = option_menu(
            menu_title=None,
            options=["Home", "Statistic", "Contact"],
            icons=["house", "book", "phone"],
            menu_icon="th-large", default_index=page_index, orientation="horizontal"
    )
    return selected_option

def display_selected_page(selected_option, workout_data):
    if selected_option == "Home":
        st.title("Overview📝")
        home_page.main(workout_data)
    elif selected_option == "Statistic":
        st.title("Welcome to Statistic Page")
        stats_page.main(workout_data)
    elif selected_option == "Contact":
        st.title("Welcome to Contact Page")



if __name__ == "__main__":
    main()
