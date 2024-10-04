import pandas as pd
from src.statistic_page.components import weighted_metrics
from src.statistic_page.components import weightless_metrics
import streamlit as st

def display_metrics(excercise_filtered_data: pd.DataFrame):
    if not excercise_filtered_data["weight_kg"].isna().all():
        weighted_metrics.create_weighted_metrics(excercise_filtered_data)
    
    elif not excercise_filtered_data["duration_seconds"].isna().all() and not excercise_filtered_data["distance_km"].isna().all():
        weightless_metrics.create_duration_distance_metrics(excercise_filtered_data)
    
    elif not excercise_filtered_data["duration_seconds"].isna().all() and excercise_filtered_data["distance_km"].isna().all():
        weightless_metrics.create_duration_only_metrics(excercise_filtered_data)

    elif not excercise_filtered_data["reps"].isna().all() and excercise_filtered_data["weight_kg"].isna().all() and excercise_filtered_data["duration_seconds"].isna().all() and excercise_filtered_data["distance_km"].isna().all():
        weightless_metrics.create_reps_metrics(excercise_filtered_data)

    else:
        st.warning("No data available for the selected filters.")
        return False

    return True

