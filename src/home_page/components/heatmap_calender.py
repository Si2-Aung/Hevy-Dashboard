import streamlit as st
import calmap
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def create_custom_colormap():
    # Create a color map that goes from white to your desired color
    colors = ["#FFB6C1", "#FF4B4B"]  # Start from white and go to #FF4B4B
    cmap = LinearSegmentedColormap.from_list("custom_heatmap", colors)
    return cmap

def limit_to_a_year(worktout_data : pd.DataFrame):
    data_copy = worktout_data.copy()
    most_recent_date = data_copy['start_time'].max()
    one_year_ago = most_recent_date - pd.DateOffset(years=1)   
     # Filter the dataframe for rows where the date is between one year ago and the current date
    limit_dataset = data_copy[(data_copy['start_time'] >= one_year_ago) & (data_copy['start_time'] <= most_recent_date)]
    return limit_dataset

def create_heatmap_data(workout_data : pd.DataFrame):
    # Create a new column for the date only (no time)
    workout_data['training_date'] = workout_data['start_time'].dt.date

    training_counts = workout_data.groupby('training_date').size()
    # Convert to a pandas Series for the heatmap (index as date)
    training_series = pd.Series(training_counts, index=pd.to_datetime(training_counts.index))
    return training_series

def create_heatmap(training_series : pd.Series, year):
    st.subheader("Training Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    cmap = create_custom_colormap()
    calmap.yearplot(training_series, year=year, ax=ax, cmap=cmap)

    # Display the heatmap in Streamlit
    st.pyplot(fig)


def main(worktout_data : pd.DataFrame):
    data_copy = worktout_data.copy()
    limited_WK = limit_to_a_year(data_copy)
    training_series = create_heatmap_data(limited_WK)
    create_heatmap(training_series,worktout_data['start_time'].max().year)

