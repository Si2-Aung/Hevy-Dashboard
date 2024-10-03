import pandas as pd
from src.statistic_page.components.weighted_metrics import create_weighted_metrics
from src.statistic_page.components.weightless_metrics import create_weightless_metrics



def display_metrics(excercise_filtered_data: pd.DataFrame):

    if excercise_filtered_data["weight_kg"].isna().any():
        create_weightless_metrics(excercise_filtered_data)

    else:
        create_weighted_metrics(excercise_filtered_data)



