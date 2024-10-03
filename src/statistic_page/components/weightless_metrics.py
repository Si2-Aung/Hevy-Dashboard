import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards



def create_weightless_metrics(excercise_filtered_data: pd.DataFrame):
    colss = st.columns(4)
    with colss[0]:
        st.metric(label="Total Workout done", value="weightless")
    with colss[1]:
        st.metric(label="⌀ Workout Time", value="weightless")
    with colss[2]:
        st.metric(label="Longest Streak", value="weightless")
    with colss[3]:
        st.metric(label="Most trained in a week", value="weightless")
    style_metric_cards("#FFF", 1, "#CCCCCC", 10, "#008DFF",True)
    return