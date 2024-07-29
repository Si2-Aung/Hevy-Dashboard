import streamlit as st
import utils.slider as slider

def main(workout_data):
    limited_workout_data = slider.limit_dataset(workout_data)
    return

