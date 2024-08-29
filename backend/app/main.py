# backend/main.py
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api.routers import main_router
from app.core.config import settings
# from app.core.init_db import create_first_superuser

logging.basicConfig(
    level=logging.INFO,  # Set the log level to INFO or DEBUG to see info logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

app.include_router(router=main_router)


# @app.lifespan('startup')
# async def startup():
#     await create_first_superuser()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    uvicorn.run("app.api:app", host="127.0.0.1", port=8000, reload=True)