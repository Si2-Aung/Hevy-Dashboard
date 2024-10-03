import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards


def display_metric(label1: str, value1: str, label2: str, value2: str):
    colss = st.columns(2)
    with colss[0]:
        st.metric(label=label1, value=value1)
    with colss[1]:
        st.metric(label=label2, value=value2)
    style_metric_cards("#FFF", 1, "#CCCCCC", 10, "#008DFF",True)
    return

def format_duration(duration_in_sec: float) -> str:
    duration_in_min = duration_in_sec / 60
    if duration_in_min <= 2:
        return f"{int(duration_in_sec)} sec"
    else:
        minutes = int(duration_in_sec // 60)
        seconds = int(duration_in_sec % 60)
        return f"{minutes}:{seconds:02d} min"
    
def calculate_best_time_per_km(excercise_data: pd.DataFrame):
    running_data = excercise_data[excercise_data['exercise_title'] == 'Running']
    if running_data.empty or running_data['distance_km'].sum() == 0:
        return 0  
    running_data['time_per_km'] = running_data['duration_seconds'] / running_data['distance_km']
    return running_data['time_per_km'].min()

def create_duration_distance_metrics(excercise_filtered_data: pd.DataFrame):
    most_distance_value = str(excercise_filtered_data["distance_km"].max()) + " km"
    best_time_per_km = calculate_best_time_per_km(excercise_filtered_data)
    formatted_best_time_per_km = format_duration(best_time_per_km)

    display_metric("Furthest distance", most_distance_value, "Best Time per km", formatted_best_time_per_km)
    return

def create_duration_only_metrics(excercise_filtered_data: pd.DataFrame):
    longest_duration_in_sec = excercise_filtered_data["duration_seconds"].max()
    avg_duration_in_sec = excercise_filtered_data["duration_seconds"].mean()
   
    longest_duration = format_duration(longest_duration_in_sec)
    avg_duration = format_duration(avg_duration_in_sec)

    display_metric("Longest duration", longest_duration, "⌀ Average duration", avg_duration)
    return

def create_reps_metrics(excercise_filtered_data: pd.DataFrame):
    most_reps = round(excercise_filtered_data["reps"].max())
    avg_reps = round(excercise_filtered_data["reps"].mean())

    display_metric("Most reps", most_reps, "⌀ Average reps", avg_reps)
    return