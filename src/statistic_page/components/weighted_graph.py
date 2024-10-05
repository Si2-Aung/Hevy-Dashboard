import streamlit_antd_components as stac
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def main(excercise_filtered_data):
    new_df = replace_nan_with_zero(excercise_filtered_data, 'weight_kg')
    create_cooler_buttons()
    create_chart(new_df)
    


def create_cooler_buttons():
    stac.buttons([
    stac.ButtonsItem(label='Heaviest weight', icon='bar-chart'),
    stac.ButtonsItem(label='Session Volume', icon='bar-chart'),
    stac.ButtonsItem(label='Best set Volume', icon='bar-chart'),
    stac.ButtonsItem(label='One Rep Max', icon='bar-chart'),
    ], label='', align='left',color='blue')

def create_chart(data: pd.DataFrame):
    session_weights = data.groupby('start_time')['weight_kg'].max().reset_index()

    # Plot the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(session_weights['start_time'], session_weights['weight_kg'], marker='o', linestyle='-', color='b')
    plt.title('Heaviest Weight per Session')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.grid(True)
    st.pyplot(plt)


def replace_nan_with_zero(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    # Ensure the column is modified correctly using .loc to avoid the warning
    df.loc[:, column_name] = df[column_name].fillna(0)
    return df