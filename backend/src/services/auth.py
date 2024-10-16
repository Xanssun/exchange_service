from db.postgres import get_session
from fastapi import Depends
from models.entity import User
from schemas.entity import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from tools.get_user_from_base import get_user_by_email


class AuthService():
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def signup(self, user_create: UserCreate):
        """Регистрация нового пользователя"""
        exists_user = await get_user_by_email(self.db_session, user_create.email)
        if not exists_user:
            user = User(**user_create.model_dump())
            self.db_session.add(user)
            await self.db_session.commit()
            await self.db_session.refresh(user)
            
            return user
        
    
    async def signin(self):
        """Авторизация"""
        pass


    async def refresh_token(self):
        pass




def get_auth_service(
    db_session: AsyncSession = Depends(get_session)
) -> AuthService:
    return AuthService(db_session=db_session)