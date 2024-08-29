# app/schemas/__init__.py
"""
This module ensures that all necessary Pydantic schemas
are loaded for proper operation.
"""

from .todo import (
    STodoCreate,
    STodoResponse,
    STodoUpdate,
    STodoInDB
)

# from .user import SUserCreate, SUserRead, SUserUpdate

# Specify which names are accessible when `from module import *` is used
__all__ = [
    'STodoCreate',
    'STodoResponse',
    'STodoUpdate',
    'STodoInDB',
]