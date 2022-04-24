from fastapi import APIRouter

from list.dto.create_list import CreateList
from list.list_service import ListService

router = APIRouter(
    prefix="/list",
)

list_service = ListService()

@router.get("/")
async def first_get():
    lists = list_service.find_all_lists()
    return lists


@router.post("/")
async def first_post(create_list: CreateList):
    return list_service.create_new_list(create_list)