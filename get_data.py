import os
import sys
import json
import pandas as pd
import numpy as np

from dotenv import load_dotenv
import pymongo

from Networksecurity.exceptions.exception import networkSecurityException
from Networksecurity.logger.logger import logging



class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise networkSecurityException(e,sys)

    def csv_to_json_converter(self):
        try:
            pass
        except Exception as e:
             raise networkSecurityException(e,sys)  

    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise networkSecurityException(e,sys)              


    if __name__=='__main__':
      pass

        
   
