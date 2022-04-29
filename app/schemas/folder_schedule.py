from typing import Optional

from pydantic import BaseModel

class FolderScheduleBase(BaseModel):
    folder_id: Optional[int] = None
    schedule_id: Optional[int] = None
    mainDivide_id: Optional[int] = None

class FolderScheduleCreate(FolderScheduleBase):
    pass

class FolderScheduleUpdate(FolderScheduleBase):
    pass

class FolderInDBScheduleBase(FolderScheduleBase):
    id: int
    folder_id: Optional[int] = None
    schedule_id: Optional[int] = None
    mainDivide_id: Optional[int] = None

    class Config:
        orm_mode = True

class FolderInDBSchedule(FolderInDBScheduleBase):
    pass
