import streamlit as st
import pandas as pd
def filter_data_by_limitation_value(workout_data, limitation_value):
    if limitation_value == 0:
        return workout_data
    else:
        latest_date = workout_data['start_time'].max()
        start_date = latest_date - pd.DateOffset(months=limitation_value)
        workout_data = workout_data.loc[workout_data['start_time'] >= start_date]
        return workout_data
    
    
def get_limitation_value(max_months_available):
    limitation_value = st.slider(
        label="Amount of months to take into account, 0 = all!",
        min_value=0,
        max_value=min(12, max_months_available),
        value=0,  # Standardwert
        step=1,  # Schrittweite
    )
    return limitation_value