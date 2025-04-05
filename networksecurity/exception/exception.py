import sys
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        
        self.lineno = exc_tb.tb_lineno if exc_tb else "unknown"
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "unknown"

        logger.error(self.__str__())

    def __str__(self):
        return (
            f"Error occured in python script name [{self.file_name}] "
            f"line number [{self.lineno}] error message [{self.error_message}]"
        )
