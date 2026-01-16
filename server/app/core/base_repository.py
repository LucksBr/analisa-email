from abc import ABC
from typing import Generic, TypeVar, List, Optional, Type
from sqlmodel import Session, select, SQLModel

T = TypeVar("T", bound = SQLModel)
ID = TypeVar("ID")

class BaseRepository(ABC, Generic[T,ID]):
    
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def find_all(self) -> List[T]:
        return self.session.exec(select(self.model)).all()
    
    def find_by_id(self, entity_id: ID) -> Optional[T]:
        return self.session.get(self.model, entity_id)
    
    def merge(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)

        return entity
    
    def delete(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.commit()