# app/schemas/application_form.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class STodo(BaseModel):
    item: str = Field(..., description="Todo")

    class Config:
        json_schema_extra = {
            "examples": [
                {"item": "Read a book."},
                {"item": "Cycle around town."},
                {"item": "I did it, well at least with help :)."},
            ]
        }


class STodoCreate(STodo):

    class Config:
        extra = "forbid"


class STodoResponse(STodo):
    id: int

    class Config:
        from_attributes = True


class STodoUpdate(BaseModel):
    item: str = Field(..., description="Updated todo item")

    class Config:
        extra = "forbid"


class STodoInDB(STodoResponse):
    pass