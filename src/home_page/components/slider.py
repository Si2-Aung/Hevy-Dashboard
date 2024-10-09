import streamlit as st
import pandas as pd

def limit_dataset(workout_data):
    max_months_available = (workout_data['start_time'].max() - workout_data['start_time'].min()).days // 30
    limit_value= get_limitation_value(max_months_available)
    limited_workout_data = filter_data_by_limitation_value(workout_data, limit_value)
    return limited_workout_data

def filter_data_by_limitation_value(workout_data, limitation_value):
    limit_dataset = workout_data.copy()
    if limitation_value == 0:
        return limit_dataset
    else:
        latest_date = limit_dataset['start_time'].max()
        start_date = latest_date - pd.DateOffset(months=limitation_value)
        limit_dataset = limit_dataset.loc[limit_dataset['start_time'] >= start_date]
        return limit_dataset
    
    
def get_limitation_value(max_months_available):
    limitation_value = st.slider(
        label="Amount of months to take into account, 0 = all!",
        min_value=0,
        max_value=min(12, max_months_available),
        value=0,  # Standardwert
        step=1,  # Schrittweite
    )
    return limitation_value