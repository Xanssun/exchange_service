import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    project_name: str = 'messages_service'
    db_name: str = os.getenv('DB_NAME', 'messages')
    db_user: str = os.getenv('DB_USER', 'app')
    db_password: str = os.getenv('DB_PASSWORD', 'emptystring')
    db_host: str = os.getenv('DB_HOST', '127.0.0.1')
    db_port: str = os.getenv('DB_PORT', '5432')

    redis_host: str = os.getenv('REDIS_HOST', '127.0.0.1')
    redis_port: int = int(os.getenv('REDIS_PORT', 6379))

    mess_api_host: str = os.getenv('FAST_API_HOST', '0.0.0.0')
    mess_api_port: int = int(os.getenv('FAST_API_PORT', 8002))

settings = Settings()
