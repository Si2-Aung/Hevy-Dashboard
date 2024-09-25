import pytest
import pandas as pd
from datetime import datetime
import src.home_page.components.calender_calculator as calender_calculator
# Sample workout data for tests
@pytest.fixture
def sample_workout_data():
    data = {
        'start_time': [
            datetime(2023, 7, 1, 8, 30),  # July
            datetime(2023, 7, 3, 9, 15),  # July
            datetime(2023, 7, 5, 10, 0),  # July
            datetime(2023, 8, 1, 7, 0),   # August
            datetime(2023, 8, 3, 6, 30),  # August
            datetime(2023, 8, 5, 8, 0),   # August
        ]
    }
    return pd.DataFrame(data)

# Test prepare_dataframe function
def test_prepare_dataframe(sample_workout_data):
    result = calender_calculator.prepare_dataframe(sample_workout_data)
    
    # Check that workout_month column is added and the type is correct
    assert 'workout_month' in result.columns
    assert result['workout_month'].dtype.name == 'period[M]'
    
    # Check if the workout_month values are correct
    assert result.iloc[0]['workout_month'] == pd.Period('2023-07', freq='M')
    assert result.iloc[-1]['workout_month'] == pd.Period('2023-08', freq='M')

# Test find_month_with_most_workouts function
def test_find_month_with_most_workouts(sample_workout_data):
    workout_time = calender_calculator.prepare_dataframe(sample_workout_data)
    most_workouts_month = calender_calculator.find_month_with_most_workouts(workout_time)
    
    # Check if the month with the most workouts is July (2023-07)
    assert most_workouts_month == pd.Period('2023-07', freq='M')

# Test get_training_days_of_month function
def test_get_training_days_of_month(sample_workout_data):
    workout_time = calender_calculator.prepare_dataframe(sample_workout_data)
    most_workouts_month = pd.Period('2023-07', freq='M')
    
    # Get training days for July 2023
    training_days = calender_calculator.get_training_days_of_month(workout_time, most_workouts_month)
    
    # Check if the training days are correctly identified
    assert set(training_days) == {1, 3, 5}

