from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.schemas import child_folder, custom_response_type

router = InferringRouter()

@cbv(router)
class ChildFolder:
    def __init__(self, crud_child_folder):
        self.crud_child_folder = crud_child_folder

    @router.get("/{folder_or_child_folder_id}/in_folder/{in_folder}", response_model=custom_response_type.CustomResponseType)
    async def get_all(self, folder_or_child_folder_id: int, in_folder: bool):
        in_child_folders = self.crud_child_folder.get_multiple_in_folder(folder_or_child_folder_id) if in_folder else self.crud_child_folder.get_multiple_in_child_folder(folder_or_child_folder_id)
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.data = in_child_folders
        return new_custom_response_type

    @router.post("/{in_folder}", response_model=custom_response_type.CustomResponseType)
    async def create_child_folder(self, in_folder: bool, create_child_folder: child_folder.ChildFolderCreate):
        created_child_folder = self.crud_child_folder.create_in_folder(create_child_folder) if in_folder else self.crud_child_folder.create_in_child_folder(create_child_folder)
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.data = created_child_folder
        return new_custom_response_type

    @router.put("/{child_folder_id}", response_model=custom_response_type.CustomResponseType)
    async def update(self, child_folder_id: int, update_child_folder: child_folder.ChildFolderUpdate):
        updated_folder = self.crud_child_folder.update(child_folder_id, update_child_folder)
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.data = updated_folder
        return new_custom_response_type

    @router.delete("/{child_folder_id}", response_model=custom_response_type.CustomResponseType)
    async def delete(self, child_folder_id: int):
        deleted_folder = self.crud_child_folder.delete(child_folder_id)
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.message = deleted_folder
        return new_custom_response_type
