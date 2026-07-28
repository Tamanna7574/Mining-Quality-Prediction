import pandas as pd
from catboost import CatBoostRegressor
import joblib
import os
import time

from .feature_engineering import create_features

start = time.time()

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_optimized_catboost_model.cbm"
)


FEATURE_PATH = os.path.join(
    BASE_DIR,
    "models",
    "feature_names.pkl"
)


# Load model
model = CatBoostRegressor()
model.load_model(MODEL_PATH)


# Load feature names
feature_names = joblib.load(
    FEATURE_PATH
)


def predict_silica(history_df):

    """
    history_df:
    Raw mining sensor dataframe
    Minimum rows required: 500
    """

    if len(history_df) < 500:
        raise ValueError(
            "Need at least 500 historical records"
        )


    # Create features
    df_features = create_features(history_df)


    # Keep only model features
    df_features = df_features.reindex(
        columns=feature_names
    )


    # Check if features exist
    if df_features.empty:
        raise ValueError(
            "Feature generation produced zero rows. Provide more historical data."
        )


    # Predict latest point
    print("API FEATURES SHAPE:", df_features.shape)
    print(df_features.tail(1))
    
    prediction = model.predict(
        df_features.tail(1)
    )

    print(
    "Prediction Time:",
    time.time()-start,
    "seconds"
)


    return float(prediction[0])