import pandas as pd
from src.statistic_page.components.weighted_metrics import create_weighted_metrics
from src.statistic_page.components import weightless_metrics
import streamlit as st



def display_metrics(excercise_filtered_data: pd.DataFrame):
    # Check for the first case (weight present)
    if not excercise_filtered_data["weight_kg"].isna().all():
        create_weighted_metrics(excercise_filtered_data)
    
    # Check for the second case (both duration and distance present)
    elif not excercise_filtered_data["duration_seconds"].isna().all() and not excercise_filtered_data["distance_km"].isna().all():
        weightless_metrics.create_duration_distance_metrics(excercise_filtered_data)
    
    # Case where only duration is available, no distance
    elif not excercise_filtered_data["duration_seconds"].isna().all() and excercise_filtered_data["distance_km"].isna().all():
        weightless_metrics.create_duration_only_metrics(excercise_filtered_data)

    # Check for the third case (reps present, no weight, duration, or distance)
    elif not excercise_filtered_data["reps"].isna().all() and excercise_filtered_data["weight_kg"].isna().all() and excercise_filtered_data["duration_seconds"].isna().all() and excercise_filtered_data["distance_km"].isna().all():
        weightless_metrics.create_reps_metrics(excercise_filtered_data)

    # Fourth case (no weight, duration, distance, or reps)
    else:
        st.warning("No data available for the selected filters.")
        return False

    return True

