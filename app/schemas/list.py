from typing import Optional

from pydantic import BaseModel

class ListBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ListCreate(ListBase):
    title: str

class ListUpdate(ListBase):
    pass

class ListInDBBase(ListBase):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class List(ListInDBBase):
    pass
