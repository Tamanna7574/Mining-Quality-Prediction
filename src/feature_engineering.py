import pandas as pd

from .utils import convert_numeric_columns, convert_date


def create_features(df):

    df = df.copy()

    # preprocessing

    df = convert_date(df)
    df = convert_numeric_columns(df)

    df = df.sort_values("date").reset_index(drop=True)


    # =====================
    # Time Features
    # =====================

    df["hour"] = df["date"].dt.hour
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month



   # =============================
    # Advanced Rolling Features
    # =============================
    
    advanced_rolling_columns = [
        "% Iron Feed",
        "% Silica Feed",
        "Starch Flow",
        "Amina Flow",
        "Ore Pulp Flow",
        "Ore Pulp pH",
        "Ore Pulp Density",
    
        "Flotation Column 01 Air Flow",
        "Flotation Column 02 Air Flow",
        "Flotation Column 03 Air Flow",
        "Flotation Column 04 Air Flow",
        "Flotation Column 05 Air Flow",
        "Flotation Column 06 Air Flow",
        "Flotation Column 07 Air Flow"
    ]
    
    
    for col in advanced_rolling_columns:
    
        for window in [5,15]:
    
            df[f"{col}_rolling_mean_{window}"] = (
                df[col]
                .rolling(window)
                .mean()
            )
    
    
        df[f"{col}_rolling_std_15"] = (
            df[col]
            .rolling(15)
            .std()
        )



    # =====================
    # Lag Features
    # =====================


    lag_features = [

        "% Iron Feed",
        "% Silica Feed",
        "Starch Flow",
        "Amina Flow",
        "Ore Pulp Flow",
        "Ore Pulp pH",
        "Ore Pulp Density",

        "Flotation Column 01 Air Flow",
        "Flotation Column 02 Air Flow",
        "Flotation Column 03 Air Flow",
        "Flotation Column 04 Air Flow",
        "Flotation Column 05 Air Flow",
        "Flotation Column 06 Air Flow",
        "Flotation Column 07 Air Flow",

        "Flotation Column 01 Level",
        "Flotation Column 02 Level",
        "Flotation Column 03 Level",
        "Flotation Column 04 Level",
        "Flotation Column 05 Level",
        "Flotation Column 06 Level",
        "Flotation Column 07 Level"

    ]


    for col in lag_features:

        for lag in [1,5,15,30,60,180,360]:

            df[f"{col}_lag_{lag}"] = (
                df[col].shift(lag)
            )



    # =====================
    # Advanced Rolling
    # =====================


    for col in lag_features:

        for window in [30,60,180]:

            df[f"{col}_rolling_mean_{window}"] = (
                df[col]
                .rolling(window)
                .mean()
            )


            df[f"{col}_rolling_std_{window}"] = (
                df[col]
                .rolling(window)
                .std()
            )



    df = df.dropna().reset_index(drop=True)


    return df