from typing import Optional

from pydantic import BaseModel

class FolderScheduleBase(BaseModel):
    folder_id: Optional[int] = None
    child_folder_id: Optional[int] = None
    name: Optional[str] = None

class FolderScheduleCreate(FolderScheduleBase):
    name: str

class FolderScheduleUpdate(FolderScheduleBase):
    name: str

class FolderScheduleInDBScheduleBase(FolderScheduleBase):
    id: int
    name: str

    class Config:
        orm_mode = True

class FolderScheduleInDBSchedule(FolderScheduleInDBScheduleBase):
    pass
