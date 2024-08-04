import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Define the stats
stats = {
    'Core': 73,
    'Leg': 223,
    'Arms': 241,
    'Back': 250,
    'Cardio': 4,
    'Chest': 211,
    'Shoulder': 105
}

def create_labels():
    return ['Core', 'Leg', 'Arms', 'Back', 'Cardio', 'Chest', 'Shoulders']

def create_radar_chart(stats):
    labels = create_labels()
    stats_values = list(stats.values())

    # Repeat the first value to close the loop
    stats_values += stats_values[:1]
    labels += labels[:1]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=stats_values,
        theta=labels,
        fill='toself',
        name='Stats',
        hoverinfo='r',
        line=dict(color='red')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=False),  # Hide radial grid lines
            angularaxis=dict(visible=True, showline=False, showticklabels=True)
        ),
        showlegend=False,
        template=None,
        title="Interactive Radar Chart Example",
        paper_bgcolor='white',  # Set background to white
        plot_bgcolor='white'    # Set plot background to white
    )

    return fig

# Create the radar chart
fig = create_radar_chart(stats)

# Display the chart in Streamlit
st.title("Interactive Radar Chart Example")
st.write("This is an example of an interactive radar chart created with Plotly and displayed using Streamlit.")
st.plotly_chart(fig, use_container_width=True)
