import streamlit_antd_components as stac
import streamlit as st
import plotly.express as px
import pandas as pd


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


def create_line_chart(data: pd.DataFrame, y_column: str, y_label: str, min_max_adjustment: int):
    # Create an interactive line chart using Plotly
    fig = px.line(data, 
                  x=data.index,  
                  y=y_column,  
                  title=f'{y_label} Progress Over Time', 
                  markers=True,
                  labels={'x': 'Index', y_column: y_label}) 
    
    # Adjust y-axis range
    min_value = data[y_column].min() - min_max_adjustment
    max_value = data[y_column].max() + min_max_adjustment

    fig.update_traces(
        customdata=data['start_time'].dt.strftime('%d-%m-%Y'), 
        hovertemplate=f'Date: %{{customdata}}<br>{y_label}: %{{y}}'
    )
    # Update layout for a modern look
    tick_interval = max(1, len(data) // 18)  
    fig.update_layout(
        xaxis=dict(
            tickmode='array',  
            tickvals=data.index[::tick_interval], 
            ticktext=data['start_time'].dt.strftime('%d-%m-%Y')[::tick_interval],
            tickangle=45
        ),  
        xaxis_title=None, yaxis_title=y_label,  # Dynamic y-axis title
        yaxis=dict(range=[min_value , max_value ]),  # Set min below the lowest value and add space above max
        plot_bgcolor='white', hovermode='x unified',
        margin=dict(t=50, b=50, l=20, r=10)
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=False)


