from fastapi import Request
from fastapi.responses import JSONResponse
from server.app.exception.base_exception import BaseAppException
from server.app.exception.utils.error_builder import build_error

def base_exception_handler(request: Request, exception: BaseAppException):
    return JSONResponse(
        status_code = exception.status_code,
        content = build_error(request = request, 
                              status = exception.status_code, 
                              error = exception.error, 
                              message = exception.message
                              ),
    )