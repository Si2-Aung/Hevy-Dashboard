import streamlit as st
import pandas as pd
from src.utils import data_cleaning
from src.utils.load_css import load_css
from src.utils import page_selector  as ps

def main():
    load_css("assets/styles.css")
    workout_data = data_cleaning.get_cleaned_csv_file()
    if workout_data is None:    
        display_how_to_upload()
        display_test_this_app()
        st.divider()
    else:
        ps.handle_page_selection(workout_data)
    
def display_how_to_upload():
    st.title("📘 How to Use This App")
    st.markdown("""
    **1.** Log in at [hevy.com](https://hevy.com) to **download your CSV file** 😃
                
    **2.** Navigate to **Settings** and select **'Export Data'** to download your CSV file 📥
                
    **3.** Drag and drop the file to the Uploader above 📤
                
    **4.** **Enjoy the app** 🎉
    """)

def display_test_this_app():
    st.title("You have no Data?")
    st.write("No Problem! You can try the app with random generated data, no upload needed 🎉")

    toggle = st.toggle("Show the random generated data", key="show_data")
    if toggle:
        st.dataframe(pd.read_csv("random_data.csv"))

    test_now = st.button("Test now", key="test_now")
    if test_now and 'uploaded_data' not in st.session_state:
        st.session_state.uploaded_data = pd.read_csv("random_data.csv")
        st.rerun() 

if __name__ == "__main__":
    main()