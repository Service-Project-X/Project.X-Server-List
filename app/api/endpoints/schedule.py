from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import status

from app.schemas import schedule, custom_response_type

router = InferringRouter()

@cbv(router)
class Schedule:
    # crud_schedule 타입 정해주면 에러남
    def __init__(self, crud_schedule):
        self.crud_schedule = crud_schedule

    @router.get("/{schedule_id}", response_model=custom_response_type.CustomResponseType)
    async def get_schedule(self, schedule_id: int):
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.data = self.crud_schedule.get_one(schedule_id)
        return new_custom_response_type

    @router.post("/{in_folder}", status_code=status.HTTP_201_CREATED, response_model=None)
    async def create_schedule(self, in_folder: bool, create_schedule: schedule.ScheduleCreate):
        self.crud_schedule.create_in_folder(create_schedule) if in_folder else self.crud_schedule.create_in_child_folder(create_schedule)
        return

    @router.put("/{schedule_id}", response_model=custom_response_type.CustomResponseType)
    async def update_schedule(self, schedule_id: int, update_schedule: schedule.ScheduleUpdate):
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.data = self.crud_schedule.update(schedule_id, update_schedule)
        return new_custom_response_type

    @router.delete("/{schedule_id", response_model=custom_response_type.CustomResponseType)
    async def delete_schedule(self, schedule_id: int):
        new_custom_response_type = custom_response_type.CustomResponseType
        new_custom_response_type.message = self.crud_schedule.delete(schedule_id)
        return new_custom_response_type
