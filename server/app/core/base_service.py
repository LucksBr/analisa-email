from abc import abstractmethod
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
    
    @abstractmethod
    def validate(self, entity: T) -> None:
        pass

    def _before_create(self, entity: T) -> T:
        return entity
    
    def _after_create(self, entity: T) -> T:
        return entity

    def create(self, entity: T) -> T:
        entity = self._before_create(entity)
        self.validate(entity)
        entity = self.repository.merge(entity)
        entity = self._after_create(entity)

        return entity
    
    def _before_update(self, entity: T) -> T:
        return entity
    
    def _after_update(self, entity: T) -> T:
        return entity
    
    def update(self, entity: T) -> T:
        entity = self._before_update(entity)
        self.validate(entity)
        entity = self.repository.merge(entity)
        entity = self._after_update(entity)

        return entity

    def delete(self, entity: T) -> None:
        self.repository.delete(entity)