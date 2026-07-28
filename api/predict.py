from fastapi import APIRouter, UploadFile, File
import pandas as pd

from src.predictor import predict


router = APIRouter()



@router.post("/predict")
async def predict_quality(
    file: UploadFile = File(...)
):

    df = pd.read_csv(file.file)


    result = predict(df)


    return {
        "Predicted Silica Concentrate": result
    }