from typing import List

from app.db.mysql_conn import engineconn
from app.models.child_folder import ChildFolder
from app.models.folder import Folder
from app.models.schedule import Schedule
from app.schemas.folder import FolderCreate, FolderUpdate

engine = engineconn()
session = engine.sessionmaker()

class CRUDFolder:
    # 공유 폴더는 팀당 하나 개인 폴더는 사람 수만큼이니까 사람 추가 될 때마다 추가 해야 될텐데
    def create(self, create_folder: FolderCreate):
        created_folder = Folder(user_team_id=create_folder.user_team_id, user_id=create_folder.user_id, team_id=create_folder.team_id, divider=create_folder.divider)
        session.add(created_folder)
        # null 반환함, 다른 걸로 바꾸기
        return session.commit()

    def delete(self, folder_id: str):
        found_folder = session.query(Folder).filter_by(id=folder_id).first()
        session.delete(found_folder)
        result = session.commit()
        print(result)

        return "deleted"
