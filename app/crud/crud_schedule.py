from typing import List

from app.db.mysql_conn import engineconn
from app.schemas.schedule import ScheduleCreate, Schedule, ScheduleUpdate

engine = engineconn()
session = engine.sessionmaker()

class CRUDSchedule:
    def get_one(self, schedule_id) -> Schedule:
        found_schedule = session.query(Schedule).filter_by(schedule_id).first()
        return found_schedule

    def get_multiple_in_folder(self, folder_id: int) -> List[Schedule]:
        found_schedules = session.query(Schedule).filter_by(folder_id).all()
        return found_schedules

    def get_multiple_in_child_folder(self, child_folder_id: int) -> List[Schedule]:
        found_schedules = session.query(Schedule).filter_by(child_folder_id).all()
        return found_schedules

    def create_in_folder(self, create_schedule: ScheduleCreate):
        schedule = Schedule(folder_id=create_schedule.folder_id, title=create_schedule.title, content=create_schedule.content, image=create_schedule.image)
        session.add(schedule)
        session.commit()
        return

    def create_in_child_folder(self, create_schedule: ScheduleCreate):
        schedule = Schedule(child_folder_id=create_schedule.folder_id, title=create_schedule.title, content=create_schedule.content, image=create_schedule.image)
        session.add(schedule)
        session.commit()
        return

    def update(self, schedule_id: int, update_schedule: ScheduleUpdate):
        found_schedule: Schedule = session.query(Schedule).filter_by(id=schedule_id).first()
        found_schedule.title = update_schedule.title
        found_schedule.content = update_schedule.content
        found_schedule.image = update_schedule.image

        session.add(found_schedule)
        session.commit()
        session.refresh(found_schedule)
        print("Update Schedule", found_schedule)
        # 반환값 때문에 에러남
        return found_schedule

    def delete(self, schedule_id: int):
        found_schedule = session.query(Schedule).filter_by(id=schedule_id).first()
        session.delete(found_schedule)
        session.commit()
        