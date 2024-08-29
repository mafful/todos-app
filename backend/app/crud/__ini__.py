# app/crud/__init__.py
"""
This module ensures that all necessary models are loaded for SQLAlchemy
to function correctly.

Proper model loading is essential for the correct operation of SQLAlchemy.
"""

from .base import CRUDBase
from .todo import todo_crud


# Specify which names are accessible when `from module import *` is used
__all__ = [
    'CRUDBase',
    'todo_crud'
]