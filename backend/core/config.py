import os


class Settings:
    PROJECT_TITLE: str = "Crud@Cloud"
    PROJECT_VERSION: str = "0.1.0"
    DATABASE_URL = os.environ.get("DATABASE_URL")
    ALLOW_ORIGINS_LIST = os.environ.get("ALLOW_ORIGINS_LIST")


settings = Settings()
