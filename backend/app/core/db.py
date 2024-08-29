# app/core/db.py
from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    """
    Base class for all SQLAlchemy models that provides
    a single primary key field.

    Attributes:
        id (int): Primary key for the table.
    """

    @declared_attr
    def __tablename__(cls):
        # The table name will be the name of the model in lowercase.
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    """
    Opens a session using an asynchronous context manager and sessionmaker.

    An asynchronous session is created and managed within the context manager,
    and the session is yielded to the calling function as a generator.

    Yields:
        async_session: The asynchronous session object.
    """
    async with AsyncSessionLocal() as async_session:
        yield async_session