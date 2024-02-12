import os 
import sys 

def get_error_message(error, error_details:sys):

    typ , er , tb_er = error_details.exc_info()
    filename = tb_er.tb_frame.f_code.co_filename

    error_name = f"File name {filename} at Line No {tb_er.tb_lineno} error message {error}"

    return error_name 


class CustomException(Exception):

    def __init__(self, error , error_details:sys):
        self.error = get_error_message(error , error_details)

    def __str__(self):
        return self.error