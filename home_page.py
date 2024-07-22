import streamlit as st
import pandas as pd
import training_metrics
import streamlit_shadcn_ui as ui


def main(workout_data):
    st.title("Overview")
    create_metrics(workout_data)
    
def create_metrics(workout_data):
    total_workouts = training_metrics.calculate_total_workouts(workout_data)
    average_duration = training_metrics.calculate_average_duration(workout_data)
    prepared_df = training_metrics.prepare_df_for_streakcalculation(workout_data)
    longest_streak = training_metrics.calculate_longest_streak(prepared_df)
    most_trained = training_metrics.calculate_weekly_streak(prepared_df)
    cols = st.columns(4)
    with cols[0]:
        ui.metric_card(title="Total Workouts", content=total_workouts, key="card1")
    with cols[1]:
        ui.metric_card(title="Average Workout Time", content=average_duration, key="card2")
    with cols[2]:
        ui.metric_card(title="Longest Streak in weeks", content=longest_streak, key="card3")
    with cols[3]:
        ui.metric_card(title="Most trained in a week", content=most_trained, key="card4")
    return