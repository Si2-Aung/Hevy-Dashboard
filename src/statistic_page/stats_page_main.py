import streamlit as st
from src.statistic_page.components import filter_category_time as fct


def main(workout_data):
    initialize_session_state()

    selected_timeframe, selected_category = display_time_category_selection()
    filtered_data = fct.main(workout_data, selected_timeframe, selected_category)

    selected_exercise = display_exercise_selection(filtered_data)
    update_session_state(selected_exercise)


def initialize_session_state():
    st.session_state.setdefault('selected_category', "All Muscles")
    st.session_state.setdefault('selected_timeframe', "Last 3 months")
    st.session_state.setdefault('selected_exercise', None)


def update_session_state(exercise):
    if exercise != st.session_state.selected_exercise:
        st.session_state.selected_exercise = exercise
        st.rerun()


def display_time_category_selection():
    columns = st.columns(2)

    with columns[0]:
        category_options = [
            "All Muscles", "Custom", "Biceps", "Lower Back", "Abdominals",
            "Upper Back", "Cardio", "Chest", "Calves", "Forearms", "Glutes",
            "Hamstrings", "Lats", "Quadriceps", "Shoulders", "Triceps", "Traps", "Neck", "Full Body"
        ]
        selected_category = st.selectbox("Select a Muscle group", category_options)

    with columns[1]:
        time_options = ["Last 3 months", "Last 6 months", "Last year", "All time"]
        selected_timeframe = st.selectbox("Select a Timeframe", time_options)

    return selected_timeframe, selected_category


def display_exercise_selection(workout_data):
    selected_exercise = st.session_state.selected_exercise

    if selected_exercise in workout_data:
        index = workout_data.tolist().index(selected_exercise)
    else:
        st.warning("Selected exercise is not available for the current filters.")
        index = 0  # Default to the first exercise

    return st.selectbox("Select an Exercise", workout_data, index=index)
