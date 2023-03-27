
import os
import sys

import numpy as np 
import pandas as pd
import dill  # for pickle file
# from sklearn.metrics import r2_score
# from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):  # to save pickle file
    try:
        dir_path = os.path.dirname(file_path)  # file path

        os.makedirs(dir_path, exist_ok=True)  # create directory

        with open(file_path, "wb") as file_obj:  # open file in wb format (binary write)
            dill.dump(obj, file_obj)  # obj - dumped # file_obj - to be written

    except Exception as e:
        raise CustomException(e, sys)