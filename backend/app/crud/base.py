# app/crud/base.py
import logging
from typing import Optional, Any, Text

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# from app.models import User


class CRUDBase:

    def __init__(self, model):
        self.model = model

    async def get(
        self,
        session: AsyncSession,
        value: Any,
        field: str = 'id',
    ):
        model_field = getattr(self.model, field)
        db_obj = await session.execute(
            select(self.model).where(model_field == value)
        )
        return db_obj.scalars().first()


    async def get_multi(
        self,
        session: AsyncSession
    ):
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()


    async def create(
            self,
            obj_in,
            session: AsyncSession,
            # user: Optional[User] = None,
            update_db: bool = True
    ):
        obj_in_data = obj_in.dict()
        # Если пользователь был передан...
        # if user is not None:
        #     # ...то дополнить словарь для создания модели.
        #     obj_in_data['user_id'] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        if update_db:
            await session.commit()
            await session.refresh(db_obj)  # Ensure db_obj is managed
        return db_obj


    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession
    ):
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)  # Ensure db_obj is managed
        return db_obj


    async def delete(
            self,
            db_obj,
            session: AsyncSession,
    ):
        await session.delete(db_obj)
        await session.commit()
        return db_obj