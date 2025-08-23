# Collecting the data and splitting it into train and test sets is called data ingestion
# This is the first step in the ML project
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # to avoid boilerplate code for class

#taking input and output path from user
@dataclass #decorator
class DataIngestionConfig:
    #giving inputs to data ingestion component class it will save train,test and raw data
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #object of dataclass

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv') #reading the data
            logging.info('Read the dataset as dataframe') #logg to store info of executed instructions

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            #creating artifacts folder to store train and test data

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            #storing raw data in artifacts folder
            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            #splitting the data into train and test set

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            #storing train and test data in artifacts folder

            logging.info("Ingestion of the data is completed")

            return ( #takes the 
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()