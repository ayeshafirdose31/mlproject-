import sys #sys controls the info if the exception gets dropped
import logging

def error_message_detail(error,error_detail:sys): #error=shows us error and error_detail gives us detail of the error 
    _,_,exc_tb=error_detail.exc_info() # first two line's data is not that imp but the third line gives us important info such as at which file, and which line the exception has occured and its reason
    file_name=exc_tb.tb_frame.f_code.co_filename #custom exception handling #at which file error has been occured
    error_message="Error occured in python script name[{0}], and line number [{1}] error messga e[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message    
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message


   