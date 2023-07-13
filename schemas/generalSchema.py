from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    result: Optional[T]