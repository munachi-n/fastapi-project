import os


class Config:
    APP_NAME = "FastAPI Project"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./db.sqlite")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
