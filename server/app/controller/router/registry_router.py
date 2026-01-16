from typing import List
from fastapi import APIRouter, FastAPI
from server.app.controller.user_controller import router as user_router

def get_routes() -> List[APIRouter]:
    return [
        user_router,
    ]

def register_routers(app: FastAPI):
    for router in get_routes():
        app.include_router(router)