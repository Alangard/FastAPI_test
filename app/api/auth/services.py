import datetime
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.schemas import UserRegister, UserAuth
from app.api.auth.utils import create_access_token
from app.api.user.crud import create_user, get_user_by_phone_number
from app.config import settings


async def auth_user(form_data: UserAuth, session: AsyncSession):     
    user = await get_user_by_phone_number(session, phone_number = form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone number or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = datetime.timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = create_access_token(data={"sub": user.phone_number}, expires_delta=access_token_expires)
    refresh_token = create_refresh_token(data={"sub": user.phone_number}, expires_delta=refresh_token_expires)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}  


async def refresh_token(refresh_token: str, session: AsyncSession):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") != "refresh":
            raise credentials_exception
        phone_number: str = payload.get("sub")
        if phone_number is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = await get_user_by_phone_number(session, phone_number=phone_number)
    if user is None:
        raise credentials_exception

    access_token_expires = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.phone_number}, expires_delta=access_token_expires)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


async def register_user_service(session: AsyncSession, user_data: UserRegister):
    db_user = await get_user_by_phone_number(session, phone_number=user_data.phone_number)
    if db_user:
        raise HTTPException(status_code=400, detail="User with this phone number is already registered")
    return await create_user(session, user_data)