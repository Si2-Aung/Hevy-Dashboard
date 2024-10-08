import streamlit_antd_components as stac
from src.statistic_page.components.line_chart_generator import create_line_chart


def create_duration_distance_graph(excercise_filtered_data):
    selected_graph = create_graph_selection(   
        buttons_data = [{'label': 'Best Pace'},{'label': 'Longest Distance'},{'label': 'Total Time'},])
    
    if selected_graph == 'Best Pace':
        excercise_filtered_data['best_pace'] = round((excercise_filtered_data['duration_seconds'] / excercise_filtered_data['distance_km']) / 60, 2)
        best_pace_data = excercise_filtered_data.groupby('start_time')['best_pace'].min().reset_index()
        create_line_chart(best_pace_data, 'best_pace', 'Best Pace km/min', 1)

    elif selected_graph == 'Longest Distance':
        longest_distance_data = excercise_filtered_data.groupby('start_time')['distance_km'].max().reset_index()
        create_line_chart(longest_distance_data, 'distance_km', 'Longest Distance (km)', 1)

    elif selected_graph == 'Total Time':
        total_time_data = excercise_filtered_data.groupby('start_time')['duration_seconds'].sum().reset_index()
        create_line_chart(total_time_data, 'duration_seconds', 'Total Time (Min)', 50)
    return

def create_duration_only_graph(excercise_filtered_data):
    selected_graph = create_graph_selection(
        buttons_data = [{'label': 'Total Time'},{'label': 'Best Time'},])
    
    if selected_graph == 'Total Time':
        total_time_data = excercise_filtered_data.groupby('start_time')['duration_seconds'].sum().reset_index()
        create_line_chart(total_time_data, 'duration_seconds', 'Total Time (Sec)', 50)

    elif selected_graph == 'Best Time':
        best_time_data = excercise_filtered_data.groupby('start_time')['duration_seconds'].max().reset_index()
        create_line_chart(best_time_data, 'duration_seconds', 'Best Time (Sec)', 1)
    return

def create_reps_graph(excercise_filtered_data):
    selected_graph = create_graph_selection(
        buttons_data = [{'label': 'Session Reps'},{'label': 'Most Reps (Set)'},])
    
    if selected_graph == 'Session Reps':
        total_reps_data = excercise_filtered_data.groupby('start_time')['reps'].sum().reset_index()
        create_line_chart(total_reps_data, 'reps', 'Session Reps', 3)

    elif selected_graph == 'Most Reps (Set)':
        most_reps_data = excercise_filtered_data.groupby('start_time')['reps'].max().reset_index()
        create_line_chart(most_reps_data, 'reps', 'Most Reps (Set)', 1)
    return


def create_graph_selection(buttons_data: list):
    buttons_items = [stac.ButtonsItem(label=button['label'], icon='bar-chart') for button in buttons_data]
    return stac.buttons(buttons_items, label='', align='left', color='blue')


    