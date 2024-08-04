import streamlit as st

def set_home_page_theme():
    st._config.set_option('theme.primaryColor',"#FF4B4B")
    st._config.set_option('theme.backgroundColor', "white")
    st._config.set_option('theme.secondaryBackgroundColor', "#d5d1d5")
    st._config.set_option('theme.textColor', "#31333F")
    return


def set_statistic_page_theme():
    st._config.set_option('theme.primaryColor',"#008DFF")
    st._config.set_option('theme.backgroundColor', "white")
    st._config.set_option('theme.secondaryBackgroundColor', "#d5d1d5")
    st._config.set_option('theme.textColor', "#4c3245")
    return 

def set_contact_page_theme():
    st._config.set_option('theme.primaryColor',"#008000")
    st._config.set_option('theme.backgroundColor', "white")
    st._config.set_option('theme.secondaryBackgroundColor', "#d5d1d5")
    st._config.set_option('theme.textColor', "#4c3245")
    return 