import pandas as pd
from pandas.testing import assert_frame_equal
import src.home_page.components.training_metrics as training_metrics

def create_extended_mock_workout_data():
    data = {
        'start_time': [
            '01 Jan 2022, 12:00', '15 Feb 2022, 15:00', '17 Feb 2022, 09:30',  # Two sessions in the same week
            '01 Mar 2022, 09:30', '10 Apr 2022, 11:00', '13 Apr 2022, 09:30',  # Two sessions in the same week
            '01 May 2022, 14:00', '15 Jun 2022, 16:00', '01 Jul 2022, 10:00',
            '15 Aug 2022, 10:00', '01 Sep 2022, 12:00', '01 Oct 2022, 09:00',
            '15 Nov 2022, 13:00', '01 Dec 2022, 10:00', '02 Dec 2022, 11:00',  # Two sessions in the same week
            '15 Jan 2023, 14:00', '01 Feb 2023, 16:00', '01 Mar 2023, 09:00',
            '15 Apr 2023, 10:00', '01 May 2023, 14:00', '15 Jun 2023, 16:00',
            '16 Jun 2023, 16:00', '17 Jun 2023, 16:00', '18 Jun 2023, 16:00'  # Three sessions in the same week
        ],
    }
    workout_data = pd.DataFrame(data)
    workout_data['start_time'] = pd.to_datetime(workout_data['start_time'], format='%d %b %Y, %H:%M')
    workout_data['end_time'] = workout_data['start_time'] + pd.Timedelta(minutes=52)
    return workout_data

def test_calculate_total_workouts():
    workout_data = create_extended_mock_workout_data()
    # Test case for the total number of workouts
    total_workouts = training_metrics.calculate_total_workouts(workout_data)
    # Expected output: 18 unique start times
    assert training_metrics.calculate_total_workouts(workout_data) == "24"


def test_calculate_average_duration():
    workout_data = create_extended_mock_workout_data()
    # Test case for the average workout duration
    average_duration = training_metrics.calculate_average_duration(workout_data)
    # Expected output: 55 min
    assert average_duration == "52 min"

def test_prepare_df_for_streak_calculation():
    workout_data = create_extended_mock_workout_data()
    # Test case for preparing the dataframe for streak calculation
    prepared_df = training_metrics.prepare_df_for_streak_calculation(workout_data)
    prepared_df = prepared_df.astype({'year': 'int64', 'week': 'int64', 'count': 'int64'})


    # Expected output: a dataframe with the number of workouts in each week
    expected_data = {
        'year': [
            2021, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 
            2022, 2022, 2022, 2023, 2023, 2023, 2023, 2023, 2023
        ],
        'week': [
            52, 7, 9, 14, 15, 17, 24, 26, 33, 35, 39, 46, 
            48, 2, 5, 9, 15, 18, 24
        ],
        'count': [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4]
    }
    expected_df = pd.DataFrame(expected_data)

    assert_frame_equal(prepared_df, expected_df)

def test_calculate_longest_streak():
    workout_data = create_extended_mock_workout_data()
    prepared_df = training_metrics.prepare_df_for_streak_calculation(workout_data)
    # Test case for the longest streak
    longest_streak = training_metrics.calculate_longest_streak(prepared_df)
    # Expected output: 2 weeks
    assert longest_streak == "2"

def test_calculate_weekly_streak():
    workout_data = create_extended_mock_workout_data()
    prepared_df = training_metrics.prepare_df_for_streak_calculation(workout_data)
    # Test case for the most trained sessions in a week
    weekly_streak = training_metrics.calculate_weekly_streak(prepared_df)
    # Expected output: 2 sessions
    assert weekly_streak == "4"