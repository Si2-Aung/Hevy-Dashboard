import streamlit as st
from streamlit_option_menu import option_menu

selected_option = option_menu(
    menu_title = None,
    options = ["Home", "Statitstic", "Contact"],
    icons=["house", "book", "phone"],
    menu_icon="th-large",
    default_index=0,
    orientation="horizontal"
)

if selected_option == "Home":
    st.title("Welcome to Home Page")

elif selected_option == "Statitstic":
    st.title("Welcome to Statitstic Page")

elif selected_option == "Contact":
    st.title("Welcome to Contact Page")
