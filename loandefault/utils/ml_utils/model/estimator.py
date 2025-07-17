from loandefault.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import os
import sys

from loandefault.exception.exception import LoandefaultException
from loandefault.logging.logger import logging

class LoanDefaultModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor =preprocessor
            self.model=model
        except Exception as e:
            raise LoandefaultException(e,sys)
        
    def predict(self,x):
        try:
            x_tranform=self.preprocessor.transform(x)
            y_hat =self.model.predict(x_tranform)
            return y_hat
        except Exception as e:
            raise LoandefaultException(e,sys)