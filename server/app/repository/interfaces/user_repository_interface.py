from abc import ABC, abstractmethod
from server.app.model.user_entity import User

class UserRepositoryInterface(ABC):

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        pass