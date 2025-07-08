import os
import sys
import numpy as np
import pandas as pd

"""
Defining common constant variables for training pipeline

"""

TARGET_COLUMN = "Default"
PIPELINE_NAME:str = "LoanDefault"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str = "Loan_default.csv"


TRAIN_FILE_NAME:str ="train.csv"
TEST_FILE_NAME:str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")


"""
Data Ingestion realted condstant start with data_ingestion VAR Name

"""

DATA_INGESTION_COLLCECTION_NAME:str = "LoandefaultData"
DATA_INGESTION_DATABASE_NAME:str = "JAGA"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "festure_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float= 0.2


"""
Data validation related constant start with  DATA_VLAIDATION VAR NAME

"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR = "validated"
DATA_VALIDATION_INVALID_DIR = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"