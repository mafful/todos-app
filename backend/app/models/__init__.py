# app/models/__init__.py
"""
This module ensures that all necessary models are loaded
for SQLAlchemy to function correctly.

It imports the following models:
- `ApplicatinForm`: Represents application form.
- `User`: Represents users.

Loading these models is essential for SQLAlchemy to operate properly.
"""
from .todo import Todo
# from .user import User

# Specify which names are accessible when `from module import *` is used
__all__ = [
    'Todo'
]