import json
from typing import List, Any

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from app.crud.crud_folder import CRUDFolder
from app.crud.crud_schedule import CRUDSchedule
from app.crud.crud_child_folder import CRUDChildFolder
from app.models.folder import Folder
from app.models.schedule import Schedule
from app.models.child_folder import ChildFolder
from app.schemas import folder, custom_response_type

router = APIRouter()
folder_repository = CRUDFolder()
child_folder_repository = CRUDChildFolder()
schedule_repository = CRUDSchedule()

@router.get("/{folder_id}", response_model=custom_response_type.CustomResponseType)
async def get_all(folder_id: int) -> [ChildFolder or Schedule]:
    child_folders: List[ChildFolder] = child_folder_repository.get_multiple_in_folder(folder_id)
    schedules: List[Schedule] = schedule_repository.get_multiple_in_folder(folder_id)

    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.data = [child_folders, schedules]
    return new_custom_response_type

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=custom_response_type.CustomResponseType)
async def create_list(create_folder: folder.FolderCreate):
    created_folder: Folder = folder_repository.create(create_folder)
    new_custom_response_type = custom_response_type.CustomResponseType[Any](message=None, data=created_folder)
    # new_custom_response_type.data = created_folder
    return jsonable_encoder(new_custom_response_type)

# 필요할까?
# @router.put("/{folder_id}", response_model=custom_response_type.CustomResponseType)
# async def update(folder_id: int, update_folder: folder.FolderUpdate):
#     updated_folder = folder_repository.update(folder_id, update_folder)
#     new_custom_response_type = custom_response_type.CustomResponseType
#     new_custom_response_type.data = updated_folder
#     return new_custom_response_type

@router.delete("/{folder_id}", response_model=custom_response_type.CustomResponseType)
async def delete(folder_id: int):
    deleted_folder = folder_repository.delete(folder_id)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.message = deleted_folder
    return new_custom_response_type
