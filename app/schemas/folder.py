from typing import Optional

from pydantic import BaseModel

class FolderBase(BaseModel):
    name: Optional[str] = None

class FolderCreate(FolderBase):
    name: str

class FolderUpdate(FolderBase):
    pass

class FolderInDBBase(FolderBase):
    id: str
    name: str

    class Config:
        orm_mode = True

class Folder(FolderInDBBase):
    pass
