from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext

from app.database import get_async_session
from app.api.user.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_phone_number(session: AsyncSession, phone_number: str):
    query = select(User).where(User.phone_number == phone_number)
    result = await session.execute(query)
    return result.scalars().first()


async def create_user(session: AsyncSession, user_data):
    hashed_password = pwd_context.hash(user_data.password)
    db_user = User(
        first_name=user_data.first_name,
        second_name=user_data.second_name,
        phone_number=user_data.phone_number,
        password=hashed_password,
    )
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user