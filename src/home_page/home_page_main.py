import streamlit as st
from src.utils.load_css import load_css
from src.home_page.components import training_metrics
from src.home_page.components import calender_calculator
from src.home_page.components import radar_chart
from src.home_page.components import heatmap_calender
from src.home_page.components import slider

def create_metrics(workout_data):
    training_metrics.create_metrics(workout_data)
    return

def create_calender(workout_data):
    calender = calender_calculator.main(workout_data)
    st.markdown(calender, unsafe_allow_html=True)
    return

def create_radar_chart(workout_data):
    chart = radar_chart.main(workout_data)   
    st.pyplot(chart)
    return

def create_heatmap(workout_data):
    heatmap_calender.main(workout_data)
    return

def main(workout_data):
    load_css("assets/home_styles.css")
    limited_workout_data = slider.limit_dataset(workout_data)
    create_metrics(limited_workout_data)

    cols = st.columns(2)
    with cols[0]:
        st.subheader("Most trained month")
        create_calender(workout_data)
    with cols[1]:
        st.subheader("Focused muscle groups")
        create_radar_chart(limited_workout_data)

    create_heatmap(workout_data)
    return