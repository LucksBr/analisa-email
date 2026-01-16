from server.app.exception.base_exception import BaseAppException

class AuthException(BaseAppException):

    def __init__(self, message: str = "Credenciais inválidas", error: str = "AUTH_INVALID_CREDENTIALS"):
        super().__init__(
            message = message,
            error = error,
            status_code = 401
        )