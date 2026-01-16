from abc import ABC, abstractmethod
from server.app.model.user_entity import User

class UserServiceInterface(ABC):

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def authenticate(self, email: str, password: str) -> str:
        pass