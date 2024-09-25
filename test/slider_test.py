import pandas as pd
from pandas.testing import assert_frame_equal
import src.utils.slider as slider  



def create_extended_mock_workout_data():
    data = {
        'start_time': [
            '01 Jan 2022, 12:00', '15 Feb 2022, 15:00', '01 Mar 2022, 09:30',
            '10 Apr 2022, 11:00', '01 May 2022, 14:00', '15 Jun 2022, 16:00',
            '01 Jul 2022, 10:00', '15 Aug 2022, 10:00', '01 Sep 2022, 12:00',
            '01 Oct 2022, 09:00', '15 Nov 2022, 13:00', '01 Dec 2022, 10:00',
            '15 Jan 2023, 14:00', '01 Feb 2023, 16:00', '01 Mar 2023, 09:00',
            '15 Apr 2023, 10:00', '01 May 2023, 14:00', '15 Jun 2023, 16:00',
        ]
    }
    workout_data = pd.DataFrame(data)
    workout_data['start_time'] = pd.to_datetime(workout_data['start_time'], format='%d %b %Y, %H:%M')
    return workout_data

def test_no_limitation():
    mock_workout_data = create_extended_mock_workout_data()
    # Test case where limitation_value is 0 
    limited_workout_data = slider.filter_data_by_limitation_value(mock_workout_data, 0)
    # Data should not be filtered, so it should match the mock_workout_data
    assert_frame_equal(limited_workout_data, mock_workout_data)


def test_3_month_limitation():
    mock_workout_data = create_extended_mock_workout_data()
    # Test case for a limitation of 3 months
    limited_workout_data = slider.filter_data_by_limitation_value(mock_workout_data, 3)

    expected_data = pd.DataFrame({
        'start_time': [
            '15 Apr 2023, 10:00', '01 May 2023, 14:00', '15 Jun 2023, 16:00',
        ]
    })
    expected_data['start_time'] = pd.to_datetime(expected_data['start_time'], format='%d %b %Y, %H:%M')

    # Reset the index for comparison
    limited_workout_data = limited_workout_data.reset_index(drop=True)
    expected_data = expected_data.reset_index(drop=True)

    # Compare the actual output with the expected data
    assert_frame_equal(limited_workout_data, expected_data)

def test_12_month_limitation():
    mock_workout_data = create_extended_mock_workout_data()
    # Test case for a limitation of 12 months

    limited_workout_data = slider.filter_data_by_limitation_value(mock_workout_data, 12)
    
    # Expected data: entries from 15 Aug 2022 - 01 Aug 2023
    expected_data = pd.DataFrame({
        'start_time': [

            '15 Jun 2022, 16:00', '01 Jul 2022, 10:00', '15 Aug 2022, 10:00', 
            '01 Sep 2022, 12:00', '01 Oct 2022, 09:00', '15 Nov 2022, 13:00', 
            '01 Dec 2022, 10:00', '15 Jan 2023, 14:00', '01 Feb 2023, 16:00',
            '01 Mar 2023, 09:00', '15 Apr 2023, 10:00', '01 May 2023, 14:00', 
            '15 Jun 2023, 16:00',
        ]
    })
    expected_data['start_time'] = pd.to_datetime(expected_data['start_time'], format='%d %b %Y, %H:%M')

    # Reset the index for comparison
    limited_workout_data = limited_workout_data.reset_index(drop=True)
    expected_data = expected_data.reset_index(drop=True)
    assert_frame_equal(limited_workout_data, expected_data)

