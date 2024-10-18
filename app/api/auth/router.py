from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from app.api.user.schemas import ResponseUserSchema
from app.api.auth.services import auth_user, refresh_token, register_user_service
from app.api.auth.schemas import UserRegister, UserAuth, Token
from app.api.auth.utils import get_current_active_user
from app.database import get_async_session

router = APIRouter(prefix = '/auth')

@router.post("/register", response_model=ResponseUserSchema)
async def register_user(user_data: UserRegister, session: AsyncSession = Depends(get_async_session)):
    user_response = await register_user_service(session, user_data)
    return user_response

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_async_session)):
    token_response = await auth_user(form_data, session)
    return token_response

@router.post("/refresh_token", response_model=Token)
async def test(refresh_token: str, session: AsyncSession = Depends(get_async_session)):
    token_response = await refresh_token(refresh_token, session)
    return token_response


from typing import Annotated
from app.api.user.models import User
from app.api.auth.utils import get_current_active_user

@router.get("/users/me", response_model=ResponseUserSchema)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
