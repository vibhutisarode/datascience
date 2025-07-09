from src.ENDTOENDDSPROJECT.logger import logging
from src.ENDTOENDDSPROJECT.exception import CustomException
from src.ENDTOENDDSPROJECT.components.data_ingestion import DataIngestion
from src.ENDTOENDDSPROJECT.components.data_ingestion import DataIngestionConfig
from src.ENDTOENDDSPROJECT.components.data_transformation import DataTransformationConfig,DataTransformation
from src.ENDTOENDDSPROJECT.components.model_tranier import ModelTrainerConfig,ModelTrainer

import sys


if __name__=="__main__":
    logging.info("The execution has started")

    import dagshub
dagshub.init(repo_owner='vibhutisarode',
             repo_name='datascience',
             mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)