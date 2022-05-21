from typing import List

from fastapi import APIRouter

from app.crud.crud_folder import CRUDFolder
from app.schemas import folder, child_folder, schedule, custom_response_type

router = APIRouter()
child_folder_repository = CRUDFolder()

@router.get("/{child_folder_id}", response_model=custom_response_type.CustomResponseType)
async def get_all(child_folder_id: str):
    in_folders = child_folder_repository.get_multiple(child_folder_id)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.data = in_folders
    return new_custom_response_type

@router.post("/", response_model=custom_response_type.CustomResponseType)
async def create_list(create_child_folder: child_folder.ChildFolderCreate):
    created_child_folder = child_folder_repository.create(create_child_folder)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.data = created_child_folder
    return new_custom_response_type

@router.put("/{folder_id}", response_model=custom_response_type.CustomResponseType)
async def update(folder_id: str, update_folder: folder.FolderUpdate):
    updated_folder = child_folder_repository.update(folder_id, update_folder)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.data = updated_folder
    return new_custom_response_type

@router.delete("/{folder_id}", response_model=custom_response_type.CustomResponseType)
async def delete(folder_id: str):
    deleted_folder = child_folder_repository.delete(folder_id)
    new_custom_response_type = custom_response_type.CustomResponseType
    new_custom_response_type.message = deleted_folder
    return new_custom_response_type
