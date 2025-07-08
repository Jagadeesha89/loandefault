from loandefault.components.data_ingestion import DataIngestion
from loandefault.components.data_validation import DataValidation
from loandefault.exception.exception import LoandefaultException
from loandefault.logging.logger import logging
from loandefault.entity.config_entity import DataIngestionConfig,DataValidationConfig
from loandefault.entity.config_entity import TrainingPipelineConfig

import sys


if __name__=='__main__':
    try:
        training_pipeline_config =TrainingPipelineConfig()
        dataingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(dataingestion_config)
        logging.info("Initiatiing the data ingestion")
        dataingestion_artifcat = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestion_artifcat)
        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_vlaidation=DataValidation(dataingestion_artifcat,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_vlaidation.initiate_data_validation()
        logging.info("data Validation completed")
        print(data_validation_artifact)

    except Exception as e:
        LoandefaultException(e,sys)