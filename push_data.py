import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from loandefault.exception.exception import LoandefaultException
from loandefault.logging import logger

class LoanDefaultDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise LoandefaultException(e,sys)
        

    def cv_to_dict_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=data.to_dict(orient='records')
            return records
        except Exception as e:
            raise LoandefaultException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise LoandefaultException(e,sys)
if __name__=='__main__':
    FILE_PATH = "D:\Git projects\loandefault\default_data\Loan_default.csv"
    DATABASE="JAGA"
    Collection="LoandefaultData"
    loandefaultobj=LoanDefaultDataExtract()
    records=loandefaultobj.cv_to_dict_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=loandefaultobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)

