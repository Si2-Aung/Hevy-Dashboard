import pandas as pd

def clean(workoutdata):
    if not isinstance(workoutdata, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    removed_wkd = remove_unnecessary_columns(workoutdata)
    convert_data_types(removed_wkd)
    
    return removed_wkd

def remove_unnecessary_columns(workoutdata):
    columns_to_remove = ['rpe', 'description', 'superset_id', 'exercise_notes', 'set_type']
    clean_wkd = workoutdata.drop(columns=columns_to_remove, errors='ignore')
    return clean_wkd

def convert_data_types(workoutdata):
    # Convert date columns to datetime objects
    date_columns = ['start_time', 'end_time']
    date_format = "%d %b %Y, %H:%M"
    for col in date_columns:
        workoutdata[col] = pd.to_datetime(workoutdata[col], format=date_format, errors='coerce')
    
    # Ensure numerical columns are in the correct numeric format
    numeric_columns = ['weight_kg', 'reps', 'distance_km', 'duration_seconds']
    for col in numeric_columns:
        workoutdata[col] = pd.to_numeric(workoutdata[col], errors='coerce')
    