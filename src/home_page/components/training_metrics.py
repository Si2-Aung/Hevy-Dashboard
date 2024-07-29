import pandas as pd

# Function to calculate total workouts
def calculate_total_workouts(workout_data: pd.DataFrame) -> str:
    return str(workout_data['start_time'].nunique())

# Function to calculate average workout duration
def calculate_average_duration(workout_data: pd.DataFrame) -> str:
    copied_workout_data = workout_data[['start_time', 'end_time']]
    filtered_workout_data = copied_workout_data.drop_duplicates(subset=['start_time'])
    list_of_duration = (filtered_workout_data['end_time'] - filtered_workout_data['start_time']).dt.total_seconds() / 60
    average_duration = list_of_duration.mean()
    return f"{round(average_duration)} min"

# Function to prepare the dataframes for calculating the longest streak
def prepare_df_for_streak_calculation(workout_data: pd.DataFrame) -> pd.DataFrame:
    workout_times  = workout_data[["start_time"]].drop_duplicates()
    workout_times['start_time'] = pd.to_datetime(workout_times ['start_time'])
    workout_times['year'] = workout_times['start_time'].dt.isocalendar().year
    workout_times['week'] = workout_times['start_time'].dt.isocalendar().week
    
    # Group by year and week and count the occurrences in each week
    weekly_workouts = workout_times.groupby(['year', 'week']).size().reset_index(name='count')
    return weekly_workouts

# Function to calculate the longest streak counted in weeks
def calculate_longest_streak(prepared_df: pd.DataFrame) -> str:
    max_streak = 0
    current_streak = 0
    previous_week = None
    
    for _, row in prepared_df.iterrows():
        year, week = row['year'], row['week']
        if (previous_week is None or 
            (year == previous_week[0] and week == previous_week[1] + 1) or 
            (year == previous_week[0] + 1 and week == 1 and previous_week[1] == 52)):
            current_streak += 1
        else:
            current_streak = 1
        max_streak = max(max_streak, current_streak)
        previous_week = (year, week)
    
    return f"{max_streak}"

# Function to calculate the most trained sessons in a week
def calculate_weekly_streak(prepared_df: pd.DataFrame):
    return f"{prepared_df['count'].max()}"