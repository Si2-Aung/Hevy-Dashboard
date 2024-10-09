import streamlit as st
from src.home_page import home_page_main
from src.statistic_page import stats_page_main
from src.contact_page import contact_main
from src.utils import themes
from streamlit_option_menu import option_menu 

def handle_page_selection(workout_data):
    selected_option = create_selection_bar()
    themes.set_page_theme(selected_option)
    display_selected_page(selected_option, workout_data)


def create_selection_bar():
    if 'page_index' in st.session_state:
        page_index = st.session_state.page_index
    else: page_index = 0
    selected_option = option_menu(
            menu_title=None,
            options=["Home", "Statistic", "Contact"],
            icons=["house", "book", "phone"],
            menu_icon="th-large", default_index = page_index, orientation="horizontal"
    )
    return selected_option

def display_selected_page(selected_option, workout_data):
    if selected_option == "Home":
        st.title("Overview📝")
        home_page_main.main(workout_data)
    elif selected_option == "Statistic":
        st.title("Welcome to Statistic Page")
        stats_page_main.main(workout_data)
    elif selected_option == "Contact":
        st.title(":mailbox: Any suggestions or feedback?")
        contact_main.main()