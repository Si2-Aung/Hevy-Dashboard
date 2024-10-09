import plotly.express as px
import pandas as pd
import streamlit as st

def create_line_chart(data: pd.DataFrame, y_column: str, y_label: str, min_max_adjustment: int):
    # Create an interactive line chart using Plotly
    fig = px.line(data, 
                  x=data.index,  
                  y=y_column,  
                  markers=True,
                  labels={'x': 'Index', y_column: y_label}) 
    
    # Adjust y-axis range
    min_value = data[y_column].min() - min_max_adjustment
    max_value = data[y_column].max() + min_max_adjustment

    fig.update_traces(
        customdata=data['start_time'].dt.strftime('%d-%m-%Y'), 
        hovertemplate=f'Date: %{{customdata}}<br>{y_label}: %{{y}}'
    )
    # Update layout for a modern look
    tick_interval = max(1, len(data) // 18)  
    fig.update_layout(
        xaxis=dict(
            tickmode='array',  
            tickvals=data.index[::tick_interval], 
            ticktext=data['start_time'].dt.strftime('%d-%m-%Y')[::tick_interval],
            tickangle=45
        ),  
        xaxis_title=None, yaxis_title=y_label,  # Dynamic y-axis title
        yaxis=dict(range=[min_value , max_value ]),  # Set min below the lowest value and add space above max
        plot_bgcolor='white',
        margin=dict(t=30, b=50, l=10, r=10)
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=False)