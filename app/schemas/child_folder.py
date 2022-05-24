from typing import Optional

from pydantic import BaseModel

class ChildFolderBase(BaseModel):
    folder_id: Optional[int] = None
    child_folder_id: Optional[int] = None
    name: Optional[str] = None

class ChildFolderCreate(ChildFolderBase):
    name: str

class ChildFolderUpdate(ChildFolderBase):
    name: str

class ChildFolderInDBBase(ChildFolderBase):
    id: int
    folder_id: Optional[int]
    child_folder_id: Optional[int]
    name: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class ChildFolder(ChildFolderInDBBase):
    pass
