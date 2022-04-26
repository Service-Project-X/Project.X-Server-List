from typing import List

from fastapi import APIRouter

from app.crud.crud_list import CRUDLists
from app.schemas import list

router = APIRouter()
list_repository = CRUDLists()

@router.get("/", response_model=List[list.List])
async def get_all():
    lists = list_repository.get_multiple()
    return lists

@router.put("/{list_id}", response_model=list.List)
async def update(list_id: str, update_list: list.ListUpdate):
    updated_list = await list_repository.update(list_id, update_list)
    return updated_list

@router.post("/")
async def create_list(create_list: list.ListCreate):
    return list_repository.create(create_list)
