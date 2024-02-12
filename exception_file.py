import os 
import sys 


def get_error_message(error , error_details:sys):

    typ, er , er_tb = error_details.exc_info()
    file_name = er_tb.tb_frame.f_code.co_filename

    error_message = f"File name {file_name} at Line_no {er_tb.tb_lineno} error message {error}"

    return error_message 

class CustomException(Exception):
    def __init__(self, error, error_details:sys):
        self.error = get_error_message(error, error_details)

    def __str__(self):
        return self.error
