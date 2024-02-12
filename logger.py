import os 
import sys 
import logging 
from datetime import datetime 

log_file = f"{datetime.now().strftime('%Y %m %d %H %M %S')}.log"

file_with_log = os.path.join(os.getcwd(), "logs", log_file)

os.makedirs(file_with_log, exist_ok=True)


final_path = os.path.join(file_with_log, log_file)


logging.basicConfig(
    filename = final_path,
    level = logging.DEBUG,
    format = ('%(asctime)s %(name)s %(message)s') 
)


