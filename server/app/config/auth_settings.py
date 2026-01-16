from pydantic_settings import BaseSettings, SettingsConfigDict

class AuthSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = AuthSettings()