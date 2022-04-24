from list.dto.create_list import CreateList
from list.entity.list_repository import ListRepository


class ListService:
    def __init__(self):
        self.list_repository = ListRepository()

    def find_all_lists(self):
        return self.list_repository.find_all()

    def create_new_list(self, create_list: CreateList):
        return self.list_repository.create(create_list)
