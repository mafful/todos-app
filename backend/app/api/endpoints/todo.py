# app/api/application_form.py
import logging
from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
# from app.core.user import current_superuser, current_user
from app.crud.todo import todo_crud
# from app.models import User
from app.schemas import (
    STodoCreate,
    STodoResponse,
    STodoUpdate,
    STodoInDB,
)
# from app.api.validators import check_application_form_exists


router = APIRouter()

todos = [
    {"id": 1, "item": "Read a book."},
    {"id": 2, "item": "Cycle around town."},
    {"id": 3, "item": "I did it, well at least with help )."},
]

@router.get("/")
async def get_todos(
    session: AsyncSession = Depends(get_async_session),
) -> dict:
    return {"data": todos}


@router.post("/", response_model=STodoResponse, status_code=HTTPStatus.CREATED)
async def add_todo(
    todo: STodoCreate,
    session: AsyncSession = Depends(get_async_session),
) -> STodoResponse:
    new_id = max(t["id"] for t in todos) + 1 if todos else 1
    todo_in_db = STodoInDB(id=new_id, **todo.dict())
    todos.append(todo_in_db.dict())
    return STodoResponse(**todo_in_db.dict())


@router.put("/{id}", response_model=STodoResponse)
async def update_todo(
    id: int,
    body: STodoUpdate,
    session: AsyncSession = Depends(get_async_session),
) -> STodoResponse:
    for todo in todos:
        if todo["id"] == id:
            todo["item"] = body.item
            return STodoResponse(id=id, item=todo["item"])

    raise HTTPException(status_code=404, detail=f"Todo with id {id} not found.")

@router.delete("/{id}")
async def delete_todo(
    id: int,
    session: AsyncSession = Depends(get_async_session)
) -> dict:
    global todos
    todos = [todo for todo in todos if int(todo["id"]) != id]

    return {"data": f"Todo with id {id} has been deleted."}