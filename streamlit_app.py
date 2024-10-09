import streamlit as st
import pandas as pd
from src.utils import data_cleaning
from src.utils import page_selector  as ps

def main():
    load_css("assets/styles.css")
    workout_data = data_cleaning.get_cleaned_csv_file()
    if workout_data is None:    
        display_how_to_upload()
        display_test_this_app()
    else:
        ps.handle_page_selection(workout_data)
    
def display_how_to_upload():
    st.title("📘 How to Use This App")
    st.markdown("""
    **1.** Log in at [hevy.com](https://hevy.com) to **download your CSV file** 😃
                
    **2.** Navigate to **Settings** and select **'Export Data'** to download your CSV file 📥
                
    **3.** **Upload your CSV file** here 📤
                
    **4.** **Enjoy the app** 🎉
    """)

def display_test_this_app():
    st.title("🎲Test this app?")
    st.write("You can try the app with the random data, no upload needed 🎉")
    test_now = st.toggle("Test now")
    
    if test_now and 'uploaded_data' not in st.session_state:
        st.session_state.uploaded_data = pd.read_csv("random_data.csv")
        st.rerun() 

def load_css(file_name:str)->None:
    with open(file_name) as f:
        st.html(f'<style>{f.read()}</style>')

if __name__ == "__main__":
    main()