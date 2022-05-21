from typing import Optional

from pydantic import BaseModel

class MentionedUserBase(BaseModel):
    schedule_id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None

class MentionedUserCreate(MentionedUserBase):
    schedule_id: int
    name: str
    email: str

class MentionedUserUpdate(MentionedUserBase):
    schedule_id: int
    name: str
    email: str

class MentionedUserInDBBase(MentionedUserBase):
    id: int
    schedule_id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class MentionedUser(MentionedUserInDBBase):
    pass
