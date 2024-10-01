import streamlit as st


def main(workout_data):
    initialize_session_state()
    
    # Display selection widgets and capture the user selections
    selected_timeframe, selected_category, selected_exercise = display_selection(workout_data)
    
    # Update the session state based on new user selections
    update_session_state(selected_timeframe, selected_category, selected_exercise)

    return


def initialize_session_state():
    st.session_state.setdefault('selected_category', "All Muscles")
    st.session_state.setdefault('selected_timeframe', "Last 3 months")
    st.session_state.setdefault('selected_exercise', None)


def update_session_state(selected_timeframe, selected_category, selected_exercise):
    state_changed = False

    if selected_timeframe != st.session_state.selected_timeframe:
        st.session_state.selected_timeframe = selected_timeframe
        state_changed = True

    if selected_category != st.session_state.selected_category: 
        st.session_state.selected_category = selected_category
        state_changed = True

    if selected_exercise != st.session_state.selected_exercise:
        st.session_state.selected_exercise = selected_exercise
        state_changed = True

    if state_changed:
        st.experimental_rerun()


def display_selection(workout_data):
    columns = st.columns(2)

    with columns[0]:
        category_options = ["All Muscles", "Abdominals", "Abductors", "Adductors", "Biceps", "Lower Back", 
                            "Upper Back", "Cardio", "Chest", "Calves", "Forearms", "Glutes", "Hamstrings", 
                            "Lats", "Quadriceps", "Shoulders", "Triceps", "Traps", "Neck", "Full Body"]
        selected_category = st.selectbox("Select a Muscle group", category_options)

    with columns[1]:
        time_options = ["Last 3 months", "Last 6 months", "Last year", "All time"]
        selected_timeframe = st.selectbox("Select a Timeframe", time_options)

    exercise_options = filter_data_by_category(workout_data, selected_category)
    selected_exercise = st.selectbox("Select an Exercise", exercise_options)

    return selected_timeframe, selected_category, selected_exercise


def filter_data_by_category(workout_data, selected_category):
    if selected_category == "All Muscles":
        return workout_data['exercise_title'].unique()
    else:
        return ["Sample Exercise 1", "Sample Exercise 2", "Specific to category exercises"]
