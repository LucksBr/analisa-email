from fastapi import Depends, APIRouter
from sqlmodel import Session
from server.app.model.user_entity import User
from server.app.service.interfaces.user_service_interface import UserServiceInterface
from server.app.service.user_service import UserService
from server.app.repository.user_repository import UserRepository
from server.app.config.database import get_session

router = APIRouter(prefix = "/users")

def get_user_service(session: Session = Depends(get_session)) -> UserServiceInterface:
    repository = UserRepository(session)
    return UserService(repository)

@router.get("/getById/{id}")
def get_by_id(id: int, service: UserServiceInterface = Depends(get_user_service)):
    return service.get_by_id(id)

@router.get("/list")
def list( service: UserServiceInterface = Depends(get_user_service)):
    return service.list();

@router.post("/")
def create(user: User, service: UserServiceInterface = Depends(get_user_service)):
    return service.create(user)

@router.get("/")
def hello():
    return "Oi"