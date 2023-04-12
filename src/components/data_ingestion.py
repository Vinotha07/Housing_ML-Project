import os
import pandas as pd
import numpy as np
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#Data class is a class that store the data, it doesnt have any methods


# Initialize the Data Ingestion config
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts', 'train.csv')
    test_data_path:str=os.path.join('artifacts', 'test.csv')
    raw_data_path:str=os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()
        


    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Method Starts')
        try:
            df=pd.read_csv(os.path.join('notebook/Data','gemstone.csv'))
            logging.info('Dataset read as Pandas')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info('Train Test Split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path)
            test_set.to_csv(self.ingestion_config.test_data_path)
            
            logging.info('DataIngestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        except Exception as e:
            logging.info('Error Occured at DataIngestion stage')    
            raise CustomException(e,sys)




