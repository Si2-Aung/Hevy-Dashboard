import pytest
import pandas as pd
import src.utils.data_cleaning as dc

setUp = {
        'title': ['Push', 'Push'],
        'start_time': ['18 May 2024, 13:22', '18 May 2024, 13:22'],
        'end_time': ['18 May 2024, 14:12', '18 May 2024, 14:12'],
        'description': ['desc1', 'desc2'],
        'superset_id': [None, None],
        'exercise_notes': [None, None],
        'set_index': [0, 0],
        'set_type': ['normal', 'normal'],
        'weight_kg': ['30.0', '50.0'],
        'reps': ['10', '12'],
        'distance_km': [None, None],
        'duration_seconds': [None, None],
        'rpe': [None, None]
        }
setup_df = pd.DataFrame(setUp)


def test_input_type():
     with pytest.raises(ValueError):
        dc.clean("This is not a dataframe")

def test_remove_unnecessary_columns():
    cleaned_data = dc.clean(setup_df.copy())
    expected_columns = ['title', 'start_time', 'end_time','set_index', 'weight_kg', 'reps', 'distance_km', 'duration_seconds']
    assert set(expected_columns) == set(cleaned_data.columns), f"Expected columns {expected_columns}, but got {cleaned_data.columns}"

def test_date_conversion():
    cleaned_data = dc.clean(setup_df.copy())
    assert pd.api.types.is_datetime64_any_dtype(cleaned_data['start_time']), "start_time is not a datetime"
    assert pd.api.types.is_datetime64_any_dtype(cleaned_data['end_time']), "end_time is not a datetime"

def test_numeric_conversion():
    cleaned_data = dc.clean(setup_df.copy())
    numeric_columns = ['weight_kg', 'reps', 'distance_km', 'duration_seconds']
    for col in numeric_columns:
        assert pd.api.types.is_numeric_dtype(cleaned_data[col]), f"{col} is not numeric"
