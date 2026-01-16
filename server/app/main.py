from fastapi import FastAPI
from server.app.exception.registry_exception import register_exceptions_handlers
from server.app.config.database import create_db_and_tables
from server.app.controller.router.registry_router import register_routers

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Resistro de handlers de exceções e rotas da Api
register_exceptions_handlers(app)
register_routers(app)