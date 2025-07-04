from loandefault.components.data_ingestion import DataIngestion
from loandefault.exception.exception import LoandefaultException
from loandefault.logging.logger import logging
from loandefault.entity.config_entity import DataIngestionConfig
from loandefault.entity.config_entity import TrainingPipelineConfig

import sys


if __name__=='__main__':
    try:
        training_pipeline_config =TrainingPipelineConfig()
        dataingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(dataingestion_config)
        logging.info("Initiatiing the data ingestion")
        dataingestion_artifcat = data_ingestion.initiate_data_ingestion()
        print(dataingestion_artifcat)
    except Exception as e:
        LoandefaultException(e,sys)