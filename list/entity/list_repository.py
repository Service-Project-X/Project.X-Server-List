from config.mysql_conn import engineconn
from list.entity.list_entity import MyList
from list.dto.create_list import CreateList

engine = engineconn()
session = engine.sessionmaker()

class ListRepository:

    def find_all(self):
        return session.query(MyList).all()

    def create(self, create_list: CreateList):
        created_list = MyList(title=create_list.title, description=create_list.description)
        session.add(created_list)
        # null 반환함, 다른 걸로 바꾸기
        return session.commit()
