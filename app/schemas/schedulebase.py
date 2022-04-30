from typing import Optional

from pydantic import BaseModel

class ScheduleBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None

class ScheduleCreate(ScheduleBase):
    title: str
    content: str
    image: str

class ScheduleUpdate(ScheduleBase):
    title: str
    content: str
    image: str

class ScheduleInDBBase(ScheduleBase):
    id: int
    title: str
    content: str
    image: str

    class Config:
        orm_mode = True

class Schedule(ScheduleInDBBase):
    pass
