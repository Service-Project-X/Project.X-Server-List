from typing import Optional

from pydantic import BaseModel

class ChildFolderBase(BaseModel):
    folder_id: Optional[int] = None
    child_folder_id: Optional[int] = None
    name: Optional[str] = None

class ChildFolderCreateBase(ChildFolderBase):
    name: str

class ChildFolderUpdateBase(ChildFolderBase):
    name: str

class ChildFolderInDBBase(ChildFolderBase):
    id: int
    name: str

    class Config:
        orm_mode = True

class ChildFolder(ChildFolderInDBBase):
    pass
