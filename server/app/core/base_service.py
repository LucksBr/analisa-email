from typing import Generic, TypeVar, List, Optional
from server.app.core.base_repository import BaseRepository

T = TypeVar("T")
ID = TypeVar("ID")

class BaseService(Generic[T,ID]):

    def __init__(self, repository):
        self.repository = repository

    def list(self) -> List[T]:
        return self.repository.find_all()
    
    def get_by_id(self, entity_id: ID) -> Optional[T]:
        return self.repository.find_by_id(entity_id)

    def create(self, entity: T) -> T:
        return self.repository.merge(entity)
    
    def update(self, entity: T) -> T:
        return self.repository.merge(entity)

    def delete(self, entity: T) -> None:
        self.repository.delete(entity)