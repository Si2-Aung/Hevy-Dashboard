import streamlit_antd_components as stac
import pandas as pd
from src.statistic_page.components.line_chart_generator import create_line_chart


def create_graph(excercise_filtered_data):
    selected_graph = get_graph_selection()

    if selected_graph == 'Heaviest weight':
        heaviest_weight_data = prepare_heaviest_weight_data(excercise_filtered_data)
        create_line_chart(heaviest_weight_data, 'weight_kg', 'Heaviest Weight', 1)

    elif selected_graph == 'Session Volume':
        set_volume_data = prepare_session_volume_data(excercise_filtered_data)
        create_line_chart(set_volume_data, 'session_volume', 'Session Volume', 100)

    elif selected_graph == 'Total Reps':
        reps_count_data = prepare_reps_count_data(excercise_filtered_data)
        create_line_chart(reps_count_data, 'reps', 'Total Reps', 3)

    elif selected_graph == 'One Rep Max':
        one_rep_max_data = prepare_one_rep_max_data(excercise_filtered_data)
        create_line_chart(one_rep_max_data, '1rm', 'One Rep Max', 1)
    return None

def prepare_heaviest_weight_data(data: pd.DataFrame) -> pd.DataFrame:
    copy_data = data.copy()
    copy_data['weight_kg'] = copy_data['weight_kg'].fillna(0)
    return copy_data.groupby('start_time')['weight_kg'].max().reset_index()
    
def prepare_session_volume_data(data: pd.DataFrame) -> pd.DataFrame:
    copy_data = data.copy()
    copy_data['weight_kg'] = copy_data['weight_kg'].fillna(0)
    copy_data['session_volume'] = copy_data['weight_kg'] * copy_data['reps']
    return copy_data.groupby('start_time')['session_volume'].sum().reset_index()

def prepare_reps_count_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.groupby('start_time')['reps'].sum().reset_index()

def prepare_one_rep_max_data(data: pd.DataFrame) -> pd.DataFrame:
    one_rep_max_data = data.copy()
    one_rep_max_data['1rm'] = one_rep_max_data['weight_kg'] * (1 + one_rep_max_data['reps'] / 30)
    return one_rep_max_data.groupby('start_time')['1rm'].max().reset_index()

def get_graph_selection():
    return stac.buttons([
    stac.ButtonsItem(label='Heaviest weight', icon='bar-chart'),
    stac.ButtonsItem(label='Session Volume', icon='bar-chart'),
    stac.ButtonsItem(label='Total Reps', icon='bar-chart'),
    stac.ButtonsItem(label='One Rep Max', icon='bar-chart'),
    ], label='', align='left', color='blue')



