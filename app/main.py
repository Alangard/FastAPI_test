from fastapi import FastAPI, Request
from contextlib import asynccontextmanager


from app.config import settings
from app.database import BaseModel, engine

from app.api.appointments.router import router as appointments_router
from app.api.auth.router import router as auth_router
from app.api.user.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Async context manager for startup and shutdown lifecycle events.
    - Creates database tables.
    - Sets up bot commands and webhook.

    Yields control during application's lifespan and performs cleanup on exit.
    - Disposes all database connections.
    - Deletes bot webhook and commands.
    - Closes aiohttp session
    """ 

    async with engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)

    # # Инициализация фабрики моковых данных
    # generate_fake_data()

    yield


application = FastAPI(title="FastAPI-example", lifespan=lifespan)
application.include_router(appointments_router)
application.include_router(auth_router)
application.include_router(user_router)


    