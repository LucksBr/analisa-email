from typing import Dict, Type, Callable
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from server.app.exception.base_exception import BaseAppException
from server.app.exception.handler_exception import base_exception_handler
from server.app.exception.service_exception import ServiceException
from server.app.exception.auth_exception import AuthException

ExceptionHandler = Callable[[Request, Exception], JSONResponse]

def get_exception_handlers() -> Dict[Type[Exception], ExceptionHandler]:
    return {
        BaseAppException: base_exception_handler,
        ServiceException: base_exception_handler,
        AuthException: base_exception_handler,
    }

def register_exceptions_handlers(app: FastAPI):
    handlers = get_exception_handlers()

    for exception, handler in handlers.items():
        app.add_exception_handler(exception, handler)