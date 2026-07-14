from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_debug: bool = True

    database_url: str
    secret_key: str
    jwt_secret: str

    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60


settings = Settings()
