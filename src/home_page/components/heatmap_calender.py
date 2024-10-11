import streamlit as st
import calmap
import pandas as pd
import matplotlib.pyplot as plt
from src.utils.load_css import load_css
from matplotlib.colors import LinearSegmentedColormap

def create_custom_colormap():
    colors = ["#FFB6C1", "#FF4B4B"] 
    cmap = LinearSegmentedColormap.from_list("custom_heatmap", colors)
    return cmap

def limit_to_a_year(workout_data: pd.DataFrame, year: int):
    data_copy = workout_data.copy()
    start_date = pd.Timestamp(year=year, month=1, day=1)
    end_date = pd.Timestamp(year=year, month=12, day=31)
    limit_dataset = data_copy[(data_copy['start_time'] >= start_date) & (data_copy['start_time'] <= end_date)]
    return limit_dataset

def create_heatmap_data(workout_data: pd.DataFrame):
    # Create a new column for the date only (no time)
    workout_data['training_date'] = workout_data['start_time'].dt.date
    training_counts = workout_data.groupby('training_date').size()
    # Convert to a pandas Series for the heatmap (index as date)
    training_series = pd.Series(training_counts, index=pd.to_datetime(training_counts.index))
    return training_series

def create_heatmap(training_series: pd.Series, year: int):
    tranied_days = training_series.count()
    st.subheader(f"Training Heatmap ({tranied_days} days trained in {year})")
    fig, ax = plt.subplots(figsize=(10, 6))
    cmap = create_custom_colormap()
    calmap.yearplot(training_series, year=year, ax=ax, cmap=cmap)
    st.pyplot(fig)

def update_session_year(direction: str, min_year: int, max_year: int):
    if direction == "backward" and st.session_state.current_year > min_year:
        st.session_state.current_year -= 1
    elif direction == "forward" and st.session_state.current_year < max_year:
        st.session_state.current_year += 1

def create_buttons(min_year: int, max_year: int):
    cols = st.columns(2)
    with cols[0]:
        st.button("⬅ Last Year", on_click=update_session_year, args=("backward", min_year, max_year),
                  disabled=st.session_state.current_year == min_year)
    with cols[1]:
        st.button("Next Year ➡", on_click=update_session_year, args=("forward", min_year, max_year),
                  disabled=st.session_state.current_year == max_year)

def main(workout_data: pd.DataFrame):
    load_css("assets/home_styles.css")
    min_year = workout_data['start_time'].min().year
    max_year = workout_data['start_time'].max().year

    if 'current_year' not in st.session_state:
        st.session_state.current_year = max_year

    # Filter the data for the current year in session state
    limited_WK = limit_to_a_year(workout_data, st.session_state.current_year)
    training_series = create_heatmap_data(limited_WK)
    create_heatmap(training_series, st.session_state.current_year)
    create_buttons(min_year, max_year)

