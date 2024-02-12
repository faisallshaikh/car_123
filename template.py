import os 
import sys 
from pathlib import Path 
from src.logger import logging 


path_dir = os.getcwd() 

list_of_files = [
    "\\src\\__init__.py",
    "\\src\\components\\__init__.py",
    "\\src\\pipeline\\__init__.py",
    "\\src\\exception_file.py",
    "\\src\\logger.py",
    "\\src\\components\\data_ingestion.py",
    "\\src\\notebooks\\EDA.ipynb"
]

for file in list_of_files:

    full_path = path_dir + file 
    whole_path = Path(full_path)
    dir_path , filename = os.path.split(whole_path)

    os.makedirs(dir_path, exist_ok=True)

    if os.path.exists(full_path):
        print(f"File already exists {filename}")
        logging.info(f"File already exists {filename}")


    if (not os.path.exists(full_path)):
        with open(full_path, 'w') as f:
            print(f"File created {filename}") 
            logging.info(f"File created {filename}")
