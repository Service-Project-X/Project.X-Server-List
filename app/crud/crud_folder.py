from typing import List

from app.db.mysql_conn import engineconn
from app.models.folder import Folder
from app.schemas import folder

engine = engineconn()
session = engine.sessionmaker()

class CRUDFolder:
    # 공유 폴더는 팀당 하나 개인 폴더는 사람 수만큼이니까 사람 추가 될 때마다 추가 해야 될텐데
    def create(self, create_folder: folder.FolderCreate) -> Folder:
        created_folder = Folder(**create_folder.dict())
        print(created_folder.divider)
        session.add(created_folder)
        session.commit()
        session.refresh(created_folder)

        return created_folder

    def delete(self, folder_id: str):
        found_folder = session.query(Folder).filter_by(id=folder_id).first()
        session.delete(found_folder)
        result = session.commit()
        print(result)

        return "deleted"
