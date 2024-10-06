import streamlit_antd_components as stac
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd


def main(excercise_filtered_data):
    new_df = replace_nan_with_zero(excercise_filtered_data, 'weight_kg')
    create_cooler_buttons()
    create_modern_line_chart(new_df)
    

def create_cooler_buttons():
    stac.buttons([
    stac.ButtonsItem(label='Heaviest weight', icon='bar-chart'),
    stac.ButtonsItem(label='Session Volume', icon='bar-chart'),
    stac.ButtonsItem(label='Best set Volume', icon='bar-chart'),
    stac.ButtonsItem(label='One Rep Max', icon='bar-chart'),
    ], label='', align='left', color='blue')



def create_modern_line_chart(data: pd.DataFrame):
   return


def replace_nan_with_zero(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    # Replacing NaN values with 0 in the specified column
    df.loc[:, column_name] = df[column_name].fillna(0)
    return df



