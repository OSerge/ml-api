from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import pickle
import numpy as np
import os

app = FastAPI(
    title="ML Model API",
    description="API для предсказаний с помощью модели XGBoost",
    version="1.0"
)

MODEL_PATH = "model.pkl"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Файл модели {MODEL_PATH} не найден")


with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f, encoding='latin1')

class PredictionRequest(BaseModel):
    features: list[float]

    @field_validator('features')
    def check_features_length(cls, v):
        if len(v) != 2:
            raise ValueError("Должно быть ровно 2 признака")
        return v

@app.post("/predict", summary="Сделать предсказание")
async def predict(request: PredictionRequest):
    try:
        features_array = np.array(request.features).reshape(1, -1)
        prediction = model.predict(features_array)
        return {
            "prediction": float(prediction[0]),
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
