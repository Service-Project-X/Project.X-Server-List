from fastapi import APIRouter

from app.api.endpoints import lists

api_router = APIRouter()
api_router.include_router(lists.router, prefix="/lists", tags=["lists"])
