from sqlmodel import Session, select
from server.app.core.base_repository import BaseRepository
from server.app.model.user_entity import User
from server.app.repository.interfaces.user_repository_interface import UserRepositoryInterface

class UserRepository(BaseRepository[User, int], UserRepositoryInterface):

    def __init__(self, session: Session):
        super().__init__(session, User)

    def find_by_email(self, email) -> User | None:
        select_search_user_by_email = select(User).where(User.email == email)
        return self.session.exec(select_search_user_by_email).first()