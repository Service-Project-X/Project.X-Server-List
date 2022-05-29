from typing import List, Any

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.models.folder import Folder
from app.models.schedule import Schedule
from app.models.child_folder import ChildFolder
from app.schemas import folder, custom_response_type

router = InferringRouter()

@cbv(router)
class Folder:
    def __init__(self, api_router, crud_folder, crud_child_folder, crud_schedule):
        self.router = api_router
        self.folder_repository = crud_folder
        self.child_folder_repository = crud_child_folder
        self.schedule_repository = crud_schedule

    @router.get("/{folder_id}", response_model=custom_response_type.CustomResponseType)
    async def get_all(self, folder_id: int) -> [ChildFolder or Schedule]:
        child_folders: List[ChildFolder] = self.child_folder_repository.get_multiple_in_folder(folder_id)
        schedules: List[Schedule] = self.schedule_repository.get_multiple_in_folder(folder_id)

        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.data = [child_folders, schedules]
        return new_custom_response_type

    @router.post("/", status_code=status.HTTP_201_CREATED, response_model=custom_response_type.CustomResponseType)
    async def create_list(self, create_folder: folder.FolderCreate):
        created_folder: Folder = self.folder_repository.create(create_folder)
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
    async def delete(self, folder_id: int):
        deleted_folder = self.folder_repository.delete(folder_id)
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.message = deleted_folder
        return new_custom_response_type
