from fastapi import FastAPI, HTTPException
from typing import List, Dict

import pandas as pd

from src.predictor import predict_silica


app = FastAPI(
    title="Mining Quality Prediction API",
    version="0.1.0"
)


@app.get("/")
def home():

    return {
        "message": "Mining Quality Prediction API Running"
    }



@app.post("/predict")
def predict(data: List[Dict]):

    try:

        # Convert JSON input to dataframe
        df = pd.DataFrame(data)


        # Prediction
        prediction = predict_silica(df)


        return {

            "prediction": round(prediction, 3),
            "unit": "%",
            "target": "% Silica Concentrate",
            "model": "Optimized CatBoost + Time Features"

        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )