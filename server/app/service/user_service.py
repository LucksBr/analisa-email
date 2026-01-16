from server.app.model.user_entity import User
from server.app.core.base_service import BaseService
from server.app.repository.interfaces.user_repository_interface import UserRepositoryInterface
from server.app.service.interfaces.user_service_interface import UserServiceInterface
from server.app.exception.service_exception import ServiceException
from server.app.exception.auth_exception import AuthException
from server.app.core.security.password_utils import hash_password, verify_password
from server.app.core.auth.jwt_utils import create_acess_token

class UserService(BaseService[User, int], UserServiceInterface):

    def __init__(self, repository: UserRepositoryInterface):
        super().__init__(repository)

    def find_by_email(self, email: str) -> User | None:
        return self.repository.find_by_email(email)

    def _before_create(self, entity: User):
        if entity.encrpyted_password:
            entity.encrpyted_password = hash_password(entity.encrpyted_password)

        return entity

    def validate(self, entity: User):
        if not entity.name:
            raise ServiceException(
                message = "O nome do usuário deve ser informado!",
                error = "USER_NAME_REQUIRED"
            )
        
        if not entity.email:
            raise ServiceException(
                message = "O email do usuário deve ser informado!",
                error = "USER_EMAIL_REQUIRED"
            )
        
        if "@" not in entity.email:
            raise ServiceException(
                message = "O email do usuário deve ser válido!",
                error = "USER_EMAIL_INVALID"
            )
        
        self._validate_if_user_email_already_exists(entity.email,entity.id)
        
        self._validate_password(entity)
        
    def _validate_if_user_email_already_exists(self,email: str, user_id: int | None):
        userSearched = self.find_by_email(email)

        if userSearched and userSearched.id != user_id:
            raise ServiceException(
                 message = "O email já está sendo usado!",
                 error = "USER_EMAIL_ALREADY_REGISTERED"
            )
        
    def _validate_password(self, entity: User):
        if not entity.id and not entity.encrpyted_password:
            raise ServiceException(
                message="A senha é obrigatória no cadastro!",
                error="USER_PASSWORD_REQUIRED"
            )
    
    def update(self, entity: User) -> User:
        entity = self._before_update(entity)

        db_entity = self.repository.find_by_id(entity.id)

        if not db_entity:
            raise ServiceException(
                message="Usuário não encontrado",
                error="USER_NOT_FOUNDED"
            )

        if entity.encrpyted_password:
            db_entity.encrpyted_password = hash_password(
                entity.encrpyted_password
            )

        if entity.email:
            db_entity.email = entity.email

        if entity.name:
            db_entity.name = entity.name

        self.validate(db_entity)
        userUpdated =  self.repository.merge(db_entity)
        
        return self._after_update(userUpdated)

    def authenticate(self, email: str, password: str) -> str:
        userSearched = self.find_by_email(email)

        if not userSearched or not verify_password(password, userSearched.encrpyted_password):
            raise AuthException()
        
        return create_acess_token({
            "sub": str(userSearched.id),
            "email": userSearched.email
        })