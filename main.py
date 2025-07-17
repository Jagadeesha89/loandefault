from loandefault.components.data_ingestion import DataIngestion
from loandefault.components.data_validation import DataValidation
from loandefault.components.data_transformation import DataTransformation
from loandefault.components.model_trainer import ModelTrainer
from loandefault.exception.exception import LoandefaultException
from loandefault.logging.logger import logging
from loandefault.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
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
        data_transformation_config=DataTransformationConfig(training_pipeline_config)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("data transformation started")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation compeletd")
        logging.info("Model training started")
        model_trainer_config=ModelTrainerConfig(training_pipeline_config)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model training artificat Created")
    except Exception as e:
        raise LoandefaultException(e,sys)