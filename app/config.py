import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from .common import EnvironmentType

__all__ = ['Config']

load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env')))


class Config(BaseSettings):
    DEBUG: int = 0
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT.value
    PORT: int = int(os.environ.get('PORT', '5555'))
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24
    MYSQL_DATABASE_HOST: str = os.environ.get("MYSQL_DATABASE_HOST")
    MYSQL_DATABASE: str = os.environ.get("MYSQL_DATABASE")
    MYSQL_DATABASE_USER: str = os.environ.get("MYSQL_DATABASE_USER")
    MYSQL_DATABASE_PASSWORD: str = os.environ.get("MYSQL_DATABASE_PASSWORD")
    MYSQL_DATABASE_PORT: int = os.environ.get("MYSQL_DATABASE_PORT")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_MINUTES: int = os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES")
