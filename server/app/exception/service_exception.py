from .base_exception import BaseAppException

class ServiceException(BaseAppException):
    
    def __init__(self, 
                 message: str, 
                 status_code = 400, 
                 error = "SERVICE_ERROR"
                 ):
        super().__init__(message, status_code, error)