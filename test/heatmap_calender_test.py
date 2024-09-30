import pandas as pd
from datetime import datetime
from src.home_page.components.heatmap_calender import limit_to_a_year, create_heatmap_data, create_heatmap

def test_limit_to_a_year():
    data = {
        'start_time': [
            datetime(2023, 9, 25), 
            datetime(2022, 10, 1), 
            datetime(2022, 6, 15), 
            datetime(2023, 3, 10), 
            datetime(2021, 12, 25)  # Outside one year range
        ]
    }
    
    df = pd.DataFrame(data)
    
    filtered_df = limit_to_a_year(df)
    
    assert len(filtered_df) == 3  # Only 3 entries should remain
    assert filtered_df['start_time'].max() == datetime(2023, 9, 25)  # Max date should be the latest
    assert filtered_df['start_time'].min() == datetime(2022, 10, 1)  # Min date within the last year

def test_create_heatmap_data():
    data = {
        'start_time': [
            pd.Timestamp('2023-09-25 10:00:00'), 
            pd.Timestamp('2023-09-25 12:00:00'), 
            pd.Timestamp('2023-09-26 10:00:00')
        ]
    }
    
    df = pd.DataFrame(data)
    
    heatmap_data = create_heatmap_data(df)
    
    assert isinstance(heatmap_data, pd.Series)
    assert heatmap_data['2023-09-25'] == 2  # Two training sessions on 2023-09-25
    assert heatmap_data['2023-09-26'] == 1  # One training session on 2023-09-26

