import os 
import sys 
import pathlib 
from pathlib import Path 


list_of_files = [
    "\\src\\logger.py",
    "\\rough.ipynb",
    "\\src\\exception_file.py"
] 

path_dir = os.getcwd()

for file in list_of_files:

    full_path = path_dir + file 
    whole_path = Path(full_path)
    dir_path , file_name = os.path.split(whole_path) 

    os.makedirs(dir_path, exist_ok=True)

    if os.path.exists(full_path):
        print("file already exists") 

    if (not os.path.exists(full_path)):
        with open(file_name, 'w') as f:
            print(f"File created {file_name}")  

