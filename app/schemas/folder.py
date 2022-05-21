from typing import Optional

from pydantic import BaseModel

class FolderBase(BaseModel):
    user_team_id: Optional[int] = None
    user_id: Optional[int] = None
    team_id: Optional[int] = None
    divider: Optional[bool] = None

class FolderCreate(FolderBase):
    user_team_id: int
    user_id: int
    team_id: int
    divider: bool

class FolderUpdate(FolderBase):
    pass

class FolderInDBBase(FolderBase):
    id: str
    user_team_id: int
    user_id: int
    team_id: int
    divider: bool

    class Config:
        orm_mode = True

class Folder(FolderInDBBase):
    pass
