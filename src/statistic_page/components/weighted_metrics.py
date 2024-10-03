import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards


def create_weighted_metrics(excercise_filtered_data: pd.DataFrame):
    heaviest_weight_value = heaviest_weight(excercise_filtered_data)
    best_1rpm_value = best_1rpm(excercise_filtered_data)

    set_volume_added_data = add_set_volume_column(excercise_filtered_data)
    best_set_volume_value = best_set_volume(set_volume_added_data)
    #best_session_volume_value = best_session_volume(set_volume_added_data)

    colss = st.columns(3)
    with colss[0]:
        st.metric(label="Heaviest Weight", value=heaviest_weight_value)
    with colss[1]:
        st.metric(label="Best 1RPM", value=best_1rpm_value)
    with colss[2]:
        st.metric(label="Best set Volume", value=best_set_volume_value)
    style_metric_cards("#FFF", 1, "#CCCCCC", 10, "#008DFF",True)
    return

def heaviest_weight(df):
    heaviest_weight = round(df['weight_kg'].max())
    return str(heaviest_weight) + " kg"

def best_1rpm(excercise_filtered_data):
    df = excercise_filtered_data.copy()
    df['1rm'] = df['weight_kg'] * (1 + df['reps'] / 30)
    best_1rpm = round(df['1rm'].max())
    return f"{best_1rpm} kg"

def best_set_volume(set_volume_added_data):
    # Get the index of the row with the maximum set volume
    idx_max_volume = set_volume_added_data['set_volume'].idxmax()
    
    best_weight = round(set_volume_added_data.loc[idx_max_volume, 'weight_kg'])
    best_reps = round(set_volume_added_data.loc[idx_max_volume, 'reps'])
    return f"{best_reps} x {best_weight} kg"

#def best_session_volume(set_volume_added_data):
    session_volumes = set_volume_added_data.groupby('start_time')['set_volume'].sum()
    best_session_volume = round(session_volumes.max())
    return str(best_session_volume) + " kg"

def add_set_volume_column(excercise_filtered_data):
    df = excercise_filtered_data.copy()
    df['set_volume'] = df['weight_kg'] * df['reps']
    return df
