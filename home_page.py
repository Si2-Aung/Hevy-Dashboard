import streamlit as st
import pandas as pd
import data_cleaning as dc
import streamlit_shadcn_ui as ui


def main(workout_data):
    st.title("Overview")
    cols = st.columns(3)
    with cols[0]:
        ui.metric_card(title="Total Workouts", content="total_workouts", key="card1")
    with cols[1]:
        ui.metric_card(title="Average Workout Time", content="average_duration", key="card2")
    with cols[2]:
        ui.metric_card(title="Longest Streak in weeks", content="longest_streak", key="card3")
    return 
    

def calculate_total_workouts(workout_data):
    return str(workout_data['start_time'].nunique())
