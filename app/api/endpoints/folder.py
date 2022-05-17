from typing import List

from fastapi import APIRouter

from app.crud.crud_folder import CRUDFolder
from app.schemas import folder, child_folder, schedule, custom_response_type

router = APIRouter()
folder_repository = CRUDFolder()

@router.get("/{folder_id}", response_model=custom_response_type.CustomResponseType)
async def get_all(folder_id: str):
    in_folders = folder_repository.get_multiple(folder_id)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.data = in_folders
    return new_custom_response_type

@router.post("/", response_model=custom_response_type.CustomResponseType)
async def create_list(create_folder: folder.FolderCreate):
    created_folder = folder_repository.create(create_folder)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.data = created_folder
    return new_custom_response_type

@router.put("/{folder_id}", response_model=custom_response_type.CustomResponseType)
async def update(folder_id: str, update_folder: folder.FolderUpdate):
    updated_folder = folder_repository.update(folder_id, update_folder)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.data = updated_folder
    return new_custom_response_type

@router.delete("/{folder_id}", response_model=custom_response_type.CustomResponseType)
async def delete(folder_id: str):
    deleted_folder = folder_repository.delete(folder_id)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.message = deleted_folder
    return new_custom_response_type
