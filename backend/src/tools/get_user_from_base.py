from typing import Union

from models.entity import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_by_email(db_session: AsyncSession, email: str) -> Union[User, None]:
    """Получаем пользователя по почте"""
    statement = select(User).where(User.email == email)
    query = await db_session.execute(statement)
    return query.scalars().first()
