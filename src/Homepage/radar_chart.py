import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Homepage.excercises import EXERCISE_MAPPING

def process_file():
    # Reverse the mapping for easier lookup
    reverse_exercise_category = {exercise: category for category, exercises in EXERCISE_MAPPING.items() for exercise in exercises}
    return reverse_exercise_category

def calculate_stats_for_chart(workout_data: pd.DataFrame,excercise_category: dict):
    workout_data.loc[:,'date'] = workout_data['start_time'].dt.date
    workout_data = workout_data.drop_duplicates(subset=['date', 'exercise_title']).copy()
    # Map exercises to categories
    workout_data.loc[:, 'category'] = workout_data['exercise_title'].map(excercise_category)
    # Aggregate the count of unique exercises per category
    category_summary = workout_data['category'].value_counts().reindex(EXERCISE_MAPPING.keys(), fill_value=0)
    return category_summary

def create_radar_chart(stats):
    labels = create_labels()

    num_vars = len(labels)
    # Winkel für die Diagrammberechnung
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Der Radarplot soll rund sein, also müssen wir die Liste schließen
    stats = np.concatenate((stats, [stats.iloc[0]]))  # Verwendung von iloc
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    
    # Füllfarbe auf kräftiges Dunkelblau setzen
    ax.fill(angles, stats, alpha=1, color="#E0FFFF", edgecolor="#2596be", linewidth=1.5)

    # Schönheitsverbesserungen
    ax.set_yticklabels([])  # Remove radial labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Remove the radial grid lines
    ax.set_rgrids([])

    # Remove the outer circle
    ax.spines['polar'].set_visible(False)

    # Ändern der Farbe der äußeren Linien zu einer helleren Farbe
    ax.xaxis.grid(True, color='black', linestyle='--', linewidth=1.5)

    return fig

def create_labels():
    return ['Core', 'Leg', 'Arms', 'Back', 'Cardio', 'Chest', "Shoulders"]


