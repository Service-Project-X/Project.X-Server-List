from typing import Optional

from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class CustomResponseTypeBase(BaseModel, Generic[T]):
    message: Optional[str] = None
    data: Optional[T] = None

class CustomResponseType(CustomResponseTypeBase):
    pass
