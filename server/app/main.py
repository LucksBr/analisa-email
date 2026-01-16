from fastapi import FastAPI
from server.app.config.database import create_db_and_tables
from server.app.controller.user_controller import router as user_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(user_router)