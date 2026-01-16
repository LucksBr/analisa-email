class BaseAppException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = 400,
        error: str = "BAD_REQUEST"
    ):
        
        self.message = message
        self.status_code = status_code
        self.error = error
        super().__init__(message)