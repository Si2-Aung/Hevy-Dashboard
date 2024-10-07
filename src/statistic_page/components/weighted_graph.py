import streamlit_antd_components as stac
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


def main(excercise_filtered_data):
    create_cooler_buttons()
    heaviest_weight = prepare_data_heaviest_weight(excercise_filtered_data)
    create_modern_line_chart(heaviest_weight)
    

def create_cooler_buttons():
    stac.buttons([
    stac.ButtonsItem(label='Heaviest weight', icon='bar-chart'),
    stac.ButtonsItem(label='Session Volume', icon='bar-chart'),
    stac.ButtonsItem(label='Best set Volume', icon='bar-chart'),
    stac.ButtonsItem(label='One Rep Max', icon='bar-chart'),
    ], label='', align='left', color='blue')




def create_modern_line_chart(data: pd.DataFrame):
    # Create an interactive line chart using Plotly
    fig = px.line(data, 
                  x=data.index,  # Keep the index for even spacing
                  y='weight_kg', 
                  title='Weight Progress Over Time', 
                  markers=True,
                  labels={'x': 'Index', 'weight_kg': 'Weight'})  # Use 'Index' label for x
    
    # Get the minimum and maximum values for the y-axis
    min_weight = data['weight_kg'].min()
    max_weight = data['weight_kg'].max()

    # Update the figure with custom hover data (start_time as the custom data)
    fig.update_traces(
        customdata=data['start_time'].dt.strftime('%d-%m-%Y'), 
        hovertemplate='Date: %{customdata}<br>Weight: %{y} kg'
    )

    # Adjust the tickvals to show every nth label (adjust n to suit your data)
    size = max(1, len(data) // 18)  

    # Update layout for modern look
    fig.update_layout(
        xaxis=dict(tickmode='array', 
                   tickvals=data.index[::size], 
                   ticktext=data['start_time'].dt.strftime('%d-%m-%Y')[::size],
                   tickangle=45),  # Rotate the labels for better readability
        xaxis_title=None,
        yaxis_title="Weight (kg)",
        yaxis=dict(range=[min_weight - 1, max_weight + 1]),  # Set min below the lowest value and add space above max
        plot_bgcolor='white',
        hovermode='x unified',
        margin=dict(t=50, b=50, l=50, r=50)
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=False)

def prepare_data_heaviest_weight(data: pd.DataFrame) -> pd.DataFrame:
    copy_data = data.copy()
    copy_data['weight_kg'] = copy_data['weight_kg'].fillna(0)
    heaviest_weight = copy_data.groupby('start_time')['weight_kg'].max().reset_index()
    return heaviest_weight
    



