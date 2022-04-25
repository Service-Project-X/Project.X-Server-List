from typing import List

from fastapi import APIRouter

from app import schemas
from app.crud.crud_list import CRUDLists
from app.schemas.list import ListCreate

router = APIRouter()
list_repository = CRUDLists()

@router.get("/", response_model=List[schemas.list.List])
async def get_all():
    lists = list_repository.get_multiple()
    return lists

@router.post("/")
async def create_list(create_list: ListCreate):
    return list_repository.create(create_list)
