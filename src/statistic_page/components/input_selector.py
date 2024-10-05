import streamlit as st
import numpy as np

def get_category_input():
    category_options = [
        "All Muscles", "Chest", "Biceps", "Lower Back", "Abdominals",
        "Upper Back", "Cardio", "Calves", "Forearms", "Glutes", "Custom",
        "Hamstrings", "Lats", "Quadriceps", "Shoulders", "Triceps", "Traps", "Neck", "Full Body"
    ]
    selected_category = st.selectbox("Select a Muscle group", category_options, key="category_selection")
    return selected_category


def get_time_input():
    time_options = ["Last 3 months", "Last 6 months", "Last year", "All time"]
    selected_timeframe = st.selectbox("Select a Timeframe", time_options, key="timeframe_selection")
    return selected_timeframe


def get_timeframe_and_category():
    columns = st.columns(2)

    with columns[0]:
        selected_category = get_category_input()

    with columns[1]:
        selected_timeframe = get_time_input()

    return selected_timeframe, selected_category

def get_exercise(workout_data):
    workout_data = np.sort(workout_data)
    selected_exercise = st.session_state.selected_exercise
    
    if selected_exercise in workout_data and selected_exercise is not None:
        index = workout_data.tolist().index(selected_exercise)
    else:
        index = 0  # Default to the first exercise

    return st.selectbox("Select an Exercise", workout_data, index=index, key="exercise_selection")