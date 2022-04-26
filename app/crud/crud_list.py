from typing import List

from app.db.mysql_conn import engineconn
from app.models.list import MyList
from app.schemas.list import ListCreate, ListUpdate

engine = engineconn()
session = engine.sessionmaker()

class CRUDLists:

    def get_multiple(self) -> List[MyList]:
        return session.query(MyList).all()

    async def update(self, list_id: str, update_list: ListUpdate) -> MyList:
        found_list = session.query(MyList).filter_by(id=list_id).first()
        found_list.title = update_list.title
        found_list.description = update_list.description

        session.add(found_list)
        session.commit()
        session.refresh(found_list)
        print(found_list)
        # 반환값 때문에 에러남
        return found_list

    def create(self, create_list: ListCreate):
        created_list = MyList(title=create_list.title, description=create_list.description)
        session.add(created_list)
        # null 반환함, 다른 걸로 바꾸기
        return session.commit()
