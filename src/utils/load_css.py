import streamlit as st

def load_css(file_name:str)->None:
    with open(file_name) as f:
        st.html(f'<style>{f.read()}</style>')