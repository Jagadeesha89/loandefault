import yaml
from loandefault.exception.exception import LoandefaultException
from loandefault.logging.logger import logging
import os,sys
import numpy as np
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise LoandefaultException(e,sys)
    

def write_yaml_file(file_path:str,content:object,replace:bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w")as file:
            yaml.dump(content,file)
    except Exception as e:
        raise LoandefaultException(e,sys)
    

def save_numpy_arry(file_path:str ,array:np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise LoandefaultException(e,sys)
    

def save_object(file_path:str, obj:object)->None:
    try:
        logging.info('Enter the save object method of main utlis class')
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb")as file_obj:
            pickle.dump(obj,file_obj)
        logging.info("Exited the save object method of main utils class")
    except Exception as e:
        raise LoandefaultException(e,sys)
    

def load_object(file_path:str,)-> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"this file: {file_path} does not exists")
        with open(file_path,'rb') as file_obj:
            print(file_obj)
            return pickle.load(file_obj)
    except Exception as e:
        raise LoandefaultException(e,sys)
    
def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,"rb")as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise LoandefaultException(e,sys)
    
def evaluate_models(x_train,y_train,x_test,y_test,models,param):
    try:
        report={}

        for i in range(len(list(models))):
            model =list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs=GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)

            y_train_predict=model.predict(x_train)
            y_test_predict=model.predict(x_test)

            train_model_score = r2_score(y_train,y_train_predict)
            test_model_score = r2_score(y_test,y_test_predict)

            report[list(models.keys())[i]]=test_model_score

        return report
    except Exception as e:
        raise LoandefaultException(e,sys)


        



