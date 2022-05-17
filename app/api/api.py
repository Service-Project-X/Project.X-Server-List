from fastapi import APIRouter

from app.api.endpoints import folder

api_router = APIRouter()
api_router.include_router(folder.router, prefix="/folder", tags=["folder"])
