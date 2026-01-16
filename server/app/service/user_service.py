from server.app.model.user_entity import User
from server.app.core.base_service import BaseService
from server.app.repository.interfaces.user_repository_interface import UserRepositoryInterface
from server.app.service.interfaces.user_service_interface import UserServiceInterface

class UserService(BaseService[User, int], UserServiceInterface):

    def __init__(self, repository: UserRepositoryInterface):
        super().__init__(repository)

    def find_by_email(self, email: str) -> User | None:
        self.repository.find_by_email(email)