from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_NAME: str = "Min Messenger Backend"
    API_V1_PREFIX: str = "/api/v1"

    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 1 week

    EMAIL_VALIDATION_API_KEY: str = ""
    EMAIL_VALIDATION_API_URL: str = "https://mailcheck.p.rapidapi.com/"

    # For avatars
    S3_ENDPOINT: str = ""
    S3_ACCESS_KEY: str = ""
    S3_SECRET_KEY: str = ""
    S3_BUCKET_NAME: str = "messenger-avatars"

    OFFLINE_MESSAGE_TTL_DAYS: int = 30

    # Blocked email domains
    BLOCKED_DOMAINS: list[str] = [
        "mail.ru",
        "yandex.ru",
        "rambler.ru",
        "qq.com",
        "163.com",
        "126.com",
    ]


class DBSettings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "db_dev"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 5432

    echo: bool = True

    @property
    def url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


class Settings:
    db: DBSettings = DBSettings()
    app: AppSettings = AppSettings()


settings = Settings()
