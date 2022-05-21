from typing import List

from app.db.mysql_conn import engineconn
from app.models.mentioned_user import MentionedUser
from app.schemas.mentioned_user import MentionedUserCreate
from app.schemas.schedule import ScheduleCreate, Schedule, ScheduleUpdate

engine = engineconn()
session = engine.sessionmaker()


class CRUDMentionedUser:
    def get_one(self, mentioned_user_id:int) -> MentionedUser:
        found_mentioned_user = session.query(MentionedUser).filter_by(id=mentioned_user_id).first()
        return found_mentioned_user

    def get_multiple_with_schedule_id(self, schedule_id: int) -> List[MentionedUser]:
        found_mentioned_users = session.query(MentionedUser).filter_by(schdedule_id=schedule_id).all()
        return found_mentioned_users

    def create(self, create_mentioned_user: MentionedUserCreate):
        mentioned_user = MentionedUser(schedule_id=create_mentioned_user.schedule_id, name=create_mentioned_user.name, email=create_mentioned_user.email)
        session.add(mentioned_user)
        session.commit()
        return

    def delete(self, schedule_id: int):
        found_schedule = session.query(Schedule).filter_by(id=schedule_id).first()
        session.delete(found_schedule)
        session.commit()
