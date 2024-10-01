import pandas as pd
import src.statistic_page.components.excercises_categorized  as ec

def main(workout_data: pd.DataFrame, selected_timeframe: str, selected_category: str):
    colum_added_data = add_category_column(workout_data)
    time_filtered_data = filter_data_by_timeframe(colum_added_data, selected_timeframe)
    category_filtered_data = filter_data_by_category(time_filtered_data, selected_category)
    return category_filtered_data

def filter_data_by_timeframe(colum_added_data: pd.DataFrame, selected_timeframe: str):
    workout_data_filtered = colum_added_data.copy()
    current_date = colum_added_data["start_time"].max()

    if selected_timeframe == 'Last 3 months':
        workout_data_filtered = workout_data_filtered[workout_data_filtered['start_time'] > current_date - pd.DateOffset(months=3)]
    elif selected_timeframe == 'Last 6 months':
        workout_data_filtered = workout_data_filtered[workout_data_filtered['start_time'] > current_date - pd.DateOffset(months=6)]
    elif selected_timeframe == 'Last year':
        workout_data_filtered = workout_data_filtered[workout_data_filtered['start_time'] > current_date - pd.DateOffset(years=1)]

    return workout_data_filtered

def filter_data_by_category(workout_data: pd.DataFrame, selected_category: str):
    if selected_category == 'All Muscles':
        return workout_data['exercise_title'].unique()
    else:
        return workout_data[workout_data['category'] == selected_category]['exercise_title'].unique() #CHANGE THIS LATER


def add_category_column(workout_data: pd.DataFrame):
    colum_added_data = workout_data.copy()
    colum_added_data['category'] = 'custom'
    exercises = colum_added_data['exercise_title']
    for index, exercise in exercises.items():
        is_in_category = False
        for category in ec.EXERCISE_CATEGORIES:
            if exercise in ec.EXERCISE_CATEGORIES[category]:
                colum_added_data.at[index, 'category'] = category
                is_in_category = True
                break
        if not is_in_category:
            colum_added_data.at[index, 'category'] = 'custom'
    return colum_added_data

if __name__ == "__main__":
    main()