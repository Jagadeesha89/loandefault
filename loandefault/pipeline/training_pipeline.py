import sys
import os

from loandefault.exception.exception import LoandefaultException
from loandefault.logging.logger import logging

from loandefault.components.data_ingestion import DataIngestion
from loandefault.components.data_transformation import DataTransformation
from loandefault.components.data_validation import DataValidation
from loandefault.components.model_trainer import ModelTrainer

from loandefault.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelTrainerConfig
)

from loandefault.entity.artifactentity import(
    DataIngestionArtifact,
    DataTransformationArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact
)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()


    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Data ingestion started")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and relative artifact created: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise LoandefaultException (e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            data_validation_config=DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            logging.info("Initiate the data validation process")
            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info("Data validation compeleted and relavent artifact created")
            return data_validation_artifact
        except Exception as e:
            raise LoandefaultException(e,sys)
        
    def start_data_transformation(self,data_validation_artifact=DataValidationArtifact):
        try:
            data_transformation_config=DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transforamtion=DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
            logging.info("Initiate the data transformation")
            data_transformation_artifact=data_transforamtion.initiate_data_transformation()
            logging.info("Data transformation completed and relavent artifact created")
            return data_transformation_artifact
        except Exception as e:
            raise LoandefaultException(e,sys)
        
    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            model_trainer_config=ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer=ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                    model_trainer_config=model_trainer_config)
            logging.info("Initiate the model trainer")
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            logging.info("Model trainer process completed")
            return model_trainer_artifact
        except Exception as e:
            raise LoandefaultException(e,sys)
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            return model_trainer_artifact

        except Exception as e:
            raise LoandefaultException(e,sys)