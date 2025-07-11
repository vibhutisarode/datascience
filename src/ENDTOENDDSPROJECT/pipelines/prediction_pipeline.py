import sys
import pandas as pd
from src.ENDTOENDDSPROJECT.exception import CustomException
from src.ENDTOENDDSPROJECT.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 district: str,
                 soil_type: str,
                 ph_level: float,
                 organic_matter: float,
                 nitrogen_content: float,
                 phosphorus_content: float,
                 potassium_content: float):
        
        self.district = district
        self.soil_type = soil_type
        self.ph_level = ph_level
        self.organic_matter = organic_matter
        self.nitrogen_content = nitrogen_content
        self.phosphorus_content = phosphorus_content
        self.potassium_content = potassium_content

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "District": [self.district],
                "Soil Type": [self.soil_type],
                "pH Level": [self.ph_level],
                "Organic Matter (%)": [self.organic_matter],
                "Nitrogen Content (kg/ha)": [self.nitrogen_content],
                "Phosphorus Content (kg/ha)": [self.phosphorus_content],
                "Potassium Content (kg/ha)": [self.potassium_content],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
