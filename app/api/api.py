from fastapi import APIRouter

from app.api.endpoints import folder, child_folder

api_router = APIRouter()
api_router.include_router(folder.router, prefix="/folder", tags=["folder"])
api_router.include_router(child_folder.router, prefix="/child_folder", tags=["child_folder"])
