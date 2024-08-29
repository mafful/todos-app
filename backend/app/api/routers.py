# app/api/routers.py
from fastapi import APIRouter

from app.api.endpoints import (
    todo_router,
    # user_router
)

main_router = APIRouter()

main_router.include_router(
    todo_router, prefix='/todo', tags=['todo']
)

# main_router.include_router(user_router)