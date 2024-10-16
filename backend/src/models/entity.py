import uuid
from datetime import datetime

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
    password = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
