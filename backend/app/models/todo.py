# app/models/todo.py
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey

# Импортируем базовый класс для моделей.
from app.core.db import Base

class Todo(Base):
    item = Column(Text(), nullable=False)
    # user_id = Column(
    #     Integer,
    #     ForeignKey(
    #         'user.id',
    #         name='fk_application_form_user_id_user'
    #     ), nullable=False
    # )

    def __repr__(self):
        return (
            f'<id={self.id!r}), '
            f'item={self.item[:20]!r}...)>'
        )