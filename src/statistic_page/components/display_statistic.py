import pandas as pd
from src.statistic_page.components import weighted_metrics
from src.statistic_page.components import weightless_metrics
from src.statistic_page.components import weighted_graph
from src.statistic_page.components import weightless_graph 
import streamlit as st

def display(excercise_filtered_data: pd.DataFrame):
    has_weight = not excercise_filtered_data["weight_kg"].isna().all()
    has_duration = not excercise_filtered_data["duration_seconds"].isna().all()
    has_distance = not excercise_filtered_data["distance_km"].isna().all()
    has_reps = not excercise_filtered_data["reps"].isna().all()

    # Check conditions and act accordingly
    if has_weight:
        weighted_graph.create_graph(excercise_filtered_data)
        st.subheader("Achievements")
        weighted_metrics.create_weighted_metrics(excercise_filtered_data)

    elif has_duration and has_distance:
        weightless_graph.create_duration_distance_graph(excercise_filtered_data)
        weightless_metrics.create_duration_distance_metrics(excercise_filtered_data)

    elif has_duration and not has_distance:
        weightless_graph.create_duration_only_graph(excercise_filtered_data)
        weightless_metrics.create_duration_only_metrics(excercise_filtered_data)

    elif has_reps and not has_weight and not has_duration and not has_distance:
        weightless_graph.create_reps_graph(excercise_filtered_data)
        weightless_metrics.create_reps_metrics(excercise_filtered_data)

    else:
        st.warning("Either there is no data, or I didnt checked this case yet. Choose other options please. ^^")
        return False
    
    st.divider()
    cols = st.columns([9,1],gap="large",vertical_alignment="bottom")
    with cols[0]:
        st.subheader("Show raw data for the selected exercise")
    with cols[1]:
        toggle = st.toggle("toogle", key="show_data", label_visibility="collapsed")

    if toggle:
        st.dataframe(excercise_filtered_data)
    
    return True

