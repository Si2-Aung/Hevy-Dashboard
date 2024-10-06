import streamlit as st
from src.statistic_page.components import display_statistic
from src.statistic_page.components import excercise_filter 
from src.statistic_page.components import input_selector


def main(workout_data):
    load_css("assets/styles.css")
    initialize_session_state()

    slected_timeframe, slected_category = input_selector.get_timeframe_and_category()
    categroy_filtered_data = excercise_filter.filter_by_category_and_time(workout_data, slected_timeframe, slected_category)
    slected_exercise = input_selector.get_exercise(categroy_filtered_data['exercise_title'].unique())
    if slected_exercise is not None:
        excercise_filtered_data = excercise_filter.filter_data_by_exercise(categroy_filtered_data, slected_exercise)

        update_session_state(slected_exercise)

        if not excercise_filtered_data.empty:
            display_statistic.display(excercise_filtered_data)
    else:
        st.warning("No data available for the selected filters. Choose other options.")
    

def initialize_session_state():
    st.session_state.setdefault('selected_category', "All Muscles")
    st.session_state.setdefault('selected_timeframe', "Last 3 months")
    st.session_state.setdefault('selected_exercise', None)


def update_session_state(exercise):
    if exercise != st.session_state.selected_exercise:
        st.session_state.selected_exercise = exercise
        st.rerun()
def load_css(file_name:str)->None:
    with open(file_name) as f:
        st.html(f'<style>{f.read()}</style>')

