import streamlit_antd_components as stac
import streamlit as st

def main():
    create_cooler_buttons()


def create_cooler_buttons():
    stac.buttons([
    stac.ButtonsItem(label='Heaviest weight', icon='bar-chart'),
    stac.ButtonsItem(label='Session Volume', icon='bar-chart'),
    stac.ButtonsItem(label='Best set Volume', icon='bar-chart'),
    stac.ButtonsItem(label='One Rep Max', icon='bar-chart'),
    ], label='', align='left',color='blue')