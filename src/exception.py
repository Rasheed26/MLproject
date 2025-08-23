# Read exception handling in python documentation on https://docs.python.org/3/tutorial/errors.html
import sys

from src.logger import logging #importing the logging module from logger.py for logging the error messages



#creating a function to get the error message details
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

#creating a custom exception class to handle exceptions/errors
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail) #calling the function to get the error message details

    def __str__(self): #overriding the __str__ method to return the error message
        return self.error_message

#this code is for testing the custom exception class
