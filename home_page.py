import streamlit as st
import pandas as pd
import data_cleaning as dc
import streamlit_shadcn_ui as ui


def main(workout_data):
    st.title("Overview")
    total_workouts = calculate_total_workouts(workout_data)
    average_duration = calculate_average_duration(workout_data)
    cols = st.columns(3)
    with cols[0]:
        ui.metric_card(title="Total Workouts", content=total_workouts, key="card1")
    with cols[1]:
        ui.metric_card(title="Average Workout Time", content=average_duration, key="card2")
    with cols[2]:
        ui.metric_card(title="Longest Streak in weeks", content="longest_streak", key="card3")
    return 
    
# Function to calculate total workouts
def calculate_total_workouts(workout_data: pd.DataFrame) -> str:
    return str(workout_data['start_time'].nunique())

# Function to calculate average workout duration
def calculate_average_duration(workout_data: pd.DataFrame) -> str:
    copied_workout_data = workout_data.copy()
    filtered_workout_data = copied_workout_data.drop_duplicates(subset=['start_time'])
    list_of_duration_minutes = (filtered_workout_data['end_time'] - filtered_workout_data['start_time']).dt.total_seconds() / 60
    average_duration = list_of_duration_minutes.mean()
    return f"{round(average_duration)} min"