import pandas as pd
import calendar

def prepare_dataframe(workout_data):
    workout_time = workout_data[['start_time']].copy()
    workout_time['workout_month'] = workout_time['start_time'].dt.to_period('M')
    return workout_time

# Function to calculate the month with the most workouts
def find_month_with_most_workouts(workout_time):
    grouped_workouts_per_month = workout_time.groupby('workout_month').size()
    most_trained_month = grouped_workouts_per_month.idxmax()
    return most_trained_month

# Function to get training days in the month with the most workouts
def get_training_days_of_month(workout_time, month):
    most_workouts_month_data = workout_time[workout_time['workout_month'] == month]
    training_days = most_workouts_month_data['start_time'].dt.day.unique().tolist()
    return training_days

# Function to create a calendar for a specific month and year
def build_calendar(year, month, training_days):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    
    # Create table header
    header = f"""
    <table style='border-collapse: collapse; width: 50%; background-color: white; color: black;'>
        <tr>
            <th colspan='7' style='text-align: center; font-size: 24px; background-color: #f0f2f6; border: 1px solid black;'>{month_name} {year}</th>
        </tr>
        <tr>
            {" ".join(f"<th style='border: 1px solid black; padding: 5px; background-color: white;'>{day}</th>" for day in days)}
        </tr>
    """
    # Create table rows
    rows = ""
    for week in cal:
        row = "<tr>"
        for day in week:
            if day == 0:
                row += "<td style='border: 1px solid black; padding: 10px; background-color: #white;'></td>"
            elif day in training_days:
                row += f"<td style='border: 1px solid black; padding: 10px; background-color: #FFB6C1; color: black;'>{day}</td>"
            else:
                row += f"<td style='border: 1px solid black; padding: 10px; background-color: #white; color: black;'>{day}</td>"
        row += "</tr>"
        rows += row
    
    # Combine header and rows
    table = header + rows + "</table>"
    return table