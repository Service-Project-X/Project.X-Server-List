from typing import List

from app.db.mysql_conn import engineconn
from app.models.child_folder import ChildFolder
from app.models.folder import Folder
from app.models.schedule import Schedule
from app.schemas.folder import FolderCreate, FolderUpdate

engine = engineconn()
session = engine.sessionmaker()

class CRUDFolder:

    def get_multiple(self, folder_id) -> List[ChildFolder or Schedule]:
        child_folders = session.query(ChildFolder).filter_by(id=folder_id).all()
        schedules = session.query(Schedule).filter_by(id=folder_id).all()
        return [child_folders, schedules]

    def create(self, create_folder: FolderCreate):
        created_folder = Folder(mainDivide_id=create_folder.mainDivide_id, name=create_folder.name)
        session.add(created_folder)
        # null 반환함, 다른 걸로 바꾸기
        return session.commit()

    def update(self, folder_id: str, update_folder: FolderUpdate) -> Folder:
        found_folder = session.query(Folder).filter_by(id=folder_id).first()
        found_folder.name = update_folder.name

        session.add(found_folder)
        session.commit()
        session.refresh(found_folder)
        print("print found_folder", found_folder)
        # 반환값 때문에 에러남
        return found_folder

    def delete(self, folder_id: str):
        found_folder = session.query(Folder).filter_by(id=folder_id).first()
        session.delete(found_folder)
        result = session.commit()
        print(result)

        return "deleted"
