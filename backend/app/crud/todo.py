# app/crud/todo.py
import logging
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Todo


class CRUDTodo(CRUDBase):
    pass


todo_crud = CRUDTodo(model=Todo)