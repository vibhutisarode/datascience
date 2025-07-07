from src.ENDTOENDDSPROJECT.logger import logging 
from src.ENDTOENDDSPROJECT.exception import CustomException
import sys
from src.ENDTOENDDSPROJECT.components.data_ingestion import DataIngestion
from src.ENDTOENDDSPROJECT.components.data_ingestion import DataIngestionConfig

if __name__== "__main__":
        logging.info("Starting the application")
                                             
        try:
            data_ingestion=DataIngestion()
            data_ingestion.initiate_data_ingestion()

        except Exception as e:
               logging.info("Exception occured")                                                                        
               raise CustomException(e,sys)
