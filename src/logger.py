import os 
import sys 
from datetime import datetime 
import logging 

log_file = f"{datetime.now().strftime('%Y %m %d %H %M %S')}.log"

log_log_file = os.path.join(os.getcwd() , "logs" , log_file)

os.makedirs(log_log_file, exist_ok=True)

final_log = os.path.join(log_log_file, log_file)

logging.basicConfig(
    filename = final_log,
    level = logging.DEBUG , 
    format = ('%(asctime)s %(name)s %(message)s') 
)