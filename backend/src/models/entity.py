import uuid
from datetime import datetime

import bcrypt
from db.postgres import Base
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = 'users'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True
    )
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password) 
    
    @staticmethod
    def hash_password(password: str) -> str:
        # Генерация соли и хеширование пароля
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        # Проверка пароля
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self) -> str:
        return f'<User {self.email}>'
