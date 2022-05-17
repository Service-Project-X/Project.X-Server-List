from typing import Optional

from pydantic import BaseModel

class ScheduleBase(BaseModel):
    folder_id: Optional[int] = None
    child_folder_id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None

class ScheduleCreate(ScheduleBase):
    title: str

class ScheduleUpdate(ScheduleBase):
    title: str

class ScheduleInDBBase(ScheduleBase):
    id: int
    title: str

    class Config:
        orm_mode = True

class Schedule(ScheduleInDBBase):
    pass
