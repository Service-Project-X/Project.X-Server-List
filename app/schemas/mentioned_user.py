from typing import Optional

from pydantic import BaseModel

class MentionedUserBase(BaseModel):
    schedule_id: Optional[int] = None
    nickname: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None

class MentionedUserCreate(MentionedUserBase):
    schedule_id: int
    nickname: str
    name: str
    email: str

class MentionedUserUpdate(MentionedUserBase):
    pass

class MentionedUserInDBBase(MentionedUserBase):
    id: int
    schedule_id: int
    nickname: str
    name: str
    email: str

    class Config:
        orm_mode = True

class MentionedUser(MentionedUserInDBBase):
    pass

# class ListInDB(FolderInDBScheduleBase):
#     pass
