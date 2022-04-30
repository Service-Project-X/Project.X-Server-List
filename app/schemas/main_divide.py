from typing import Optional

from pydantic import BaseModel

class MainDivideBase(BaseModel):
    user_team_id: Optional[int] = None
    user_id: Optional[int] = None
    team_id: Optional[int] = None
    divider: Optional[bool] = None

class MainDivideCreate(MainDivideBase):
    user_team_id: int
    user_id: int
    team_id: int
    divider: bool = False

class MainDivideUpdate(MainDivideBase):
    user_team_id: int
    user_id: int
    team_id: int
    divider: bool

class MainDivideInDBBase(MainDivideBase):
    id: int
    user_team_id: int
    user_id: int
    team_id: int
    divider: bool = False

    class Config:
        orm_mode = True

class MainDivide(MainDivideInDBBase):
    pass
