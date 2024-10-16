from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    """Схема для создания нового пользователя"""
    username: str
    email: str
    password: str


class UserInDB(BaseModel):
    """Схема для представления пользователя в базе данных"""
    id: UUID
    username: str
    email: str

    class Config:
        orm_mode = True


class UserSignIn(BaseModel):
    """Схема для аутентификации пользователя"""
    email: str
    password: str
