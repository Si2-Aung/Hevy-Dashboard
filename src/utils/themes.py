import streamlit as st

def set_page_theme(selected_option):
    set_initial_session_state()
    handle_option_change(selected_option)
    reload_page_if_needed()

def set_initial_session_state():
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = "Home"

    keys = ['homereloaded', 'statisticreloaded', 'contactreloaded']
    for key in keys:
        if f"{key}" not in st.session_state:
            st.session_state[f"{key}"] = False

def handle_option_change(selected_option):
    if st.session_state.selected_option != selected_option:
        if selected_option == "Home":
            st.session_state.homereloaded = True
        elif selected_option == "Statistic":
            st.session_state.statisticreloaded = True
        elif selected_option == "Contact":
            st.session_state.contactreloaded = True
        st.session_state.selected_option = selected_option

def reload_page_if_needed():
    if st.session_state.homereloaded:
        set_color("#FF4B4B", "white", "#d5d1d5", "#31333F")
        st.session_state.homereloaded = False
        st.rerun()
    elif st.session_state.statisticreloaded:
        set_color("#008DFF", "white", "#d5d1d5", "#4c3245")
        st.session_state.statisticreloaded = False
        st.rerun()
    elif st.session_state.contactreloaded:
        set_color("#008000", "white", "#d5d1d5", "#4c3245")
        st.session_state.contactreloaded = False
        st.rerun()

def set_color(primaryColor, backgroundColor, secondaryBackgroundColor, textColor):
    st._config.set_option('theme.primaryColor',primaryColor)
    st._config.set_option('theme.backgroundColor', backgroundColor)
    st._config.set_option('theme.secondaryBackgroundColor', secondaryBackgroundColor)
    st._config.set_option('theme.textColor', textColor)
    return