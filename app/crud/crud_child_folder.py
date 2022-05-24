from typing import List

from app.db.mysql_conn import engineconn
from app.models.child_folder import ChildFolder
from app.schemas.child_folder import ChildFolderCreate, ChildFolderUpdate

engine = engineconn()
session = engine.sessionmaker()

class CRUDChildFolder:
    def get_multiple_in_folder(self, folder_id: int) -> List[ChildFolder]:
        child_folders = session.query(ChildFolder).filter_by(folder_id=folder_id).all()
        return child_folders

    def get_multiple_in_child_folder(self, child_folder_id: int) -> List[ChildFolder]:
        child_folders = session.query(ChildFolder).filter_by(child_folder_id=child_folder_id).all()
        return child_folders

    def create_in_folder(self, create_child_folder: ChildFolderCreate):
        created_child_folder = ChildFolder(folder_id=create_child_folder.folder_id, name=create_child_folder.name)
        session.add(created_child_folder)
        # null 반환함, 다른 걸로 바꾸기
        return session.commit()

    def create_in_child_folder(self, create_child_folder: ChildFolderCreate):
        created_child_folder = ChildFolder(child_foler_id=create_child_folder.child_folder_id, name=create_child_folder.name)
        session.add(created_child_folder)
        # null 반환함, 다른 걸로 바꾸기
        return session.commit()

    # 구분이 필요한 가?
    def update_in_child_folder(self, child_folder_id: int, update_folder: ChildFolderUpdate) -> ChildFolder:
        found_child_folder = session.query(ChildFolder).filter_by(id=child_folder_id).first()
        found_child_folder.name = update_folder.name

        session.add(found_child_folder)
        session.commit()
        session.refresh(found_child_folder)
        print("print found_child_folder", found_child_folder)
        # 반환값 때문에 에러남
        return found_child_folder

    def delete_in_child_folder(self, child_folder_id: int):
        found_child_folder = session.query(ChildFolder).filter_by(id=child_folder_id).first()
        session.delete(found_child_folder)
        result = session.commit()
        print(result)

        return "deleted"
