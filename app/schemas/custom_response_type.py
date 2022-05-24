from typing import Optional

from typing import TypeVar, Generic
from pydantic.generics import GenericModel

T = TypeVar('T')

class CustomResponseType(GenericModel, Generic[T]):
    message: Optional[str]
    data: Optional[T]
