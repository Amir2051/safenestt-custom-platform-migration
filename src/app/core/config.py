from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SafeNestT Custom Platform"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://safenestt:safenestt@localhost:5432/safenestt"
    jwt_secret: str = "change-me"
    jwt_issuer: str = "safenestt-custom-platform"
    access_token_minutes: int = 15
    refresh_token_days: int = 30

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
