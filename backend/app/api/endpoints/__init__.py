# app/api/endpoints/__init__.py
"""
This module initializes the API endpoints for the application.

It imports and re-exports the routers from the `charity_project`, `donation`,
and `user` modules, making it easier to include them in the main FastAPI app.

Imported routers:

- user_router: Handles all user-related endpoints.
"""
from .todo import router as todo_router
# from .user import router as user_router

# Specify which names are accessible when `from module import *` is used
__all__ = [
    'todo_router',
]