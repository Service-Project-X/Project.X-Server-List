from typing import List

from app.db.mysql_conn import engineconn
from app.models.list import MyList
from app.schemas.list import ListCreate

engine = engineconn()
session = engine.sessionmaker()

class CRUDLists:

    def get_multiple(self) -> List[MyList]:
        return session.query(MyList).all()

    def create(self, create_list: ListCreate):
        created_list = MyList(title=create_list.title, description=create_list.description)
        session.add(created_list)
        # null 반환함, 다른 걸로 바꾸기
        return session.commit()
