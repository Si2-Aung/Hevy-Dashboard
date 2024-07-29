import streamlit as st
import Homepage.training_metrics as training_metrics
import Homepage.calender_calculator as calender_calculator
import Homepage.radar_chart as radar_chart
import Homepage.slider as slider
from streamlit_extras.metric_cards import style_metric_cards
import datetime
def main(workout_data):
    st.title("Overview")
    limited_workout_data = limit_dataset(workout_data)
    create_metrics(limited_workout_data)

    cols = st.columns(2)
    with cols[0]:
        st.subheader("Most tryhard month")
        create_calender(workout_data)
    with cols[1]:
        st.subheader("Focused muscle groups")
        create_radar_chart(limited_workout_data)
    

def create_metrics(workout_data):
    total_workouts = training_metrics.calculate_total_workouts(workout_data)

    average_duration = training_metrics.calculate_average_duration(workout_data)

    prepared_df = training_metrics.prepare_df_for_streak_calculation(workout_data)

    longest_streak = training_metrics.calculate_longest_streak(prepared_df)

    most_trained = training_metrics.calculate_weekly_streak(prepared_df)

    colss = st.columns(4)
    with colss[0]:
        st.metric(label="Total Workout done", value=total_workouts)
    with colss[1]:
        st.metric(label="⌀ Workout Time", value=average_duration)
    with colss[2]:
        st.metric(label="Longest Streak", value=longest_streak)
    with colss[3]:
        st.metric(label="Most trained in a week", value=most_trained)
    style_metric_cards("white", 1, "#CCCCCC", 10, "#FF6347",True)
    return

def create_calender(workout_data):
    prepared_dataframe = calender_calculator.prepare_dataframe(workout_data)

    most_workouts_month = calender_calculator.find_month_with_most_workouts(prepared_dataframe)

    training_days = calender_calculator.get_training_days_of_month(prepared_dataframe, most_workouts_month)

    most_workouts_year = most_workouts_month.year

    calender = calender_calculator.build_calendar(most_workouts_year, most_workouts_month.month, training_days)

    st.markdown(calender, unsafe_allow_html=True)
    return

def create_radar_chart(workout_data):
    excercise_category = radar_chart.process_file()

    chart_stats = radar_chart.calculate_stats_for_chart(workout_data,excercise_category)

    chart = radar_chart.create_radar_chart(chart_stats)
    
    st.pyplot(chart)
    return

def limit_dataset(workout_data):
    max_months_available = (workout_data['start_time'].max() - workout_data['start_time'].min()).days // 30

    limit_value= slider.get_limitation_value(max_months_available)

    limited_workout_data = slider.filter_data_by_limitation_value(workout_data, limit_value)

    return limited_workout_data