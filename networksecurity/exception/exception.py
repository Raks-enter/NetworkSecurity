import sys
from fastapi.responses import JSONResponse
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
            f"Error occurred in python script [{self.file_name}] "
            f"at line [{self.lineno}]: {self.error_message}"
        )

    def as_response(self):
        return JSONResponse(
            status_code=500,
            content={
                "error": str(self),
                "file": self.file_name,
                "line": self.lineno
            }
        )
