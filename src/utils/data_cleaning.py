import pandas as pd
import streamlit as st

def get_cleaned_csv_file():
    workout_data = get_csv_file()
    if workout_data is not None:
        return clean(workout_data)

def get_csv_file():
    if 'uploaded_data' not in st.session_state:
        csv_file = st.file_uploader(" ", type="csv", label_visibility="collapsed", key="file_uploader")
        if csv_file is not None:
            st.success("Data uploaded successfully")
            st.session_state.uploaded_data = pd.read_csv(csv_file)
            st.rerun()
    else:
        return st.session_state.uploaded_data
    return None

def clean(workoutdata):
    if not isinstance(workoutdata, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    removed_wkd = remove_unnecessary_columns(workoutdata)
    cleaned_data = convert_data_types(removed_wkd)
    
    return cleaned_data

def remove_unnecessary_columns(workoutdata):
    columns_to_remove = ['rpe', 'description', 'superset_id', 'exercise_notes', 'set_type']
    clean_wkd = workoutdata.drop(columns=columns_to_remove, errors='ignore')
    return clean_wkd

def convert_data_types(workoutdata):
    cleaned_data = workoutdata.copy()
    # Convert date columns to datetime objects
    date_columns = ['start_time', 'end_time']
    date_format = "%d %b %Y, %H:%M"
    for col in date_columns:
        cleaned_data[col] = pd.to_datetime(cleaned_data[col], format=date_format, errors='coerce')
    
    # Ensure numerical columns are in the correct numeric format
    numeric_columns = ['weight_kg', 'reps', 'distance_km', 'duration_seconds']
    for col in numeric_columns:
        cleaned_data[col] = pd.to_numeric(cleaned_data[col], errors='coerce')

    return cleaned_data
    
    