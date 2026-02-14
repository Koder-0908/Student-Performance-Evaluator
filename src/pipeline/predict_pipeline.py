import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        self.base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        
        self.model_path = os.path.join(self.base_path, 'artifacts', 'model.pkl')
        self.ml_model_path = os.path.join(self.base_path, 'artifacts', 'ML_model.pkl')

        self.model = load_object(self.model_path)
        self.ml_model = load_object(self.ml_model_path)

    def predict(self, features):
        try:
            data_scaled = self.model.transform(features)
            pred = self.ml_model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, gender: str, race_ethnicity: str, parental_level_of_education: str, lunch: str, test_preparation_course: str, reading_score: int, writing_score: int):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def create_dataframe(self):
        try:
            data = {
                'gender': [self.gender],
                'race/ethnicity': [self.race_ethnicity],
                'parental level of education': [self.parental_level_of_education],
                'lunch': [self.lunch],
                'test preparation course': [self.test_preparation_course],
                'reading score': [self.reading_score],
                'writing score': [self.writing_score]
            }

            return pd.DataFrame(data)
        except Exception as e:
            raise CustomException(e, sys)
            
