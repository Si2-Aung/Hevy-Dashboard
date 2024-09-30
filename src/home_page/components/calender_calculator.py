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
    <table style='border-collapse: collapse; width: 90%; background-color: #FFFFFF; color: black; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.15);'>
        <tr>
            <th colspan='7' style='text-align: center; font-size: 24px; background-color: #f0f2f6; color: black; padding: 10px 0;'>{month_name} {year}</th>
        </tr>
        <tr>
            {" ".join(f"<th style='padding: 10px; background-color: #f0f2f6; color: black;'>{day}</th>" for day in days)}
        </tr>
    """
    # Create table rows
    rows = ""
    for week in cal:
        row = "<tr>"
        for day in week:
            if day == 0:
                row += "<td style= padding: 10px; background-color: #white; text-align: center;'></td>"
            elif day in training_days:
                row += f"<td style=' padding: 10px; background-color: #FFB6C1; color: black; text-align: center;'>{day}</td>"
            else:
                row += f"<td style=' padding: 10px; background-color: #white; color: black;text-align: center;'>{day}</td>"
        row += "</tr>"
        rows += row
    
    # Combine header and rows
    table = header + rows + "</table>"
    return table
    

def main(workout_data):
    prepared_dataframe = prepare_dataframe(workout_data)

    most_workouts_month = find_month_with_most_workouts(prepared_dataframe)

    training_days = get_training_days_of_month(prepared_dataframe, most_workouts_month)

    most_workouts_year = most_workouts_month.year

    calender = build_calendar(most_workouts_year, most_workouts_month.month, training_days)

    return calender
    


