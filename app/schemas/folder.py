from typing import Optional

from pydantic import BaseModel

class FolderBase(BaseModel):
    mainDivide_id: Optional[int] = None
    name: Optional[str] = None

class FolderCreate(FolderBase):
    mainDivide_id: int
    name: str

class FolderUpdate(FolderBase):
    pass

class FolderInDBBase(FolderBase):
    id: str
    mainDivide_id: int
    name: str

    class Config:
        orm_mode = True

class Folder(FolderInDBBase):
    pass
