from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import pandas as pd

MODEL_VERSION = '0.0.1'

app = FastAPI()

class Data(BaseModel):
    gender: Annotated[str, Field(..., description = 'Male/Female')]
    race_ethnicity: Annotated[str, Field(..., description = 'Your Race/Ethnicity')]
    parental_level_of_education: Annotated[str, Field(..., description = 'Enter parental level of education')]
    lunch: Annotated[str, Field(..., description = 'Standard/Free')]
    test_preparation_course: Annotated[str, Field(..., description = 'None/Completed')]
    reading_score: Annotated[int, Field(..., ge = 0, le = 100, description = 'Enter reading score')]
    writing_score: Annotated[int, Field(..., ge = 0, le = 100, description = 'Enter writing score')]

@app.get('/')
def home():
    return {'message': 'Home page'}

@app.get('/healeh')
def home():
    return {
        'Status': 'Ok',
        'Model Version': MODEL_VERSION
    }

@app.post('/predict')
def predict(input: Data):
    data = CustomData(
        gender =  input.gender,
        race_ethnicity = input.race_ethnicity,
        parental_level_of_education = input.parental_level_of_education,
        lunch = input.lunch,
        test_preparation_course = input.test_preparation_course,
        reading_score = input.reading_score,
        writing_score = input.writing_score
    )
    df = data.create_dataframe()
    pred = PredictPipeline()
    prediction = pred.predict(df)

    return JSONResponse(status_code = 200, content = {'predicted': prediction.tolist()})
