import sys
import os
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OrdinalEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

from loandefault.constant.training_pipeline import  TARGET_COLUMN,SCHEMA_FILE_PATH
from loandefault.entity.artifactentity import(
    DataValidationArtifact,
    DataTransformationArtifact
)

from loandefault.entity.config_entity import DataTransformationConfig
from loandefault.logging.logger import logging
from loandefault.exception.exception import LoandefaultException
from loandefault.utils.main_utils.utils import read_yaml_file
from loandefault.utils.main_utils.utils import save_numpy_arry,save_object

class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        self.data_validation_artifact:DataValidationArtifact=data_validation_artifact
        self.data_transformation_config:DataTransformationConfig =data_transformation_config
        self.schema_config=read_yaml_file(file_path=SCHEMA_FILE_PATH)

    @staticmethod
    def read_csv(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise LoandefaultException(e,sys)
        
    def get_data_transformer(self)->Pipeline:
        logging.info("Enter the get data transformation object")
        try:
            
            one_ht_encod=OneHotEncoder()
            stand_scaler=StandardScaler()
            ord_encod=OrdinalEncoder()

            one_ht_encod_columns=self.schema_config['one_ht_encode']
            ord_encod_columns=self.schema_config['ord_encode']
            std_scaler_columns=self.schema_config['std_scaler']

            preprocesser=ColumnTransformer(
                [
                ('Onehotencoder',one_ht_encod,one_ht_encod_columns),
                ('OrdinalEncoder',ord_encod,ord_encod_columns),
                ('StandardScaler',stand_scaler,std_scaler_columns),
                 ]
            )
            return preprocesser
        except Exception as e:
            raise LoandefaultException(e,sys)



    def initiate_data_transformation(self)->DataTransformationArtifact:
        logging.info("Enterd initiate the data transformation class")
        try:
            logging.info("Starting data transformation")
            train_df=DataTransformation.read_csv(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_csv(self.data_validation_artifact.valid_test_file_path)

            ##Training dataframe
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            traget_feature_train_df=train_df[TARGET_COLUMN]
            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN],axis=1)
            traget_feature_test_df=test_df[TARGET_COLUMN]

            preprocesser=self.get_data_transformer()
            preprocesser_object=preprocesser.fit(input_feature_train_df)
            transformed_train_df=preprocesser_object.transform(input_feature_train_df)
            transformed_test_df=preprocesser_object.transform(input_feature_test_df)

            train_arr=np.c_[transformed_train_df,np.array(traget_feature_train_df)]
            test_arr=np.c_[transformed_test_df,np.array(traget_feature_test_df)]

            save_numpy_arry(self.data_transformation_config.transformed_train_file_path,array=train_arr,)
            save_numpy_arry(self.data_transformation_config.transformed_test_file_path,array=test_arr,)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocesser_object,)

            save_object("final_models/preprocesser.pkl",preprocesser_object,)

            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )

            return data_transformation_artifact

        except Exception as e:
            raise LoandefaultException(e,sys)
